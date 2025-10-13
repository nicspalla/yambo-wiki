# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "yambo-wiki"
copyright = "2025, Yambo Team"
author = "Yambo Team"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  "myst_parser",
  "sphinx_design",
  "sphinx.ext.todo",
  "sphinx_togglebutton",
  "sphinx_new_tab_link",
]

myst_enable_extensions = [
  "colon_fence",
]

togglebutton_hint = " " #Displayed when the toggle is closed
togglebutton_hint_hide = " " #Displayed when the toggle is open

source_suffix = {
  '.rst': 'restructuredtext',
  '.md' : 'markdown',
}

templates_path = ['_templates']

exclude_patterns = [
  'development/example_files',
]

# Display todos by setting to True
todo_include_todos = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

###
### COLORS FROM YAMBO WEBSITE
### - #bf69bb pink
### - #471c46 purple
### - #e37378 peach
### - #cd3a36 red
### - #e69225 yellow
### - #757575 gray
###

html_theme = 'furo'
html_title = "Yambo Wiki"

html_favicon = '_static/yambo_favicon.png'
html_logo = '_static/logo_main.png'

html_theme_options = {
    #
    "sidebar_hide_name": True,
    #
    "light_css_variables": {
        #
        "admonition-font-size": "1.0rem",
        "admonition-title-font-size": "1.0rem",
        #
        "color-brand-primary": "#BF69BB", #pink from yambo website
        "color-brand-content": "#BF69BB", #pink from yambo website
        #"color-brand-visited": "#471C46", #purple from yambo website
        #
        "color-background-secondary"     : "#faedf9", #light pink
        "color-card-marginals-background": "#faedf9", #light pink
        "color-inline-code-background"   : "#f8f9fb", #light gray
        "color-highlight-on-target"      : "#f7b5b8", #light peach
        "color-highlighted-background"   : "#f7b5b8", #light peach
    },
    #
    "dark_css_variables": {
        #
        "admonition-font-size": "1.0rem",
        "admonition-title-font-size": "1.0rem",
        #
        "color-brand-primary": "#BF69BB", #pink from yambo website
        "color-brand-content": "#BF69BB", #pink from yambo website
        #"color-brand-visited": "#471C46", #purple from yambo website
        #
        "color-background-secondary"     : "#2e122d", #dark purple
        "color-card-marginals-background": "#2e122d", #dark purple
        "color-inline-code-background"   : "#1f2024", #dark gray
        "color-highlight-on-target"      : "#a85458", #dark peach
        "color-highlighted-background"   : "#a85458", #dark peach
    },
}

html_static_path = ['_static']
html_css_files = ['custom.css']

