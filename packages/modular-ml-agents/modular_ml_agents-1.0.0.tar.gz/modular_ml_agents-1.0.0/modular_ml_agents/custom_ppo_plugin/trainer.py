import numpy as np

from mlagents_envs.base_env import BehaviorSpec
from mlagents.trainers.behavior_id_utils import BehaviorIdentifiers

from mlagents_envs.logging_util import get_logger
from mlagents.trainers.buffer import BufferKey, RewardSignalUtil
from mlagents.trainers.policy.torch_policy import TorchPolicy
from mlagents.trainers.trainer.on_policy_trainer import OnPolicyTrainer
from mlagents.trainers.torch_entities.networks import SimpleActor, SharedActorCritic
from mlagents.trainers.optimizer.torch_optimizer import TorchOptimizer
from mlagents.trainers.ppo.optimizer_torch import PPOSettings
from mlagents.trainers.trajectory import Trajectory
from mlagents.trainers.settings import TrainerSettings
from mlagents.trainers.trainer.trainer_utils import get_gae
from mlagents.trainers.policy.policy import Policy

from typing import cast, Type, Union, Dict, Any
import attr
from .wrapper_actor import WrapperActor, WrapperSharedActorCritic
from .optimizer import CustomPPOOptimizer

logger = get_logger(__name__)
TRAINER_NAME = "custom_ppo"

@attr.s(auto_attribs=True)
class CustomPPOSettings(PPOSettings):
    path_to_model: str = ""
    path_to_mapping: str = ""

