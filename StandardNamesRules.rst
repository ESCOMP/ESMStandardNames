.. # define a hard line break for HTML
.. |br| raw:: html

   <br />

*******************
CCPP Standard Names
*******************

This document contains information about the rules used to create Standard Names
for use with the Common Community Physics Package (CCPP). It describes the

* CCPP Standard Name rules
* Standard Name qualifiers
* Other common standard name components
* Acronyms, abbreviations, and aliases
* Units

.. _Rules

CCPP Standard Name Rules
========================

#. Standard names should be identical to those from the latest version
   of the `Climate and Forecast (CF) metadata
   conventions <https://cfconventions.org/standard-names.html>`_ unless
   an appropriate name does not exist in that standard, or the adoption
   of said names leads to inconsistencies in the naming convention.

#. When no suitable standard name exists in the CF conventions, the following guidelines should be followed for constructing a new name.
   The phrases in brackets are optional. The words in *italic* appear explicitly as stated,
   while the words in ``this font`` indicate other words or phrases to be substituted.
   The new standard name is constructed by joining the base standard name to the qualifiers using underscores.

   [``transformation``] [``component``] [``non-instant time``] base_name [*in* ``medium``] [*at* ``level``] [*due_to* ``process``] [``non-current time``] [*assuming* ``condition``]

   This construction was originally based on rules set forth in the
   `CF guidelines <http://cfconventions.org/Data/cf-standard-names/docs/guidelines.html>`_),
   but have since evolved for better consistency and generality across a broader set of fields
   than was originally envisioned by the CF conventions. "``medium``" should be specified when
   the variable in question is a substance or other quantity contained within some other medium
   (e.g. for ``mole_fraction_of_ozone_in_air``, the base name is "ozone", while the medium is "air"). 
   "Transformation" refers to descriptors such as "``tendency_of``", "``log10``", or other operations or processes describing some transformation or adjustment of a variable; a detailed list of possible transformations can be found `later in this document <#transformations>`_.
   Other parts of the construction provide information about a variable's horizontal surface
   (e.g. ``at_cloud_base``), component (i.e. direction of variable, e.g. ``downward``), process (e.g.
   ``due_to_deep_convection``), or condition (e.g., ``assuming_clear_sky``). These qualifications do not
   change the units of the quantity. This is not an exhaustive list of qualifiers that may be needed for a given standard name;
   see subsequent rules below for more information.

   The following table provides a few concrete examples of standard names and how they are constructed
   with respect to the guideline template.

.. image:: https://raw.githubusercontent.com/wiki/ESCOMP/CCPPStandardNames/images/standard_name_construction_examples.png
   :alt: image of table providing standard name construction examples

   Note that "transformations" are a special case, where multiple transformations may be applied,
   and multiple quantities may be compared, operated on, etc. For transformations involving
   multiple quantities (e.g. ``ratio_of_X_to_Y``; see the `section on Transformations <#transformations>`_
   for more information), the above formula may be extended around multiple base names.

.. image:: https://raw.githubusercontent.com/wiki/ESCOMP/CCPPStandardNames/images/standard_name_transformation_examples.png
   :alt: image of table providing standard name construction examples with multiple transformations

   In the latter example, ``ln`` is operating on the quantity ``water_vapor_partial_pressure_assuming_saturation``,
   while ``derivative_of`` is a combined transformation of ``water_vapor_partial_pressure_assuming_saturation``
   and ``air_temperature``. When multiple transformations are present, a more detailed description
   should be provided in the ``long_name`` field to prevent any possible ambiguity.

#. Variables are current and instantaneous unless specified. Variables that are not
   current (e.g., previous timestep) or non-instantaneous (e.g., accumulated values)
   should have qualifiers in the standard name to describe what they represent.

#. By default (when not specified otherwise), variables are grid means or centers
   (defined by the host). If a variable is defined at a different physical location,
   a qualifier should be used to denote this. For example, to specify the vertical
   location of a variable with respect to vertical grid cells, the following variants
   are possible:

   * ``[variable]``, with no location suffix, is defined at vertical-cell centers or
     as vertical-cell averages.

   * ``[variable]_at_interfaces`` is defined at the interfaces between grid cells
     vertically, including the bottom-most and top-most interfaces.
   * ``[variable]_at_top_interfaces`` is defined at the interfaces between grid cells
     vertically, including the top-most interface *but excluding the bottom-most
     interface*.

   * ``[variable]_at_bottom_interfaces`` is defined at the interfaces between grid
     cells vertically, including the bottom-most interface *but excluding the
     top-most interface*.

   This implies that if ``[variable]`` is defined on `n` points vertically,
   ``[variable]_at_interfaces`` is defined on `n+1` points,
   ``[variable]_at_top_interfaces`` is defined on `n` points, and
   ``[variable]_at_bottom_interfaces`` is defined on `n` points.

