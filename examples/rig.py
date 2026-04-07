import os
from pathlib import Path

import aind_behavior_services.rig as rig
import aind_behavior_services.rig.cameras as cameras
from aind_behavior_services.rig.cameras import SpinnakerCameraAdcBitDepth

from aind_behavior_directed_foraging.rig import (
    AindBehaviorDirectedForagingRig,
    HarpDelphiController
)

FFMPEG_OUTPUT_8BIT = '-vf "scale=out_range=full,setparams=range=full:colorspace=bt709:color_primaries=bt709:color_trc=linear" -c:v h264_nvenc -pix_fmt yuv420p -color_range 2 -colorspace bt709 -color_trc linear -tune hq -preset p3 -rc vbr -cq 18 -b:v 0M -metadata author="Allen Institute for Neural Dynamics" -maxrate 700M -bufsize 350M -f matroska -write_crc32 0'
FFMPEG_OUTPUT_16BIT = '-vf "format=yuv420p10le,scale=out_range=full,setparams=range=full:colorspace=bt709:color_primaries=bt709:color_trc=linear" -c:v hevc_nvenc -pix_fmt p010le -color_range 2 -colorspace bt709 -color_trc linear -tune hq -preset p4 -rc vbr -cq 12 -b:v 0M -metadata author="Allen Institute for Neural Dynamics" -maxrate 700M -bufsize 350M -f matroska -write_crc32 0'
FFMPEG_INPUT = "-colorspace bt709 -color_primaries bt709 -color_range 2 -color_trc linear"

video_writer = cameras.VideoWriterFfmpeg(frame_rate=60, container_extension="mp4", output_arguments=FFMPEG_OUTPUT_16BIT, input_arguments=FFMPEG_INPUT)

rig = AindBehaviorDirectedForagingRig(
    computer_name="TestRigComputer", 
    rig_name="test_rig", 
    data_directory=Path("../temp_data"),
    harp_delphi_controller=HarpDelphiController(port_name="COM4", enable_valve_leds=True),
    triggered_camera_controller=cameras.CameraController[cameras.SpinnakerCamera](
        frame_rate=60,
        cameras = {
            "MainCamera": cameras.SpinnakerCamera(
                serial_number="23113702", binning=1, exposure=3000, gain=0, video_writer=video_writer, adc_bit_depth=SpinnakerCameraAdcBitDepth.ADC10BIT
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
