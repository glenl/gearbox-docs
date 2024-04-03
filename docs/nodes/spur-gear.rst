.. _node-spur-gear:

*********
Spur Gear
*********

.. figure:: /images/nodes-spur_gear.png
   :align: right

   The Spur Gear node.

The **Spur Gear** group generates a simple spur gear.


See the section on :ref:`spur-gear-notes` in the :ref:`working-notes`
for more detail on the math used to generate this node group.

Inputs
======

|FLOAT| Module
   The module for this gear.

|INTEGER| Teeth
   The number of teeth on the gear.

|FLOAT| Pressure Angle
   The pressure angle in degrees.

|INTEGER| Flank Resolution
   This integer value sets the resolution of the sides of the gear
   cog. The default sets a reasonable default but set this lower if to
   control vertex count. Any large value may be reduced by distance
   merging in the implementation.

|FLOAT| Clearance Fac
   A value from :math:`[0\dots 1]` that is multiplied by the *Module*
   to determine addition depth on the dedendum.

|FLOAT| Depth
   The thickness of the gear.

|BOOLEAN| Half Pitch rotation
   All gears are created with a right side cog that straddles the
   X-axis. Checking this will rotate the gear a half a tooth thickness
   so that the root straddles the X-axis. This is convenient for
   meshing gears.

|FLOAT_FIELD_SINGLE| Hole Radius
   The size of the center hole. This may be zero. The upper bound is
   constrained so the hole can't be larger than the dedendum.

Outputs
=======

|GEOMETRY| Geometry
   The generated gear geometry.

|FLOAT| Ref. Pitch Radius
   The reference pitch radius of the generated gear. This is useful
   for setting the distance between two meshed gears.

|INTEGER| Teeth
   For convenience, the number of teeth on this gear.


.. _meshed-spur-example:

Examples
========

.. figure:: /images/eg-meshed_spur_01.png
   :align: right
   :width: 300

Spur gears are simple gears and this example shows how a basic gear
set can be constructed. The default values are used for both gears
with the exception of the number of teeth. The second 16-tooth gear is
translated by the sum of the *reference pitch radii* of the two gears.
The *Half pitch rotation* has been checked on the second gear so that
it properly aligns with the first gear.

.. figure:: /images/eg-meshed_spur_02.png
   :width: 800
