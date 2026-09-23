# ESMStandardNames

The Earth System Modeling Standard Names Repository contains community-accepted Standard Names, publishing tools, and search tools.

Rules governing the designation and format of standard names are published as a chaptered
Sphinx/Read the Docs site built from the [docs/](docs/) directory; see
[docs/index.rst](https://github.com/ESCOMP/ESMStandardNames/blob/main/docs/index.rst) for the
table of contents, or build it locally with `sphinx-build -b html docs docs/html`.

A [Markdown file describing the standard names is included](https://github.com/ESCOMP/ESMStandardNames/blob/main/Metadata-standard-names.md), as well as a [YAML version of the XML file](https://github.com/ESCOMP/ESMStandardNames/blob/main/Metadata-standard-names.yaml).

Edits to standard names must be made in the xml file `standard_names.xml` only. When a pull request is opened into the main branch, the YAML and Markdown files should be updated using the `tools/write_standard_name_table.py` script. This can be done manually by the pull request author, or by activating the GitHub action available on an open pull request.
