from typing import List, Dict, Any, Union
import scipy
import numpy as np
from pydantic import BaseModel
from banditbench.agents.classics import MABAgent, CBAgent, UCBAgent, ThompsonSamplingAgent, GreedyAgent, LinUCBAgent
from banditbench.tasks.cb.env import State
from banditbench.agents.typing import ActionInfo, ActionInfoField
from banditbench.sampling.sampler import DataCollectWithAG

class VerbalGuide:
    # VerbalGuide can be retrieved in two ways:
    # it's a verbal analog of a Q-function
    # Q(s=None, a) # MAB
    # Q(s, a) # CB

    def __init__(self, agent: Union[MABAgent, CBAgent]):
        self.agent = agent

    def get_action_guide_info(self, arm: int) -> ActionInfo:
        raise NotImplementedError("Only for MAB agents")

    def get_actions_guide_info(self) -> List[ActionInfo]:
        raise NotImplementedError("Only for MAB agents")

    def get_state_action_guide_info(self, state: State, arm: int) -> ActionInfo:
        raise NotImplementedError("Only for RL and CB agents")

    def get_state_actions_guide_info(self, state: State) -> List[ActionInfo]:
        raise NotImplementedError("Only for RL and CB agents")


class UCBGuide(VerbalGuide, DataCollectWithAG):
    # takes in UCBAgent and then return info on each arm (a block of text)
    def __init__(self, agent: UCBAgent):
        super().__init__(agent)

    def get_actions_guide_info(self) -> List[ActionInfo]:
        actions_info = []
        for arm in range(self.agent.k_arms):
            arm_info = self.get_action_guide_info(arm)
            actions_info.append(arm_info)

        assert len(actions_info) == self.agent.k_arms
        return actions_info

    def get_action_guide_info(self, arm: int) -> ActionInfo:
        exploration_bonus = self.agent.calculate_exp_bonus(arm) if self.agent.arms[arm] > 0 else "inf"
        exp_bonus_guide = ActionInfoField(info_name='exploration bonus', value=exploration_bonus)

        exploitation_value = self.agent.calculate_exp_value(arm) if self.agent.arms[arm] > 0 else 0
        exp_value_guide = ActionInfoField(info_name='exploitation value', value=exploitation_value)
        return exp_bonus_guide + exp_value_guide


class GreedyGuide(VerbalGuide, DataCollectWithAG):
    def __init__(self, agent: GreedyAgent):
        super().__init__(agent)

    def get_actions_guide_info(self) -> List[ActionInfo]:
        actions_info = []
        for arm in range(self.agent.k_arms):
            arm_info = self.get_action_guide_info(arm)
            actions_info.append(arm_info)
        return actions_info

    def get_action_guide_info(self, arm: int) -> ActionInfo:
        exploitation_value = self.agent.calculate_exp_value(arm) if self.agent.arms[arm] > 0 else 0
        exp_value_guide = ActionInfoField(info_name='exploitation value', value=exploitation_value)
        arm_info = ActionInfo(action_info_fields=[exp_value_guide])
        return arm_info


class ThompsonSamplingGuide(VerbalGuide, DataCollectWithAG):
    def __init__(self, agent: ThompsonSamplingAgent):
        super().__init__(agent)

    def get_actions_guide_info(self) -> List[ActionInfo]:
        actions_info = []
        for arm in range(self.agent.k_arms):
            arm_info = self.get_action_guide_info(arm)
            actions_info.append(arm_info)

        assert len(actions_info) == len(self.agent.actions)
        return actions_info

    def get_action_guide_info(self, arm: int) -> ActionInfo:
        alpha = self.agent.alpha[arm]
        beta = self.agent.beta[arm]
        p = scipy.stats.beta.rvs(self.agent.alpha[arm], self.agent.beta[arm])
        alpha_guide = ActionInfoField(info_name='alpha', value=alpha,
                                      info_template='prior beta distribution(alpha={:.2f}')
        beta_guide = ActionInfoField(info_name='beta', value=beta, info_template='beta={:.2f})')
        probability_guide = ActionInfoField(info_name='probability', value=p,
                                            info_template='posterior bernoulli p={:.2f}')
        return alpha_guide + beta_guide + probability_guide


class LinUCBGuide(VerbalGuide, DataCollectWithAG):
    def __init__(self, agent: LinUCBAgent):
        super().__init__(agent)

    def get_state_action_guide_info(self, state: State, arm: int) -> ActionInfo:
        a = arm
        context = state.feature

        A_inv = np.linalg.inv(self.agent.A[a])
        theta = A_inv.dot(self.agent.b[a])
        exploration_bonus = self.agent.alpha * np.sqrt(context.T.dot(A_inv).dot(context))
        # exploitation_value = theta.T.dot(context)[0, 0]
        exploitation_value = theta.T.dot(context)[0]

        exp_bonus_guide = ActionInfoField(info_name='exploration bonus', value=exploration_bonus)
        exp_value_guide = ActionInfoField(info_name='exploitation value', value=exploitation_value)

        return exp_bonus_guide + exp_value_guide

    def get_state_actions_guide_info(self, state: State) -> List[ActionInfo]:
        actions_info = []
        for arm in range(self.agent.k_arms):
            arm_info = self.get_state_action_guide_info(state, arm)
            actions_info.append(arm_info)

        return actions_info
