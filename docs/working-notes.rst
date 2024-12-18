.. _working-notes:

*************
Working Notes
*************

This chapter captures some notes that I needed as this library was
developed.

.. _spur-gear-notes:

==================
Spur Gear Geometry
==================

.. index::
   single: spur gear; module
   single: spur gear; pitch radius
   single: spur gear; profile curve
   single: spur gear; teeth count

The gear's *module* (:math:`m`) and the *number of teeth* (:math:`z`)
are the main inputs to a gear's size. Two meshing gears **must** have
matching *module* and *profile curve* values. The *profile curve* has
a role in the shape of the flank and is better explained by the
references above. The default is a reasonable value.  The *module*
declares the length of the :index:`addendum`, that part of the cog
above the :index:`pitch radius`, as well as the length of the
:index:`dedendum`, the part of the cog below the :index:`pitch
radius`.

.. index::
   single: spur gear; pitch diameter

Two gears coincide at their pitch point and the diameter of the gear
at that point is known as the *pitch diameter*.

.. math:: D_{pitch} = m \times z

.. tip:: If you want a physically larger gear, increase the module
         size.

.. index:: spur gear; tip diameter

As mentioned earlier the *module* is the length of the gear's cog
above the pitch radius, so the diameter at the tip is,

.. math:: D_{tip} = D_{pitch} + ( m \times 2 )

To construct a set of gears with a specific diameter start with the
number of teeth and the target diameter, then derive the *module*,

.. math::
   :nowrap:

   \begin{eqnarray}
   D_{tip} & = & D_{pitch} + ( m \times 2 ) \\
           & = & (m \times z) + ( m \times 2 ) \\
           & = & m \times (z + 2) \\
         m & = & \frac{D_{tip}}{z+2}
   \end{eqnarray}

Spur gear on plane
~~~~~~~~~~~~~~~~~~

.. figure:: /images/eg-index_diameter_01.png
   :align: right
   :width: 300

Here is an example of creating a gear that fits into a specific
dimension using geometry nodes. We start with the TARGET shown as a
rectanglular grid that is 80mm square and we want to fit a 14-tooth
spur gear onto it.

.. figure:: /images/eg-index_diameter_02.png
   :align: center
   :width: 800

   Geometry nodes for calculating the module from a target diameter.

Remember that the very first step to working with these nodes is to
set the Scene Properties to the proper Units. Refer to the
:ref:`modeling-setup` section for more details.

Angle at base
~~~~~~~~~~~~~

The shape of a gear is controlled by the *pressure angle*. The angle
controls the width at the base as well as the spur tip. Gears with
small pressure angles will have a wider root and thicker tip than
those with a larger pressure angle.

.. math::
   :nowrap:

   \begin{eqnarray}
      Angle_{base} = 2 \times \frac{\pi}{(2 \times z)} + \tan\alpha - \alpha
   \end{eqnarray}


Regarding clearance
~~~~~~~~~~~~~~~~~~~

The :index:`clearance` value for gears defines additional space added to the
root between two cogs to allow for the passage of the tip of a cog of
an opposing gear. When gears are cut, these are created somewhat
naturally by the machine tool and usually form a circular shape. That
is not strictly necessary and, in fact, it would create
more topology than I was willing to add. The :index:`whole depth` is the
total size of the gear's cog, from tip to root,

.. math::

   Depth_{whole} = (2 \times m) + (clearance \times m)

The default clearance is usually sufficient.


.. _bevel-gear-notes:

===========
Bevel Gears
===========

If you visualize spur gears as two cylinders rotating against each
other, a pair of bevel gears can be seen as two cones rotating against
each other. These cones are known as *pitch cones* because the pitch
radius slides along the edge of the cone and, just like spur gears,
they are sized according to their *module* and number of teeth.

The first figure in the next section shows this visualization from a
side view.

.. _pitch-cone:

The Pitch Cone
~~~~~~~~~~~~~~

.. figure:: /images/ref-cone-angle.png
   :width: 400
   :align: center

   Reference Cone Angle

.. index::
   single: bevel gear; pitch cone
   single: bevel gear; cone angle

