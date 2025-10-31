# Configuration file for the Sphinx documentation builder.

import os
import sys

# Set the path FIRST, before any other imports
config_dir = os.path.dirname(os.path.abspath(__file__))  # docs/source
docs_dir = os.path.dirname(config_dir)                   # docs
project_root = os.path.dirname(docs_dir)                 # sphinx_test (where lumache.py is)
sys.path.insert(0, project_root)

import lumache
import sphinx_wagtail_theme

# -- Project information -----------------------------------------------------
html_baseurl = 'https://github.com/Aaron299792/Sphinx-Test/'

project = 'Lumache'
copyright = '2025, Graziella'
author = 'Graziella'
release = '0.1'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary', 
    'sphinx.ext.autosectionlabel',  # Fixed: added dot
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.todo',              # Fixed: added comma
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

# FIXED: Use string values instead of boolean
doctest_test_doctest_blocks = 'True'

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}

autosummary_generate = True
autosummary_imported_members = True
autosummary_ignore_module_all = False

# Don't generate duplicates in the main documentation
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
    "no-index": True,  # This prevents duplicate warnings
}

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_wagtail_theme'
html_theme_path = [sphinx_wagtail_theme.get_html_theme_path()]
html_show_sphinx = False