#. By default, *mixing_ratio* refers to mass mixing ratios. The long name should
   explicitly specify that it refers to the *mass* mixing ratio.
   Mass mixing ratios should contain information regarding
   with respect to what quantity they are defined, and options are *wrt_dry_air*,
   *wrt_moist_air*, or *wrt_moist_air_and_condensed_water*, where *moist_air*
   refers to dry air plus vapor and *moist_air_and_condensed_water* refers
   to dry air plus vapor and hydrometeors.

   Use of the term *specific_humidity* should be avoided, as there is no consensus on
   whether it refers to *water_vapor_mixing_ratio_wrt_moist_air* or
   *water_vapor_mixing_ratio_wrt_moist_air_and_condensed_water*.
   *total_water* can be used to designate water in every form, i.e. water
   vapor plus condensed water.

   Volume mixing ratios should be qualified as *volume_mixing_ratio*.

#. By default, *mole_fraction_of_X_in_Y* refers to the total amount of *Y*. So, for example,
   *mole_fraction_of_ozone_in_air* refers to the total amount of (moist) air. (In the case of air,
   the default meaning is moist air, as described in the *mixing ratio* rule.) When this is not
   the case, a qualifier should be used to denote this. *e.g.*, *mole_fraction_of_ozone_in_dry_air*.

#. When referring to soil quantities,
   *volume_fraction* should be used to express the volumetric soil moisture.

#. Number concentration should appear as a prefix, that is, *number_concentration_of*. By default,
   number concentrations are specified per unit of volume. When they are specified per
   unit of mass, they should be written as *mass_number_concentration_of*.

#. By default, *precipitation* refers to the sum of all phases of precipitating hydrometeors,
   for example rain plus graupel plus hail.  The term *frozen_precipitation* refers to the
   sum of all frozen precipitating hydrometers, for example graupel plus hail (but not rain).
   Otherwise the standard name should explicitly state the type of hydrometeor(s) the
   named quantity represents (e.g. *graupel*).

#. By default, the term *cloud* refers to all cloud phases and cloud types. Otherwise
   an additional prefix or suffix should be added to the standard name specifying what kind(s)
   of clouds the variable represents (e.g. *ice_cloud* if only including glaciated clouds, or
   *cloud_at_500hPa* if only including clouds that exist at 500 hPa).

#. If possible, qualifiers should be limited in order to allow for a wide
   applicability of the variable. In other words, don't qualify with ``_for_specific_context``
   unless a variable could not conceivably be used outside of the more
   narrowly-defined context or a variable without the scope-narrowing qualifiers
   already exists and cannot be reused.

   **Discouraged:** surface_upward_specific_humidity_flux_for_mellor_yamada_janjic_surface_layer_scheme

   **Preferred:** surface_upward_specific_humidity_flux

#. Spell out acronyms unless they are obvious to a vast majority of
   scientists/developers who may come across them. A
   list of currently-used acronyms and aliases is below.

#. For control-oriented variables, if the variable is a Fortran logical,
   use flag_for ``_X``. If it is any other data type, use control_for ``_X``. All flags
   should be Fortran logicals.

#. Reserved names: The prefix ``ccpp_`` represents CCPP framework-provided variables.
   All other standard names should avoid the use of ``ccpp`` in their name.

#. No punctuation should appear in standard names except for underscores (_).

#. Standard names are case insensitive, i.e. example = EXAMPLE.

.. _qualifiers:

Qualifiers
========================

black = existing CF qualifier

**bold** = **proposed new qualifier**

``this font`` = words or phrases to be substituted

XY-surface
----------

Prefixes
^^^^^^^^

None. Note that this is a departure from the CF conventions, which in
many cases - but not all - use surface_ as a prefix. This departure from
the CF convention is to maintain consistency with all other level
qualifiers that are used as _at_level-qualifier (i.e. as suffix).

Suffixes
^^^^^^^^

