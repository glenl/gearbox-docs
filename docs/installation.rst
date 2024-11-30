.. _installation:

==============
 Installation
==============

This product is delivered as a zip file containing the blend file and
an associated asset catalog file. An asset file is nothing more than a
blend file containing node groups (in this case) marked as
assets. When properly installed, the assets can accessed in the
geometry node editor from the `Add` dropdown menu or by dragging from
the asset browser.

Two methods of installation are described here, both require that your
`File Paths` are set up properly.

.. figure:: /images/install-pref_dialog.png
   :align: center

   The Asset Library section in the preferences dialog

If you've not installed any assets the `Path:` may be defined but not
created. Make sure that folder exists. You may want to do what I did
and point to a folder of your choosing. The `Import Method` defaults
to `Append` and should be left that way.

Method #1
=========

  1. Unzip the distributed file into a temporary folder

  2. Open the asset's blend file with Blender

  3. The `Asset Browser` will be open in the top-left of
     the workspace. The `Asset Library` entry should be set to
     `Current File`.

  4. Click on `Copy Bundle to Asset Library`, then select `User
     Library`.

  5. Close blender

This will copy the necessary files and add a `Gearbox` entry to your
asset library. The temporary folder is no longer needed and you can
copy the Gearbox zip file to a location for possible future
re-installations.

Method #2
=========

If you prefer to organize your own assets, all you need to do
is copy the unzipped blend file somewhere under the `User Library`
folder. If you do nothing else, the gearbox assets will be found in an
area named `Unassigned`. If you want them to appear under something
called `Gearbox`, you will need to open the blend file, select
`Current File` in the `Asset Browser` and do the manual work of
creating and modifying the asset catalog file.

Some links to the Blender documentation,

  * `Blender Asset Browser <https://docs.blender.org/manual/en/latest/editors/asset_browser.html>`_

  * `Blender Asset Library <https://docs.blender.org/manual/en/latest/files/asset_libraries/index.html>`_
