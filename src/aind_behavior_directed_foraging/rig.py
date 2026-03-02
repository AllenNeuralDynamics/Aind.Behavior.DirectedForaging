# Import core types
from typing import Literal

import aind_behavior_services.rig as rig

from aind_behavior_directed_foraging import __semver__


class AindBehaviorDirectedForagingRig(rig.AindBehaviorRigModel):
    version: Literal[__semver__] = __semver__
    ...