class CustomPPOTrainer(OnPolicyTrainer):
    """The PPOTrainer is an implementation of the PPO algorithm."""

    def __init__(
        self,
        behavior_name: str,
        reward_buff_cap: int,
        trainer_settings: TrainerSettings,
        training: bool,
        load: bool,
        seed: int,
        artifact_path: str,
    ):
        """
        Responsible for collecting experiences and training PPO model.
        :param behavior_name: The name of the behavior associated with trainer config
        :param reward_buff_cap: Max reward history to track in the reward buffer
        :param trainer_settings: The parameters for the trainer.
        :param training: Whether the trainer is set for training.
        :param load: Whether the model should be loaded.
        :param seed: The seed the model will be initialized with
        :param artifact_path: The directory within which to store artifacts from this trainer.
        """
        super().__init__(
            behavior_name,
            reward_buff_cap,
            trainer_settings,
            training,
            load,
            seed,
            artifact_path,
        )
        self.hyperparameters: CustomPPOSettings = cast(
            CustomPPOSettings, self.trainer_settings.hyperparameters
        )
        self.seed = seed
        self.shared_critic = self.hyperparameters.shared_critic
        self.policy: TorchPolicy = None  # type: ignore

    def create_policy(
        self, parsed_behavior_id: BehaviorIdentifiers, behavior_spec: BehaviorSpec
    ) -> TorchPolicy:
        actor_cls: Union[Type[SimpleActor], Type[SharedActorCritic]] = WrapperActor
        actor_kwargs: Dict[str, Any] = {
            "conditional_sigma": False,
            "tanh_squash": False,
        }
        if self.shared_critic:
            reward_signal_configs = self.trainer_settings.reward_signals
            reward_signal_names = [
                key.value for key, _ in reward_signal_configs.items()
            ]
            actor_cls = WrapperSharedActorCritic
            actor_kwargs.update({"stream_names": reward_signal_names})

        network_settings = self.trainer_settings.network_settings
        network_settings.path_to_model = self.hyperparameters.path_to_model
        network_settings.path_to_mapping = self.hyperparameters.path_to_mapping

        policy = TorchPolicy(
            self.seed,
            behavior_spec,
            network_settings,
            actor_cls,
            actor_kwargs,
        )

        policy.use_recurrent = True
        policy.m_size = 1
        return policy

    def create_optimizer(self) -> TorchOptimizer:
        return CustomPPOOptimizer(  # type: ignore
            cast(TorchPolicy, self.policy), self.trainer_settings  # type: ignore
        )  # type: ignore

    def _process_trajectory(self, trajectory: Trajectory) -> None:
        super()._process_trajectory(trajectory)
        agent_id = trajectory.agent_id  # All the agents should have the same ID

        agent_buffer_trajectory = trajectory.to_agentbuffer()
        # Check if we used group rewards, warn if so.
        self._warn_if_group_reward(agent_buffer_trajectory)

        # Update the normalization
        if self.is_training:
            self.policy.actor.update_normalization(agent_buffer_trajectory)
            self.optimizer.critic.update_normalization(agent_buffer_trajectory)

        # Get all value estimates
        (
            value_estimates,
            value_next,
            value_memories,
        ) =  self.optimizer.get_trajectory_value_estimates(
            agent_buffer_trajectory,
            trajectory.next_obs,
            trajectory.done_reached and not trajectory.interrupted,
        )
        if value_memories is not None:
            agent_buffer_trajectory[BufferKey.CRITIC_MEMORY].set(value_memories)

        for name, v in value_estimates.items():
            agent_buffer_trajectory[RewardSignalUtil.value_estimates_key(name)].extend(
                v
            )
            self._stats_reporter.add_stat(
                f"Policy/{self.optimizer.reward_signals[name].name.capitalize()} Value Estimate",
                np.mean(v),
            )

        # Evaluate all reward functions
        self.collected_rewards["environment"][agent_id] += np.sum(
            agent_buffer_trajectory[BufferKey.ENVIRONMENT_REWARDS]
        )
        for name, reward_signal in self.optimizer.reward_signals.items():
            evaluate_result = (
                reward_signal.evaluate(agent_buffer_trajectory) * reward_signal.strength
            )
            agent_buffer_trajectory[RewardSignalUtil.rewards_key(name)].extend(
                evaluate_result
            )
            # Report the reward signals
            self.collected_rewards[name][agent_id] += np.sum(evaluate_result)
        
        # Compute GAE and returns
        tmp_advantages = []
        tmp_returns = []
        for name in self.optimizer.reward_signals:
            bootstrap_value = value_next[name]

            local_rewards = agent_buffer_trajectory[
                RewardSignalUtil.rewards_key(name)
            ].get_batch()
            local_value_estimates = agent_buffer_trajectory[
                RewardSignalUtil.value_estimates_key(name)
            ].get_batch()

            local_advantage = get_gae(
                rewards=local_rewards,
                value_estimates=local_value_estimates,
                value_next=bootstrap_value,
                gamma=self.optimizer.reward_signals[name].gamma,
                lambd=self.hyperparameters.lambd,
            )
            local_return = local_advantage + local_value_estimates
            # This is later use as target for the different value estimates
            agent_buffer_trajectory[RewardSignalUtil.returns_key(name)].set(
                local_return
            )
            agent_buffer_trajectory[RewardSignalUtil.advantage_key(name)].set(
                local_advantage
            )
            tmp_advantages.append(local_advantage)
            tmp_returns.append(local_return)

        # Get global advantages
        global_advantages = list(
            np.mean(np.array(tmp_advantages, dtype=np.float32), axis=0)
        )
        global_returns = list(np.mean(np.array(tmp_returns, dtype=np.float32), axis=0))
        agent_buffer_trajectory[BufferKey.ADVANTAGES].set(global_advantages)
        agent_buffer_trajectory[BufferKey.DISCOUNTED_RETURNS].set(global_returns)

        self._append_to_update_buffer(agent_buffer_trajectory)

        # If this was a terminal trajectory, append stats and reset reward collection
        if trajectory.done_reached:
            self._update_end_episode_stats(agent_id, self.optimizer)

    @staticmethod
    def get_settings_type():
        return CustomPPOSettings

    @staticmethod
    def get_trainer_name() -> str:
        return TRAINER_NAME
    
    def get_policy(self, name_behavior_id: str) -> Policy:
        """
        Gets policy from trainer associated with name_behavior_id
        :param name_behavior_id: full identifier of policy
        """

        return self.policy

def get_type_and_setting():
    return {CustomPPOTrainer.get_trainer_name(): CustomPPOTrainer}, {
        CustomPPOTrainer.get_trainer_name(): CustomPPOTrainer.get_settings_type()
    }
