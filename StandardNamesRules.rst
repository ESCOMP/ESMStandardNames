Standard Name Rules Have Moved
===============================

The ESM Standard Name rules have moved into a proper `Sphinx <https://www.sphinx-doc.org/>`_
documentation set, built by `Read the Docs <https://readthedocs.org/>`_, so that they can be
organized into browsable chapters instead of one long file. This branch demonstrates writing
the chapters in plain CommonMark/GFM Markdown instead of reStructuredText (parsed by
`myst-parser <https://myst-parser.readthedocs.io/>`_, but without MyST-specific syntax, so the
files also render correctly on GitHub and in a typical IDE's Markdown preview).

The source for the rules now lives under `docs/chapters/ <docs/chapters/>`_ in this repository:

* `docs/chapters/naming_rules.md <docs/chapters/naming_rules.md>`_ -- ESM Standard Name rules
* `docs/chapters/technical_specifications.md <docs/chapters/technical_specifications.md>`_ -- Technical specifications
* `docs/chapters/vocabulary.md <docs/chapters/vocabulary.md>`_ -- Qualifiers, other common standard name components, acronyms/abbreviations/aliases, and units

See `docs/index.md <docs/index.md>`_ for the table of contents, or build the docs locally with::

    python -m pip install -r docs/requirements.txt
    cd docs && make html
