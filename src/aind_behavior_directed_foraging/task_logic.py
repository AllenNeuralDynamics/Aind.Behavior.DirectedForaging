import logging
from typing import Literal, List

import aind_behavior_services.task.distributions as distributions
from aind_behavior_services.task import Task, TaskParameters
from pydantic import Field, BaseModel

from aind_behavior_directed_foraging import (
    __semver__,
)

logger = logging.getLogger(__name__)

# ==================== MAIN TASK LOGIC CLASSES ====================

class OdorDefinition(BaseModel):
    odor_id: str
    olfactometer_mask: int

class Trial(BaseModel):
    odor_definition: OdorDefinition = Field(description="The odor that will be released on this trial")
    release_time: float = Field(description="The amount of time this odor will be released")
    dig_threshold: float = Field(description="The distance a subject must dig before reward delivery, if reward is available")
    trial_timeout: float = Field(description="Subject must begin digging within this amount of time to register a response")
    threshold_reward: int = Field(ge=0, description="Reward amount to be delivered when threshold reached")
    threshold_punishment: float = Field(ge=0, description="Punishment time added when threshold is reached")

class AindBehaviorDirectedForagingTaskParameters(TaskParameters):
    """
    Complete parameter specification for the directed-foraging task.
    """
    trials: List[Trial]

class AindBehaviorDirectedForagingTaskLogic(Task):
    """
    Main task logic model for the directed-foraging task.
    """

    version: Literal[__semver__] = __semver__
    name: Literal["AindBehaviorDirectedForaging"] = Field(default="AindBehaviorDirectedForaging", description="Name of the task logic", frozen=True)
    task_parameters: AindBehaviorDirectedForagingTaskParameters = Field(description="Parameters of the task logic")
