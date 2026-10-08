# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

project = "ESM Standard Names"
copyright = "ESCOMP"
author = "ESCOMP"

extensions = ["myst_parser"]

# Chapters use plain CommonMark links like [text](other.md#heading) rather than
# MyST's {ref}/(label)= syntax, so GitHub and IDE previews render them too;
# this makes heading ids resolvable for those links.
myst_heading_anchors = 3

# naming_rules.md anchors #mixing_ratio with a raw <a id=...> tag (it marks a
# list item, not a heading), which myst's own xref checker can't see even
# though the link resolves correctly in the built HTML.
suppress_warnings = ["myst.xref_missing"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
