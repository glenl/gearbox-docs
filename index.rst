.. _ref_manual:

Gearbox Asset Reference
=======================

This asset library contains a collection of geometry nodes that
generate mathematically accurate gears and gear-related items. My
:index:`goals` were to,

   * Challenge my math skills

   * Improve my geometry node skills

   * Generate gears that have a chance of working properly if printed

   * Create meshes that are topologically sound

.. index:: references

I'm not a mechanical engineer but the geometry of gears is well-known
and documented throughout the internet. This document doesn't do a
deep dive on the calculations but these sites will provide some useful
background,

   * `Wikipedia page on the Involute Gear
     <https://en.wikipedia.org/wiki/Involute_gear>`_ (nice animation here.)

   * `Wikipedia page on the Involute of a circle
     <https://en.wikipedia.org/wiki/Involute#Involutes_of_a_circle>`_

   * `tec-science
     <https://www.tec-science.com/category/mechanical-power-transmission/involute-gear/>`_


Changes in V1.3
---------------

 * Uses Blender 4.1-beta

 * Everything is now sized in meters instead of something
   smaller. This follows with the normal use of Blender and results in
   fewer problems when trying to merge vertices of very small
   components.

 * Added straight bevel gears.

 * Reworked the cog mesh, resulting in fewer vertices.

 * The pressure angle is constrained to a reasonable range. This was
   necessary because too large an angle can result in a base diameter
   below the root of the gear.

 * Categorized many node inputs into panels where.

 * Pumped up documentation, added :ref:`working-notes` in an attempt to
   keep the math organized.


:index:`Working in millimeters`

Gears in millimeters
--------------------

In early versions I was making an attempt to create gears in
millimeter sizes. Discovering the error of my ways or, at least, the
difficulties associated with trying to do that, I now just think in
meters and leave it up to the user to do any necessary scaling.

The following simple node set shows how to resize a spu gear with a
module of 3 to its _actual_ size in Blender. I believe most 3D
printers have the capability of scaling from whatever input.

.. figure:: /images/eg-mm_spur.png
   :width: 800


.. toctree::
   :maxdepth: 2
   :hidden:

   installation.rst
   nodes/bevel-gear.rst
   nodes/spur-gear.rst
   nodes/helical-gear.rst
   nodes/herringbone-gear.rst
   working-notes.rst

Indices and tables
==================

* :ref:`genindex`
