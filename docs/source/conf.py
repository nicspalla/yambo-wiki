# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'YAMBO docs'
copyright = '2025, The Yambo Project'
author = 'The Yambo Project'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_theme_options = {
        'link'           : '#bf69bb',
        'sidebar_link'   : '#bf69bb',
        'sidebar_header' : '#471c46',
        'pre_bg'         : '#eeeeee',
        'warn_bg'        : '#ffffff',
        'warn_border'    : '#cc3a35',
        'note_bg'        : '#ffffff',
        'note_border'    : '#0693e3',
        'seealso_bg'     : '#ffffff',
        'seealso_border' : '#00d084',
        #
        'narrow_sidebar_bg'   : '#471c46',
        'narrow_sidebar_fg'   : '#ffffff',
        'narrow_sidebar_link' : '#bf69bb',
        #
        'head_font_family'    : 'monospace',
        'font_family'         : 'monospace',
        'caption_font_family' : 'monospace',
        'font_size'           : '15px',
        'code_font_size'      : '15px',
        #
        'fixed_sidebar'   : True,
        'show_powered_by' : False,
}

html_static_path = ['_static']
html_css_files = ['custom.css']
