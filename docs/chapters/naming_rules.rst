.. _Rules

ESM Standard Name Rules
========================

Constructing names
------------------

#. Standard names should be identical to those from the latest version
   of the `Climate and Forecast (CF) metadata
   conventions <https://cfconventions.org/standard-names.html>`_ unless
   an appropriate name does not exist in that standard, or the adoption
   of said names leads to inconsistencies in the naming convention.

#. When no suitable standard name exists in the CF conventions, the following guidelines should be followed for constructing a new name.
   The phrases in brackets are optional. The words in *italic* appear explicitly as stated,
   while the words in ``this font`` indicate other words or phrases to be substituted.
   The new standard name is constructed by joining the base standard name to the qualifiers using underscores.

   [``transformation``] [``component``] [``non-instant time``] base_name [*in*/*of* ``medium``] [*at* ``level``] [*due_to* ``process``] [``non-current time``] [*assuming* ``condition``]

   This construction was originally based on rules set forth in the
   `CF guidelines <http://cfconventions.org/Data/cf-standard-names/docs/guidelines.html>`_,
   but have since evolved for better consistency and generality across a broader set of fields
   than was originally envisioned by the CF conventions. "``medium``" should be specified when
   the variable in question is a substance or other quantity contained within some other medium
   (e.g. for ``mole_fraction_of_ozone_in_air``, the base name is "ozone", while the medium is "air").
   "Transformation" refers to descriptors such as "``tendency_of``", "``log10``", or other operations or processes describing some transformation or adjustment of a variable; a detailed list of possible transformations can be found :ref:`later in this document <transformations>`.
   Other parts of the construction provide information about a variable's horizontal surface
   (e.g. ``at_cloud_base``), component (i.e. direction of variable, e.g. ``downward``), process (e.g.
   ``due_to_deep_convection``), or condition (e.g., ``assuming_clear_sky``). These qualifications do not
   change the units of the quantity. This is not an exhaustive list of qualifiers that may be needed for a given standard name;
   see subsequent rules below for more information.

   The following table provides a few concrete examples of standard names and how they are constructed
   with respect to the guideline template.

   `image of table providing standard name construction examples <https://raw.githubusercontent.com/wiki/ESCOMP/ESMStandardNames/images/standard_name_construction_examples.png>`_

   Note that "transformations" are a special case, where multiple transformations may be applied,
   and multiple quantities may be compared, operated on, etc. For transformations involving
   multiple quantities (e.g. ``ratio_of_X_to_Y``; see the :ref:`section on Transformations <transformations>`
   for more information), the above formula may be extended around multiple base names.

   `image of table providing standard name construction examples with multiple transformations <https://raw.githubusercontent.com/wiki/ESCOMP/ESMStandardNames/images/standard_name_transformation_examples.png>`_

   In the latter example, ``ln`` is operating on the quantity ``water_vapor_partial_pressure_assuming_saturation``,
   while ``derivative_of`` is a combined transformation of ``water_vapor_partial_pressure_assuming_saturation``
   and ``air_temperature``. When multiple transformations are present, a more detailed description
   should be provided in the ``description`` field to prevent any possible ambiguity.

Variable scope
--------------

#. Variables are current and instantaneous unless specified. Variables that are not
   current (e.g., previous timestep) or non-instantaneous (e.g., accumulated values)
   should have qualifiers in the standard name to describe what they represent.

#. For accumulated variables, or variables representing a change over some period of time, the
   following suffixes are available":

   * ``over_[time]`` indicates an accumulation or other change over the previous duration/time
   * ``reset_every_[date/time]`` an accumulation or other change reset every set duration/time
     since the start of the simulation
   * ``since_[date/time]`` indicates an accumulation or other change since a given date/time.

   Dates, times, and durations should follow the `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`
   international standard, modified only to use lowercase rather than uppercase letters. Note that
   the standard is slightly different for dates and times vs durations. For example:

   * ``accumulated_precipitation_over_pt3h`` accumulated precipitation over the last 3 hours
   * ``accumulated_precipitation_over_p1dt12h`` accumulated precipitation over the last 1 day 12 hours
   * ``accumulated_precipitation_reset_every_pt1h`` accumulated precipitation reset every 1 hour
   * ``accumulated_precipitation_reset_every_p1y`` accumulated precipitation reset every 1 year
   * ``accumulated_precipitation_reset_every_p2dt12h`` accumulated precipitation reset every 2 days, 12 hours
   * ``accumulated_precipitation_since_20230522t120000`` accumulated precipitation since May 22, 2023 at 12:00
   * ``accumulated_precipitation_since_20251225`` accumulated precipitation since December 25, 2025
   * ``accumulated_precipitation_since_t00`` accumulated precipitation since 00:00:00 (midnight)

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

   This implies that if ``[variable]`` is defined on ``n`` points vertically,
   ``[variable]_at_interfaces`` is defined on ``n+1`` points,
   ``[variable]_at_top_interfaces`` is defined on ``n`` points, and
   ``[variable]_at_bottom_interfaces`` is defined on ``n`` points.

#. If possible, qualifiers should be limited in order to allow for a wide
   applicability of the variable. In other words, don't qualify with ``_for_specific_context``
   unless a variable could not conceivably be used outside of the more
   narrowly-defined context or a variable without the scope-narrowing qualifiers
   already exists and cannot be reused.

   **Discouraged:** upward_virtual_potential_temperature_flux_for_mellor_yamada_janjic_surface_layer_scheme

   **Preferred:** upward_virtual_potential_temperature_flux

#. If there are two identical quantities from different schemes/processes that
   need to be kept apart, suitable qualifiers are added to the names of the processes.
   If one process is already established and more common than the other, then it is
   sufficient to only prefix the new process with a suitable qualifier. Example:
   ``due_to_convective_GWD`` and ``due_to_convective_whole_atmosphere_GWD``
   as discussed in https://github.com/ESCOMP/ESMStandardNames/issues/79.

Terminology
-----------

   `annotated image detailing some of the terminology in this section <https://raw.githubusercontent.com/wiki/ESCOMP/ESMStandardNames/images/standard_name_terms.png>`_

#. A "layer" is a vertical level of a model. A variable for a given layer is either at the vertical
   centerpoint of a level, or the vertical average of a level, as defined by the host (see above).
   An "interface" is the boundary above or below a layer.

#. By default, *surface* refers to the liquid or solid substance immediately beneath the atmosphere
   for a given vertical column. This can be land, ocean, ice, lake, etc.

   For variables describing properties of the atmosphere near/adjacent to the actual surface,
   care should be taken to specify the specific "surface variable" quantity needed for a specific application:

   *  ``[variable]_at_surface`` is the lowest interface of the atmospheric model, adjacent to the surface.
      This is equivalent to the surface-adjacent/bottom interface (as described above).
   *  ``[variable]_at_surface_adjacent_layer`` is the bottom layer of the atmospheric model
   *  ``[variable]_at_[level]`` for variables defined at specific height above the surface, e.g. ``temperature_at_2m``, ``wind_at_10m``

   Note that some commonly used terms with a prefix ``surface_`` are unavoidable due to the common
   definition being fundamentally different from unqualified ``X``. For example, ``surface_skin_temperature``
   is a fundamentally different quantity than the unqualified ``skin_temperature``. In cases such as these,
   a comment should be included noting this special usage of the word "surface".

#. By default, `water` refers to all types of water in any phase (e.g. solid, liquid, gas,
   fresh water, salt water, etc.). The terms `sea` and `ocean` are synonymous, though new names
   should default to using `ocean` unless part of one of the following phrases:
   * sea_water
   * sea_ice
   * sea_level
   * sea_salt
   * sea_surface
   * sea_floor
   * sea_binary_mask
   * sea_area 

#. By default, *mixing_ratio* refers to mass mixing ratios. The description should
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

#. Spell out acronyms unless they are defined in the list of "Acronyms, Abbreviations, and Aliases"
   below. Whenever such an alias exist, use the alias in the
   standard name and the full term in the description.

#. Chemical species in standard names should be denoted by chemical formulae (e.g. ``co2``,
   ``ch4``, ``c5h8``) or commonly accepted designations (e.g. ``cfc12``); generally when there are
   multiple options the shorter name is preferred. A few species with well-established and
   unambiguous common names (e.g. water, ozone) are also included. In all cases, the standard name
   should include specific details about the substance's chemical makeup, as well as the
   phase/state of matter if relevant; e.g. ``water_vapor``, ``liquid_h2so4``

#. If the ionization of the chemical species is relevant, "ionized" should be included in the standard
   name as a prefix to the substance; e.g. ``number_density_of_ionized_he`` for ionized helium. If
   relevant, the net ionization charge should be included as a prefix (in words, because +/- are
   not valid standard name characters); e.g. ``number_density_of_plus_1_ionized_he``

#. For control-oriented variables, there are a few different prefixes that should be used depending on
   the use case for that specific variable:

   +-------------------+-----------+-----------------------------------------------------------------------------------------------+
   | **Prefix**        |  **Type** | **Use case**                    | **Example**                                                 |
   +===================+===========+=================================+=============================================================+
   | `is_`             | `logical` | A flag indicating some state or | `is_mpi_root` indicates whether or not the code is running  |
   |                   |           | condition is true or false      | on the MPI root process                                     |
   +-------------------+-----------+-------------------------------- +-------------------------------------------------------------+
   | `do_`             | `logical` | A flag whose value directs some | `do_chemical_tracer_diagnostics` indicates to a physics     |
   |                   |           | behavior                        | scheme that it should compute chemical tracer diagnostics   |
   +-------------------+-----------+---------------------------------+-------------------------------------------------------------+
   | `identifier_for_` | `integer` | A parameter indicating some     | `identifier_for_noah_land_surface_scheme` is an integer     |
   |                   |           | state or condition              | identifying the Noah land surface model                     |
   +-------------------+-----------+---------------------------------+-------------------------------------------------------------+
   | `control_for_`    | `integer` | A control whose value directs   | `control_for_land_surface_scheme` is an integer identifying |
   |                   |           | some behavior                   | the land surface scheme type                                |
   +-------------------+-----------+---------------------------------+-------------------------------------------------------------+
   | `index_of_`       | `integer` | An index entry for an array     | `index_of_ice_vegetation_category` is an index describing   |
   |                   |           |                                 | the location of the ice vegetation category in the array of |
   |                   |           |                                 | vegetation categories                                       |
   +-------------------+-----------+---------------------------------+-------------------------------------------------------------+

#. The ``direction`` of a vector, unless noted otherwise, is the geographical bearing measured in the positive clockwise direction from due north. For example, ``wind_to_direction = 90`` is the same as ``wind_from_direction = 270``, meaning wind blowing towards the east.

#. **Disallowed terms:** A few terms are disallowed as standard name components for various reasons; mostly due to
   ambiguity.

   - ``specific_humidity`` Disallowed due to ambiguity and different definitions between different fields. See above section describing ``mixing_ratio`` for more information.
   - ``amount`` In most contexts this word is superfluous, and in all contexts it is non-descriptive. Consider a more specific term such as ``mass_content``

#. **Reserved names:** The prefix ``ccpp_`` is reserved for CCPP framework-provided variables.
   All other standard names should avoid the use of ``ccpp`` in their name.
