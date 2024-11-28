.. _motor:

*****
Motor
*****

The **Motor** node takes a speed in RPM and outputs the appropriate
axial rotation for the scene.

.. figure:: /images/nodes-motor.png
   :align: right

   The **Motor** node group

======
Inputs
======

|BOOLEAN_FIELD_SINGLE| Invert
    Reverse the rotation of the output.

|FLOAT_FIELD_SINGLE| RPM
    Rotations Per Minute, sets the desired rotation speed.

|VECTOR_FIELD_SINGLE| Axis
    The axis on which to set the rotation.

=======
Outputs
=======

|VECTOR_FIELD_SINGLE| Rotation
    A rotation vector that can be used to rotation some geometry.

|FLOAT_FIELD_SINGLE| Angle
    The rotation represented in radians.
