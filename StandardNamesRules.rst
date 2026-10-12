Standard Name Rules Have Moved
===============================

The ESM Standard Name rules have moved into a proper `Sphinx <https://www.sphinx-doc.org/>`_
documentation set, built by `Read the Docs <https://readthedocs.org/>`_, so that they can be
organized into browsable chapters instead of one long file.

The source for the rules now lives under `docs/chapters/ <docs/chapters/>`_ in this repository:

* `docs/chapters/naming_rules.rst <docs/chapters/naming_rules.rst>`_ -- ESM Standard Name rules
* `docs/chapters/technical_specifications.rst <docs/chapters/technical_specifications.rst>`_ -- Technical specifications
* `docs/chapters/reference.rst <docs/chapters/reference.rst>`_ -- Qualifiers, other common standard name components, acronyms/abbreviations/aliases, and units

See `docs/index.rst <docs/index.rst>`_ for the table of contents, or build the docs locally with::

    python -m pip install -r docs/requirements.txt
    cd docs && make html
