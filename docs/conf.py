# Configuration file for the Sphinx documentation builder.

# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import datetime

# -- Project information -----------------------------------------------------

# The full version, including alpha/beta/rc tags
version = release = 'v2.0'

project = 'Gearbox %s Reference' % version
copyright = f': {datetime.date.today().year} by Glen Larsen'
author = 'Glen (g60) Larsen'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python' : ('https://docs.python.org/3/', None),
    'sphinx' : ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = 'sphinx'
html_use_smartypants = True

source_suffix = '.rst'
master_doc = 'index'

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'
try:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    del sphinx_rtd_theme
except ModuleNotFoundError:
    pass

# A dictionary of options that influence the look and feel of
# the selected theme. These are theme-specific.
html_theme_options = {}
html_theme_path = []
if html_theme == "sphinx_rtd_theme":
    html_css_files = ["css/theme_tweaks.css"]
    html_theme_options = {
        # included in the title
        "display_version": False,
        "collapse_navigation": True,
        "navigation_depth": -1,
        "logo_only" : False
    }

    extensions.append('sphinx_rtd_theme')

html_static_path = ['_static']

rst_prolog = """
.. |GEARBOX_VERSION| replace:: %s
.. |OBJECT| image:: /images/glyph-socket_object.svg
.. |MATERIAL| image:: /images/glyph-socket_material.svg
.. |COLLECTION| image:: /images/glyph-socket_collection.svg
.. |GEOMETRY| image:: /images/glyph-socket_geometry.svg
.. |BOOLEAN_FIELD| image:: /images/glyph-socket_boolean_field.svg
.. |BOOLEAN_FIELD_SINGLE| image:: /images/glyph-socket_boolean_field_single.svg
.. |BOOLEAN| image:: /images/glyph-socket_boolean.svg
.. |FLOAT_FIELD| image:: /images/glyph-socket_float_field.svg
.. |FLOAT_FIELD_SINGLE| image:: /images/glyph-socket_float_field_single.svg
.. |FLOAT| image:: /images/glyph-socket_float.svg
.. |INTEGER_FIELD| image:: /images/glyph-socket_integer_field.svg
.. |INTEGER_FIELD_SINGLE| image:: /images/glyph-socket_integer_field_single.svg
.. |INTEGER| image:: /images/glyph-socket_integer.svg
.. |VECTOR_FIELD| image:: /images/glyph-socket_vector_field.svg
.. |VECTOR_FIELD_SINGLE| image:: /images/glyph-socket_vector_field_single.svg
.. |VECTOR| image:: /images/glyph-socket_vector.svg
.. |IMAGE| image:: /images/glyph-socket_image.svg
.. |COLOR| image:: /images/glyph-socket_color.svg
.. |COLOR_FIELD| image:: /images/glyph-socket_color_field.svg
.. |COLOR_FIELD_SINGLE| image:: /images/glyph-socket_color_field_single.svg
""" % version

rst_epilog = """
.. |GEARBOX_ZIPFILE| replace:: gearbox-assets-%s.zip
""" % version

# If true, “(C) Copyright …” is shown in the HTML footer.
html_show_copyright = True

# If true, “Created using Sphinx” is shown in the HTML footer.
html_show_sphinx = True

#html_logo = "_static/gearbox-logo.svg"
