json-schema
-------------
The following json-schemas are used as the format definition of the input for this task. They are the result of the `Pydantic`` models defined in `src/aind_behavior_directed_foraging`, and are also used to generate `src/Extensions/AindBehaviorDirectedForaging.cs` via `Bonsai.Sgen`.

`Download Schema <https://raw.githubusercontent.com/AllenNeuralDynamics/Aind.Behavior.DirectedForaging/main/src/DataSchemas/aind_behavior_directed_foraging.json>`_

Task Logic Schema
~~~~~~~~~~~~~~~~~
.. jsonschema:: https://raw.githubusercontent.com/AllenNeuralDynamics/Aind.Behavior.DirectedForaging/main/src/DataSchemas/aind_behavior_directed_foraging.json#/$defs/AindBehaviorDirectedForagingTaskLogic
   :lift_definitions:
   :auto_reference:


Rig Schema
~~~~~~~~~~~~~~
.. jsonschema:: https://raw.githubusercontent.com/AllenNeuralDynamics/Aind.Behavior.DirectedForaging/main/src/DataSchemas/aind_behavior_directed_foraging.json#/$defs/AindBehaviorDirectedForagingRig
   :lift_definitions:
   :auto_reference:
