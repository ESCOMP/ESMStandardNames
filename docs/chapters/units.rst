.. _units_section:

Units
=====

Entries in the Standard Names dictionary contain a "units" property that serves to indicate the
typical/recommended units for a given variable. It is not mandatory to use the indicated units exactly,
but any use of a given standard name variable should have units of the same dimensionality.

When adding a new standard name, units should follow the `International System of Units (SI/metric system) <http://nist.gov/pml/owm/metric-si/si-units>`_.
If the new standard name has an existing match in the `Climate and Forecast (CF) metadata
conventions <https://cfconventions.org/standard-names.html>`_, the units should be identical to the canonical units listed there

For dimensionless variables, the following units can be used:

+------------------------+-----------------------------------------------------------------------------------------------+
| **Unit**               |  **Use case**                                                                                 |
+========================+===============================================================================================+
| count                  | integers that describe the dimension/length of an array                                       |
+------------------------+-----------------------------------------------------------------------------------------------+
| flag                   | logicals/booleans that can be either true or false                                            |
+------------------------+-----------------------------------------------------------------------------------------------+
| index                  | integers that can be an index in an array                                                     |
+------------------------+-----------------------------------------------------------------------------------------------+
| kg kg-1                | mass mixing ratios                                                                            |
+------------------------+-----------------------------------------------------------------------------------------------+
| m3 m-3                 | volume fraction (e.g. for soil moisture)                                                      |
+------------------------+-----------------------------------------------------------------------------------------------+
| mol mol-1              | molar mixing ratios (also volumetric mixing ratio for gases)                                  |
+------------------------+-----------------------------------------------------------------------------------------------+
| none                   | strings and character arrays                                                                  |
+------------------------+-----------------------------------------------------------------------------------------------+
| fraction               | fractions not listed above, typically valid in the range [0,1]                                |
+------------------------+-----------------------------------------------------------------------------------------------+
| percent                | fractions expressed in percent, typically ranging from 0% to 100%                             |
+------------------------+-----------------------------------------------------------------------------------------------+
| 1                      | any number (integer, real, complex) not listed above, e.g. scaling factors, error codes, etc. |
+------------------------+-----------------------------------------------------------------------------------------------+
