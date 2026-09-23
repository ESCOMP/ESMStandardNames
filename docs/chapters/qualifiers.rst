.. _qualifiers:

Qualifiers
========================

 * ``X``, ``Y``, ``Z``, etc. = words or phrases to be substituted
 * ``something[_optional]`` = "_optional" is an optional portion of the qualifier to include as needed

XY-surface
----------

Prefixes
^^^^^^^^

None. Note that this is a departure from the CF conventions, which in
many cases - but not all - use surface\_ as a prefix. This departure from
the CF convention is to maintain consistency with all other level
qualifiers that are used as _at_level-qualifier (i.e. as suffix), as well as
reducing ambiguity between different uses of the word "surface" (see above).

Suffixes
^^^^^^^^

| ``_at_adiabatic_condensation_level``
| ``_at_cloud_top``
| ``_at_convective_cloud_top``
| ``_at_cloud_base``
| ``_at_convective_cloud_base``
| ``_at_freezing_level``
| ``_at_ground_level``
| ``_at_maximum_wind_speed_level``
| ``_at_sea_ice_base``
| ``_at_sea_level``
| ``_at_top_of_atmosphere_boundary_layer``
| ``_at_top_of_atmosphere_model``
| ``_at_top_of_dry_convection``
| ``_at_interfaces``
| ``_at_toa``
| ``_at_tropopause``
| ``_at_surface``
| ``_at_surface_adjacent_layer``
| ``_at_2m``
| ``_at_10m``
| ``_at_bottom_interface``
| ``_at_pressure_levels``
| ``_at_top_of_viscous_sublayer``
| ``_at_various_atmosphere_layers``
| ``_extended_up_by_1``


Component
---------

Prefixes
^^^^^^^^

| ``upward``
| ``downward``
| ``northward``
| ``southward``
| ``eastward``
| ``westward``
| ``x``
| ``y``

Special Radiation Component
---------------------------

Prefixes
^^^^^^^^

| ``net_``
| ``upwelling_``
| ``downwelling_``
| ``incoming_``
| ``outgoing_``

Medium
------

Suffixes
^^^^^^^^

| ``_in_air``
| ``_in_atmosphere_boundary_layer``
| ``_in_mesosphere``
| ``_in_sea_ice``
| ``_in_sea_water``
| ``_in_soil``
| ``_in_soil_water``
| ``_in_stratosphere``
| ``_in_thermosphere``
| ``_in_troposphere``
| ``_in_atmosphere``
| ``_in_surface_snow``
| ``_in_diurnal_thermocline``
| ``_in_canopy``
| ``_in_lake``
| ``_in_aquifer``
| ``_in_aquifer_and_saturated_soil``
| ``_in_convective_tower``
| ``_between_soil_bottom_and_water_table``

Process
-------

Suffixes
^^^^^^^^

| ``_due_to_advection``
| ``_due_to_convection``
| ``_due_to_deep_convection``
| ``_due_to_diabatic_processes``
| ``_due_to_diffusion``
| ``_due_to_dry_convection``
| ``_due_to_gwd``
| ``_due_to_convective_gwd``
| ``_due_to_convective_whole_atmosphere_gwd``
| ``_due_to_orographic_gwd``
| ``_due_to_gyre``
| ``_due_to_isostatic_adjustment``
| ``_due_to_large_scale_precipitation``
| ``_due_to_longwave_heating``
| ``_due_to_moist_convection``
| ``_due_to_overturning``
| ``_due_to_shallow_convection``
| ``_due_to_pbl_processes``
| ``_due_to_shortwave_heating``
| ``_due_to_thermodynamics``
| ``_due_to_background``
| ``_due_to_subgrid_scale_vertical_mixing``
| ``_due_to_convective_microphysics``
| ``_due_to_model_physics``
| ``_due_to_shoc``
| ``_due_to_dynamics``

Condition
---------

Suffixes
^^^^^^^^

| ``_assuming_clear_sky``
| ``_assuming_deep_snow``
| ``_assuming_no_snow``
| ``_over_land``
| ``_over_ocean``
| ``_over_ice``
| ``_for_momentum``
| ``_for_heat``
| ``_for_moisture``
| ``_for_heat_and_moisture``
| ``_assuming_shallow``
| ``_assuming_deep``

Time
----

Suffixes
^^^^^^^^

| ``_of_new_state``
| ``_on_physics_timestep``
| ``_on_dynamics_timestep``
| ``_on_radiation_timestep``
| ``_on_previous_timestep``
| ``_N_timesteps_back``
| ``_since_T``
| ``_over_T``
| ``_reset_every_T``

Computational
-------------

Prefixes
^^^^^^^^

| ``lower_bound_of_``
| ``upper_bound_of_``
| ``unfiltered_``
| ``nonnegative_``
| ``is_``
| ``do_``
| ``identifier_for_``
| ``control_for_``
| ``number_of_``
| ``index_of_``
| ``vertical_index_at_``
| ``vertical_dimension_of_``
| ``cumulative_``
| ``iounit_of_``
| ``filename_of_``
| ``frequency_of_``
| ``period_of_``
| ``xyz_dimensioned_``
| ``tendency_of_X``
| ``generic_tendency_``
| ``one_way_coupling_of_X_to_Y``
| ``tunable_parameter[s]_for_X``
| ``map_of_``


Infixes
^^^^^^^

| ``directory_for_X_source_code``

Suffixes
^^^^^^^^

| ``_for_coupling``
| ``_for_chemistry_coupling``
| ``_from_coupled_process``
| ``_from_wave_model``
| ``_collection_array``
| ``_multiplied_by_timestep``
| ``_for_current_mpi_rank``
| ``_for_current_cubed_sphere_tile``
| ``_plus_one``
| ``_minus_one``
| ``_for_radiation``
| ``_for_deep_convection``
| ``_for_microphysics``

.. _transformations:

Transformations
---------------

Prefixes
^^^^^^^^
| ``change_over_time_in_X``
| ``convergence_of_X`` or ``horizontal_convergence_of_X``
| ``correlation_of_X_and_Y[_over_Z]``
| ``cosine_of_X``
| ``covariance_of_X_and_Y[_over_Z]``
| ``component_derivative_of_X``
| ``derivative_of_X_wrt_Y``
| ``direction_of_X``
| ``divergence_of_X`` or ``horizontal_divergence_of_X``
| ``histogram_of_X[_over _Z]``
| ``integral_of_Y_wrt_X``
| ``ln_X``
| ``log10_X``
| ``lwe_thickness_of_X``
| ``magnitude_of_X``
| ``probability_distribution_of_X[_over_Z]``
| ``probability_density_function_of_X[_over_Z]``
| ``product_of_X_and_Y``
| ``ratio_of_X_to_Y``
| ``reciprocal_of_X``
| ``sine_of_X``
| ``square_of_X``
| ``standard_deviation_of_X``
| ``tendency_of_X``
| ``variance_of_X``
| ``volume_mixing_ratio_of_X``

Suffixes
^^^^^^^^
| ``X_mixing_ratio_wrt_Y``