This drawing shows a generalized bevel gear set with the pitch
:index:`cone angles` (:math:`\delta_1` and :math:`\delta_2`) where the
sum :math:`\sum` doesn't equal :math:`90^\circ`. When the number of
teeth (:math:`z`) in the pinion is equal to the number of teeth in the
bull gear (a gear ratio of :math:`1:1`), and the gears are set at a
:math:`90^\circ` angle, they are known as miter gears.

The sum of the pitch cone angles is known as the :index:`shaft angle`,
usually annotated as :math:`\Sigma`,

.. math::
   :label: shaft-angle
   :nowrap:

   \begin{eqnarray}
      \Sigma = \delta_1 + \delta_2
   \end{eqnarray}

.. math::
   :label: pitch-cone
   :nowrap:

   \begin{eqnarray}
      \tan \delta_1 & = & \frac{\sin\Sigma}{\frac{z_2}{z_1}+\cos\Sigma} \\
      \tan \delta_2 & = & \frac{\sin\Sigma}{\frac{z_1}{z_2}+\cos\Sigma}
   \end{eqnarray}

Bevel gears must be considered in pairs since the tooth counts will
affect the pitch cone angle. For the miter gear described earlier (set
at a right angle with :math:`z_1 = z_2`), the above calculation will
result in a pitch cone angle of :math:`45^\circ`.

It is typically necessary to provide the pitch cone angles during
construction of the bevel gear, which can be determined with this
derivation,

.. math::
   :label: pitch-cone-angle
   :nowrap:

   \begin{eqnarray}
      \tan \delta_1 & = & \frac{\sin\frac{\pi}{2}}{\frac{z_2}{z_1}+\cos\frac{\pi}{2}} \\
      \delta_1 & = & \arctan{\frac{1}{\frac{z_2}{z_1}}} \\
      \delta_1 & = & \arctan{\frac{z_1}{z_2}}
   \end{eqnarray}


For bevel gearing, the :index:`reference diameter` :math:`d` is known
as the pitch diameter. The equations should look familiar (:math:`m`
is the module of the gear),

.. math::
   :label: ref-diameter
   :nowrap:

   \begin{eqnarray}
      d_1 & = & z_1 \times m \\
      d_2 & = & z_2 \times m
   \end{eqnarray}

The :index:`cone distance` (:math:`R`) defines the linear distance between the
reference points at the intersection of the reference diameters,

.. math::
   :label: cone-distance
   :nowrap:

   \begin{eqnarray}
      R = \frac{d_2}{2\times\sin \delta_2}
   \end{eqnarray}

.. index::
   single: bevel gear; tooth profile

Face Width
~~~~~~~~~~

The face width (:math:`b`) is the distance across the gear teeth and
length should match for a bevel gear pair. Not much is said
about this but the going recommendation is,

.. math::
   :label: face-width
   :nowrap:

   \begin{eqnarray}
      b < \frac{R}{3}
   \end{eqnarray}


==========
Gear Racks
==========


.. figure:: /images/gear-rack-detail.svg
   :align: center
   :width: 300

   Basic dimensions of a gear rack

Where,

.. math::
   :label: gear-rack
   :nowrap:

   \begin{eqnarray}
      m & = & module \\
      \alpha & = & pressure\ angle \\
      h & = & 2\times{m} \\
      pitch & = & m\times\pi
   \end{eqnarray}

As with other types of gears, sizing a rack depends on the :math:`m`
value and the shape of the cog depends on :math:`\alpha`. As
:math:`\alpha` increases the tip and root get narrower.  The center of
the tooth is the pitch line and is analogous to a circular gear's
pitch diameter.

Not shown in the diagram is a small clearance below the root (between
the gears). This clearance is defined in terms of a factor multiplied
by the module to set the depth and is hardcoded to :math:`0.25`.


==========
References
==========

 * `Spur Gears wiki
   <https://en.wikipedia.org/wiki/Spur_gear>`_

 * `Bevel Gears wiki
   <https://en.wikipedia.org/wiki/Bevel_gear>`_

 * `Wikipedia page on the Involute Gear
   <https://en.wikipedia.org/wiki/Involute_gear>`_ (nice animation here.)

 * `Wikipedia page on the Involute of a circle
   <https://en.wikipedia.org/wiki/Involute#Involutes_of_a_circle>`_

 * `tec-science
   <https://www.tec-science.com/category/mechanical-power-transmission/involute-gear/>`_
