.. _tech_specs:

Technical specifications
========================

#. The standard name dictionary consists of a number of individual XML elements:
   one ``standard_name`` element for each entry. A standard name entry consist of a ``name`` attribute
   that represents the variable name, and (optionally) a ``description`` attribute that gives
   a detailed description of what that name represents. Note that the ``description`` field is only
   provided for information and disambiguation only (though it should be unique), and does not need to be included for
   individual implementations of the standard names. This is not necessarily the same as the ``long_name`` entry as described
   in the `CCPP Technical Documentation <https://ccpp-techdoc.readthedocs.io/en/latest/CompliantPhysicsParams.html#ccpp-arg-table>`_,
   but it can be used to inform the contents of that field. The ``standard_name`` XML entry also contains a nested
   ``type`` entry, indicating the data type that a ``standard_name`` should represent, and as an attribute the
   physical units of that variable quantity (see the :ref:`section on Units <units_section>`). For example, the element
   for the variable name ``exner_function`` may look similar to this::

    <standard_name name="exner_function"
                   description="exner function, (p/p0)^(Rd/cp), where p0 is 1000 hPa">
      <type units="1">real</type>
    </standard_name>

   This XML element indicates that the variable ``exner_function`` represents the quantity described by the ``description``
   attribute. It is a real variable with units of "1", meaning it is non-dimensional and
   does not correspond to a more descriptive non-dimensional type such as "fraction"; see the :ref:`section on Units <units_section>`
   for more details.

   The standard_name elements are grouped into sections by "section" elements. These are parsed out into human-readable sections
   in the generated markdown file (``Metadata-standard-names.md``). Sections can contain nested sections for further categorization.
   Standard Names should be sorted alphabetically by name within a given section. A python tool ``tools/sort_standard_names.py`` is
   provided to sort the names automatically.

#. Only alphanumeric, punctuation, and whitespace characters from the ASCII character set may be used in the standard_names dictionary.
   The "name" attributes of ``standard_name`` entries (i.e. the standard names themselves) are further restricted to the character set of capital/lowercase letters, numerals, and ``_`` (underscore).

#. The `<type>` element should include a value that is one of the following valid Fortran types:

   - ``integer``
   - ``real``
   - ``logical``
   - ``character``
   - ``complex``
   - ``ddt`` (derived data type)

#. The standard name dictionary XML file should validate according to the schema file ``standard_names.xsd`` All of the above specifications should be coded into this schema file as is appropriate.
