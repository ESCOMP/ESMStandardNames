.. _qualifiers:

Qualifiers
========================

``this font`` = words or phrases to be substituted

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
| at_interfaces
| at_toa
| at_tropopause
| at_surface
| at_surface_adjacent_layer
| at_2m
| at_10m
| at_bottom_interface
| at_pressure_levels
| at_top_of_viscous_sublayer
| at_various_atmosphere_layers
| extended_up_by_1


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
| in_diurnal_thermocline
| in_canopy
| in_lake
| in_aquifer
| in_aquifer_and_saturated_soil
| in_convective_tower
| between_soil_bottom_and_water_table

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
| due_to_gwd
| due_to_convective_gwd
| due_to_convective_whole_atmosphere_gwd
| due_to_orographic_gwd
| due_to_gyre
| due_to_isostatic_adjustment
| due_to_large_scale_precipitation
| due_to_longwave_heating
| due_to_moist_convection
| due_to_overturning
| due_to_shallow_convection
| due_to_pbl_processes
| due_to_shortwave_heating
| due_to_thermodynamics
| due_to_background
| due_to_subgrid_scale_vertical_mixing
| due_to_convective_microphysics
| due_to_model_physics
| due_to_shoc
| due_to_dynamics

Condition
---------

Suffixes
^^^^^^^^

| assuming_clear_sky
| assuming_deep_snow
| assuming_no_snow
| over_land
| over_ocean
| over_ice
| for_momentum
| for_heat
| for_moisture
| for_heat_and_moisture
| assuming_shallow
| assuming_deep

Time
----

Suffixes
^^^^^^^^

| of_new_state
| on_physics_timestep
| on_dynamics_timestep

| on_radiation_timestep
| on_previous_timestep
| ``N`` _timesteps_back
| since\_ ``T``
| over\_ ``T``
| reset_every\_ ``T``

Computational
-------------

Prefixes
^^^^^^^^

| lower_bound_of
| upper_bound_of
| unfiltered
| nonnegative
| is
| do
| identifier_for
| control_for
| number_of
| index_of
| vertical_index_at
| vertical_dimension_of
| cumulative
| iounit_of
| filename_of
| frequency_of
| period_of
| XYZ_dimensioned
| tendency_of ``X``
| generic_tendency
| one_way_coupling_of ``_X`` _to ``_Y``
| tunable_parameter[s]_for ``_X``
| map_of


Infixes
^^^^^^^

| directory_for ``_X`` _source_code

Suffixes
^^^^^^^^

| for_coupling
| for_chemistry_coupling
| from_coupled_process
| from_wave_model
| collection_array
| multiplied_by_timestep
| for_current_mpi_rank
| for_current_cubed_sphere_tile
| plus_one
| minus_one
| for_radiation
| for_deep_convection
| for_microphysics

.. _transformations:

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
