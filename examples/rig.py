import os
from pathlib import Path

import aind_behavior_services.rig as rig
import aind_behavior_services.rig.cameras as cameras

from aind_behavior_directed_foraging.rig import (
    AindBehaviorDirectedForagingRig,
    HarpDelphiController
)

video_writer = cameras.VideoWriterFfmpeg(frame_rate=60, container_extension="mp4")

rig = AindBehaviorDirectedForagingRig(
    computer_name="TestRigComputer", 
    rig_name="test_rig", 
    data_directory=Path("../temp_data"),
    harp_delphi_controller=HarpDelphiController(port_name="COM3", enable_valve_leds=True),
    triggered_camera_controller=cameras.CameraController[cameras.SpinnakerCamera](
        frame_rate=60,
        cameras = {
            "MainCamera": cameras.SpinnakerCamera(
                serial_number="Serial Number", binning=1, exposure=5000, gain=0, video_writer=video_writer
            )
        }
    )
)

def main(path_seed: str = "./local/{schema}.json"):
    os.makedirs(os.path.dirname(path_seed), exist_ok=True)
    models = [rig]

    for model in models:
        with open(path_seed.format(schema=model.__class__.__name__), "w", encoding="utf-8") as f:
            f.write(model.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
