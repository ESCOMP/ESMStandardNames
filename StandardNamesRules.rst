Standard Name Rules Have Moved
===============================

The ESM Standard Name rules have moved into a proper `Sphinx <https://www.sphinx-doc.org/>`_
documentation set, built by `Read the Docs <https://readthedocs.org/>`_, so that they can be
organized into browsable chapters instead of one long file.

The source for the rules now lives under `docs/chapters/ <docs/chapters/>`_ in this repository:

* `docs/chapters/naming_rules.rst <docs/chapters/naming_rules.rst>`_ -- ESM Standard Name rules
* `docs/chapters/technical_specifications.rst <docs/chapters/technical_specifications.rst>`_ -- Technical specifications
* `docs/chapters/qualifiers.rst <docs/chapters/qualifiers.rst>`_ -- Qualifiers
* `docs/chapters/common_components.rst <docs/chapters/common_components.rst>`_ -- Other common standard name components
* `docs/chapters/aliases.rst <docs/chapters/aliases.rst>`_ -- Acronyms, abbreviations, and aliases
* `docs/chapters/units.rst <docs/chapters/units.rst>`_ -- Units

See `docs/index.rst <docs/index.rst>`_ for the table of contents, or build the docs locally with::

    python -m pip install -r docs/requirements.txt
    sphinx-build -b html docs docs/_build/html
