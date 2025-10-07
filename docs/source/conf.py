# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'yambo-wiki'
copyright = '2025, Yambo-Team'
author = 'Yambo-Team'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#BF69BB", #pink from yambo website
        "color-brand-content": "#BF69BB", #pink from yambo website
        "color-admonition-title-warning": "FF0000",
    },
    #
    "dark_css_variables": {
        "color-brand-primary": "#BF69BB", #pink from yambo website
        "color-brand-content": "#BF69BB", #pink from yambo website
    },
}

html_static_path = ['_static']
html_css_files = ['custom.css']

