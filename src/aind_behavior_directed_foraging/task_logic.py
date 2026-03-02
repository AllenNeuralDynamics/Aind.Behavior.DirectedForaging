import logging
from typing import Literal

import aind_behavior_services.task_logic.distributions as distributions
from aind_behavior_services.task_logic import AindBehaviorTaskLogicModel, TaskParameters
from pydantic import Field

from aind_behavior_directed_foraging import (
    __semver__,
)

logger = logging.getLogger(__name__)

# ==================== MAIN TASK LOGIC CLASSES ====================


class AindBehaviorDirectedForagingTaskParameters(TaskParameters):
    """
    Complete parameter specification for the directed-foraging task.
    """
    ...

class AindBehaviorDirectedForagingTaskLogic(AindBehaviorTaskLogicModel):
    """
    Main task logic model for the directed-foraging task.
    """

    version: Literal[__semver__] = __semver__
    name: Literal["AindBehaviorDirectedForaging"] = Field(default="AindBehaviorDirectedForaging", description="Name of the task logic", frozen=True)
    task_parameters: AindBehaviorDirectedForagingTaskParameters = Field(description="Parameters of the task logic")
