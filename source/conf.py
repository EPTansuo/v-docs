# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'verilog-docs'
copyright = '2024, EPTansuo'
author = 'EPTansuo'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'
source_encoding = 'utf-8-sig'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

source_suffix = ['.rst', '.md', '.MD']
extensions = [
  "myst_parser",
]

myst_enable_extensions = ["colon_fence"]

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']



html_domain_indices = True

