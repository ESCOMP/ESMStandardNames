# ESMStandardNames

The Earth System Modeling Standard Names Repository contains community-accepted
Standard Names, publishing tools, and search tools.

A Markdown file describing the standard names
[is included](https://github.com/ESCOMP/ESMStandardNames/blob/main/Metadata-standard-names.md).
Rules governing the designation and format of standard names can be found in [StandardNamesRules.rst](https://github.com/ESCOMP/ESMStandardNames/blob/main/StandardNamesRules.rst) 

Edits to standard names should be made in the xml file, using the included python tools to generate
the human-readable standard name Markdown file:
```
tools/write_standard_name_table.py standard_names.xml
```

Then, commit the new Metadata-standard-names.md file and push to GitHub.
