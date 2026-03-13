# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import django

# Make the project root importable by autodoc
sys.path.insert(0, os.path.abspath('../..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
os.environ.setdefault('SECRET_KEY', 'sphinx-doc-build')
os.environ.setdefault('DJANGO_ALLOWED_HOSTS', 'localhost')
os.environ.setdefault('DEBUG', '0')
django.setup()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Orange County Lettings'
copyright = '2026, Gresse Mickael'
author = 'Gresse Mickael'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pyramid'
html_static_path = ['_static']
html_css_files = ['custom.css']
