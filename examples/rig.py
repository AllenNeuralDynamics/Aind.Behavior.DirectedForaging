import os
from pathlib import Path

import aind_behavior_services.rig as rig

from aind_behavior_directed_foraging.rig import (
    AindBehaviorDirectedForagingRig,
    HarpDelphiController
)

rig = AindBehaviorDirectedForagingRig(
    computer_name="TestRigComputer", 
    rig_name="test_rig", 
    data_directory=Path("../temp_data"),
    harp_delphi_controller=HarpDelphiController(port_name="COM3", enable_valve_leds=True)
)

def main(path_seed: str = "./local/{schema}.json"):
    os.makedirs(os.path.dirname(path_seed), exist_ok=True)
    models = [rig]

    for model in models:
        with open(path_seed.format(schema=model.__class__.__name__), "w", encoding="utf-8") as f:
            f.write(model.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
