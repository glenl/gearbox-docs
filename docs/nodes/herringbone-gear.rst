.. _herringbone-gear:

****************
Herringbone Gear
****************

.. figure:: /images/nodes-herringbone_gear.png
   :align: right

   The Herringbone Gear node.

The **Herringbone Gear** group generates a set of helical gears
stacked with opposing helix angles.


Inputs
======

|FLOAT| Module
   The module for this gear.

|INTEGER| Teeth
   The number of teeth on the gear.

|FLOAT| Pressure Angle
   The pressure angle in degrees.

|FLOAT| Depth
   The thickness of the gear.

|FLOAT_FIELD_SINGLE| Hole Radius
   The size of the center hole. This may be zero. The upper bound is
   constrained so the hole can't be larger than the dedendum.

|BOOLEAN| Half pitch rotation
   All gears are created with a right side cog that straddles the
   X-axis. Checking this will rotate the gear a half a tooth thickness
   so that the root straddles the X-axis. This is convenient for
   meshing gears.

|INTEGER| Flank Resolution
   This integer value sets the resolution of the sides of a gear
   tooth. The default is a reasonable value, setting it lower will
   reduce vertex count at the expense of smoothness. Any large value
   may be reduced by distance merging in the implementation.

|FLOAT| Gap
   The distance between the two helical components that form the
   herringbone.

|FLOAT| Angle
   The angle, in degrees, specifed from :math:`90^\circ` on the
   Z-axis.

|BOOLEAN| Left twist
   Negates the *Helix Angle* for meshing gears. For the herringbone
   this sets the angle of the lower gear and an opposite twist is
   given to the upper gear.

|INTEGER_FIELD_SINGLE| Z Faces
   The integer number of horizontal slices that form the resolution of
   the helix. The default is a reasonable value for :math:`20^\circ` but
   you may need more for larger values..

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

.. figure:: /images/eg-herringbone_01.png
   :align: right
   :width: 300

   12 to 16 herringbone gear set.

Here is a simple example of a 12-to-16 herringbone gear set.

.. figure:: /images/eg-herringbone_02.png

   Geometry node network for a meshed herringbone gear set.

As in spur gears, each member of a gear set has the same module and
pressure angle. In addition, for any gear with a helix angle it is
necessary that one member have an apposing twist. For this gear set is
was also necessary to tick the *half pitch notatation* on one of the
gears.