| at_adiabatic_condensation_level
| at_cloud_top
| at_convective_cloud_top
| at_cloud_base
| at_convective_cloud_base
| at_freezing_level
| at_ground_level
| at_maximum_wind_speed_level
| at_sea_ice_base
| at_sea_level
| at_top_of_atmosphere_boundary_layer
| at_top_of_atmosphere_model
| at_top_of_dry_convection
| **at_interfaces**
| **at_toa**
| **at_tropopause**
| **at_surface**
| **at_surface_adjacent_layer**
| **at_2m**
| **at_10m**
| **at_bottom_interface**
| **at_pressure_levels**
| **at_top_of_viscous_sublayer**
| **at_various_atmosphere_layers**
| **extended_up_by_1**


Component
---------

Prefixes
^^^^^^^^

| upward
| downward
| northward
| southward
| eastward
| westward
| x
| y

Special Radiation Component
---------------------------

Prefixes
^^^^^^^^

| net
| upwelling
| downwelling
| incoming
| outgoing

Medium
------

Suffixes
^^^^^^^^

| in_air
| in_atmosphere_boundary_layer
| in_mesosphere
| in_sea_ice
| in_sea_water
| in_soil
| in_soil_water
| in_stratosphere
| in_thermosphere
| in_troposphere
| in_atmosphere
| in_surface_snow
| **in_diurnal_thermocline**
| **in_canopy**
| **in_lake**
| **in_aquifer**
| **in_aquifer_and_saturated_soil**
| **in_convective_tower**
| **between_soil_bottom_and_water_table**

Process
-------

Suffixes
^^^^^^^^

| due_to_advection
| due_to_convection
| due_to_deep_convection
| due_to_diabatic_processes
| due_to_diffusion
| due_to_dry_convection
| due_to_gravity_wave_drag
| due_to_gyre
| due_to_isostatic_adjustment
| due_to_large_scale_precipitation
| due_to_longwave_heating
| due_to_moist_convection
| due_to_overturning
| due_to_shallow_convection
| due_to_shortwave_heating
| due_to_thermodynamics
| due_to_background
| **due_to_subgrid_scale_vertical_mixing**
| **due_to_convective_microphysics**
| **due_to_model_physics**
| **due_to_convective_gravity_wave_drag**
| **due_to_shoc**
| **due_to_dynamics**

Condition
---------

Suffixes
^^^^^^^^

| assuming_clear_sky
| assuming_deep_snow
| assuming_no_snow
| **over_land**
| **over_ocean**
| **over_ice**
| **for_momentum**
| **for_heat**
| **for_moisture**
| **for_heat_and_moisture**
| **assuming_shallow**
| **assuming_deep**

Time
----

Suffixes
^^^^^^^^

| **of_new_state**
| **on_physics_timestep**
| **on_dynamics_timestep**

| **on_radiation_timestep**
| **on_previous_timestep**
| ``N`` **_timesteps_back**
| **since_** ``T``

Computational
-------------

Prefixes
^^^^^^^^

| **lower_bound_of**
| **upper_bound_of**
| **unfiltered**
| **nonnegative**
| **flag_for**
| **control_for**
| **number_of**
| **index_of**
| **vertical_index_at**
| **vertical_dimension_of**
| **cumulative**
| **iounit_of**
| **filename_of**
| **frequency_of**
| **period_of**
| **XYZ_dimensioned**
| **tendency_of** ``X``
| **generic_tendency**
| **one_way_coupling_of** ``_X`` **_to** ``_Y``
| **tunable_parameter[s]_for** ``_X``
| **map_of**


Infixes
^^^^^^^

| **directory_for** ``_X`` **_source_code**
| **flag_for_reading** ``_X`` **_from_input**

Suffixes
^^^^^^^^

| **for_coupling**
| **for_chemistry_coupling**
| **from_coupled_process**
| **from_wave_model**
| **collection_array**
| **multiplied_by_timestep**
| **for_current_mpi_rank**
| **for_current_cubed_sphere_tile**
| **plus_one**
| **minus_one**
| **for_radiation**
| **for_deep_convection**
| **for_microphysics**

Transformations
---------------

Prefixes
^^^^^^^^
| change_over_time_in ``_X``
| convergence_of ``_X`` or horizontal_convergence_of ``_X``
| correlation_of ``_X`` _and ``_Y`` [_over ``_Z``]
| cosine_of ``_X``
| covariance_of ``_X`` _and ``_Y`` [_over ``_Z``]
| component_derivative_of ``_X``
| derivative_of ``_X`` _wrt ``_Y``
| direction_of ``_X``
| divergence_of ``_X`` or horizontal_divergence_of ``_X``
| histogram_of ``_X`` [_over ``_Z``]
| integral_of ``_Y`` _wrt ``_X``
| ln ``_X``
| log10 ``_X``
| lwe_thickness_of ``_X``
| magnitude_of ``_X``
| probability_distribution_of ``_X`` [_over ``_Z``]
| probability_density_function_of ``_X`` [_over ``_Z``]
| product_of ``_X`` _and ``_Y``
| ratio_of ``_X`` _to ``_Y``
| reciprocal_of ``_X``
| sine_of ``_X``
| square_of ``_X``
| standard_deviation_of ``_X``
| tendency_of ``_X``
| variance_of ``_X``
| volume_mixing_ratio_of ``_X``

