Standard Name Rules Have Moved
===============================

The ESM Standard Name rules have moved into a proper `Sphinx <https://www.sphinx-doc.org/>`_
documentation set, built by `Read the Docs <https://readthedocs.org/>`_, so that they can be
organized into browsable chapters instead of one long file. This branch demonstrates writing
the chapters in `MyST Markdown <https://myst-parser.readthedocs.io/>`_ instead of reStructuredText.

The source for the rules now lives under `docs/chapters/ <docs/chapters/>`_ in this repository:

* `docs/chapters/naming_rules.md <docs/chapters/naming_rules.md>`_ -- ESM Standard Name rules
* `docs/chapters/technical_specifications.md <docs/chapters/technical_specifications.md>`_ -- Technical specifications
* `docs/chapters/qualifiers.md <docs/chapters/qualifiers.md>`_ -- Qualifiers
* `docs/chapters/common_components.md <docs/chapters/common_components.md>`_ -- Other common standard name components
* `docs/chapters/aliases.md <docs/chapters/aliases.md>`_ -- Acronyms, abbreviations, and aliases
* `docs/chapters/units.md <docs/chapters/units.md>`_ -- Units

See `docs/index.md <docs/index.md>`_ for the table of contents, or build the docs locally with::

    python -m pip install -r docs/requirements.txt
    cd docs && make html
