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