Suffixes
^^^^^^^^
| ``X_`` mixing_ratio_wrt ``_Y``

Other common standard name components
=====================================

Reserved phrase
---------------

These words/phrases should not be used outside of the described context

+------------------------+-------------------------------------------------------------------------------------+
| **Phrase**             |  **Usage**                                                                          |
+========================+=====================================================================================+
| ccpp                   | Variable names provided by the CCPP framework                                       |
+------------------------+-------------------------------------------------------------------------------------+


Special phrases
---------------

+------------------------+-------------------------------------------------------------------------------------+
| **Phrase**             |  **Meaning**                                                                        |
+========================+=====================================================================================+
| anomaly                | difference from climatology                                                         |
+------------------------+-------------------------------------------------------------------------------------+
| area                   | horizontal area unless otherwise stated                                             |
+------------------------+-------------------------------------------------------------------------------------+
| atmosphere             | used instead of in_air for quantities which are large-scale rather than local       |
+------------------------+-------------------------------------------------------------------------------------+
| condensed_water        | liquid and ice                                                                      |
+------------------------+-------------------------------------------------------------------------------------+
|frozen_water            | ice                                                                                 |
+------------------------+-------------------------------------------------------------------------------------+
| longwave               | Longwave radiation. Defined as thermal emission of radiation from the planet.       |
+------------------------+-------------------------------------------------------------------------------------+
| moisture               | water in all phases contained in soil                                               |
+------------------------+-------------------------------------------------------------------------------------+
| ocean                  | used instead of in_sea_water for quantities which are large-scale rather than local |
+------------------------+-------------------------------------------------------------------------------------+
| shortwave              | Shortwave radiation. Defined as electromagnetic emissions from the sun              |
+------------------------+-------------------------------------------------------------------------------------+
| specific               | per unit mass unless otherwise stated                                               |
+------------------------+-------------------------------------------------------------------------------------+
| unfrozen_water         | liquid and vapor                                                                    |
+------------------------+-------------------------------------------------------------------------------------+
| water                  | water in all phases if not otherwise qualified                                      |
+------------------------+-------------------------------------------------------------------------------------+
| **dimensionless**      | **lacking units**                                                                   |
+------------------------+-------------------------------------------------------------------------------------+
| **kinematic**          | **refers to surface fluxes in "native" units (K m s-1 and kg kg-1 m s-1)**          |
+------------------------+-------------------------------------------------------------------------------------+
| **direct**             | **used in radiation (as opposed to diffuse)**                                       |
+------------------------+-------------------------------------------------------------------------------------+
| **diffuse**            | **used in radiation (as opposed to direct)**                                        |
+------------------------+-------------------------------------------------------------------------------------+

Chemical Species
----------------

+------------------------+
| **Species**            |
+========================+
|carbon_dioxide          |
+------------------------+
|dimethyl_sulfide        |
+------------------------+
|nitrate                 |
+------------------------+
|nitrate_and_nitrite     |
+------------------------+
|nitrite                 |
+------------------------+
|oxygen                  |
+------------------------+
|ozone                   |
+------------------------+
|phosphate               |
+------------------------+
|silicate                |
+------------------------+
|sulfate                 |
+------------------------+
|sulfur_dioxide          |
+------------------------+

Generic Names
-------------

The following names are used with consistent meanings and units as elements in
other standard names, although they are themselves too general to be chosen as
standard names. They are recorded here for reference only. These are not
standard names.

