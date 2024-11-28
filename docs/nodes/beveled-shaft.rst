.. _beveled-shaft:

*************
Beveled Shaft
*************

.. figure:: /images/nodes-beveled_shaft.png
   :align: right

   The Beveled Shaft node group.

The **Beveled Shaft** group generates a simple shaft with an
adjustable bevel at each end. These can be useful for gear shafts or
smaller pins or dowels. Nothing super fancy here except an object that
was used in several examples.

Inputs
======

|INTEGER| Vertices
    Circular resolution of the shaft.

|FLOAT| Radius
    Radius of cylinder that forms the shaft.

|FLOAT| Length
    End-to-end length of the shaft

|FLOAT| Width
    The width of the bevel.

|INTEGER_FIELD_SINGLE| Resolution
    The width and resolution of the bevel on each end of the shaft.


Outputs
=======

|GEOMETRY| Mesh
   The generated gear mesh.
