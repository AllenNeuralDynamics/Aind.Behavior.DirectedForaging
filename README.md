# aind-behavior-directed-foraging

![CI](https://github.com/AllenNeuralDynamics/Aind.Behavior.DirectedForaging/actions/workflows/aind-behavior-directed-foraging-cicd.yml/badge.svg)
[![License](https://img.shields.io/badge/license-MIT-brightgreen)](LICENSE)
[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

A repository for the Directed Foraging task.

---

## General instructions

This repository follows the project structure laid out in the [Aind.Behavior.Services repository](https://github.com/AllenNeuralDynamics/Aind.Behavior.Services).

---

## Prerequisites

[Pre-requisites for running the project can be found here](https://allenneuraldynamics.github.io/Aind.Behavior.Services/articles/requirements.html).

---

## Deployment

For convenience, once third-party dependencies are installed, `Bonsai` and `python` virtual environments can be bootstrapped by running:

```powershell
./scripts/deploy.ps1
```

from the root of the repository.

## Generating settings files

The task is instantiated by a set of three settings files that strictly follow a DSL schema. These files are:

- `task_logic.json`
- `rig.json`
- `session.json`

Examples on how to generate these files can be found in the `./examples` directory of the repository. Once generated - e.g. by ```uv run .\examples\session.py ``` - these are the only required inputs to run the Bonsai workflow in `./src/main.bonsai`.

The workflow can thus be executed using the [Bonsai CLI](https://bonsai-rx.org/docs/articles/cli.html):

```powershell
"./bonsai/bonsai.exe" "./src/main.bonsai" -p SessionPath=<path-to-session.json> -p RigPath=<path-to-rig.json> -p TaskLogicPath=<path-to-task_logic.json>
```

## Regenerating schemas

DSL schemas can be modified in `./src/aind_behavior_directed_foraging/rig.py` (or `(...)/task_logic.py`).

Once modified, changes to the DSL must be propagated to `json-schema` and `csharp` API. This can be done by running:

```powershell
 uv run .\src\aind_behavior_directed_foraging\regenerate.py
```

## Designing a Directed Foraging Experiment

### Rig

In general, the settings file for the `rig` should change very little on any given experimental rig, we just need to define the appropriate COM ports and camera serial numbers once the rig is set up. You may also want to modify the `data_directory` where data is logged occasionally.

### Session

As the name suggests, a `session` settings file should be generated for each experimental session, as it contains information specific to that sessions such as subject ID and experiment date and time.

### Task Logic

#### Trials

The `task_logic` settings file is where the majority of the actualy experiment design occurs. An example is provided in `examples\task_logic.py`.

An experiment is made up of a set of `trials` and a `trigger_source`. The trial list defines a sequence of odor releases and the associated reward parameters. For example, an odor can be defined as:

```
odorA = OdorDefinition(odor_id="OdorA", olfactometer_mask=1)
```

The `olfactometer_mask` here defines which valve(s) should be used to load the odor, in the above case this will load odorA on the 1st valve of the olfactometer. The `olfactometer_mask` is structured as a bitmask, 1 = 0001 and opens valve 1, 2 = 0010 and opens valve 2, 3 = 0011 and opens both valves 1 and 2. This odor definition can then be used to define a trial, for example:

```
Trial(odor_definition=odorA, release_time=0.5, dig_threshold=15, trial_timeout=15, threshold_reward=2, threshold_punishment=1)
```

When this trial is triggered it will release odorA for 0.5s. After release the trial will finish after 15 seconds, but if the subject reaches a dig threshold of 15 it will be given 2 pellets and an additional 1 second of time before the next trial is loaded.

#### Triggers

The `task_logic` definition allows for 3 types of triggers:

- `RadiusThreshold`: a trigger that occurs when a subject is within a certain radius of a central point.
- `RandomisedTimer`: a trigger that occurs periodically with a random interval between triggers.
- `FixedTimer`: a trigger that occurs periodically with predefined intervals between triggers. This can also be used to 'replay' a previous experiment by choosing the fixed triggers from trial initiation times of a previous dataset.

An example of a radius trigger:
```
RadiusThreshold(trigger_type="radius", radius=60, trigger_center=Point2f(x=333, y=329))
```

Triggers when subject is within 60 pixels of a center point in the camera image of (333, 329).

An example of a randomised trigger:
```
RandomisedTimer(trigger_type="randomised_timer", distribution=distributions.UniformDistribution(distribution_parameters=distributions.UniformDistributionParameters(min=17, max=20)))
```

Triggers randomly with intervals between 17 and 20s drawn from a uniform distribution.

An example of a fixed trigger:
```
FixedTimer(trigger_type="fixed_timer", sequence=[5, 20, 30.06, 40, 50.2])
```

Triggers at the times listed in `sequence`.

#### Tracking

Another important part of the `task_logic` are the tracking parameters. The `track_threshold` parameter defines the threshold value applied to segment the tracked subject from the background. `mask_region` allows the experimenter to define a set of polygon masks that can be used to exclude parts of the image for tracking, for example for masking external walls or fixed objects in the experiment arena. Each `MaskRegion` has a `fill_value` and a polygon definition. `mask_polygon` contains a sequence of points that define the shape of the polygon, and `fill_value` specifies what grayscale value to 'fill' the mask region with. This is important for tracking as e.g. if we have a white arena and are tracking a black subject, we want to fill the masked region close to white to that it is not picked up by the tracking algorithm.

Picking the points for a mask region can be done initially in the `main.bonsai` workflow. Run the workflow and then navigate to the `Tracking` sub-workflow. Double-click the `MaskPolygon` operator to open the visualizer, and then select the `Regions` editor on the property grid to define individual mask regions (drag to create new region, click to select region, double right-click to add control point). Once done, expand the `Regions` section of the property grid and copy the points over the `task_logic` settings.
