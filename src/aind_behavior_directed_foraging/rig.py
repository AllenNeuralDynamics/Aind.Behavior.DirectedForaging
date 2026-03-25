# Import core types
from typing import Literal
from pydantic import Field

import aind_behavior_services.rig as rig
import aind_behavior_services.rig.harp as harp
import aind_behavior_services.rig.cameras as cameras

from aind_behavior_directed_foraging import __semver__

class HarpDelphiController(harp.HarpDeviceBase):
    device_type: Literal["DelphiController"] = "DelphiController"
    who_am_i: Literal[1409] = 1409
    enable_valve_leds: bool
    minimum_poke_time: float = Field(default=0.1)
    minimum_odor_delivery_time: float = Field(default=0.5)
    final_valve_energized_time: float = Field(default=0.11)
    vacuum_setup_time: float = Field(default=0.01)
    vacuum_close_time: float = Field(default=0.02)
    odor_transition_time: float = Field(default=0.02)
    max_odor_delivery_time: float = Field(default=0.6)
    
class HarpUndergroundFeeder(harp.HarpOutputExpander):
    retry_delivery_count: int
    retry_delivery_due_time: float
    radius: float

class AindBehaviorDirectedForagingRig(rig.Rig):
    version: Literal[__semver__] = __semver__
    harp_delphi_controller: HarpDelphiController
    triggered_camera_controller: cameras.CameraController[cameras.SpinnakerCamera]
    # harp_underground_feeder: HarpUndergroundFeeder
    