+-------------------------------------------+-----------------+
| **Generic Name**                          |  **Units**      |
+===========================================+=================+
| amount                                    | kg m-2          |
+-------------------------------------------+-----------------+
| area                                      | m2              |
+-------------------------------------------+-----------------+
| area_fraction                             | 1               |
+-------------------------------------------+-----------------+
| binary_mask                               | 1               |
+-------------------------------------------+-----------------+
| data_mask                                 | 1               |
+-------------------------------------------+-----------------+
| density                                   | kg m-3          |
+-------------------------------------------+-----------------+
| energy                                    | J               |
+-------------------------------------------+-----------------+
| energy_content                            | J m-2           |
+-------------------------------------------+-----------------+
| energy_density                            | J m-3           |
+-------------------------------------------+-----------------+
| frequency                                 | s-1             |
+-------------------------------------------+-----------------+
| frequency_of_occurrence                   | s-1             |
+-------------------------------------------+-----------------+
| heat_flux                                 | W m-2           |
+-------------------------------------------+-----------------+
| heat_transport                            | W               |
+-------------------------------------------+-----------------+
| streamfunction                            | m2 s-1          |
+-------------------------------------------+-----------------+
| velocity_potential                        | m2 s-1          |
+-------------------------------------------+-----------------+
| mass                                      | kg              |
+-------------------------------------------+-----------------+
| mass_flux                                 | kg m-2 s-1      |
+-------------------------------------------+-----------------+
| mass_fraction                             | 1               |
+-------------------------------------------+-----------------+
| mixing_ratio                              | kg kg-1         |
+-------------------------------------------+-----------------+
| mass_transport k                          | g s-1           |
+-------------------------------------------+-----------------+
| mole_fraction                             | 1               |
+-------------------------------------------+-----------------+
| mole_flux mol                             | m-2 s-1         |
+-------------------------------------------+-----------------+
| momentum_flux                             | Pa              |
+-------------------------------------------+-----------------+
| partial_pressure                          | Pa              |
+-------------------------------------------+-----------------+
| period                                    | s               |
+-------------------------------------------+-----------------+
| power                                     | W               |
+-------------------------------------------+-----------------+
| pressure                                  | Pa              |
+-------------------------------------------+-----------------+
| probability                               | 1               |
+-------------------------------------------+-----------------+
| radiative_flux                            | W m-2           |
+-------------------------------------------+-----------------+
| specific_eddy_kinetic_energy              | m2 s-2          |
+-------------------------------------------+-----------------+
| speed                                     | m s-1           |
+-------------------------------------------+-----------------+
| stress                                    | Pa              |
+-------------------------------------------+-----------------+
| temperature                               | K               |
+-------------------------------------------+-----------------+
| thickness                                 | m               |
+-------------------------------------------+-----------------+
| velocity                                  | m s-1           |
+-------------------------------------------+-----------------+
| volume                                    | m3              |
+-------------------------------------------+-----------------+
| volume_flux                               | m s-1           |
+-------------------------------------------+-----------------+
| volume_fraction                           | 1               |
+-------------------------------------------+-----------------+
| volume_mixing_ratio                       | mol mol-1       |
+-------------------------------------------+-----------------+
| volume_transport                          | m3 s-1          |
+-------------------------------------------+-----------------+
| vorticity                                 | s-1             |
+-------------------------------------------+-----------------+

.. _Aliases:

Acronyms, Abbreviations, and Aliases
====================================

+---------------------+---------------------------------------------------------+
| **Short**           |  **Meaning**                                            |
+=====================+=========================================================+
| ir                  | infrared                                                |
+---------------------+---------------------------------------------------------+
| lwe                 | liquid water equivalent                                 |
+---------------------+---------------------------------------------------------+
| max                 | maximum                                                 |
+---------------------+---------------------------------------------------------+
| min                 | minimum                                                 |
+---------------------+---------------------------------------------------------+
| nir                 | near-infrared part of the EM spectrum (radiation)       |
+---------------------+---------------------------------------------------------+
| stp                 | standard temperature (0 degC) and pressure (101325 Pa)  |
+---------------------+---------------------------------------------------------+
| tke                 | turbulent kinetic energy                                |
+---------------------+---------------------------------------------------------+
| toa                 | top of atmosphere                                       |
+---------------------+---------------------------------------------------------+
| uv                  | ultraviolet part of the EM spectrum (radiation)         |
+---------------------+---------------------------------------------------------+
| vis                 | visible part of the EM spectrum (radiation)             |
+---------------------+---------------------------------------------------------+
| wrt                 | with respect to                                         |
+---------------------+---------------------------------------------------------+

Units
=====

#. For variables with an existing match in the `Climate and Forecast (CF) metadata
   conventions <https://cfconventions.org/standard-names.html>`_, the units should
   be identical to the canonical units listed there

#. For variables without an existing match in the CF conventions, the units should
   follow the `International System of Units (SI/metric system) <https://www.nist.gov/pml/weights-and-measures/metric-si/si-units>`_

#. For dimensionless variables, the following units can be used:

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
