.. _ref_manual:

Gearbox Asset Reference
=======================

This asset library contains a collection of geometry nodes that
generate mathematically accurate gears and gear-related items. My
goals were to,

   * Challenge my math skills

   * Improve my geometry node skills

   * Generate gears that have a chance of working properly if printed

   * Create meshes that are topologically sound


Gear Geometry
-------------

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

If you have not played with spur gears before, the basic thing to
learn is that two meshing gears must have the same *module* and
*profile curve* value. The module declares the length of the
*addendum*, that part of the cog above the *pitch radius*, as well as
the length of the *dedendum*, the part of the cog below the *pitch
radius*. The *profile curve* has a role in the shape of the flank and
is better explained by the references above. The default is a
reasonable value.

.. tip:: If you want a physically larger gear, increase the module
         size.

.. index:: Pitch Diameter

The gear's module (:math:`m`) and the number of teeth (:math:`z`) are
the main inputs to a gear's size. Two gears coincide at their pitch
point and the diameter of the gear at that point can be given as,

.. math:: D_{pitch} = m \times z

.. index:: Tip Diameter

As mentioned earlier the *module* is the length of the gear's cog
above the pitch radius, so the diameter at the tip is,

.. math:: D_{tip} = D_{pitch} + ( m \times 2 )

To construct a set of gears with a specific diameter start with the
number of teeth and the target diameter, then derive the *module*,

.. math::

   D_{tip} &= D_{pitch} + ( m \times 2 ) \\
           &= (m \times z) + ( m \times 2 ) \\
           &= m \times (z + 2) \\
         m &= \frac{D_{tip}}{z+2}

.. figure:: /images/eg-index_diameter_01.png
   :align: right

Of course, we never do math in our head, we use geometry nodes. I've
constructed an example using a 12-toothed :ref:`node-spur-gear` joined
with a grid. The target diameter is 1M. This beast of a gear is then
translated so that the lower left corner is aligned with the origin to
clarify the dimensions. Modifying either DIAMETER or TEETH will result
in a grid and gear with matching bounds.

.. figure:: /images/eg-index_diameter_02.png
   :align: center
   :width: 800

Regarding clearance
-------------------

The *clearance* value for gears defines additional space added to the
root between two cogs to allow for the passage of cog of an opposing
gear. When gears are cut, these are created somewhat naturally by the
machine tool and usually form a circular shape. That is not strictly
necessary and, in fact, it would create substantially more topology
than I was willing to add. The *whole depth* is the total size of the
gear's cog, from tip to root,

.. math::

   Depth_{whole} = (2 \times m) + (clearance \times m)

The default clearance is usually sufficient.


.. toctree::
   :maxdepth: 2
   :hidden:

   installation.rst
   nodes/helical-gear.rst
   nodes/spur-gear.rst

Indices and tables
==================

* :ref:`genindex`
