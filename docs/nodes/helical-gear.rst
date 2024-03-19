.. _helical-gear:

************
Helical Gear
************

.. figure:: /images/nodes-helical_gear.png
   :align: right

   The Helical Gear node.

The **Helical Gear** group generates a spur gear with a helical twist.


Inputs
======

|FLOAT| Module
   The module for this gear.

|INTEGER| Teeth
   The number of teeth on the gear.

|FLOAT| Pressure Angle
   The pressure angle in degrees. A typical value is the default
   :math:`20^\circ` but some gears may need a slight tweak. This value
   influences the shape of the gear flank.

|INTEGER| Flank Resolution
   This integer value sets the resolution of the sides of the gear
   cog. The default sets a reasonable default but set this lower if to
   control vertex count. Any large value may be reduced by distance
   merging in the implementation.

|FLOAT_FIELD_SINGLE| Clearance Fac
   A value from :math:`[0\dots 1]` that is multiplied by the *Module*
   to determine addition depth on the dedendum.

|FLOAT| Depth
   The thickness of the gear.

|BOOLEAN| Half pitch rotation
   All gears are created with a right side cog that straddles the
   X-axis. Checking this will rotate the gear a half a tooth thickness
   so that the root straddles the X-axis. This is convenient for
   meshing gears.

|FLOAT_FIELD_SINGLE| Hole Radius
   The size of the center hole. This may be zero. The upper bound is
   constrained so the hole can't be larger than the dedendum.

|FLOAT| Twist Degrees
   The angle, in degrees, specifed from :math:`90^\circ` on the
   Z-axis. For two meshing helical gears the angle of the second gear
   must have the negated angle value of the first.

|BOOLEAN| Left twist
   Negates the *Helix Angle* for meshing gears.

|INTEGER_FIELD_SINGLE| Z Faces
   The integer number of horizontal slices that form the resolution of
   the helix. The default is a reasonable value for :math:`20^\circ` but
   you may need more for :math:`45^\circ`.

Outputs
=======

|GEOMETRY| Geometry
   The generated gear geometry.

|FLOAT| Ref. Pitch Radius
   The reference pitch radius of the generated gear. This is useful
   for setting the distance between two meshed gears.

|INTEGER| Teeth
   For convenience, the number of teeth on this gear.


Examples
========
.. figure:: /images/eg-meshed_helical_01.png
   :align: right

This example is similar to the
:ref:`meshed spur <meshed-spur-example>`
but notice how with meshed helical gears, the
second gear has a negative matching helix angle.

.. figure:: /images/eg-meshed_helical_02.png
   :align: center
   :width: 800
