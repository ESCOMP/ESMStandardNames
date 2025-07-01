# ESMStandardNames

The Earth System Modeling Standard Names Repository contains community-accepted Standard Names, publishing tools, and search tools.

Rules governing the designation and format of standard names can be found in [StandardNamesRules.rst](https://github.com/ESCOMP/ESMStandardNames/blob/main/StandardNamesRules.rst). 

A [Markdown file describing the standard names is included](https://github.com/ESCOMP/ESMStandardNames/blob/main/Metadata-standard-names.md), as well as a [Yaml version of the XML file](https://github.com/ESCOMP/ESMStandardNames/blob/main/Metadata-standard-names.yaml).

Edits to standard names must be made in the xml file `standard_names.xml` only. When pull requests are merged into the authoritative branch, a tool is run in GitHub actions that automatically updates the human-readable standard name Markdown file and the Yaml version.
