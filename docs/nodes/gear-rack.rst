.. _node-gear-rack:

**********
Gear Rack
**********


.. figure:: /images/nodes-gear_rack.png
   :align: right

   The Gear Rack node.


A rack, or toothed bar, is simply an unwinding of a cylindrical gear
and can be thought of as a gear with an infinite diameter. The
important sizing variable, like any other gear, is the
*module*. Increasing the tooth count will only increase the length of
the rack. The same rules as any other gear meshing apply: to fit a
gear to a rack, they must have the same *module* value and
*pressure angle*.

Inputs
======

|FLOAT| Module
   The module for this gear.

|INTEGER| Teeth
   The number of teeth on the gear.

|FLOAT| Pressure Angle
   The pressure angle in degrees. This effects the shape of the gear
   as it does in other types of gears. This directly changes the slope
   of the sides of gear without changing the pitch, resulting larger
   or smaller tip sizes. In most cases, this value should match the
   pressure angle of the gear to which it is being meshed.

|FLOAT| Height
   The height of the rack. This is measured from the base to the
   bottom of the tooth, not counting the clearance.

|FLOAT_FIELD_SINGLE| Clearance Fac
   A value from :math:`[0\dots 1]` that is multiplied by the *module*
   to determine addition depth on the dedendum.

|FLOAT_FIELD_SINGLE| Depth
   The thickness of the rack.

|FLOAT_FIELD_SINGLE| Angle
   The angle of the helix. This defaults to :math:`0^\circ` to form a
   straight gear rack.

|BOOLEAN_FIELD_SINGLE| Left Hand
   The direction of the helix.


Outputs
=======

|GEOMETRY| Geometry
   The output gear rack geometry.

|FLOAT| Pitch height
   The height from the base to the pitch line. Like circular gears,
   this value provides the distance necessary for meshing.

|INTEGER| Teeth
   For convenience, the number of teeth on this gear.
