"""Sphinx configuration."""
project = "Testing_Hypermodern"
author = "George Lenton"
copyright = "2022, George Lenton"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
