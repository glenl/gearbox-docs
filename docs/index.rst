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


Changes in V2.0
---------------

 * Uses Blender 4.3 release candidate.

 * Added straight bevel gears.

 * Added a gear rack node.

 * Added a beveled shaft

 * Reworked the cog mesh to allow better smoothing.

 * The clearance value was moved to an internal constant value.

 * The pressure angle is constrained to a reasonable range. As with
   all geometry nodes, if you want to over-ride any default, you can
   plug in the appropriate constant attribute node.

 * Categorized many node inputs into panels where appropriate.

 * Added a :ref:`working-notes` section in an attempt to
   keep the math organized.

 * Added a :ref:`modeling-tips` section to improve usability.


.. toctree::
   :maxdepth: 2
   :hidden:

   installation.rst
   nodes.rst
   modeling-tips.rst
   working-notes.rst
   examples.rst

Indices and tables
==================

* :ref:`genindex`
