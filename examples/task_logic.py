import os

import aind_behavior_services.task.distributions as distributions
from aind_behavior_curriculum import Stage, TrainerState
from aind_behavior_services.common import Point2f

from aind_behavior_directed_foraging.task_logic import (
    AindBehaviorDirectedForagingTaskLogic,
    AindBehaviorDirectedForagingTaskParameters,
    Trial,
    OdorDefinition,
    RadiusThreshold,
    RandomisedTimer,
    MaskRegion,
    FixedTimer
)

odorA = OdorDefinition(odor_id="OdorA", olfactometer_mask=1)
odorB = OdorDefinition(odor_id="OdorB", olfactometer_mask=2)

task_logic = AindBehaviorDirectedForagingTaskLogic(
    task_parameters=AindBehaviorDirectedForagingTaskParameters(
        trials = [
            Trial(odor_definition=odorA, release_time=0.5, dig_threshold=15, trial_timeout=15, threshold_reward=2, threshold_punishment=1),
            Trial(odor_definition=odorB, release_time=0.5, dig_threshold=15, trial_timeout=15, threshold_reward=2, threshold_punishment=1),
            Trial(odor_definition=odorA, release_time=0.5, dig_threshold=15, trial_timeout=15, threshold_reward=2, threshold_punishment=1),
            Trial(odor_definition=odorB, release_time=0.5, dig_threshold=15, trial_timeout=15, threshold_reward=2, threshold_punishment=1)
        ],
        # trigger_source=RadiusThreshold(trigger_type="radius", radius=60, trigger_center=Point2f(x=333, y=329)),
        trigger_source=RandomisedTimer(trigger_type="randomised_timer", distribution=distributions.UniformDistribution(distribution_parameters=distributions.UniformDistributionParameters(min=17, max=20))),
        # trigger_source=FixedTimer(trigger_type="fixed_timer", sequence=[5, 20, 30.06, 40, 50.2]),
        track_threshold=2,
        mask_region=MaskRegion(
            fill_value=150,
            mask_polygon=[
                Point2f(x=9, y=134),
                Point2f(x=323, y=76),
                Point2f(x=615, y=70),
                Point2f(x=719, y=120),
                Point2f(x=719, y=539),
                Point2f(x=269, y=539),
                Point2f(x=0, y=539),
                Point2f(x=9, y=277),
            ]
        )
    )
)


def main(path_seed: str = "./local/example_{schema}.json"):
    example_task_logic = task_logic
    example_trainer_state = TrainerState(
        stage=Stage(name="example_stage", task=example_task_logic), curriculum=None, is_on_curriculum=False
    )
    os.makedirs(os.path.dirname(path_seed), exist_ok=True)
    models = [example_task_logic, example_trainer_state]

    for model in models:
        with open(path_seed.format(schema=model.__class__.__name__), "w", encoding="utf-8") as f:
            f.write(model.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
