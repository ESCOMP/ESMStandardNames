# CCPP Standard Name Library
#### Table of Contents
* [base_names](#base_names)
* [dimensions](#dimensions)
* [constants](#constants)
* [coordinates](#coordinates)
* [state_variables](#state_variables)
* [land_surface](#land_surface)
* [diagnostics](#diagnostics)
* [atmospheric_composition](#atmospheric_composition)
* [atmospheric_composition: GOCART aerosols](#atmospheric_composition-gocart-aerosols)
* [required framework-provided variables](#required-framework-provided-variables)
* [optional framework-provided variables](#optional-framework-provided-variables)
* [system variables](#system-variables)
* [GFS_typedefs_GFS_control_type](#gfs_typedefs_gfs_control_type)
* [GFS_typedefs_GFS_interstitial_type](#gfs_typedefs_gfs_interstitial_type)
* [GFS_typedefs_GFS_tbd_type](#gfs_typedefs_gfs_tbd_type)
* [GFS_typedefs_GFS_sfcprop_type](#gfs_typedefs_gfs_sfcprop_type)
* [GFS_typedefs_GFS_coupling_type](#gfs_typedefs_gfs_coupling_type)
* [GFS_typedefs_GFS_statein_type](#gfs_typedefs_gfs_statein_type)
* [GFS_typedefs_GFS_cldprop_type](#gfs_typedefs_gfs_cldprop_type)
* [GFS_typedefs_GFS_radtend_type](#gfs_typedefs_gfs_radtend_type)
* [GFS_typedefs_GFS_grid_type](#gfs_typedefs_gfs_grid_type)
* [GFS_typedefs_GFS_stateout_type](#gfs_typedefs_gfs_stateout_type)

## base_names
Base names are the 'elemental' quantities from which
the more complex standard names are constructed.
Base names can roughly be broken down into three categories:
### generic_names
The following names are too general to be chosen as
standard names, but they can serve as base names for
more specific standard names.
* `amount`: amount
    * `real`: units = kg m-2
* `area`: area
    * `real`: units = m2
* `area_fraction`: area_fraction
    * `real`: units = 1
* `binary_mask`: binary_mask
    * `integer`: units = 1
* `coefficient`: coefficient
    * `real`: units = 1
* `data_mask`: data_mask
    * `real`: units = 1
* `density`: density
    * `real`: units = kg m-3
* `energy`: energy
    * `real`: units = J
* `energy_content`: energy_content
    * `real`: units = J m-2
* `energy_density`: energy_density
    * `real`: units = J m-3
* `frequency`: frequency
    * `real`: units = s-1
* `heat_flux`: heat_flux
    * `real`: units = W m-2
* `heat_transport`: heat_transport
    * `real`: units = W
* `mass`: mass
    * `real`: units = kg
* `mass_flux`: mass_flux
    * `real`: units = kg m-2 s-1
* `mass_fraction`: mass_fraction
    * `real`: units = 1
* `mixing_ratio`: mixing_ratio
    * `real`: units = kg kg-1
* `mass_transport`: mass_transport
    * `real`: units = kg s-1
* `mole_fraction`: mole_fraction
    * `real`: units = 1
* `mole_flux`: mole_flux
    * `real`: units = mol m-2 s-1
* `momentum_flux`: momentum_flux
    * `real`: units = Pa
* `partial_pressure`: partial_pressure
    * `real`: units = Pa
* `period`: period
    * `real`: units = s
* `power`: power
    * `real`: units = W
* `pressure`: pressure
    * `real`: units = Pa
* `probability`: probability
    * `real`: units = 1
* `radiative_flux`: radiative_flux
    * `real`: units = W m-2
* `radius`: radius
    * `real`: units = m
* `specific_eddy_kinetic_energy`: specific_eddy_kinetic_energy
    * `real`: units = m2 s-2
* `speed`: speed
    * `real`: units = m s-1
* `stress`: stress
    * `real`: units = Pa
* `streamfunction`: streamfunction
    * `real`: units = m2 s-1
* `temperature`: temperature
    * `real`: units = K
* `thickness`: thickness
    * `real`: units = m
* `velocity`: velocity
    * `real`: units = m s-1
* `velocity_potential`: velocity_potential
    * `real`: units = m2 s-1
* `volume`: volume
    * `real`: units = m3
* `volume_flux`: volume_flux
    * `real`: units = m s-1
* `volume_fraction`: volume_fraction
    * `real`: units = 1
* `volume_mixing_ratio`: volume_mixing_ratio
    * `real`: units = mol mol-1
* `volume_transport`: volume_transport
    * `real`: units = m3 s-1
* `vorticity`: vorticity
    * `real`: units = s-1
### chemical_species
These are the base names for specific chemical species
* `c5h8`: Isoprene
* `co2`: Carbon dioxide
* `co`: Carbon monoxide
* `ccl4`: Tetrachloromethane
* `cfc11`: Trichlorofluoromethane
* `cfc12`: Dichlorodifluoromethane
* `cfc113`: 1,1,2-Trichloro-1,2,2-trifluoroethane
* `cfc22`: Chlorodifluoromethane
* `dimethyl_sulfide`: Dimethyl sulfide; DMS
* `hcho`: Formaldehyde
* `hydrophilic_black_carbon`: hydrophilic_black_carbon
* `hydrophobic_black_carbon`: hydrophobic_black_carbon
* `hydrophilic_organic_carbon`: hydrophilic_organic_carbon
* `hydrophobic_organic_carbon`: hydrophobic_organic_carbon
* `methane`: ch4
* `n2o`: Nitrous Oxide, N_2O
* `nitrate`: Chemical species containing the nitrate ion
* `nitrite`: Chemical species containing the nitrite ion
* `no2`: Nitrogen dioxide
* `no`: Nitric oxide NO (Nitrogen oxide, Nitrogen monoxide)
* `oxygen`: Molecular oxygen, O_2
* `ozone`: Ozone, O_3
* `phosphate`: Chemical species containing the phosphate ion
* `silicate`: Chemical species containing the silicate ion
* `sulfate`: Chemical species containing the sulfate ion
* `sulfur_dioxide`: so2
### base_standard_names
These names are used as bases for other names, but may
also be considered standard names on their own. See the
full list of standard names for further details.
* `absolute_vorticity`: absolute_vorticity
* `air_potential_temperature`: air_potential_temperature
* `air_pressure`: air_pressure
* `air_pressure_thickness`: air_pressure_thickness
* `air_temperature`: air_temperature
* `albedo`: albedo
* `atmosphere_heat_diffusivity`: atmosphere_heat_diffusivity
* `cloud_area_fraction`: cloud_area_fraction
* `cloud_condensate`: cloud_condensate
* `cloud_ice`: cloud_ice
* `cloud_liquid_water`: cloud_liquid_water
* `date`: date
* `density`: density
* `diffuse_nir_albedo`: diffuse near-infrared albedo
* `diffuse_nir_shortwave_flux`: diffuse near-infrared shortwave flux
* `diffuse_shortwave_albedo`: diffuse_shortwave_albedo
* `diffuse_uv_and_vis_shortwave_flux`: diffuse ultraviolet and visible shortwave flux
* `diffuse_vis_albedo`: diffuse visible albedo
* `direct_nir_albedo`: direct near-infrared albedo
* `direct_nir_shortwave_flux`: direct near-infrared shortwave flux
* `direct_uv_and_vis_shortwave_flux`: direct ultraviolet and visible shortwave flux
* `direct_vis_albedo`: direct visible albedo
* `divergence`: divergence
* `dry_air_density`: dry_air_density
* `dry_air_enthalpy`: dry_air_enthalpy
* `exner_function`: exner_function
* `filename`: filename
* `forecast_time`: forecast_time
* `geopotential`: geopotential
* `geopotential_height`: geopotential_height
* `graupel`: graupel
* `gravitational_acceleration`: gravitational_acceleration
* `hail`: hail
* `heat_flux`: heat_flux
* `hygroscopic_aerosols`: hygroscopic_aerosols
* `ice`: ice
* `latent_heat_flux`: latent_heat_flux
* `liquid_water`: liquid_water
* `longwave_flux`: longwave_flux
* `momentum_flux`: momentum_flux
* `nonhygroscopic_ice_nucleating_aerosols`: nonhygroscopic_ice_nucleating_aerosols
* `ozone`: ozone
* `pressure`: pressure
* `rain`: rain
* `rain_water`: rain_water
* `random_number`: random_number
* `random_number_seed`: random_number_seed
* `reference_pressure`: reference_pressure
* `relative_humidity`: relative_humidity
* `roughness_length`: roughness_length
* `sensible_heat_flux`: sensible_heat_flux
* `shortwave_flux`: shortwave_flux
* `snow`: snow
* `snow_area_fraction`: snow_area_fraction
* `soil_moisture`: soil_moisture
* `soil_temperature`: soil_temperature
* `solar_declination_angle`: solar_declination_angle
* `solar_zenith_angle`: solar_zenith_angle
* `streamfunction`: streamfunction
* `surface_skin_temperature`: surface_skin_temperature
* `temperature`: temperature
* `temperature_flux`: temperature_flux
* `time`: time
* `total_energy`: total_energy
* `total_water`: All water phases (solid, liquid, gas)
* `tracer`: tracer
* `tracers`: tracers
* `turbulent_kinetic_energy`: turbulent_kinetic_energy
* `velocity_potential`: velocity_potential
* `virtual_potential_temperature`: virtual_potential_temperature
* `virtual_temperature`: virtual_temperature
* `water_vapor`: water_vapor
* `wind`: wind
* `wind_speed`: wind_speed
## dimensions
Dimension standard names may come in sets of six related standard names for each dimension:
```
[dim_name]_dimension -- The full dimension size
[dim_name]_loop_extent -- Size of dim for current call
[dim_name]_begin - Start index for dimension
[dim_name]_end - End index for dimension
[dim_name]_index - Single index for dimension
[dim_name]_selection - Array of selected indices for dimension
```
Note that the cap generator may substitute among standard names in this category in order to properly call suite parts and individual schemes. In the substitutions below, the name on the left is the standard_name in the dimensions field of the caller while the name(s) on the right is (are) the standard name(s) of the callee (in the form used in the subroutine call).
```
[dim_name]_dimension ==> 1:[dim_name]_loop_extent
[dim_name]_loop_extent ==> 1:[dim_name]_loop_extent
[dim_name]_begin:[dim_name]_end ==> 1:[dim_name]_loop_extent
[dim_name]_begin:[dim_name]_end ==> 1:[dim_name]_dimension
```
Also note that horizontal_dimension should be used in xxx_[timestep_]init and xxx_[timestep_]final routines but not in xxx_run routines.
Currently, the only dimension which supports all six dimension types is horizontal_dimension. This and other supported dimension standard names are listed below.
* `horizontal_dimension`: Size horizontal dimension
    * `integer`: units = count
* `vertical_layer_dimension`: number of vertical layers
    * `integer`: units = count
* `vertical_layer_dimension_extended_up_by_1`: number of vertical layers extended up by 1
    * `integer`: units = count
* `vertical_interface_dimension`: number of vertical interfaces
    * `integer`: units = count
* `vertical_layer_index`: index of a particular vertical layer
    * `integer`: units = index
* `vertical_interface_index`: index of a particular vertical interface
    * `integer`: units = index
* `vertical_index_at_surface_adjacent_layer`: Vertical index at surface adjacent layer
    * `integer`: units = index
* `vertical_index_at_top_adjacent_layer`: Vertical index at top adjacent layer
    * `integer`: units = index
* `vertical_index_at_surface_interface`: Vertical index at surface interface
    * `integer`: units = index
* `vertical_index_at_top_interface`: Vertical index at top interface
    * `integer`: units = index
* `number_of_openmp_threads`: Total number of thread blocks which the host model may use to call CCPP physics run groups during the CCPP run phase.
    * `integer`: units = count
* `ccpp_thread_number`: Number of current thread block. This variable may only be used during CCPP run phase
    * `integer`: units = index
## constants
* `avogadro_number`: Avogadro number
    * `real(kind=kind_phys)`: units = molecules mol-1
* `base_state_surface_pressure_for_hybrid_vertical_coordinate`: Base state surface pressure for hybrid vertical coordinate
    * `real(kind=kind_phys)`: units = Pa
* `boltzmann_constant`: Boltzmann constant
    * `real(kind=kind_phys)`: units = J K-1
* `gas_constant_of_dry_air`: Gas constant of dry air
    * `real(kind=kind_phys)`: units = J kg-1 K-1
* `seconds_in_calendar_day`: Seconds in calendar day
    * `integer(kind=kind_phys)`: units = s
* `specific_heat_of_dry_air_at_constant_pressure`: Specific heat of dry air at constant pressure
    * `real(kind=kind_phys)`: units = J kg-1 K-1
* `specific_heat_of_liquid_water_at_20c`: specific heat of liquid water at 20c
    * `real(kind=kind_phys)`: units = J kg-1 K-1
* `latent_heat_of_vaporization_of_water_at_0c`: latent heat of vaporization of water at 0c
    * `real(kind=kind_phys)`: units = J kg-1
* `dry_air_density_at_stp`: density of dry air at STP
    * `real(kind=kind_phys)`: units = kg m-3
* `fresh_liquid_water_density_at_0c`: density of liquid water at 0c
    * `real(kind=kind_phys)`: units = kg m-3
* `ratio_of_water_vapor_to_dry_air_gas_constants_minus_one`: (Rwv / Rdair) - 1.0
    * `real(kind=kind_phys)`: units = 1
* `standard_gravitational_acceleration`: scalar constant representing gravitational acceleration
    * `real(kind=kind_phys)`: units = m s-2
## coordinates
* `latitude`: Latitude
    * `real(kind=kind_phys)`: units = degree_north
* `longitude`: Longitude
    * `real(kind=kind_phys)`: units = degree_east
* `cell_area`: Cell area
    * `real(kind=kind_phys)`: units = m2
* `cell_weight`: Cell weight
    * `real(kind=kind_phys)`: units = 1
## state_variables
Note that appending '_on_previous_timestep' to standard_names in this section yields another valid standard_name
* `physics_state_due_to_dynamics`: Physics state due to dynamics
    * `physics_state(kind=kind_phys)`: units = none
* `timestep_for_physics`: Timestep for physics
    * `integer(kind=kind_phys)`: units = s
* `total_tendency_of_physics`: Total tendency of physics
    * `physics_tend(kind=kind_phys)`: units = none
* `air_pressure_at_top_of_atmosphere_model`: Air pressure at top of atmosphere model
    * `real(kind=kind_phys)`: units = Pa
* `air_pressure_at_sea_level`: Air pressure at sea level
    * `real(kind=kind_phys)`: units = Pa
* `air_pressure_at_surface`: Air pressure at local surface
    * `real(kind=kind_phys)`: units = Pa
* `surface_pressure_of_dry_air`: Surface pressure of dry air
    * `real(kind=kind_phys)`: units = Pa
* `geopotential_at_surface`: Geopotential at surface
    * `real(kind=kind_phys)`: units = m2 s-2
* `air_temperature`: Air temperature
    * `real(kind=kind_phys)`: units = K
* `air_temperature_on_previous_timestep`: Air temperature on previous timestep
    * `real(kind=kind_phys)`: units = K
* `x_wind`: Horizontal wind in a direction perpendicular to y_wind
    * `real(kind=kind_phys)`: units = m s-1
* `y_wind`: Horizontal wind in a direction perpendicular to x_wind
    * `real(kind=kind_phys)`: units = m s-1
* `eastward_wind`: Wind vector component, positive when directed eastward
    * `real(kind=kind_phys)`: units = m s-1
* `northward_wind`: Wind vector component, positive when directed northward
    * `real(kind=kind_phys)`: units = m s-1
* `eastward_wind_at_10m`: Wind vector component at 10m, positive when directed eastward
    * `real(kind=kind_phys)`: units = m s-1
* `northward_wind_at_10m`: Wind vector component at 10m, positive when directed northward
    * `real(kind=kind_phys)`: units = m s-1
* `eastward_wind_at_surface`: Wind vector component closest to surface, positive when directed eastward
    * `real(kind=kind_phys)`: units = m s-1
* `northward_wind_at_surface`: Wind vector component closest to surface, positive when directed northward
    * `real(kind=kind_phys)`: units = m s-1
* `wind_speed_at_surface`: Scalar wind speed closest to surface
    * `real(kind=kind_phys)`: units = m s-1
* `wind_from_direction_at_surface`: Direction, from north, of wind speed closest to surface
    * `real(kind=kind_phys)`: units = degrees
* `dry_static_energy`: Dry static energy Content of Atmosphere Layer
    * `real(kind=kind_phys)`: units = J kg-1
* `do_lagrangian_vertical_coordinate`: flag indicating if vertical coordinate is lagrangian
    * `logical(kind=)`: units = flag
* `lagrangian_tendency_of_air_pressure`: Vertical pressure velocity
    * `real(kind=kind_phys)`: units = Pa s-1
* `dry_air_density`: Density of dry air
    * `real(kind=kind_phys)`: units = kg m-3
* `air_pressure`: Midpoint air pressure
    * `real(kind=kind_phys)`: units = Pa
* `air_pressure_of_dry_air`: Dry midpoint pressure
    * `real(kind=kind_phys)`: units = Pa
* `air_pressure_thickness`: Air pressure thickness
    * `real(kind=kind_phys)`: units = Pa
* `air_pressure_thickness_of_dry_air`: Air pressure thickness of dry air
    * `real(kind=kind_phys)`: units = Pa
* `reciprocal_of_air_pressure_thickness`: Reciprocal of air pressure thickness
    * `real(kind=kind_phys)`: units = Pa-1
* `reciprocal_of_air_pressure_thickness_of_dry_air`: Reciprocal of air pressure thickness of dry air
    * `real(kind=kind_phys)`: units = Pa-1
* `ln_air_pressure`: Ln air pressure
    * `real(kind=kind_phys)`: units = 1
* `ln_air_pressure_of_dry_air`: Ln air pressure of dry air
    * `real(kind=kind_phys)`: units = 1
* `reciprocal_of_exner_function_wrt_air_pressure_at_surface`: inverse exner function w.r.t. surface pressure, (ps/p)^(R/cp)
    * `real(kind=kind_phys)`: units = 1
* `geopotential_height`: geopotential height w.r.t. sea level
    * `real(kind=kind_phys)`: units = m
* `geopotential_height_at_surface`: Geopotential height at local surface w.r.t. sea level
    * `real(kind=kind_phys)`: units = m
* `geopotential_height_wrt_surface`: geopotential height w.r.t. local surface
    * `real(kind=kind_phys)`: units = m
* `geopotential_height_wrt_surface_at_interfaces`: geopotential height w.r.t. local surface at interfaces
    * `real(kind=kind_phys)`: units = m
* `potentially_advected_quantities`: Potentially advected quantities
    * `real(kind=kind_phys)`: units = various
* `air_pressure_at_interfaces`: Air pressure at interfaces
    * `real(kind=kind_phys)`: units = Pa
* `air_pressure_of_dry_air_at_interfaces`: Air pressure of dry air at interfaces
    * `real(kind=kind_phys)`: units = Pa
* `ln_air_pressure_at_interfaces`: Ln air pressure at interfaces
    * `real(kind=kind_phys)`: units = 1
* `ln_air_pressure_of_dry_air_at_interfaces`: Ln air pressure of dry air at interfaces
    * `real(kind=kind_phys)`: units = 1
* `air_pressure_extended_up_by_1`: Air pressure extended up by 1
    * `real(kind=kind_phys)`: units = Pa
* `largest_model_top_pressure_that_allows_molecular_diffusion`: Largest model top pressure that allows molecular diffusion
    * `real(kind=kind_phys)`: units = Pa
* `do_molecular_diffusion`: Do molecular diffusion
    * `logical(kind=kind_phys)`: units = flag
* `is_initialized_physics_grid`: Flag to indicate if physics grid is initialized
    * `logical(kind=kind_phys)`: units = flag
* `control_for_negative_constituent_warning`: Logging setting for negative constituent mass fixer
    * `character(kind=len=*)`: units = 1
* `geopotential_height_at_interfaces`: Geopotential height at interfaces
    * `real(kind=kind_phys)`: units = m
* `vertically_integrated_total_energy_of_initial_state`: Vertically integrated total energy of initial state
    * `real(kind=kind_phys)`: units = J m-2
* `vertically_integrated_total_energy_of_current_state`: Vertically integrated total energy of current state
    * `real(kind=kind_phys)`: units = J m-2
* `vertically_integrated_total_water_of_initial_state`: Vertically integrated total water of initial state
    * `real(kind=kind_phys)`: units = kg m-2
* `vertically_integrated_total_water_of_current_state`: Vertically integrated total water of current state
    * `real(kind=kind_phys)`: units = kg m-2
* `tendency_of_dry_air_enthalpy_at_constant_pressure`: Tendency of dry air enthalpy at constant pressure
    * `real(kind=kind_phys)`: units = J kg-1 s-1
* `tendency_of_air_temperature`: Change in temperature from a parameterization
    * `real(kind=kind_phys)`: units = K s-1
* `tendency_of_air_temperature_due_to_model_physics`: Total change in air temperature from a physics suite
    * `real(kind=kind_phys)`: units = K s-1
* `tendency_of_air_potential_temperature`: Change in potential temperature from a parameterization
    * `real(kind=kind_phys)`: units = K s-1
* `tendency_of_air_potential_temperature_due_to_model_physics`: Tendency of air potential temperature due to model physics
    * `real(kind=kind_phys)`: units = K s-1
* `tendency_of_x_wind`: Change in x wind from a parameterization
    * `real(kind=kind_phys)`: units = m s-2
* `tendency_of_x_wind_due_to_model_physics`: Tendency of x wind due to model physics
    * `real(kind=kind_phys)`: units = m s-2
* `tendency_of_y_wind`: Change in y wind from a parameterization
    * `real(kind=kind_phys)`: units = m s-2
* `tendency_of_y_wind_due_to_model_physics`: Tendency of y wind due to model physics
    * `real(kind=kind_phys)`: units = m s-2
* `tendency_of_eastward_wind`: Change in eastward wind from a parameterization
    * `real(kind=kind_phys)`: units = m s-2
* `tendency_of_eastward_wind_due_to_model_physics`: Total change in eastward wind from a physics suite
    * `real(kind=kind_phys)`: units = m s-2
* `tendency_of_northward_wind`: Change in northward wind from a parameterization
    * `real(kind=kind_phys)`: units = m s-2
* `tendency_of_northward_wind_due_to_model_physics`: Total change in northward wind from a physics suite
    * `real(kind=kind_phys)`: units = m s-2
* `horizontal_streamfunction_of_air`: Scalar function describing the streamlines of the horizontal wind
    * `real(kind=kind_phys)`: units = m2 s-1
* `horizontal_velocity_potential_of_air`: Scalar potential of the horizontal wind
    * `real(kind=kind_phys)`: units = m2 s-1
* `upward_absolute_vorticity_of_air`: The upward (kth) component of the curl of the vector wind field
    * `real(kind=kind_phys)`: units = s-1
* `horizontal_divergence_of_air`: The (horizontal) divergence of the 2-D vector wind field
    * `real(kind=kind_phys)`: units = s-1
* `upward_heat_flux_in_air_at_surface`: Upward heat flux in air at surface
    * `real(kind=kind_phys)`: units = W m-2
* `cumulative_boundary_flux_of_total_energy`: Cumulative boundary flux of total energy
    * `real(kind=kind_phys)`: units = W m-2
* `cumulative_boundary_flux_of_total_water`: Cumulative boundary flux of total water
    * `real(kind=kind_phys)`: units = W m-2
* `us_standard_air_pressure_at_sea_level`: US Standard Atmospheric pressure at sea level
    * `real(kind=kind_phys)`: units = Pa
* `surface_reference_pressure`: Reference pressure used in definition of potential temperature, Exner function, etc.
    * `real(kind=kind_phys)`: units = Pa
* `reference_pressure_in_atmosphere_layer`: reference pressure in atmosphere layer
    * `real(kind=kind_phys)`: units = Pa
* `reference_air_pressure_normalized_by_air_pressure_at_surface`: reference pressure normalized by surface pressure
    * `real(kind=kind_phys)`: units = 1
* `reference_pressure_in_atmosphere_layer_normalized_by_surface_reference_pressure`: Reference pressure in atmosphere layer normalized by surface reference pressure
    * `real(kind=kind_phys)`: units = 1
* `exner_function`: exner function, (p/p0)^(Rd/cp), where p0 is 1000 hPa
    * `real(kind=kind_phys)`: units = 1
* `air_potential_temperature`: air potential temperature
    * `real(kind=kind_phys)`: units = K
* `air_potential_temperature_on_previous_timestep`: air potential temperature on previous timestep
    * `real(kind=kind_phys)`: units = K
* `virtual_temperature`: virtual temperature
    * `real(kind=kind_phys)`: units = K
* `virtual_potential_temperature`: virtual potential temperature
    * `real(kind=kind_phys)`: units = K
* `composition_dependent_gas_constant_of_dry_air`: Composition dependent gas constant of dry air
    * `real(kind=kind_phys)`: units = J kg-1 K-1
* `composition_dependent_specific_heat_of_dry_air_at_constant_pressure`: composition dependent specific heat of dry air at constant pressure
    * `real(kind=kind_phys)`: units = J kg-1 K-1
* `composition_dependent_ratio_of_dry_air_gas_constant_to_specific_heat_of_dry_air_at_constant_pressure`: composition dependent ratio of dry air gas constant to specific heat of dry air at constant pressure
    * `real(kind=kind_phys)`: units = 1
* `ratio_of_water_vapor_gas_constant_to_composition_dependent_dry_air_gas_constant_minus_one`: (Rwv / Rdair) - 1.0
    * `real(kind=kind_phys)`: units = 1
* `mass_content_of_cloud_ice_in_atmosphere_layer`: Mass content of cloud ice in atmosphere layer
    * `real(kind=kind_phys)`: units = kg m-2
* `mass_content_of_cloud_liquid_water_in_atmosphere_layer`: Mass content of cloud liquid water in atmosphere layer
    * `real(kind=kind_phys)`: units = kg m-2
* `mass_content_of_rain_in_atmosphere_layer`: Mass content of rain in atmosphere layer
    * `real(kind=kind_phys)`: units = kg m-2
* `mass_content_of_snow_in_atmosphere_layer`: Mass content of snow in atmosphere layer
    * `real(kind=kind_phys)`: units = kg m-2
* `mass_content_of_graupel_in_atmosphere_layer`: Mass content of graupel in atmosphere layer
    * `real(kind=kind_phys)`: units = kg m-2
* `mass_content_of_hail_in_atmosphere_layer`: Mass content of hail in atmosphere layer
    * `real(kind=kind_phys)`: units = kg m-2
* `nonconvective_cloud_area_fraction_in_atmosphere_layer`: cloud area fraction in atmosphere layer excluding clouds produced by the convective schemes
    * `real(kind=kind_phys)`: units = fraction
* `relative_humidity`: Relative humidity
    * `real(kind=kind_phys)`: units = fraction
* `relative_humidity_at_2m`: Relative humidity at 2m
    * `real(kind=kind_phys)`: units = fraction
* `gravitational_acceleration`: Gravitational acceleration
    * `real(kind=kind_phys)`: units = m s-2
## land_surface
* `land_ice_area_fraction_of_cell_area`: fraction of horizontal area of grid cell that is land ice
    * `real(kind=kind_phys)`: units = frac
* `mass_content_of_water_in_top_soil_layer`: content per unit area of water in top layer of soil
    * `real(kind=kind_phys)`: units = kg m-2
* `density_of_snow_at_surface`: Density of snow at surface
    * `real(kind=kind_phys)`: units = kg m-3
* `urban_area_fraction_of_cell_area`: fraction of horizontal area of grid cell that is urban
    * `real(kind=kind_phys)`: units = frac
* `volume_fraction_of_liquid_water_in_soil_at_critical_point`: volume fraction of water in liquid phase in soil at critical point
    * `real(kind=kind_phys)`: units = m3 m-3
* `volume_fraction_of_liquid_water_in_soil_at_saturation`: volume fraction of water in liquid phase in soil at saturation
    * `real(kind=kind_phys)`: units = m3 m-3
* `volume_fraction_of_liquid_water_in_soil_at_wilting_point`: volume fraction of water in liquid phase in soil at wilting point
    * `real(kind=kind_phys)`: units = m3 m-3
## diagnostics
* `total_precipitation_rate_at_surface`: Total precipitation rate at surface
    * `real(kind=kind_phys)`: units = m s-1
## atmospheric_composition
* `number_of_chemical_species`: Number of chemical species
    * `integer(kind=kind_phys)`: units = count
* `number_of_tracers`: Number of tracers
    * `integer(kind=kind_phys)`: units = count
* `water_vapor_mixing_ratio_wrt_moist_air`: Ratio of the mass of water vapor to the mass of moist air
    * `real(kind=kind_phys)`: units = kg kg-1
* `water_vapor_mixing_ratio_wrt_moist_air_and_condensed_water`: Ratio of the mass of water vapor to the mass of moist air and hydrometeors
    * `real(kind=kind_phys)`: units = kg kg-1
* `water_vapor_mixing_ratio_wrt_moist_air_and_condensed_water_at_top_interfaces`: Ratio of the mass of water vapor to the mass of moist air and hydrometeors at all interfaces excluding surface
    * `real(kind=kind_phys)`: units = kg kg-1
* `mole_fraction_of_water_vapor`: Mole fraction of water vapor
    * `real(kind=kind_phys)`: units = mol mol-1
* `water_vapor_mixing_ratio_wrt_dry_air`: Ratio of the mass of water vapor to the mass of dry air
    * `real(kind=kind_phys)`: units = kg kg-1
* `water_vapor_mixing_ratio_wrt_dry_air_at_top_interfaces`: Ratio of the mass of water vapor to the mass of dry air at all interfaces excluding surface
    * `real(kind=kind_phys)`: units = kg kg-1
* `cloud_liquid_water_mixing_ratio_wrt_moist_air_and_condensed_water`: Ratio of the mass of liquid water to the mass of moist air and condensed water
    * `real(kind=kind_phys)`: units = kg kg-1
* `cloud_liquid_water_mixing_ratio_wrt_moist_air_and_condensed_water_at_top_interfaces`: Ratio of the mass of liquid water to the mass of moist air and condensed water at all interfaces excluding surface
    * `real(kind=kind_phys)`: units = kg kg-1
* `cloud_liquid_water_mixing_ratio_wrt_moist_air`: Ratio of the mass of liquid water to the mass of moist air
    * `real(kind=kind_phys)`: units = kg kg-1
* `cloud_liquid_water_mixing_ratio_wrt_dry_air`: Ratio of the mass of liquid water to the mass of dry air
    * `real(kind=kind_phys)`: units = kg kg-1
* `cloud_liquid_water_mixing_ratio_wrt_dry_air_at_top_interfaces`: Ratio of the mass of liquid water to the mass of dry air at all interfaces excluding surface
    * `real(kind=kind_phys)`: units = kg kg-1
* `cloud_ice_mixing_ratio_wrt_moist_air_and_condensed_water`: Ratio of the mass of ice to the mass of moist air and condensed water
    * `real(kind=kind_phys)`: units = kg kg-1
* `cloud_ice_mixing_ratio_wrt_moist_air_and_condensed_water_at_top_interfaces`: Ratio of the mass of ice to the mass of moist air and condensed water at all interfaces excluding surface
    * `real(kind=kind_phys)`: units = kg kg-1
* `cloud_ice_mixing_ratio_wrt_dry_air`: Ratio of the mass of ice to the mass of dry air
    * `real(kind=kind_phys)`: units = kg kg-1
* `cloud_ice_mixing_ratio_wrt_dry_air_at_top_interfaces`: Ratio of the mass of ice to the mass of dry air at all interfaces excluding surface
    * `real(kind=kind_phys)`: units = kg kg-1
* `rain_mixing_ratio_wrt_moist_air_and_condensed_water`: ratio of the mass of rain to the mass of moist air and condensed water
    * `real(kind=kind_phys)`: units = kg kg-1
* `rain_mixing_ratio_wrt_moist_air_and_condensed_water_at_top_interfaces`: ratio of the mass of rain to the mass of moist air and condensed water at all interfaces excluding surface
    * `real(kind=kind_phys)`: units = kg kg-1
* `rain_mixing_ratio_wrt_moist_air`: ratio of the mass of rain to the mass of moist air
    * `real(kind=kind_phys)`: units = kg kg-1
* `rain_mixing_ratio_wrt_dry_air`: ratio of the mass of rain to the mass of dry air
    * `real(kind=kind_phys)`: units = kg kg-1
* `rain_mixing_ratio_wrt_dry_air_at_top_interfaces`: ratio of the mass of rain to the mass of dry air at all interfaces excluding surface
    * `real(kind=kind_phys)`: units = kg kg-1
* `total_water_mixing_ratio_wrt_moist_air_and_condensed_water`: ratio of the mass of water to the mass of moist air and condensed water
    * `real(kind=kind_phys)`: units = kg kg-1
* `total_water_mixing_ratio_wrt_moist_air_and_condensed_water_at_top_interfaces`: ratio of the mass of water to the mass of moist air and condensed water at all interfaces excluding surface
    * `real(kind=kind_phys)`: units = kg kg-1
* `total_water_mixing_ratio_wrt_dry_air`: ratio of the mass of water to the mass of dry air
    * `real(kind=kind_phys)`: units = kg kg-1
* `total_water_mixing_ratio_wrt_dry_air_at_top_interfaces`: ratio of the mass of water to the mass of dry air at all interfaces excluding surface
    * `real(kind=kind_phys)`: units = kg kg-1
* `water_vapor_mixing_ratio_wrt_moist_air_and_condensed_water_assuming_saturation`: saturated water vapor mass mixing ratio with respect to moist air and condensed water
    * `real(kind=kind_phys)`: units = kg kg-1
* `water_vapor_mixing_ratio_wrt_moist_air_and_condensed_water_at_top_interfaces_assuming_saturation`: saturated water vapor mass mixing ratio with respect to moist air and condensed water at all interfaces excluding surface
    * `real(kind=kind_phys)`: units = kg kg-1
* `derivative_of_ln_water_vapor_partial_pressure_assuming_saturation_wrt_air_temperature`: log derivative of the water vapor partial pressure at saturation with respect to air temperature
    * `real(kind=kind_phys)`: units = K-1
* `derivative_of_ln_water_vapor_partial_pressure_assuming_saturation_wrt_air_temperature_at_top_interfaces`: log derivative of the water vapor partial pressure at saturation with respect to air temperature at all interfaces excluding surface
    * `real(kind=kind_phys)`: units = K-1
* `mole_fraction_of_ozone_in_air`: Mole fraction of ozone in air
    * `real(kind=kind_phys)`: units = mol mol-1
* `mole_fraction_of_co2_in_air`: Mole fraction of co2 in air
    * `real(kind=kind_phys)`: units = mol mol-1
* `volume_mixing_ratio_of_ch4`: Methane volume mixing ratio
    * `real(kind=kind_phys)`: units = mol mol-1
* `volume_mixing_ratio_of_co`: Carbon monoxide volume mixing ratio
    * `real(kind=kind_phys)`: units = mol mol-1
* `volume_mixing_ratio_of_co2`: Carbon dioxide volume mixing ratio
    * `real(kind=kind_phys)`: units = mol mol-1
* `volume_mixing_ratio_of_ccl4`: Tetrachloromethane volume mixing ratio
    * `real(kind=kind_phys)`: units = mol mol-1
* `volume_mixing_ratio_of_cfc11`: Trichlorofluoromethane volume mixing ratio
    * `real(kind=kind_phys)`: units = mol mol-1
* `volume_mixing_ratio_of_cfc12`: Dichlorodifluoromethane volume mixing ratio
    * `real(kind=kind_phys)`: units = mol mol-1
* `volume_mixing_ratio_of_cfc113`: 1,1,2-Trichloro-1,2,2-trifluoroethane volume mixing ratio
    * `real(kind=kind_phys)`: units = mol mol-1
* `volume_mixing_ratio_of_cfc22`: Chlorodifluoromethane volume mixing ratio
    * `real(kind=kind_phys)`: units = mol mol-1
* `volume_mixing_ratio_of_o2`: Dioxygen volume mixing ratio
    * `real(kind=kind_phys)`: units = mol mol-1
* `volume_mixing_ratio_of_n2o`: Nitrous oxide volume mixing ratio
    * `real(kind=kind_phys)`: units = mol mol-1
* `volume_mixing_ratio_of_no2`: Nitrogen dioxide volume mixing ratio
    * `real(kind=kind_phys)`: units = mol mol-1
* `volume_mixing_ratio_of_no`: Nitrogen oxide volume mixing ratio
    * `real(kind=kind_phys)`: units = mol mol-1
* `volume_mixing_ratio_of_o3`: Ozone volume mixing ratio
    * `real(kind=kind_phys)`: units = mol mol-1
* `volume_mixing_ratio_of_hcho`: Formaldehyde volume mixing ratio
    * `real(kind=kind_phys)`: units = mol mol-1
* `volume_mixing_ratio_of_c5h8`: Isoprene volume mixing ratio
    * `real(kind=kind_phys)`: units = mol mol-1
* `volume_mixing_ratio_of_so2`: Sulfur dioxide volume mixing ratio
    * `real(kind=kind_phys)`: units = mol mol-1
## atmospheric_composition: GOCART aerosols
* `mass_fraction_of_dust001_in_air`: Dust bin1 mass fraction
    * `real(kind=kind_phys)`: units = kg kg-1
* `mass_fraction_of_dust002_in_air`: Dust bin2 mass fraction
    * `real(kind=kind_phys)`: units = kg kg-1
* `mass_fraction_of_dust003_in_air`: Dust bin3 mass fraction
    * `real(kind=kind_phys)`: units = kg kg-1
* `mass_fraction_of_dust004_in_air`: Dust bin4 mass fraction
    * `real(kind=kind_phys)`: units = kg kg-1
* `mass_fraction_of_dust005_in_air`: Dust bin5 mass fraction
    * `real(kind=kind_phys)`: units = kg kg-1
* `mass_fraction_of_sea_salt001_in_air`: Sea salt bin5 mass fraction
    * `real(kind=kind_phys)`: units = kg kg-1
* `mass_fraction_of_sea_salt002_in_air`: Sea salt bin2 mass fraction
    * `real(kind=kind_phys)`: units = kg kg-1
* `mass_fraction_of_sea_salt003_in_air`: Sea salt bin3 mass fraction
    * `real(kind=kind_phys)`: units = kg kg-1
* `mass_fraction_of_sea_salt004_in_air`: Sea salt bin4 mass fraction
    * `real(kind=kind_phys)`: units = kg kg-1
* `mass_fraction_of_sea_salt005_in_air`: Sea salt bin5 mass fraction
    * `real(kind=kind_phys)`: units = kg kg-1
* `mass_fraction_of_hydrophobic_black_carbon_in_air`: Hydrophobic black carbon mass fraction
    * `real(kind=kind_phys)`: units = kg kg-1
* `mass_fraction_of_hydrophilic_black_carbon_in_air`: Hydrophilic black carbon mass fraction
    * `real(kind=kind_phys)`: units = kg kg-1
* `mass_fraction_of_hydrophobic_organic_carbon_in_air`: Hydrophobic organic carbon mass fraction
    * `real(kind=kind_phys)`: units = kg kg-1
* `mass_fraction_of_hydrophilic_organic_carbon_in_air`: Hydrophilic organic carbon mass fraction
    * `real(kind=kind_phys)`: units = kg kg-1
* `mass_fraction_of_sulfate_in_air`: Sulfate mass fraction
    * `real(kind=kind_phys)`: units = kg kg-1
* `mass_fraction_of_sea_nitrate001_in_air`: Nitrate bin1 mass fraction
    * `real(kind=kind_phys)`: units = kg kg-1
* `mass_fraction_of_sea_nitrate002_in_air`: Nitrate bin2 mass fraction
    * `real(kind=kind_phys)`: units = kg kg-1
* `mass_fraction_of_sea_nitrate003_in_air`: Nitrate bin3 mass fraction
    * `real(kind=kind_phys)`: units = kg kg-1
* `volume_extinction_in_air_due_to_aerosol_particles_lambda1`: Aerosol extinction at wavelength1
    * `real(kind=kind_phys)`: units = m-1
* `volume_extinction_in_air_due_to_aerosol_particles_lambda2`: Aerosol extinction at wavelength2
    * `real(kind=kind_phys)`: units = m-1
* `volume_extinction_in_air_due_to_aerosol_particles_lambda3`: Aerosol extinction at wavelength3
    * `real(kind=kind_phys)`: units = m-1
## required framework-provided variables
Required CCPP framework-provided variables
* `ccpp_error_message`: Error message for error handling in CCPP
    * `character(kind=len=512)`: units = none
* `ccpp_error_code`: Error code for error handling in CCPP
    * `integer(kind=)`: units = 1
## optional framework-provided variables
Optional CCPP framework-provided variables
* `scheme_name`: CCPP physics scheme name
    * `character(kind=len=64)`: units = none
* `ccpp_constituent_properties`: CCPP Constituent Properties
    * `ccpp_constituent_prop_ptr_t(kind=)`: units = none
* `ccpp_constituents`: Array of constituents managed by CCPP Framework
    * `real(kind=kind_phys)`: units = none
* `ccpp_constituent_minimum_values`: CCPP constituent minimum values
    * `real(kind=kind_phys)`: units = none
* `number_of_ccpp_constituents`: Number of constituents managed by CCPP Framework
    * `integer(kind=)`: units = count
## system variables
Variables related to the compute environment
* `flag_for_mpi_root`: Flag for MPI root
    * `logical(kind=)`: units = flag
* `log_output_unit`: Log output unit
    * `integer(kind=)`: units = 1
## GFS_typedefs_GFS_control_type
* `sigma_pressure_hybrid_coordinate_a_coefficient`: Sigma pressure hybrid coordinate a coefficient
    * `real(kind=kind_phys)`: units = Pa
* `radiatively_active_gases_as_string`: Radiatively active gases as string
    * `character(kind=len=128)`: units = none
* `aerosol_aware_multiplicative_rain_conversion_parameter_for_deep_convection`: Aerosol aware multiplicative rain conversion parameter for deep convection
    * `real(kind=kind_phys)`: units = 1
* `aerosol_aware_multiplicative_rain_conversion_parameter_for_shallow_convection`: Aerosol aware multiplicative rain conversion parameter for shallow convection
    * `real(kind=kind_phys)`: units = 1
* `number_of_microphysics_variables_in_xy_dimensioned_restart_array`: Number of microphysics variables in xy dimensioned restart array
    * `integer(kind=)`: units = count
* `number_of_microphysics_variables_in_xyz_dimensioned_restart_array`: Number of microphysics variables in xyz dimensioned restart array
    * `integer(kind=)`: units = count
* `number_of_random_numbers`: Number of random numbers
    * `integer(kind=)`: units = count
* `multiplicative_tuning_parameter_for_atmosphere_diffusivity`: Multiplicative tuning parameter for atmosphere diffusivity
    * `real(kind=kind_phys)`: units = 1
* `atmosphere_heat_diffusivity_due_to_background`: Atmosphere heat diffusivity due to background
    * `real(kind=kind_phys)`: units = m2 s-1
* `max_atmosphere_heat_diffusivity_due_to_background`: Max atmosphere heat diffusivity due to background
    * `real(kind=kind_phys)`: units = m2 s-1
* `atmosphere_momentum_diffusivity_due_to_background`: Atmosphere momentum diffusivity due to background
    * `real(kind=kind_phys)`: units = m2 s-1
* `sigma_pressure_hybrid_coordinate_b_coefficient`: Sigma pressure hybrid coordinate b coefficient
    * `real(kind=kind_phys)`: units = 1
* `ccpp_block_count`: Ccpp block count
    * `integer(kind=)`: units = count
* `ccpp_block_sizes`: Ccpp block sizes
    * `integer(kind=)`: units = count
* `cellular_automata_finer_grid`: Cellular automata finer grid
    * `integer(kind=)`: units = count
* `cellular_automata_lifetime`: Cellular automata lifetime
    * `integer(kind=)`: units = count
* `cellular_automata_seed_frequency`: Cellular automata seed frequency
    * `integer(kind=)`: units = count
* `cellular_automata_seed_probability`: Cellular automata seed probability
    * `real(kind=kind_phys)`: units = fraction
* `identifier_for_2018_scale_aware_tke_moist_edmf_pbl`: Identifier for 2018 scale aware tke moist edmf pbl
    * `integer(kind=)`: units = 1
* `control_for_scale_aware_tke_moist_edmf_pbl_scheme`: Control for scale aware tke moist edmf pbl scheme
    * `integer(kind=)`: units = 1
* `identifier_for_2019_scale_aware_tke_moist_edmf_pbl`: Identifier for 2019 scale aware tke moist edmf pbl
    * `integer(kind=)`: units = 1
* `cloud_condensate_autoconversion_threshold_coefficient`: Cloud condensate autoconversion threshold coefficient
    * `real(kind=kind_phys)`: units = 1
* `cloud_condensate_autoconversion_threshold_coefficient_for_deep_convection`: Cloud condensate autoconversion threshold coefficient for deep convection
    * `real(kind=kind_phys)`: units = 1
* `control_for_cloud_area_fraction_option`: Control for cloud area fraction option
    * `integer(kind=)`: units = 1
* `reciprocal_of_cloud_phase_transition_temperature_range`: Reciprocal of cloud phase transition temperature range
    * `real(kind=kind_phys)`: units = K-1
* `cloud_phase_transition_threshold_temperature`: Cloud phase transition threshold temperature
    * `real(kind=kind_phys)`: units = K
* `control_for_cloud_species_mixing_in_mellor_yamada_nakanishi_niino_pbl_scheme`: Control for cloud species mixing in mellor yamada nakanishi niino pbl scheme
    * `integer(kind=)`: units = 1
* `control_for_cloud_pdf_in_mellor_yamada_nakanishi_niino_pbl_scheme`: Control for cloud pdf in mellor yamada nakanishi niino pbl scheme
    * `integer(kind=)`: units = 1
* `precipitation_evaporation_coefficient`: Precipitation evaporation coefficient
    * `real(kind=kind_phys)`: units = 1
* `coefficient_for_variable_bulk_richardson_number_over_land`: Coefficient for variable bulk richardson number over land
    * `real(kind=kind_phys)`: units = 1
* `coefficient_for_variable_bulk_richardson_number_over_water`: Coefficient for variable bulk richardson number over water
    * `real(kind=kind_phys)`: units = 1
* `autoconversion_to_snow_coefficient`: Autoconversion to snow coefficient
    * `real(kind=kind_phys)`: units = 1
* `autoconversion_to_snow_coefficient_for_deep_convection`: Autoconversion to snow coefficient for deep convection
    * `real(kind=kind_phys)`: units = 1
* `autoconversion_to_rain_coefficient`: Autoconversion to rain coefficient
    * `real(kind=kind_phys)`: units = 1
* `autoconversion_to_rain_coefficient_for_deep_convection`: Autoconversion to rain coefficient for deep convection
    * `real(kind=kind_phys)`: units = 1
* `chemical_tracer_scavenging_fractions`: Chemical tracer scavenging fractions
    * `real(kind=kind_phys)`: units = fraction
* `cloud_condensate_detrainment_coefficient`: Cloud condensate detrainment coefficient
    * `real(kind=kind_phys)`: units = 1
* `control_for_convective_cloud_diagnostics`: Control for convective cloud diagnostics
    * `real(kind=kind_phys)`: units = 1
* `cosine_of_solar_declination_angle`: Cosine of solar declination angle
    * `real(kind=kind_phys)`: units = 1
* `control_for_sgs_cloud_radiation_coupling_in_mellor_yamamda_nakanishi_niino_pbl_scheme`: Control for sgs cloud radiation coupling in mellor yamamda nakanishi niino pbl scheme
    * `integer(kind=)`: units = 1
* `tunable_parameter_for_critical_cloud_top_entrainment_instability_criteria`: Tunable parameter for critical cloud top entrainment instability criteria
    * `real(kind=kind_phys)`: units = 1
* `critical_relative_humidity_at_top_of_atmosphere_boundary_layer`: Critical relative humidity at top of atmosphere boundary layer
    * `real(kind=kind_phys)`: units = fraction
* `critical_relative_humidity_at_surface`: Critical relative humidity at surface
    * `real(kind=kind_phys)`: units = fraction
* `critical_relative_humidity_at_toa`: Critical relative humidity at toa
    * `real(kind=kind_phys)`: units = fraction
* `date_and_time_at_model_initialization_in_iso_order`: Date and time at model initialization in iso order
    * `integer(kind=)`: units = 1
* `date_and_time_at_model_initialization_in_united_states_order`: Date and time at model initialization in united states order
    * `integer(kind=)`: units = 1
* `decorrelation_length_used_by_overlap_method`: Decorrelation length used by overlap method
    * `real(kind=kind_phys)`: units = km
* `density_of_fresh_water`: Density of fresh water
    * `real(kind=kind_phys)`: units = kg m-3
* `depth_of_soil_layers`: Depth of soil layers
    * `real(kind=kind_phys)`: units = m
* `tunable_parameter_1_for_detrainment_and_precipitation_partitioning_in_chikira_sugiyama_deep_convection`: Tunable parameter 1 for detrainment and precipitation partitioning in chikira sugiyama deep convection
    * `real(kind=kind_phys)`: units = m
* `tunable_parameter_2_for_detrainment_and_precipitation_partitioning_in_chikira_sugiyama_deep_convection`: Tunable parameter 2 for detrainment and precipitation partitioning in chikira sugiyama deep convection
    * `real(kind=kind_phys)`: units = m
* `detrainment_conversion_parameter_for_deep_convection`: Detrainment conversion parameter for deep convection
    * `real(kind=kind_phys)`: units = m-1
* `detrainment_conversion_parameter_for_shallow_convection`: Detrainment conversion parameter for shallow convection
    * `real(kind=kind_phys)`: units = m-1
* `do_unified_gravity_wave_physics_diagnostics`: Do unified gravity wave physics diagnostics
    * `logical(kind=)`: units = flag
* `do_chemical_tracer_diagnostics`: Do chemical tracer diagnostics
    * `logical(kind=)`: units = flag
* `sigma_pressure_threshold_at_upper_extent_of_background_diffusion`: Sigma pressure threshold at upper extent of background diffusion
    * `real(kind=kind_phys)`: units = 1
* `directory_for_rte_rrtmgp_source_code`: Directory for rte rrtmgp source code
    * `character(kind=len=128)`: units = none
* `do_mellor_yamada_janjic_pbl_scheme`: Do mellor yamada janjic pbl scheme
    * `logical(kind=)`: units = flag
* `do_mellor_yamada_janjic_surface_layer_scheme`: Do mellor yamada janjic surface layer scheme
    * `logical(kind=)`: units = flag
* `do_mellor_yamada_nakanishi_niino_pbl_scheme`: Do mellor yamada nakanishi niino pbl scheme
    * `logical(kind=)`: units = flag
* `do_mellor_yamada_nakanishi_niino_surface_layer_scheme`: Do mellor yamada nakanishi niino surface layer scheme
    * `logical(kind=)`: units = flag
* `do_unified_gravity_wave_physics_gravity_wave_drag_scheme`: Do unified gravity wave physics gravity wave drag scheme
    * `logical(kind=)`: units = flag
* `downdraft_area_fraction_in_scale_aware_tke_moist_edmf_pbl_scheme`: Downdraft area fraction in scale aware tke moist edmf pbl scheme
    * `real(kind=kind_phys)`: units = fraction
* `downdraft_fraction_reaching_surface_over_land_for_deep_convection`: Downdraft fraction reaching surface over land for deep convection
    * `real(kind=kind_phys)`: units = fraction
* `downdraft_fraction_reaching_surface_over_water_for_deep_convection`: Downdraft fraction reaching surface over water for deep convection
    * `real(kind=kind_phys)`: units = fraction
* `control_for_edmf_in_mellor_yamada_nakanishi_niino_pbl_scheme`: Control for edmf in mellor yamada nakanishi niino pbl scheme
    * `integer(kind=)`: units = 1
* `control_for_edmf_momentum_transport_in_mellor_yamada_nakanishi_niino_pbl_scheme`: Control for edmf momentum transport in mellor yamada nakanishi niino pbl scheme
    * `integer(kind=)`: units = 1
* `control_for_edmf_partitioning_in_mellor_yamada_nakanishi_niino_pbl_scheme`: Control for edmf partitioning in mellor yamada nakanishi niino pbl scheme
    * `integer(kind=)`: units = 1
* `control_for_edmf_tke_transport_in_mellor_yamada_nakanishi_niino_pbl_scheme`: Control for edmf tke transport in mellor yamada nakanishi niino pbl scheme
    * `integer(kind=)`: units = 1
* `surface_layer_scheme_enthalpy_flux_factor`: Surface layer scheme enthalpy flux factor
    * `real(kind=kind_phys)`: units = 1
* `tunable_parameter_for_entrainment_efficiency_in_chikira_sugiyama_deep_convection`: Tunable parameter for entrainment efficiency in chikira sugiyama deep convection
    * `real(kind=kind_phys)`: units = 1
* `entrainment_rate_coefficient_for_deep_convection`: Entrainment rate coefficient for deep convection
    * `real(kind=kind_phys)`: units = 1
* `entrainment_rate_coefficient_for_shallow_convection`: Entrainment rate coefficient for shallow convection
    * `real(kind=kind_phys)`: units = 1
* `equation_of_time`: Equation of time
    * `real(kind=kind_phys)`: units = radian
* `relative_humidity_threshold_for_condensation`: Relative humidity threshold for condensation
    * `real(kind=kind_phys)`: units = fraction
* `do_arakawa_wu_downdrafts_for_deep_convection`: Do arakawa wu downdrafts for deep convection
    * `logical(kind=)`: units = flag
* `do_debug_output`: Do debug output
    * `logical(kind=)`: units = flag
* `do_diagnostics`: Do diagnostics
    * `logical(kind=)`: units = flag
* `do_xyz_dimensioned_diagnostics`: Do xyz dimensioned diagnostics
    * `logical(kind=)`: units = flag
* `do_flip`: Do flip
    * `logical(kind=)`: units = flag
* `control_for_flux_adjusting_surface_data_assimilation_system`: Control for flux adjusting surface data assimilation system
    * `integer(kind=)`: units = 1
* `do_flux_form_in_chikira_sugiyama_deep_convection_scheme`: Do flux form in chikira sugiyama deep convection scheme
    * `logical(kind=)`: units = flag
* `do_nrl_2015_ozone_scheme`: Do nrl 2015 ozone scheme
    * `logical(kind=)`: units = flag
* `do_prescribed_aerosols`: Do prescribed aerosols
    * `logical(kind=)`: units = flag
* `do_aerosol_physics`: Do aerosol physics
    * `logical(kind=)`: units = flag
* `do_arakawa_wu_adjustment`: Do arakawa wu adjustment
    * `logical(kind=)`: units = flag
* `do_canopy_heat_storage_in_land_surface_scheme`: Do canopy heat storage in land surface scheme
    * `logical(kind=)`: units = flag
* `control_for_land_surface_scheme_canopy_stomatal_resistance`: Control for land surface scheme canopy stomatal resistance
    * `integer(kind=)`: units = 1
* `do_cellular_automata`: Do cellular automata
    * `logical(kind=)`: units = flag
* `do_chemistry_coupling`: Do chemistry coupling
    * `logical(kind=)`: units = flag
* `do_chikira_sugiyama_deep_convection_scheme`: Do chikira sugiyama deep convection scheme
    * `logical(kind=)`: units = flag
* `do_in_cloud_condensate`: Do in cloud condensate
    * `logical(kind=)`: units = flag
* `do_cloud_effective_radii`: Do cloud effective radii
    * `logical(kind=)`: units = flag
* `control_for_cloud_overlap_method_for_radiation`: Control for cloud overlap method for radiation
    * `integer(kind=)`: units = 1
* `identifier_for_constant_decorrelation_length_method`: Identifier for constant decorrelation length method
    * `integer(kind=)`: units = 1
* `do_convective_gravity_wave_drag`: Do convective gravity wave drag
    * `logical(kind=)`: units = flag
* `do_convective_transport_of_tracers`: Do convective transport of tracers
    * `logical(kind=)`: units = flag
* `do_converting_hydrometeors_from_moist_to_dry_air`: Do converting hydrometeors from moist to dry air
    * `logical(kind=)`: units = flag
* `do_crick_elimination`: Do crick elimination
    * `logical(kind=)`: units = flag
* `identifier_for_decorrelation_length_cloud_overlap_method`: Identifier for decorrelation length cloud overlap method
    * `integer(kind=)`: units = 1
* `control_for_decorrelation_length_method`: Control for decorrelation length method
    * `integer(kind=)`: units = 1
* `control_for_shortwave_radiation_aerosols`: Control for shortwave radiation aerosols
    * `integer(kind=)`: units = 1
* `control_for_land_surface_scheme_dynamic_vegetation`: Control for land surface scheme dynamic vegetation
    * `integer(kind=)`: units = 1
* `identifier_for_exponential_cloud_overlap_method`: Identifier for exponential cloud overlap method
    * `integer(kind=)`: units = 1
* `identifier_for_exponential_random_cloud_overlap_method`: Identifier for exponential random cloud overlap method
    * `integer(kind=)`: units = 1
* `identifier_for_fer_hires_microphysics_scheme`: Identifier for fer hires microphysics scheme
    * `integer(kind=)`: units = 1
* `is_first_timestep`: Is first timestep
    * `logical(kind=)`: units = flag
* `do_surface_flux_coupling`: Do surface flux coupling
    * `logical(kind=)`: units = flag
* `do_fractional_landmask`: Do fractional landmask
    * `logical(kind=)`: units = flag
* `control_for_land_surface_scheme_frozen_soil_permeability`: Control for land surface scheme frozen soil permeability
    * `integer(kind=)`: units = 1
* `do_cellular_automata_gaussian_spatial_filter`: Do cellular automata gaussian spatial filter
    * `logical(kind=)`: units = flag
* `do_gcycle_surface_option`: Do gcycle surface option
    * `logical(kind=)`: units = flag
* `do_generic_tendency_due_to_deep_convection`: Do generic tendency due to deep convection
    * `logical(kind=)`: units = flag
* `do_generic_tendency_due_to_gravity_wave_drag`: Do generic tendency due to gravity wave drag
    * `logical(kind=)`: units = flag
* `do_generic_tendency_due_to_planetary_boundary_layer`: Do generic tendency due to planetary boundary layer
    * `logical(kind=)`: units = flag
* `do_generic_tendency_due_to_shallow_convection`: Do generic tendency due to shallow convection
    * `logical(kind=)`: units = flag
* `identifier_for_grell_freitas_deep_convection`: Identifier for grell freitas deep convection
    * `integer(kind=)`: units = 1
* `identifier_for_grell_freitas_shallow_convection`: Identifier for grell freitas shallow convection
    * `integer(kind=)`: units = 1
* `do_gfdl_microphysics_radiation_interaction`: Do gfdl microphysics radiation interaction
    * `logical(kind=)`: units = flag
* `identifier_for_gfdl_microphysics_scheme`: Identifier for gfdl microphysics scheme
    * `integer(kind=)`: units = 1
* `do_global_cellular_automata`: Do global cellular automata
    * `logical(kind=)`: units = flag
* `do_global_cellular_automata_closure`: Do global cellular automata closure
    * `logical(kind=)`: units = flag
* `do_global_cellular_automata_deep_convective_entrainment`: Do global cellular automata deep convective entrainment
    * `logical(kind=)`: units = flag
* `do_global_cellular_automata_trigger`: Do global cellular automata trigger
    * `logical(kind=)`: units = flag
* `do_gravity_wave_drag`: Do gravity wave drag
    * `logical(kind=)`: units = flag
* `control_for_land_surface_scheme_surface_snow_albedo`: Control for land surface scheme surface snow albedo
    * `integer(kind=)`: units = 1
* `do_gsl_drag_suite_large_scale_orographic_and_blocking_drag`: Do gsl drag suite large scale orographic and blocking drag
    * `logical(kind=)`: units = flag
* `do_gsl_drag_suite_small_scale_orographic_drag`: Do gsl drag suite small scale orographic drag
    * `logical(kind=)`: units = flag
* `do_gsl_drag_suite_turbulent_orographic_form_drag`: Do gsl drag suite turbulent orographic form drag
    * `logical(kind=)`: units = flag
* `do_hybrid_edmf_pbl_scheme`: Do hybrid edmf pbl scheme
    * `logical(kind=)`: units = flag
* `identifier_for_hogan_decorrelation_length_method`: Identifier for hogan decorrelation length method
    * `integer(kind=)`: units = 1
* `do_hurricane_specific_code_in_scale_aware_mass_flux_deep_convection`: Do hurricane specific code in scale aware mass flux deep convection
    * `logical(kind=)`: units = flag
* `do_hurricane_specific_code_in_scale_aware_mass_flux_shallow_convection`: Do hurricane specific code in scale aware mass flux shallow convection
    * `logical(kind=)`: units = flag
* `do_hydrostatic_solver`: Do hydrostatic solver
    * `logical(kind=)`: units = flag
* `control_for_ice_cloud_condensation_nuclei_forcing`: Control for ice cloud condensation nuclei forcing
    * `integer(kind=)`: units = 1
* `do_separate_advection_of_condensate_species`: Do separate advection of condensate species
    * `logical(kind=)`: units = flag
* `control_for_initial_time_date`: Control for initial time date
    * `integer(kind=)`: units = 1
* `control_for_lake_surface_scheme`: Control for lake surface scheme
    * `integer(kind=)`: units = 1
* `control_for_land_surface_scheme`: Control for land surface scheme
    * `integer(kind=)`: units = 1
* `do_cloud_area_fraction_option_for_radiation`: Do cloud area fraction option for radiation
    * `logical(kind=)`: units = flag
* `control_for_land_surface_scheme_lower_boundary_soil_temperature`: Control for land surface scheme lower boundary soil temperature
    * `integer(kind=)`: units = 1
* `control_for_lw_clouds_subgrid_approximation`: Control for lw clouds subgrid approximation
    * `integer(kind=)`: units = 1
* `control_for_deep_convection_scheme`: Control for deep convection scheme
    * `integer(kind=)`: units = 1
* `control_for_shallow_convection_scheme`: Control for shallow convection scheme
    * `integer(kind=)`: units = 1
* `control_for_maximum_cloud_overlap_method`: Control for maximum cloud overlap method
    * `integer(kind=)`: units = 1
* `identifier_for_maximum_random_cloud_overlap_method`: Identifier for maximum random cloud overlap method
    * `integer(kind=)`: units = 1
* `control_for_microphysics_scheme`: Control for microphysics scheme
    * `integer(kind=)`: units = 1
* `do_moorthi_stratus`: Do moorthi stratus
    * `logical(kind=)`: units = flag
* `identifier_for_morrison_gettelman_microphysics_scheme`: Identifier for morrison gettelman microphysics scheme
    * `integer(kind=)`: units = 1
* `do_mountain_blocking_for_sppt`: Do mountain blocking for sppt
    * `logical(kind=)`: units = flag
* `identifier_for_noah_land_surface_scheme`: Identifier for noah land surface scheme
    * `integer(kind=)`: units = 1
* `do_noah_lsm_ua_extension`: Do noah lsm ua extension
    * `logical(kind=)`: units = flag
* `identifier_for_noah_wrfv4_land_surface_scheme`: Identifier for noah wrfv4 land surface scheme
    * `integer(kind=)`: units = 1
* `identifier_for_noahmp_land_surface_scheme`: Identifier for noahmp land surface scheme
    * `integer(kind=)`: units = 1
* `do_nsstm_analysis_in_gcycle`: Do nsstm analysis in gcycle
    * `logical(kind=)`: units = flag
* `control_for_nsstm`: Control for nsstm
    * `integer(kind=)`: units = 1
* `identifier_for_new_tiedtke_deep_convection`: Identifier for new tiedtke deep convection
    * `integer(kind=)`: units = 1
* `identifier_for_new_tiedtke_shallow_convection`: Identifier for new tiedtke shallow convection
    * `integer(kind=)`: units = 1
* `do_surface_layer_scheme_ocean_currents`: Do surface layer scheme ocean currents
    * `logical(kind=)`: units = flag
* `do_old_pbl_scheme`: Do old pbl scheme
    * `logical(kind=)`: units = flag
* `control_for_optical_property_for_ice_clouds_for_longwave_radiation`: Control for optical property for ice clouds for longwave radiation
    * `integer(kind=)`: units = 1
* `control_for_optical_property_for_ice_clouds_for_shortwave_radiation`: Control for optical property for ice clouds for shortwave radiation
    * `integer(kind=)`: units = 1
* `control_for_optical_property_for_liquid_clouds_for_longwave_radiation`: Control for optical property for liquid clouds for longwave radiation
    * `integer(kind=)`: units = 1
* `control_for_optical_property_for_liquid_clouds_for_shortwave_radiation`: Control for optical property for liquid clouds for shortwave radiation
    * `integer(kind=)`: units = 1
* `identifier_for_oreopoulos_decorrelation_length_method`: Identifier for oreopoulos decorrelation length method
    * `integer(kind=)`: units = 1
* `do_output_of_tendency_of_air_temperature_due_to_longwave_heating_on_radiation_timestep_assuming_clear_sky`: Do output of tendency of air temperature due to longwave heating on radiation timestep assuming clear sky
    * `logical(kind=)`: units = flag
* `do_output_of_tendency_of_air_temperature_due_to_shortwave_heating_on_radiation_timestep_assuming_clear_sky`: Do output of tendency of air temperature due to shortwave heating on radiation timestep assuming clear sky
    * `logical(kind=)`: units = flag
* `do_nrl_2006_ozone_scheme`: Do nrl 2006 ozone scheme
    * `logical(kind=)`: units = flag
* `control_for_pdf_shape_for_microphysics`: Control for pdf shape for microphysics
    * `integer(kind=)`: units = 1
* `do_surface_layer_scheme_surface_drag_coefficient_for_momentum_in_air_perturbations`: Do surface layer scheme surface drag coefficient for momentum in air perturbations
    * `logical(kind=)`: units = flag
* `disable_precipitation_radiative_effect`: Disable precipitation radiative effect
    * `logical(kind=)`: units = flag
* `control_for_land_surface_scheme_precipitation_type_partition`: Control for land surface scheme precipitation type partition
    * `integer(kind=)`: units = 1
* `do_dominant_precipitation_type_partition`: Do dominant precipitation type partition
    * `logical(kind=)`: units = flag
* `do_radar_reflectivity`: Do radar reflectivity
    * `logical(kind=)`: units = flag
* `control_for_land_surface_scheme_radiative_transfer`: Control for land surface scheme radiative transfer
    * `integer(kind=)`: units = 1
* `identifier_for_random_cloud_overlap_method`: Identifier for random cloud overlap method
    * `integer(kind=)`: units = 1
* `do_random_clouds_in_relaxed_arakawa_schubert_deep_convection`: Do random clouds in relaxed arakawa schubert deep convection
    * `logical(kind=)`: units = flag
* `do_relaxed_arakawa_schubert_deep_convection`: Do relaxed arakawa schubert deep convection
    * `logical(kind=)`: units = flag
* `do_read_leaf_area_index_from_input`: Do read leaf area index from input
    * `logical(kind=)`: units = flag
* `do_read_surface_albedo_for_diffused_shortwave_from_input`: Do read surface albedo for diffused shortwave from input
    * `logical(kind=)`: units = flag
* `do_limited_roughness_length_over_ocean`: Do limited surface roughness length over ocean
    * `logical(kind=)`: units = flag
* `do_reference_pressure_theta`: Do reference pressure theta
    * `logical(kind=)`: units = flag
* `is_restart`: Is restart
    * `logical(kind=)`: units = flag
* `do_rrtmgp_radiation_scheme`: Do rrtmgp radiation scheme
    * `logical(kind=)`: units = flag
* `identifier_for_ruc_land_surface_scheme`: Identifier for ruc land surface scheme
    * `integer(kind=)`: units = 1
* `control_for_land_surface_scheme_runoff_and_groundwater`: Control for land surface scheme runoff and groundwater
    * `integer(kind=)`: units = 1
* `identifier_for_scale_aware_mass_flux_deep_convection`: Identifier for scale aware mass flux deep convection
    * `integer(kind=)`: units = 1
* `identifier_for_scale_aware_mass_flux_shallow_convection`: Identifier for scale aware mass flux shallow convection
    * `integer(kind=)`: units = 1
* `identifier_for_simplified_arakawa_schubert_deep_convection`: Identifier for simplified arakawa schubert deep convection
    * `integer(kind=)`: units = 1
* `identifier_for_simplified_arakawa_schubert_shallow_convection`: Identifier for simplified arakawa schubert shallow convection
    * `integer(kind=)`: units = 1
* `do_scale_aware_mass_flux_deep_convection`: Do scale aware mass flux deep convection
    * `logical(kind=)`: units = flag
* `do_scale_aware_shin_hong_pbl_scheme`: Do scale aware shin hong pbl scheme
    * `logical(kind=)`: units = flag
* `do_scale_aware_tke_moist_edmf_pbl`: Do scale aware tke moist edmf pbl
    * `logical(kind=)`: units = flag
* `do_sgs_cellular_automata`: Do sgs cellular automata
    * `logical(kind=)`: units = flag
* `do_simplified_arakawa_schubert_shallow_convection`: Do simplified arakawa schubert shallow convection
    * `logical(kind=)`: units = flag
* `do_shoc`: Do shoc
    * `logical(kind=)`: units = flag
* `do_shoc_after_convection`: Do shoc after convection
    * `logical(kind=)`: units = flag
* `control_for_land_surface_scheme_soil_and_snow_temperature_time_integration`: Control for land surface scheme soil and snow temperature time integration
    * `integer(kind=)`: units = 1
* `control_for_land_surface_scheme_soil_moisture_factor_stomatal_resistance`: Control for land surface scheme soil moisture factor stomatal resistance
    * `integer(kind=)`: units = 1
* `control_for_solar_constant`: Control for solar constant
    * `integer(kind=)`: units = 1
* `do_stochastic_cloud_fraction_perturbations`: Do stochastic cloud fraction perturbations
    * `logical(kind=)`: units = flag
* `do_stochastic_microphysics_perturbations`: Do stochastic microphysics perturbations
    * `logical(kind=)`: units = flag
* `do_stochastic_physics_perturbations`: Do stochastic physics perturbations
    * `logical(kind=)`: units = flag
* `do_stochastic_radiative_heating_perturbations`: Do stochastic radiative heating perturbations
    * `logical(kind=)`: units = flag
* `do_stochastic_shum_option`: Do stochastic shum option
    * `logical(kind=)`: units = flag
* `do_stochastic_skeb_option`: Do stochastic skeb option
    * `logical(kind=)`: units = flag
* `do_stratospheric_water_vapor_physics`: Do stratospheric water vapor physics
    * `logical(kind=)`: units = flag
* `control_for_land_surface_scheme_supercooled_liquid_water`: Control for land surface scheme supercooled liquid water
    * `integer(kind=)`: units = 1
* `control_for_surface_emissivity`: Control for surface emissivity
    * `integer(kind=)`: units = 1
* `control_for_land_surface_scheme_surface_layer_drag_coefficient`: Control for land surface scheme surface layer drag coefficient
    * `integer(kind=)`: units = 1
* `control_for_surface_roughness_option_over_water`: Control for surface roughness option over water
    * `integer(kind=)`: units = 1
* `control_for_sw_clouds_subgrid_approximation`: Control for sw clouds subgrid approximation
    * `integer(kind=)`: units = 1
* `control_for_land_surface_scheme_thermal_conductivity_option`: Control for land surface scheme thermal conductivity option
    * `integer(kind=)`: units = 1
* `identifier_for_thompson_microphysics_scheme`: Identifier for thompson microphysics scheme
    * `integer(kind=)`: units = 1
* `do_ugwp_version_0`: Do ugwp version 0
    * `logical(kind=)`: units = flag
* `do_ugwp_version_0_nonorographic_gwd`: Do ugwp version 0 nonorographic gwd
    * `logical(kind=)`: units = flag
* `do_ugwp_version_0_orographic_gwd`: Do ugwp version 0 orographic gwd
    * `logical(kind=)`: units = flag
* `do_ugwp_version_1`: Do ugwp version 1
    * `logical(kind=)`: units = flag
* `do_ugwp_version_1_nonorographic_gwd`: Do ugwp version 1 nonorographic gwd
    * `logical(kind=)`: units = flag
* `do_ugwp_version_1_orographic_gwd`: Do ugwp version 1 orographic gwd
    * `logical(kind=)`: units = flag
* `do_shoc_cloud_area_fraction_for_radiation`: Do shoc cloud area fraction for radiation
    * `logical(kind=)`: units = flag
* `control_for_surface_layer_scheme_skin_temperature_update`: Control for surface layer scheme skin temperature update
    * `integer(kind=)`: units = 1
* `control_for_surface_albedo`: Control for surface albedo
    * `integer(kind=)`: units = 1
* `control_for_prescribed_co2`: Control for prescribed co2
    * `integer(kind=)`: units = 1
* `control_for_vertical_index_direction`: Control for vertical index direction
    * `integer(kind=)`: units = 1
* `do_ocean_wave_coupling`: Do ocean wave coupling
    * `logical(kind=)`: units = flag
* `do_one_way_ocean_wave_coupling_to_atmosphere`: Do one way ocean wave coupling to atmosphere
    * `logical(kind=)`: units = flag
* `identifier_for_wsm6_microphysics_scheme`: Identifier for wsm6 microphysics scheme
    * `integer(kind=)`: units = 1
* `do_ysu_pbl_scheme`: Do ysu pbl scheme
    * `logical(kind=)`: units = flag
* `identifier_for_zhao_carr_microphysics_scheme`: Identifier for zhao carr microphysics scheme
    * `integer(kind=)`: units = 1
* `identifier_for_zhao_carr_pdf_microphysics_scheme`: Identifier for zhao carr pdf microphysics scheme
    * `integer(kind=)`: units = 1
* `do_hurricane_specific_code_in_hybrid_edmf_pbl_scheme`: Do hurricane specific code in hybrid edmf pbl scheme
    * `logical(kind=)`: units = flag
* `do_integrated_dynamics_through_earths_atmosphere`: Do integrated dynamics through earths atmosphere
    * `logical(kind=)`: units = flag
* `do_print`: Do print
    * `logical(kind=)`: units = flag
* `do_save_shallow_convective_cloud_area_fraction`: Do save shallow convective cloud area fraction
    * `logical(kind=)`: units = flag
* `do_tke_dissipation_heating`: Do tke dissipation heating
    * `logical(kind=)`: units = flag
* `do_call_longwave_radiation`: Do call longwave radiation
    * `logical(kind=)`: units = flag
* `do_rrtmg_cloud_optics`: Do rrtmg cloud optics
    * `logical(kind=)`: units = flag
* `do_rrtmgp_cloud_optics_look_up_table`: Do rrtmgp cloud optics look up table
    * `logical(kind=)`: units = flag
* `do_rrtmgp_cloud_optics_with_pade_approximation`: Do rrtmgp cloud optics with pade approximation
    * `logical(kind=)`: units = flag
* `do_rrtmgp_longwave_jacobian`: Do rrtmgp longwave jacobian
    * `logical(kind=)`: units = flag
* `do_call_shortwave_radiation`: Do call shortwave radiation
    * `logical(kind=)`: units = flag
* `do_longwave_scattering_in_cloud_optics`: Do longwave scattering in cloud optics
    * `logical(kind=)`: units = flag
* `do_tracer_xyz_dimensioned_diagnostics`: Do tracer xyz dimensioned diagnostics
    * `logical(kind=)`: units = flag
* `control_for_variable_bulk_richardson_number`: Control for variable bulk richardson number
    * `real(kind=kind_phys)`: units = 1
* `date_and_time_of_forecast_in_united_states_order`: Date and time of forecast in united states order
    * `integer(kind=)`: units = 1
* `forecast_utc_hour`: Forecast utc hour
    * `real(kind=kind_phys)`: units = h
* `forecast_time`: Forecast time
    * `real(kind=kind_phys)`: units = h
* `forecast_time_on_previous_timestep`: Forecast time on previous timestep
    * `real(kind=kind_phys)`: units = h
* `period_of_longwave_radiation_calls`: Period of longwave radiation calls
    * `real(kind=kind_phys)`: units = s
* `period_of_shortwave_radiation_calls`: Period of shortwave radiation calls
    * `real(kind=kind_phys)`: units = s
* `all_ice_cloud_threshold_temperature`: All ice cloud threshold temperature
    * `real(kind=kind_phys)`: units = K
* `control_for_gravitational_settling_of_cloud_droplets`: Control for gravitational settling of cloud droplets
    * `integer(kind=)`: units = 1
* `control_for_drag_suite_gravity_wave_drag`: Control for drag suite gravity wave drag
    * `integer(kind=)`: units = 1
* `horizontal_loop_extent`: Horizontal loop extent
    * `integer(kind=)`: units = count
* `period_of_diagnostics_reset`: Period of diagnostics reset
    * `real(kind=kind_phys)`: units = h
* `tunable_parameter_for_ice_supersaturation`: Tunable parameter for ice supersaturation
    * `real(kind=kind_phys)`: units = 1
* `index_of_ice_vegetation_category`: Index of ice vegetation category
    * `integer(kind=)`: units = index
* `vertical_dimension_of_sea_ice`: Vertical dimension of sea ice
    * `integer(kind=)`: units = count
* `index_of_air_temperature_on_previous_timestep_in_xyz_dimensioned_restart_array`: Index of air temperature on previous timestep in xyz dimensioned restart array
    * `integer(kind=)`: units = index
* `index_of_air_temperature_two_timesteps_back_in_xyz_dimensioned_restart_array`: Index of air temperature two timesteps back in xyz dimensioned restart array
    * `integer(kind=)`: units = index
* `index_of_nonconvective_cloud_area_fraction_in_atmosphere_layer_in_tracer_concentration_array`: Index of nonconvective cloud area fraction in atmosphere layer in tracer concentration array
    * `integer(kind=)`: units = index
* `index_of_nonconvective_cloud_area_fraction_in_atmosphere_layer_in_xyz_dimensioned_restart_array`: Index of nonconvective cloud area fraction in atmosphere layer in xyz dimensioned restart array
    * `integer(kind=)`: units = index
* `index_of_cloud_liquid_water_effective_radius_in_xyz_dimensioned_restart_array`: Index of cloud liquid water effective radius in xyz dimensioned restart array
    * `integer(kind=)`: units = index
* `index_of_convective_cloud_area_fraction_in_xyz_dimensioned_restart_array`: Index of convective cloud area fraction in xyz dimensioned restart array
    * `integer(kind=)`: units = index
* `index_of_convective_cloud_condensate_mixing_ratio_wrt_moist_air_in_xyz_dimensioned_restart_array`: Index of convective cloud condensate mass mixing ratio with respect to moist air in the XYZ-dimensioned restart array
    * `integer(kind=)`: units = index
* `index_of_horizontal_gridpoint_for_debug_output`: Index of horizontal gridpoint for debug output
    * `integer(kind=)`: units = index
* `index_of_first_chemical_tracer_in_tracer_concentration_array`: Index of first chemical tracer in tracer concentration array
    * `integer(kind=)`: units = index
* `index_of_graupel_mixing_ratio_wrt_moist_air_in_tracer_concentration_array`: Index of graupel mass mixing ratio with respect to moist air in the tracer concentration array
    * `integer(kind=)`: units = index
* `index_of_graupel_effective_radius_in_xyz_dimensioned_restart_array`: Index of graupel effective radius in xyz dimensioned restart array
    * `integer(kind=)`: units = index
* `index_of_mass_number_concentration_of_graupel_in_tracer_concentration_array`: Index of mass number concentration of graupel in tracer concentration array
    * `integer(kind=)`: units = index
* `index_of_cloud_ice_mixing_ratio_wrt_moist_air_in_tracer_concentration_array`: Index of cloud ice mass mixing ratio with respect to moist air in the tracer concentration array
    * `integer(kind=)`: units = index
* `index_of_mass_number_concentration_of_cloud_ice_in_tracer_concentration_array`: Index of mass number concentration of cloud ice in tracer concentration array
    * `integer(kind=)`: units = index
* `index_of_cloud_ice_effective_radius_in_xyz_dimensioned_restart_array`: Index of cloud ice effective radius in xyz dimensioned restart array
    * `integer(kind=)`: units = index
* `index_of_mass_number_concentration_of_nonhygroscopic_ice_nucleating_aerosols_in_tracer_concentration_array`: Index of mass number concentration of nonhygroscopic ice nucleating aerosols in tracer concentration array
    * `integer(kind=)`: units = index
* `index_of_cloud_liquid_water_mixing_ratio_wrt_moist_air_in_tracer_concentration_array`: Index of liquid water mass mixing ratio with respect to moist air in the tracer concentration array
    * `integer(kind=)`: units = index
* `index_of_mass_number_concentration_of_cloud_droplets_in_tracer_concentration_array`: Index of mass number concentration of cloud droplets in tracer concentration array
    * `integer(kind=)`: units = index
* `index_of_mass_weighted_rime_factor_in_tracer_concentration_array`: Index of mass weighted rime factor in tracer concentration array
    * `integer(kind=)`: units = index
* `index_of_ozone_mixing_ratio_wrt_moist_air_in_tracer_concentration_array`: Index of ozone mass mixing ratio with respect to moist air in the tracer concentration array
    * `integer(kind=)`: units = index
* `index_of_rain_effective_radius_in_xyz_dimensioned_restart_array`: Index of rain effective radius in xyz dimensioned restart array
    * `integer(kind=)`: units = index
* `index_of_mass_number_concentration_of_rain_in_tracer_concentration_array`: Index of mass number concentration of rain in tracer concentration array
    * `integer(kind=)`: units = index
* `index_of_rain_mixing_ratio_wrt_moist_air_in_tracer_concentration_array`: Index of rain mass mixing ratio with respect to moist air in the tracer concentration array
    * `integer(kind=)`: units = index
* `index_of_snow_effective_radius_in_xyz_dimensioned_restart_array`: Index of snow effective radius in xyz dimensioned restart array
    * `integer(kind=)`: units = index
* `index_of_mass_number_concentration_of_snow_in_tracer_concentration_array`: Index of mass number concentration of snow in tracer concentration array
    * `integer(kind=)`: units = index
* `index_of_snow_mixing_ratio_wrt_moist_air_in_tracer_concentration_array`: Index of snow mass mixing ratio with respect to moist air in the tracer concentration array
    * `integer(kind=)`: units = index
* `index_of_water_vapor_mixing_ratio_wrt_moist_air_on_previous_timestep_in_xyz_dimensioned_restart_array`: Index of specific humidity (water vapor mass mixing ratio with respect to moist air) on previous timestep in xyz dimensioned restart array
    * `integer(kind=)`: units = index
* `index_of_water_vapor_mixing_ratio_wrt_moist_air_two_timesteps_back_in_xyz_dimensioned_restart_array`: Index of specific humidity (water vapor mass mixing ratio with respect to moist air) two timesteps back in xyz dimensioned restart array
    * `integer(kind=)`: units = index
* `control_for_stochastic_land_surface_perturbation`: Control for stochastic land surface perturbation
    * `integer(kind=)`: units = 1
* `index_of_air_pressure_at_surface_on_previous_timestep_in_xyz_dimensioned_restart_array`: Index of air pressure at surface on previous timestep in xyz dimensioned restart array
    * `integer(kind=)`: units = index
* `index_of_air_pressure_at_surface_two_timesteps_back_in_xyz_dimensioned_tracer_array`: Index of air pressure at surface two timesteps back in xyz dimensioned tracer array
    * `integer(kind=)`: units = index
* `index_of_enhancement_to_wind_speed_at_surface_adjacent_layer_due_to_convectionin_in_xy_dimensioned_restart_array`: Index of enhancement to wind speed at surface adjacent layer due to convectionin in xy dimensioned restart array
    * `integer(kind=)`: units = index
* `index_of_turbulent_kinetic_energy_in_tracer_concentration_array`: Index of turbulent kinetic energy in tracer concentration array
    * `integer(kind=)`: units = index
* `index_of_mass_number_concentration_of_hygroscopic_aerosols_in_tracer_concentration_array`: Index of mass number concentration of hygroscopic aerosols in tracer concentration array
    * `integer(kind=)`: units = index
* `index_of_water_vapor_mixing_ratio_wrt_moist_air_in_tracer_concentration_array`: Index of specific humidity (water vapor mass mixing ratio with respect to moist air) in tracer concentration array
    * `integer(kind=)`: units = index
* `index_of_atmosphere_heat_diffusivity_in_xyz_dimensioned_restart_array`: Index of atmosphere heat diffusivity in xyz dimensioned restart array
    * `integer(kind=)`: units = index
* `index_of_upward_virtual_potential_temperature_flux_in_xyz_dimensioned_restart_array`: Index of upward virtual potential temperature flux in xyz dimensioned restart array
    * `integer(kind=)`: units = index
* `index_of_subgrid_cloud_area_fraction_in_atmosphere_layer_in_xyz_dimensioned_restart_array`: Index of subgrid cloud area fraction in atmosphere layer in xyz dimensioned restart array
    * `integer(kind=)`: units = index
* `index_of_timestep`: Index of timestep
    * `integer(kind=)`: units = index
* `reciprocal_of_grid_scale_range`: Reciprocal of grid scale range
    * `real(kind=kind_phys)`: units = rad2 m-2
* `iounit_of_log`: Iounit of log
    * `integer(kind=)`: units = 1
* `iounit_of_namelist`: Iounit of namelist
    * `integer(kind=)`: units = 1
* `forecast_julian_day`: Forecast julian day
    * `real(kind=kind_phys)`: units = days
* `min_lake_ice_area_fraction`: Min lake ice area fraction
    * `real(kind=kind_phys)`: units = fraction
* `multiplicative_tuning_parameter_for_reduced_latent_heat_flux_due_to_canopy_heat_storage`: Multiplicative tuning parameter for reduced latent heat flux due to canopy heat storage
    * `real(kind=kind_phys)`: units = 1
* `max_tendency_of_air_potential_temperature_due_to_large_scale_precipitation`: Max tendency of air potential temperature due to large scale precipitation
    * `real(kind=kind_phys)`: units = K s-1
* `lower_bound_of_vertical_dimension_of_surface_snow`: Lower bound of vertical dimension of surface snow
    * `integer(kind=)`: units = count
* `land_surface_perturbation_magnitudes`: Land surface perturbation magnitudes
    * `real(kind=kind_phys)`: units = variable
* `max_critical_relative_humidity`: Max critical relative humidity
    * `real(kind=kind_phys)`: units = fraction
* `max_grid_scale`: Max grid scale
    * `real(kind=kind_phys)`: units = m2 rad-2
* `maximum_soil_moisture_content_for_land_surface_model`: Maximum soil moisture content for land surface model
    * `real(kind=kind_phys)`: units = m
* `do_allow_supersaturation_after_sedimentation`: Do allow supersaturation after sedimentation
    * `logical(kind=)`: units = flag
* `autoconversion_to_snow_size_threshold`: Autoconversion to snow size threshold
    * `real(kind=kind_phys)`: units = um
* `bergeron_findeisen_process_efficiency_factor`: Bergeron findeisen process efficiency factor
    * `real(kind=kind_phys)`: units = fraction
* `relative_variance_of_subgrid_cloud_condensate_distribution`: Relative variance of subgrid cloud condensate distribution
    * `real(kind=kind_phys)`: units = kg2 kg-2
* `prescribed_number_concentration_of_cloud_droplets`: Prescribed number concentration of cloud droplets
    * `real(kind=kind_phys)`: units = m-3
* `do_prescribed_number_concentration_of_cloud_droplets`: Do prescribed number concentration of cloud droplets
    * `logical(kind=)`: units = flag
* `do_cloud_ice_processes`: Do cloud ice processes
    * `logical(kind=)`: units = flag
* `do_gmao_autoconversion_to_snow`: Do gmao autoconversion to snow
    * `logical(kind=)`: units = flag
* `do_graupel_instead_of_hail`: Do graupel instead of hail
    * `logical(kind=)`: units = flag
* `do_hail_instead_of_graupel`: Do hail instead of graupel
    * `logical(kind=)`: units = flag
* `do_heterogeneous_nucleation`: Do heterogeneous nucleation
    * `logical(kind=)`: units = flag
* `do_liu_autoconversion_to_rain`: Do liu autoconversion to rain
    * `logical(kind=)`: units = flag
* `do_seifert_and_beheng_2001_autoconversion`: Do seifert and beheng 2001 autoconversion
    * `logical(kind=)`: units = flag
* `do_uniform_subcolumns`: Do uniform subcolumns
    * `logical(kind=)`: units = flag
* `do_prescribed_number_concentration_of_graupel`: Do prescribed number concentration of graupel
    * `logical(kind=)`: units = flag
* `do_prescribed_number_concentration_of_cloud_ice`: Do prescribed number concentration of cloud ice
    * `logical(kind=)`: units = flag
* `prescribed_number_concentration_of_graupel`: Prescribed number concentration of graupel
    * `real(kind=kind_phys)`: units = m-3
* `prescribed_number_concentration_of_cloud_ice`: Prescribed number concentration of cloud ice
    * `real(kind=kind_phys)`: units = m-3
* `minimum_cloud_condensate_mixing_ratio_wrt_moist_air_threshold`: Minimum threshold cloud condensate mass mixing ratio with respect to moist air
    * `real(kind=kind_phys)`: units = kg kg-1
* `minimum_cloud_liquid_water_mixing_ratio_wrt_moist_air_threshold`: Minimum threshold cloud liquid water mass mixing ratio with respect to moist air
    * `real(kind=kind_phys)`: units = kg kg-1
* `minimum_cloud_ice_mixing_ratio_wrt_moist_air_threshold`: Minimum threshold cloud ice mass mixing ratio with respect to moist air
    * `real(kind=kind_phys)`: units = kg kg-1
* `relative_humidity_threshold_for_ice_nucleation`: Relative humidity threshold for ice nucleation
    * `real(kind=kind_phys)`: units = fraction
* `timescale_for_autoconversion_to_snow`: Timescale for autoconversion to snow
    * `real(kind=kind_phys)`: units = s
* `alpha_tuning_coefficient_for_morrison_gettelman_microphysics_scheme`: Alpha tuning coefficient for morrison gettelman microphysics scheme
    * `real(kind=kind_phys)`: units = 1
* `control_for_precipitation_area_fraction_method`: Control for precipitation area fraction method
    * `character(kind=len=16)`: units = none
* `minimum_large_ice_fraction`: Minimum large ice fraction
    * `real(kind=kind_phys)`: units = fraction
* `minimum_pressure_in_rrtmgp`: Minimum pressure in rrtmgp
    * `real(kind=kind_phys)`: units = Pa
* `min_grid_scale`: Min grid scale
    * `real(kind=kind_phys)`: units = m2 rad-2
* `minimum_soil_moisture_content_for_land_surface_model`: Minimum soil moisture content for land surface model
    * `real(kind=kind_phys)`: units = m
* `minimum_temperature_in_rrtmgp`: Minimum temperature in rrtmgp
    * `real(kind=kind_phys)`: units = K
* `control_for_total_water_mixing_in_mellor_yamada_nakanishi_niino_pbl_scheme`: Control for total water mixing in mellor yamada nakanishi niino pbl scheme
    * `integer(kind=)`: units = 1
* `control_for_mixing_length_in_mellor_yamada_nakanishi_niino_pbl_scheme`: Control for mixing length in mellor yamada nakanishi niino pbl scheme
    * `integer(kind=)`: units = 1
* `momentum_transport_reduction_factor_due_to_pressure_gradient_force_for_deep_convection`: Momentum transport reduction factor due to pressure gradient force for deep convection
    * `real(kind=kind_phys)`: units = fraction
* `momentum_transport_reduction_factor_due_to_pressure_gradient_force_for_shallow_convection`: Momentum transport reduction factor due to pressure gradient force for shallow convection
    * `real(kind=kind_phys)`: units = fraction
* `mpi_communicator`: Mpi communicator
    * `integer(kind=)`: units = index
* `mpi_rank`: Mpi rank
    * `integer(kind=)`: units = index
* `mpi_root`: Mpi root
    * `integer(kind=)`: units = index
* `number_of_mpi_tasks`: Number of mpi tasks
    * `integer(kind=)`: units = count
* `tunable_parameter_for_critical_cloud_workfunction_in_relaxed_arakawa_schubert_deep_convection`: Tunable parameter for critical cloud workfunction in relaxed arakawa schubert deep convection
    * `real(kind=kind_phys)`: units = 1
* `tunable_parameters_for_convective_gravity_wave_drag`: Tunable parameters for convective gravity wave drag
    * `real(kind=kind_phys)`: units = 1
* `multiplicative_tunable_parameters_for_mountain_blocking_and_orographic_gravity_wave_drag`: Multiplicative tunable parameters for mountain blocking and orographic gravity wave drag
    * `real(kind=kind_phys)`: units = 1
* `control_for_additional_diagnostics_in_mellor_yamada_nakanishi_niino_pbl_scheme`: Control for additional diagnostics in mellor yamada nakanishi niino pbl scheme
    * `integer(kind=)`: units = 1
* `filename_of_namelist`: Filename of namelist
    * `character(kind=len=64)`: units = none
* `filename_of_internal_namelist`: Filename of internal namelist
    * `character(kind=len=256)`: units = none
* `number_of_xy_dimensioned_auxiliary_arrays`: Number of xy dimensioned auxiliary arrays
    * `integer(kind=)`: units = count
* `number_of_pdf_based_variables_in_xyz_dimensioned_restart_array`: Number of pdf based variables in xyz dimensioned restart array
    * `integer(kind=)`: units = count
* `number_of_xyz_dimensioned_auxiliary_arrays`: Number of xyz dimensioned auxiliary arrays
    * `integer(kind=)`: units = count
* `number_of_radiatively_active_gases`: Number of radiatively active gases
    * `integer(kind=)`: units = count
* `number_of_aerosol_tracers`: Number of aerosol tracers
    * `integer(kind=)`: units = count
* `number_of_gaussian_quadrature_angles_for_radiation`: Number of gaussian quadrature angles for radiation
    * `integer(kind=)`: units = count
* `number_of_chemical_tracers`: Number of chemical tracers
    * `integer(kind=)`: units = count
* `number_of_condensate_species`: Number of condensate species
    * `integer(kind=)`: units = count
* `number_of_cloud_types_in_chikira_sugiyama_deep_convection`: Number of cloud types in chikira sugiyama deep convection
    * `integer(kind=)`: units = count
* `number_of_convective_cloud_variables_in_xyz_dimensioned_restart_array`: Number of convective cloud variables in xyz dimensioned restart array
    * `integer(kind=)`: units = count
* `number_of_days_in_current_year`: Number of days in current year
    * `integer(kind=)`: units = days
* `number_of_equatorial_longitude_points`: Number of equatorial longitude points
    * `integer(kind=)`: units = count
* `number_of_variables_in_xy_dimensioned_restart_array`: Number of variables in xy dimensioned restart array
    * `integer(kind=)`: units = count
* `number_of_variables_in_xyz_dimensioned_restart_array`: Number of variables in xyz dimensioned restart array
    * `integer(kind=)`: units = count
* `number_of_frozen_precipitation_species`: Number of frozen precipitation species
    * `integer(kind=)`: units = count
* `number_of_hydrometeors`: Number of hydrometeors
    * `integer(kind=)`: units = count
* `number_of_independent_cellular_automata`: Number of independent cellular automata
    * `integer(kind=)`: units = count
* `number_of_iterations_to_spin_up_cellular_automata`: Number of iterations to spin up cellular automata
    * `integer(kind=)`: units = count
* `number_of_perturbed_land_surface_variables`: Number of perturbed land surface variables
    * `integer(kind=)`: units = count
* `number_of_latitude_points`: Number of latitude points
    * `integer(kind=)`: units = count
* `number_of_lines_in_internal_namelist`: Number of lines in internal namelist
    * `integer(kind=)`: units = count
* `number_of_longwave_bands`: Number of longwave bands
    * `integer(kind=)`: units = count
* `number_of_longwave_spectral_points`: Number of longwave spectral points
    * `integer(kind=)`: units = count
* `number_of_x_points_for_current_cubed_sphere_tile`: Number of x points for current cubed sphere tile
    * `integer(kind=)`: units = count
* `number_of_x_points_for_current_mpi_rank`: Number of x points for current mpi rank
    * `integer(kind=)`: units = count
* `number_of_y_points_for_current_cubed_sphere_tile`: Number of y points for current cubed sphere tile
    * `integer(kind=)`: units = count
* `number_of_y_points_for_current_mpi_rank`: Number of y points for current mpi rank
    * `integer(kind=)`: units = count
* `number_of_diagnostics_variables_for_radiation`: Number of diagnostics variables for radiation
    * `integer(kind=)`: units = count
* `number_of_ice_roughness_categories`: Number of ice roughness categories
    * `integer(kind=)`: units = count
* `number_of_spectral_wave_truncation_for_simplified_arakawa_schubert_convection`: Number of spectral wave truncation for simplified arakawa schubert convection
    * `integer(kind=)`: units = count
* `number_of_statistical_measures_of_subgrid_orography`: Number of statistical measures of subgrid orography
    * `integer(kind=)`: units = count
* `number_of_shortwave_bands`: Number of shortwave bands
    * `integer(kind=)`: units = count
* `number_of_shortwave_spectral_points`: Number of shortwave spectral points
    * `integer(kind=)`: units = count
* `index_of_cubed_sphere_tile`: Index of cubed sphere tile
    * `integer(kind=)`: units = index
* `number_of_timesteps_between_diagnostics_resetting`: Number of timesteps between diagnostics resetting
    * `integer(kind=)`: units = count
* `number_of_timesteps_between_longwave_radiation_calls`: Number of timesteps between longwave radiation calls
    * `integer(kind=)`: units = count
* `number_of_timesteps_between_shortwave_radiation_calls`: Number of timesteps between shortwave radiation calls
    * `integer(kind=)`: units = count
* `number_of_timesteps_between_surface_cycling_calls`: Number of timesteps between surface cycling calls
    * `integer(kind=)`: units = count
* `number_of_timesteps_for_concurrent_radiation_and_remainder_physics_calls_after_model_initialization`: Number of timesteps for concurrent radiation and remainder physics calls after model initialization
    * `integer(kind=)`: units = count
* `number_of_tracers_plus_one`: Number of tracers plus one
    * `integer(kind=)`: units = count
* `vertical_dimension_for_radiation`: Vertical dimension for radiation
    * `integer(kind=)`: units = count
* `vertical_interface_dimension_for_radiation`: Vertical interface dimension for radiation
    * `integer(kind=)`: units = count
* `multiplicative_tuning_parameter_for_potential_evaporation`: Multiplicative tuning parameter for potential evaporation
    * `real(kind=kind_phys)`: units = 1
* `air_pressure_at_bottom_extent_of_rayleigh_damping`: Air pressure at bottom extent of rayleigh damping
    * `real(kind=kind_phys)`: units = Pa
* `rain_conversion_parameter_for_deep_convection`: Rain conversion parameter for deep convection
    * `real(kind=kind_phys)`: units = m-1
* `rain_conversion_parameter_for_shallow_convection`: Rain conversion parameter for shallow convection
    * `real(kind=kind_phys)`: units = m-1
* `rain_evaporation_coefficient_over_ocean_for_deep_convection`: Rain evaporation coefficient over ocean for deep convection
    * `real(kind=kind_phys)`: units = fraction
* `rain_evaporation_coefficient_over_land_for_deep_convection`: Rain evaporation coefficient over land for deep convection
    * `real(kind=kind_phys)`: units = fraction
* `filename_of_rrtmgp_longwave_cloud_optics_coefficients`: Filename of rrtmgp longwave cloud optics coefficients
    * `character(kind=len=128)`: units = none
* `filename_of_rrtmgp_shortwave_cloud_optics_coefficients`: Filename of rrtmgp shortwave cloud optics coefficients
    * `character(kind=len=128)`: units = none
* `filename_of_rrtmgp_longwave_k_distribution`: Filename of rrtmgp longwave k distribution
    * `character(kind=len=128)`: units = none
* `filename_of_rrtmgp_shortwave_k_distribution`: Filename of rrtmgp shortwave k distribution
    * `character(kind=len=128)`: units = none
* `do_rrtmgp_shortwave_and_rrtmg_longwave_radiation`: Do rrtmgp shortwave and rrtmg longwave radiation
    * `logical(kind=)`: units = flag
* `min_sea_ice_area_fraction`: Min sea ice area fraction
    * `real(kind=kind_phys)`: units = fraction
* `forecast_time_in_seconds`: Forecast time in seconds
    * `real(kind=kind_phys)`: units = s
* `random_number_seed_for_cellular_automata`: Random number seed for cellular automata
    * `integer(kind=)`: units = 1
* `random_number_seed_for_deep_convection`: Random number seed for deep convection
    * `integer(kind=)`: units = 1
* `control_for_tke_dissipation_method`: Control for tke dissipation method
    * `real(kind=kind_phys)`: units = 1
* `uncentering_coefficient_for_implicit_tke_integration`: Uncentering coefficient for implicit tke integration
    * `real(kind=kind_phys)`: units = 1
* `pressure_threshold_for_increased_tke_dissipation`: Pressure threshold for increased tke dissipation
    * `real(kind=kind_phys)`: units = Pa
* `multiplicative_tunable_parameter_for_tke_dissipation`: Multiplicative tunable parameter for tke dissipation
    * `real(kind=kind_phys)`: units = 1
* `multiplicative_tunable_parameter_for_tke_dissipation_at_surface_adjacent_layer`: Multiplicative tunable parameter for tke dissipation at surface adjacent layer
    * `real(kind=kind_phys)`: units = 1
* `sine_of_solar_declination_angle`: Sine of solar declination angle
    * `real(kind=kind_phys)`: units = 1
* `vertical_dimension_of_surface_snow`: Vertical dimension of surface snow
    * `integer(kind=)`: units = count
* `control_for_soil_type_dataset`: Control for soil type dataset
    * `integer(kind=)`: units = 1
* `vertical_dimension_of_soil`: Vertical dimension of soil
    * `integer(kind=)`: units = count
* `vertical_dimension_of_soil_internal_to_land_surface_scheme`: Vertical dimension of soil internal to land surface scheme
    * `integer(kind=)`: units = count
* `solar_constant`: Solar constant
    * `real(kind=kind_phys)`: units = W m-2
* `starting_x_index_for_current_mpi_rank`: Starting x index for current mpi rank
    * `integer(kind=)`: units = index
* `starting_y_index_for_current_mpi_rank`: Starting y index for current mpi rank
    * `integer(kind=)`: units = index
* `multiplicative_tuning_parameter_for_reduced_surface_heat_fluxes_due_to_canopy_heat_storage`: Multiplicative tuning parameter for reduced surface heat fluxes due to canopy heat storage
    * `real(kind=kind_phys)`: units = 1
* `thickness_of_soil_layers_for_land_surface_model`: Thickness of soil layers for land surface model
    * `real(kind=kind_phys)`: units = m
* `cellular_automata_vertical_velocity_perturbation_threshold_for_deep_convection`: Cellular automata vertical velocity perturbation threshold for deep convection
    * `real(kind=kind_phys)`: units = m s-1
* `period_of_maximum_diagnostics_reset`: Period of maximum diagnostics reset
    * `real(kind=kind_phys)`: units = s
* `timescale_for_rayleigh_damping`: Timescale for rayleigh damping
    * `real(kind=kind_phys)`: units = d
* `time_elapsed_since_diagnostics_reset`: Time elapsed since diagnostics reset
    * `real(kind=kind_phys)`: units = h
* `timestep_for_dynamics`: Timestep for dynamics
    * `real(kind=kind_phys)`: units = s
* `do_tke_advection`: Do tke advection
    * `logical(kind=)`: units = flag
* `control_for_tke_budget_output`: Control for tke budget output
    * `integer(kind=)`: units = 1
* `multiplicative_tuning_parameter_for_tke_dissipative_heating`: Multiplicative tuning parameter for tke dissipative heating
    * `real(kind=kind_phys)`: units = 1
* `total_amplitude_of_sppt_perturbation`: Total amplitude of sppt perturbation
    * `real(kind=kind_phys)`: units = 1
* `do_turbulent_orographic_form_drag_in_unified_gravity_wave_physics_gravity_wave_drag_scheme`: Do turbulent orographic form drag in unified gravity wave physics gravity wave drag scheme
    * `logical(kind=)`: units = flag
* `updraft_area_fraction_in_scale_aware_tke_moist_edmf_pbl_scheme`: Updraft area fraction in scale aware tke moist edmf pbl scheme
    * `real(kind=kind_phys)`: units = fraction
* `tunable_parameter_1_for_maximum_cloud_base_updraft_velocity_in_chikira_sugiyama_deep_convection`: Tunable parameter 1 for maximum cloud base updraft velocity in chikira sugiyama deep convection
    * `real(kind=kind_phys)`: units = m s-1
* `tunable_parameter_2_for_maximum_cloud_base_updraft_velocity_in_chikira_sugiyama_deep_convection`: Tunable parameter 2 for maximum cloud base updraft velocity in chikira sugiyama deep convection
    * `real(kind=kind_phys)`: units = m s-1
* `upper_bound_of_vertical_dimension_of_surface_snow`: Upper bound of vertical dimension of surface snow
    * `integer(kind=)`: units = count
* `index_of_urban_vegetation_category`: Index of urban vegetation category
    * `integer(kind=)`: units = index
* `land_surface_perturbation_variables`: Land surface perturbation variables
    * `character(kind=len=3)`: units = none
* `control_for_vegetation_dataset`: Control for vegetation dataset
    * `integer(kind=)`: units = 1
* `vertical_layer_dimension_minus_one`: Vertical layer dimension minus one
    * `integer(kind=)`: units = count
* `sigma_pressure_hybrid_vertical_coordinate`: Sigma pressure hybrid vertical coordinate
    * `real(kind=kind_phys)`: units = 1
* `lower_bound_for_depth_of_sea_temperature_for_nsstm`: Lower bound for depth of sea temperature for nsstm
    * `integer(kind=)`: units = mm
* `upper_bound_for_depth_of_sea_temperature_for_nsstm`: Upper bound for depth of sea temperature for nsstm
    * `integer(kind=)`: units = mm
* `index_of_water_vegetation_category`: Index of water vegetation category
    * `integer(kind=)`: units = index
* `filename_of_micm_configuration`: Filename of micm configuration
    * `character(kind=len=*)`: units = none
## GFS_typedefs_GFS_interstitial_type
* `cloud_ice_mixing_ratio_wrt_moist_air_interstitial`: Cloud ice mass mixing ratio with respect to moist air in interstitial scheme
    * `real(kind=kind_phys)`: units = kg kg-1
* `cloud_liquid_water_mixing_ratio_wrt_moist_air_interstitial`: Cloud liquid water mass mixing ratio with respect to moist air in interstitial scheme
    * `real(kind=kind_phys)`: units = kg kg-1
* `radiatively_active_gases`: Radiatively active gases
    * `character(kind=len=128)`: units = none
* `process_split_cumulative_tendency_of_air_temperature`: Process split cumulative tendency of air temperature
    * `real(kind=kind_phys)`: units = K s-1
* `process_split_cumulative_tendency_of_mass_number_concentration_of_cloud_liquid_water_particles_in_air`: Process split cumulative tendency of mass number concentration of cloud liquid water particles in air
    * `real(kind=kind_phys)`: units = kg-1 s-1
* `process_split_cumulative_tendency_of_graupel_mixing_ratio_wrt_moist_air`: Process-split cumulative tendency of the graupel mass mixing ratio with respect to moist air
    * `real(kind=kind_phys)`: units = kg kg-1 s-1
* `process_split_cumulative_tendency_of_cloud_ice_mixing_ratio_wrt_moist_air`: Process-split cumulative tendency of the cloud ice mass mixing ratio with respect to moist air
    * `real(kind=kind_phys)`: units = kg kg-1 s-1
* `process_split_cumulative_tendency_of_mass_number_concentration_of_nonhygroscopic_ice_nucleating_aerosols`: Process split cumulative tendency of mass number concentration of nonhygroscopic ice nucleating aerosols
    * `real(kind=kind_phys)`: units = kg-1 s-1
* `process_split_cumulative_tendency_of_mass_number_concentration_of_cloud_ice_water_crystals_in_air`: Process split cumulative tendency of mass number concentration of cloud ice water crystals in air
    * `real(kind=kind_phys)`: units = kg-1 s-1
* `process_split_cumulative_tendency_of_cloud_liquid_water_mixing_ratio_wrt_moist_air`: Process-split cumulative tendency of the cloud liquid water mass mixing ratio with respect to moist air
    * `real(kind=kind_phys)`: units = kg kg-1 s-1
* `process_split_cumulative_tendency_of_ozone_mixing_ratio_wrt_moist_air`: Process-split cumulative tendency of the ozone mass mixing ratio with respect to moist air
    * `real(kind=kind_phys)`: units = kg kg-1 s-1
* `process_split_cumulative_tendency_of_rain_mixing_ratio_wrt_moist_air`: Process-split cumulative tendency of the rain mass mixing ratio with respect to moist air
    * `real(kind=kind_phys)`: units = kg kg-1 s-1
* `process_split_cumulative_tendency_of_snow_mixing_ratio_wrt_moist_air`: Process-split cumulative tendency of the snow mass mixing ratio with respect to moist air
    * `real(kind=kind_phys)`: units = kg kg-1 s-1
* `process_split_cumulative_tendency_of_tracers`: Process split cumulative tendency of tracers
    * `real(kind=kind_phys)`: units = kg kg-1 s-1
* `process_split_cumulative_tendency_of_turbulent_kinetic_energy`: Process split cumulative tendency of turbulent kinetic energy
    * `real(kind=kind_phys)`: units = J s-1
* `process_split_cumulative_tendency_of_mass_number_concentration_of_hygroscopic_aerosols`: Process split cumulative tendency of mass number concentration of hygroscopic aerosols
    * `real(kind=kind_phys)`: units = kg-1 s-1
* `process_split_cumulative_tendency_of_water_vapor_mixing_ratio_wrt_moist_air`: Process-split cumulative tendency of specific humidity (water vapor mass mixing ratio with respect to moist air)
    * `real(kind=kind_phys)`: units = kg kg-1 s-1
* `process_split_cumulative_tendency_of_x_wind`: Process split cumulative tendency of x wind
    * `real(kind=kind_phys)`: units = m s-2
* `process_split_cumulative_tendency_of_y_wind`: Process split cumulative tendency of y wind
    * `real(kind=kind_phys)`: units = m s-2
* `vertical_interface_dimension_interstitial`: Vertical interface dimension interstitial
    * `integer(kind=)`: units = count
## GFS_typedefs_GFS_tbd_type
* `absolute_momentum_flux_due_to_nonorographic_gravity_wave_drag`: Absolute momentum flux due to nonorographic gravity wave drag
    * `real(kind=kind_phys)`: units = various
* `cumulative_lwe_thickness_of_convective_precipitation_amount_between_sw_radiation_calls`: Cumulative lwe thickness of convective precipitation amount between sw radiation calls
    * `real(kind=kind_phys)`: units = m
* `mass_number_concentration_of_aerosol_from_gocart_climatology`: Mass number concentration of aerosol from gocart climatology
    * `real(kind=kind_phys)`: units = kg-1
* `air_temperature_on_previous_timestep_in_xyz_dimensioned_restart_array`: Air temperature on previous timestep in xyz dimensioned restart array
    * `real(kind=kind_phys)`: units = K
* `air_temperature_two_timesteps_back`: Air temperature two timesteps back
    * `real(kind=kind_phys)`: units = K
* `atmosphere_boundary_layer_thickness`: Atmosphere boundary layer thickness
    * `real(kind=kind_phys)`: units = m
* `atmosphere_heat_diffusivity_from_shoc`: Atmosphere heat diffusivity from shoc
    * `real(kind=kind_phys)`: units = m2 s-1
* `atmosphere_updraft_convective_mass_flux_at_cloud_base_by_cloud_type`: Atmosphere updraft convective mass flux at cloud base by cloud type
    * `real(kind=kind_phys)`: units = kg m-2 s-1
* `cloud_fraction_for_mg`: Cloud fraction for mg
    * `real(kind=kind_phys)`: units = fraction
* `counter_for_grell_freitas_convection`: Counter for grell freitas convection
    * `integer(kind=)`: units = count
* `convective_cloud_area_fraction`: Convective cloud area fraction
    * `real(kind=kind_phys)`: units = fraction
* `convective_cloud_condensate_mixing_ratio_wrt_moist_air`: Convective cloud condensate mass mixing ratio with respect to moist air
    * `real(kind=kind_phys)`: units = kg kg-1
* `effective_radius_of_stratiform_cloud_graupel_particle`: Effective radius of stratiform cloud graupel particle
    * `real(kind=kind_phys)`: units = um
* `effective_radius_of_stratiform_cloud_ice_particle`: Effective radius of stratiform cloud ice particle
    * `real(kind=kind_phys)`: units = um
* `effective_radius_of_stratiform_cloud_liquid_water_particle`: Effective radius of stratiform cloud liquid water particle
    * `real(kind=kind_phys)`: units = um
* `effective_radius_of_stratiform_cloud_rain_particle`: Effective radius of stratiform cloud rain particle
    * `real(kind=kind_phys)`: units = um
* `effective_radius_of_stratiform_cloud_snow_particle`: Effective radius of stratiform cloud snow particle
    * `real(kind=kind_phys)`: units = um
* `stratospheric_water_vapor_forcing`: Stratospheric water vapor forcing
    * `real(kind=kind_phys)`: units = various
* `heat_exchange_coefficient_for_myj_schemes`: Heat exchange coefficient for myj schemes
    * `real(kind=kind_phys)`: units = m s-1
* `ice_nucleation_number_from_climatology`: Ice nucleation number from climatology
    * `real(kind=kind_phys)`: units = kg-1
* `upward_virtual_potential_temperature_flux`: Upward virtual potential temperature flux
    * `real(kind=kind_phys)`: units = K m s-1
* `upward_flux_of_water_vapor_mixing_ratio_wrt_moist_air_at_surface_for_mellor_yamada_janjic_surface_layer_scheme`: Upward flux of specific humidity (water vapor mass mixing ratio with respect to moist air) at surface for MYJ surface layer scheme
    * `real(kind=kind_phys)`: units = m s-1 kg kg-1
* `cumulative_max_vertical_index_at_cloud_base_between_sw_radiation_calls`: Cumulative max vertical index at cloud base between sw radiation calls
    * `real(kind=kind_phys)`: units = 1
* `map_of_block_column_number_to_global_i_index`: Map of block column number to global i index
    * `integer(kind=)`: units = index
* `map_of_block_column_number_to_global_j_index`: Map of block column number to global j index
    * `integer(kind=)`: units = index
* `turbulent_mixing_length`: Turbulent mixing length
    * `real(kind=kind_phys)`: units = m
* `water_vapor_mixing_ratio_wrt_moist_air_on_previous_timestep`: Specific humidity (water vapor mass mixing ratio with respect to moist air) on previous timestep
    * `real(kind=kind_phys)`: units = kg kg-1
* `tendency_of_water_vapor_mixing_ratio_wrt_moist_air_due_to_nonphysics`: Tendency of specific humidity (water vapor mass mixing ratio with respect to moist air) due to nonphysics
    * `real(kind=kind_phys)`: units = kg kg-1 s-1
* `momentum_exchange_coefficient_for_myj_schemes`: Momentum exchange coefficient for myj schemes
    * `real(kind=kind_phys)`: units = m s-1
* `ozone_forcing`: Ozone forcing
    * `real(kind=kind_phys)`: units = various
* `air_potential_temperature_at_top_of_viscous_sublayer`: Air potential temperature at top of viscous sublayer
    * `real(kind=kind_phys)`: units = K
* `variance_of_water_vapor_mixing_ratio_wrt_moist_air`: Variance of specific humidity (water vapor mass mixing ratio with respect to moist air)
    * `real(kind=kind_phys)`: units = kg2 kg-2
* `random_number`: Random number
    * `real(kind=kind_phys)`: units = 1
* `random_number_seed_for_mcica_longwave`: Random number seed for mcica longwave
    * `integer(kind=)`: units = 1
* `random_number_seed_for_mcica_shortwave`: Random number seed for mcica shortwave
    * `integer(kind=)`: units = 1
* `cumulative_min_vertical_index_at_cloud_base_between_sw_radiation_calls`: Cumulative min vertical index at cloud base between sw radiation calls
    * `real(kind=kind_phys)`: units = 1
* `water_vapor_mixing_ratio_wrt_moist_air_at_top_of_viscous_sublayer`: Specific humidity (water vapor mass mixing ratio with respect to moist air) at the top of the viscous sublayer
    * `real(kind=kind_phys)`: units = kg kg-1
* `stability_function_for_heat`: Stability function for heat
    * `real(kind=kind_phys)`: units = 1
* `subgrid_scale_cloud_area_fraction_in_atmosphere_layer`: Subgrid scale cloud area fraction in atmosphere layer
    * `real(kind=kind_phys)`: units = fraction
* `subgrid_scale_cloud_ice_mixing_ratio_wrt_moist_air`: Subgrid-scale cloud ice mass mixing ratio with respect to moist air
    * `real(kind=kind_phys)`: units = kg kg-1
* `subgrid_scale_cloud_liquid_water_mixing_ratio_wrt_moist_air`: Subgrid-scale cloud liquid water mass mixing ratio with respect to moist air
    * `real(kind=kind_phys)`: units = kg kg-1
* `subgrid_scale_cloud_fraction_from_shoc`: Subgrid scale cloud fraction from shoc
    * `real(kind=kind_phys)`: units = fraction
* `air_pressure_at_surface_on_previous_timestep`: Air pressure at surface on previous timestep
    * `real(kind=kind_phys)`: units = Pa
* `air_pressure_at_surface_two_timesteps_back`: Air pressure at surface two timesteps back
    * `real(kind=kind_phys)`: units = Pa
* `control_for_surface_layer_evaporation`: Control for surface layer evaporation
    * `real(kind=kind_phys)`: units = 1
* `water_vapor_mixing_ratio_wrt_moist_air_at_surface_for_myj_schemes`: Surface specific humidity (water vapor mass mixing ratio with respect to moist air) for MYJ schemes
    * `real(kind=kind_phys)`: units = kg kg-1
* `enhancement_to_wind_speed_at_surface_adjacent_layer_due_to_convection`: Enhancement to wind speed at surface adjacent layer due to convection
    * `real(kind=kind_phys)`: units = m s-1
* `covariance_of_air_temperature_and_water_vapor_mixing_ratio_wrt_moist_air`: Covariance of air temperature and specific humidity (water vapor mass mixing ratio with respect to moist air)
    * `real(kind=kind_phys)`: units = K kg kg-1
* `variance_of_air_temperature`: Variance of air temperature
    * `real(kind=kind_phys)`: units = K2
* `tendency_of_air_temperature_due_to_nonphysics`: Tendency of air temperature due to nonphysics
    * `real(kind=kind_phys)`: units = K s-1
* `tendency_of_air_temperature_to_withhold_from_sppt`: Tendency of air temperature to withhold from sppt
    * `real(kind=kind_phys)`: units = K s-1
* `tendency_of_activated_cloud_condensation_nuclei_from_climatology`: Tendency of activated cloud condensation nuclei from climatology
    * `real(kind=kind_phys)`: units = kg-1 s-1
* `lwe_thickness_of_rain_amount_on_dynamics_timestep_for_coupling`: Lwe thickness of rain amount on dynamics timestep for coupling
    * `real(kind=kind_phys)`: units = m
* `lwe_thickness_of_snowfall_amount_on_dynamics_timestep_for_coupling`: Lwe thickness of snowfall amount on dynamics timestep for coupling
    * `real(kind=kind_phys)`: units = m
* `nonadvected_turbulent_kinetic_energy_multiplied_by_2`: Nonadvected turbulent kinetic energy multiplied by 2
    * `real(kind=kind_phys)`: units = m2 s-2
* `x_wind_at_top_of_viscous_sublayer`: X wind at top of viscous sublayer
    * `real(kind=kind_phys)`: units = m s-1
* `y_wind_at_top_of_viscous_sublayer`: Y wind at top of viscous sublayer
    * `real(kind=kind_phys)`: units = m s-1
* `water_vapor_mixing_ratio_wrt_moist_air_on_previous_timestep_in_xyz_dimensioned_restart_array`: Specific humidity (water vapor mass mixing ratio with respect to moist air) on previous timestep in XYZ-dimensioned restart array
    * `real(kind=kind_phys)`: units = kg kg-1
* `water_vapor_mixing_ratio_wrt_moist_air_two_timesteps_back`: Specific humidity (water vapor mass mixing ratio with respect to moist air) two timesteps back
    * `real(kind=kind_phys)`: units = kg kg-1
* `weight_for_momentum_at_top_of_viscous_sublayer`: Weight for momentum at top of viscous sublayer
    * `real(kind=kind_phys)`: units = 1
* `weight_for_potential_temperature_at_top_of_viscous_sublayer`: Weight for potential temperature at top of viscous sublayer
    * `real(kind=kind_phys)`: units = 1
* `weight_for_water_vapor_mixing_ratio_wrt_moist_air_at_top_of_viscous_sublayer`: Weight for specific humidity (water vapor mass mixing ratio with respect to moist air) at the top of the viscous sublayer
    * `real(kind=kind_phys)`: units = 1
## GFS_typedefs_GFS_sfcprop_type
* `wet_canopy_area_fraction`: Wet canopy area fraction
    * `real(kind=kind_phys)`: units = fraction
* `baseline_surface_longwave_emissivity`: Baseline surface longwave emissivity
    * `real(kind=kind_phys)`: units = fraction
* `baseline_roughness_length`: Baseline surface roughness length
    * `real(kind=kind_phys)`: units = m
* `air_temperature_in_canopy`: Air temperature in canopy
    * `real(kind=kind_phys)`: units = K
* `air_vapor_pressure_in_canopy`: Air vapor pressure in canopy
    * `real(kind=kind_phys)`: units = Pa
* `canopy_intercepted_ice_mass`: Canopy intercepted ice mass
    * `real(kind=kind_phys)`: units = mm
* `canopy_intercepted_liquid_water`: Canopy intercepted liquid water
    * `real(kind=kind_phys)`: units = mm
* `canopy_water_amount`: Canopy water amount
    * `real(kind=kind_phys)`: units = kg m-2
* `cloud_condensed_water_mixing_ratio_wrt_moist_air_at_surface_over_ice`: Cloud condensed water mass mixing ratio with respect to moist air at surface over ice
    * `real(kind=kind_phys)`: units = kg kg-1
* `cloud_condensed_water_mixing_ratio_wrt_moist_air_at_surface_over_land`: Cloud condensed water mass mixing ratio with respect to moist air at surface over land
    * `real(kind=kind_phys)`: units = kg kg-1
* `coefficient_c_0`: Coefficient c 0
    * `real(kind=kind_phys)`: units = 1
* `coefficient_c_d`: Coefficient c d
    * `real(kind=kind_phys)`: units = 1
* `coefficient_w_0`: Coefficient w 0
    * `real(kind=kind_phys)`: units = 1
* `coefficient_w_d`: Coefficient w d
    * `real(kind=kind_phys)`: units = 1
* `convective_precipitation_rate_on_previous_timestep`: Convective precipitation rate on previous timestep
    * `real(kind=kind_phys)`: units = mm s-1
* `deep_soil_temperature`: Deep soil temperature
    * `real(kind=kind_phys)`: units = K
* `frozen_precipitation_density`: Frozen precipitation density
    * `real(kind=kind_phys)`: units = kg m-3
* `heat_content_in_diurnal_thermocline`: Heat content in diurnal thermocline
    * `real(kind=kind_phys)`: units = K m
* `diurnal_thermocline_layer_thickness`: Diurnal thermocline layer thickness
    * `real(kind=kind_phys)`: units = m
* `x_current_in_diurnal_thermocline`: X current in diurnal thermocline
    * `real(kind=kind_phys)`: units = m2 s-1
* `y_current_in_diurnal_thermocline`: Y current in diurnal thermocline
    * `real(kind=kind_phys)`: units = m2 s-1
* `volumetric_equilibrium_soil_moisture`: Volumetric equilibrium soil moisture
    * `real(kind=kind_phys)`: units = m3 m-3
* `explicit_precipitation_rate_on_previous_timestep`: Explicit precipitation rate on previous timestep
    * `real(kind=kind_phys)`: units = mm s-1
* `fast_soil_pool_mass_content_of_carbon`: Fast soil pool mass content of carbon
    * `real(kind=kind_phys)`: units = g m-2
* `fine_root_mass_content`: Fine root mass content
    * `real(kind=kind_phys)`: units = g m-2
* `control_for_frozen_soil_physics`: Control for frozen soil physics
    * `real(kind=kind_phys)`: units = 1
* `precipitation_type`: Precipitation type
    * `real(kind=kind_phys)`: units = 1
* `strong_cosz_area_fraction`: Strong cosz area fraction
    * `real(kind=kind_phys)`: units = fraction
* `weak_cosz_area_fraction`: Weak cosz area fraction
    * `real(kind=kind_phys)`: units = fraction
* `free_convection_layer_thickness_in_sea_water`: Free convection layer thickness in sea water
    * `real(kind=kind_phys)`: units = m
* `consecutive_calls_for_grell_freitas_convection`: Consecutive calls for grell freitas convection
    * `real(kind=kind_phys)`: units = 1
* `graupel_precipitation_rate_on_previous_timestep`: Graupel precipitation rate on previous timestep
    * `real(kind=kind_phys)`: units = mm s-1
* `ground_temperature`: Ground temperature
    * `real(kind=kind_phys)`: units = K
* `ice_precipitation_rate_on_previous_timestep`: Ice precipitation rate on previous timestep
    * `real(kind=kind_phys)`: units = mm s-1
* `control_for_diurnal_thermocline_calculation`: Control for diurnal thermocline calculation
    * `real(kind=kind_phys)`: units = 1
* `temperature_in_ice_layer`: Temperature in ice layer
    * `real(kind=kind_phys)`: units = K
* `upward_flux_of_water_vapor_mixing_ratio_wrt_moist_air_at_surface`: Upward flux of water vapor mixing ratio wrt moist air at surface
    * `real(kind=kind_phys)`: units = kg kg-1 m s-1
* `upward_temperature_flux_at_surface`: Upward temperature flux at surface
    * `real(kind=kind_phys)`: units = K m s-1
* `lake_area_fraction`: Lake area fraction
    * `real(kind=kind_phys)`: units = fraction
* `lake_depth`: Lake depth
    * `real(kind=kind_phys)`: units = m
* `water_storage_in_lake`: Water storage in lake
    * `real(kind=kind_phys)`: units = mm
* `land_area_fraction`: Land area fraction
    * `real(kind=kind_phys)`: units = fraction
* `depth_from_snow_surface_at_bottom_interface`: Depth from snow surface at bottom interface
    * `real(kind=kind_phys)`: units = m
* `leaf_area_index`: Leaf area index
    * `real(kind=kind_phys)`: units = 1
* `leaf_mass_content`: Leaf mass content
    * `real(kind=kind_phys)`: units = g m-2
* `lwe_thickness_of_convective_precipitation_amount_on_previous_timestep`: Lwe thickness of convective precipitation amount on previous timestep
    * `real(kind=kind_phys)`: units = m
* `lwe_thickness_of_explicit_precipitation_amount_on_previous_timestep`: Lwe thickness of explicit precipitation amount on previous timestep
    * `real(kind=kind_phys)`: units = m
* `lwe_thickness_of_graupel_amount_on_previous_timestep`: Lwe thickness of graupel amount on previous timestep
    * `real(kind=kind_phys)`: units = m
* `lwe_thickness_of_ice_precipitation_amount_on_previous_timestep`: Lwe thickness of ice precipitation amount on previous timestep
    * `real(kind=kind_phys)`: units = m
* `snow_mass_on_previous_timestep`: Snow mass on previous timestep
    * `real(kind=kind_phys)`: units = m
* `max_vegetation_area_fraction`: Max vegetation area fraction
    * `real(kind=kind_phys)`: units = fraction
* `nir_albedo_strong_cosz`: albedo for near-infrared radiation with strong dependence on cosine of the zenith angle
    * `real(kind=kind_phys)`: units = fraction
* `nir_albedo_weak_cosz`: Nir albedo weak cosz
    * `real(kind=kind_phys)`: units = fraction
* `vis_albedo_strong_cosz`: Vis albedo strong cosz
    * `real(kind=kind_phys)`: units = fraction
* `vis_albedo_weak_cosz`: Vis albedo weak cosz
    * `real(kind=kind_phys)`: units = fraction
* `min_vegetation_area_fraction`: Min vegetation area fraction
    * `real(kind=kind_phys)`: units = fraction
* `monin_obukhov_similarity_function_for_heat`: Monin obukhov similarity function for heat
    * `real(kind=kind_phys)`: units = 1
* `monin_obukhov_similarity_function_for_momentum`: Monin obukhov similarity function for momentum
    * `real(kind=kind_phys)`: units = 1
* `dimensionless_age_of_surface_snow`: Dimensionless age of surface snow
    * `real(kind=kind_phys)`: units = 1
* `nonnegative_lwe_thickness_of_precipitation_amount_on_dynamics_timestep`: Nonnegative lwe thickness of precipitation amount on dynamics timestep
    * `real(kind=kind_phys)`: units = m
* `normalized_soil_wetness_for_land_surface_model`: Normalized soil wetness for land surface model
    * `real(kind=kind_phys)`: units = fraction
* `number_of_snow_layers`: Number of snow layers
    * `real(kind=kind_phys)`: units = 1
* `ocean_mixed_layer_thickness`: Ocean mixed layer thickness
    * `real(kind=kind_phys)`: units = m
* `height_above_mean_sea_level`: Height above mean sea level
    * `real(kind=kind_phys)`: units = m
* `height_above_mean_sea_level_at_surface`: Height above mean sea level at local surface
    * `real(kind=kind_phys)`: units = m
* `unfiltered_height_above_mean_sea_level`: Unfiltered height above mean sea level
    * `real(kind=kind_phys)`: units = m
* `air_potential_temperature_at_2m`: Air potential temperature at 2m
    * `real(kind=kind_phys)`: units = K
* `ratio_of_wind_at_surface_adjacent_layer_to_wind_at_10m`: Ratio of wind at surface adjacent layer to wind at 10m
    * `real(kind=kind_phys)`: units = ratio
* `reciprocal_of_obukhov_length`: Reciprocal of obukhov length
    * `real(kind=kind_phys)`: units = m-1
* `sea_area_fraction`: Sea area fraction
    * `real(kind=kind_phys)`: units = fraction
* `sea_ice_area_fraction_of_sea_area_fraction`: Sea ice area fraction of sea area fraction
    * `real(kind=kind_phys)`: units = fraction
* `sea_ice_temperature`: Sea ice temperature
    * `real(kind=kind_phys)`: units = K
* `sea_ice_thickness`: Sea ice thickness
    * `real(kind=kind_phys)`: units = m
* `area_type`: Area type
    * `real(kind=kind_phys)`: units = 1
* `reference_sea_surface_temperature`: Reference sea surface temperature
    * `real(kind=kind_phys)`: units = K
* `sea_surface_temperature`: Sea surface temperature
    * `real(kind=kind_phys)`: units = K
* `sea_water_salinity_in_diurnal_thermocline`: Sea water salinity in diurnal thermocline
    * `real(kind=kind_phys)`: units = ppt m
* `surface_sensible_heat_due_to_rainfall`: Surface sensible heat due to rainfall
    * `real(kind=kind_phys)`: units = W
* `derivative_of_heat_content_in_diurnal_thermocline_wrt_surface_skin_temperature`: Derivative of heat content in diurnal thermocline wrt surface skin temperature
    * `real(kind=kind_phys)`: units = m
* `derivative_of_diurnal_thermocline_layer_thickness_wrt_surface_skin_temperature`: Derivative of diurnal thermocline layer thickness wrt surface skin temperature
    * `real(kind=kind_phys)`: units = m K-1
* `slow_soil_pool_mass_content_of_carbon`: Slow soil pool mass content of carbon
    * `real(kind=kind_phys)`: units = g m-2
* `albedo_on_previous_timestep_assuming_deep_snow`: Albedo on previous timestep assuming deep snow
    * `real(kind=kind_phys)`: units = fraction
* `lwe_thickness_of_ice_in_surface_snow`: Lwe thickness of ice in surface snow
    * `real(kind=kind_phys)`: units = mm
* `lwe_thickness_of_liquid_water_in_surface_snow`: Lwe thickness of liquid water in surface snow
    * `real(kind=kind_phys)`: units = mm
* `lwe_thickness_of_snowfall_amount_on_previous_timestep`: Lwe thickness of snowfall amount on previous timestep
    * `real(kind=kind_phys)`: units = mm
* `lwe_snowfall_rate`: Lwe snowfall rate
    * `real(kind=kind_phys)`: units = mm s-1
* `snowfall_rate_on_previous_timestep`: Snowfall rate on previous timestep
    * `real(kind=kind_phys)`: units = mm s-1
* `temperature_in_surface_snow`: Temperature in surface snow
    * `real(kind=kind_phys)`: units = K
* `temperature_in_surface_snow_at_surface_adjacent_layer_over_ice`: Temperature in surface snow at surface adjacent layer over ice
    * `real(kind=kind_phys)`: units = K
* `temperature_in_surface_snow_at_surface_adjacent_layer_over_land`: Temperature in surface snow at surface adjacent layer over land
    * `real(kind=kind_phys)`: units = K
* `soil_temperature`: Soil temperature
    * `real(kind=kind_phys)`: units = K
* `soil_temperature_for_land_surface_model`: Soil temperature for land surface model
    * `real(kind=kind_phys)`: units = K
* `volumetric_soil_moisture_between_soil_bottom_and_water_table`: Volumetric soil moisture between soil bottom and water table
    * `real(kind=kind_phys)`: units = m3 m-3
* `water_vapor_mixing_ratio_wrt_moist_air_at_2m`: Specific humidity (water vapor mass mixing ratio with respect to moist air) at two meters above surface
    * `real(kind=kind_phys)`: units = kg kg-1
* `water_vapor_mixing_ratio_wrt_moist_air_and_condensed_water_at_2m`: mixing ratio of the mass of water vapor to the mass of moist air and hydrometeors, at two meters above surface
    * `real(kind=kind_phys)`: units = kg kg-1
* `specified_upward_flux_of_water_vapor_mixing_ratio_wrt_moist_air_at_surface`: Specified upward specific humidity (water vapor mass mixing ratio with respect to moist air) flux at surface
    * `real(kind=kind_phys)`: units = kg kg-1 m s-1
* `specified_upward_temperature_flux_at_surface`: Specified upward temperature flux at surface
    * `real(kind=kind_phys)`: units = K m s-1
* `standard_deviation_of_subgrid_orography`: Standard deviation of subgrid orography
    * `real(kind=kind_phys)`: units = m
* `statistical_measures_of_subgrid_orography_collection_array`: Statistical measures of subgrid orography collection array
    * `real(kind=kind_phys)`: units = various
* `stem_area_index`: Stem area index
    * `real(kind=kind_phys)`: units = 1
* `stem_mass_content`: Stem mass content
    * `real(kind=kind_phys)`: units = g m-2
* `molecular_sublayer_temperature_correction_in_sea_water`: Molecular sublayer temperature correction in sea water
    * `real(kind=kind_phys)`: units = K
* `molecular_sublayer_thickness_in_sea_water`: Molecular sublayer thickness in sea water
    * `real(kind=kind_phys)`: units = m
* `diffuse_nir_albedo_of_ice`: ice surface albedo for diffuse near-infrared radiation
    * `real(kind=kind_phys)`: units = fraction
* `diffuse_nir_albedo_of_land`: land surface albedo for diffuse near-infrared radiation
    * `real(kind=kind_phys)`: units = fraction
* `diffuse_vis_albedo_of_ice`: ice surface albedo for diffuse visible radiation
    * `real(kind=kind_phys)`: units = fraction
* `diffuse_vis_albedo_of_land`: land surface albedo for diffuse visible radiation
    * `real(kind=kind_phys)`: units = fraction
* `direct_nir_albedo_of_ice`: ice surface albedo for direct near-infrared radiation
    * `real(kind=kind_phys)`: units = fraction
* `direct_nir_albedo_of_land`: land surface albedo for direct near-infrared radiation
    * `real(kind=kind_phys)`: units = fraction
* `direct_vis_albedo_of_ice`: ice surface albedo for direct visible radiation
    * `real(kind=kind_phys)`: units = fraction
* `direct_vis_albedo_of_land`: land surface albedo for direct visible radiation
    * `real(kind=kind_phys)`: units = fraction
* `diffuse_shortwave_albedo_of_ice`: ice surface albedo for diffuse shortwave radiation
    * `real(kind=kind_phys)`: units = fraction
* `diffuse_shortwave_albedo_of_land`: land surface albedo for diffuse shortwave radiation
    * `real(kind=kind_phys)`: units = fraction
* `surface_drag_coefficient_for_heat_and_moisture_for_noahmp`: Surface drag coefficient for heat and moisture for noahmp
    * `real(kind=kind_phys)`: units = 1
* `surface_drag_coefficient_for_momentum_for_noahmp`: Surface drag coefficient for momentum for noahmp
    * `real(kind=kind_phys)`: units = 1
* `surface_exchange_coefficient_for_heat`: Surface exchange coefficient for heat
    * `real(kind=kind_phys)`: units = W m-2 K-1
* `surface_exchange_coefficient_for_heat_at_2m`: Surface exchange coefficient for heat at 2m
    * `real(kind=kind_phys)`: units = m s-1
* `surface_exchange_coefficient_for_moisture`: Surface exchange coefficient for moisture
    * `real(kind=kind_phys)`: units = kg m-2 s-1
* `surface_exchange_coefficient_for_moisture_at_2m`: Surface exchange coefficient for moisture at 2m
    * `real(kind=kind_phys)`: units = m s-1
* `surface_friction_velocity`: Surface friction velocity
    * `real(kind=kind_phys)`: units = m s-1
* `surface_friction_velocity_for_momentum`: Surface friction velocity for momentum
    * `real(kind=kind_phys)`: units = m s-1
* `upward_latent_heat_flux_at_surface`: Upward latent heat flux at surface
    * `real(kind=kind_phys)`: units = W m-2
* `surface_longwave_emissivity_over_ice`: Surface longwave emissivity over ice
    * `real(kind=kind_phys)`: units = fraction
* `surface_longwave_emissivity_over_land`: Surface longwave emissivity over land
    * `real(kind=kind_phys)`: units = fraction
* `roughness_length`: surface roughness length
    * `real(kind=kind_phys)`: units = cm
* `roughness_length_from_wave_model`: surface roughness length from wave model
    * `real(kind=kind_phys)`: units = cm
* `roughness_length_over_ice`: surface roughness length over ice
    * `real(kind=kind_phys)`: units = cm
* `roughness_length_over_land`: surface roughness length over land
    * `real(kind=kind_phys)`: units = cm
* `roughness_length_over_water`: surface roughness length over water
    * `real(kind=kind_phys)`: units = cm
* `surface_skin_temperature`: Surface skin temperature
    * `real(kind=kind_phys)`: units = K
* `surface_skin_temperature_over_land`: Surface skin temperature over land
    * `real(kind=kind_phys)`: units = K
* `snow_area_fraction_at_surface_over_ice`: Snow area fraction at surface over ice
    * `real(kind=kind_phys)`: units = fraction
* `snow_area_fraction_at_surface_over_land`: Snow area fraction at surface over land
    * `real(kind=kind_phys)`: units = fraction
* `albedo_of_land_assuming_no_snow_cover`: surface snow-free albedo over land
    * `real(kind=kind_phys)`: units = fraction
* `lwe_surface_snow`: Lwe surface snow
    * `real(kind=kind_phys)`: units = mm
* `water_vapor_mixing_ratio_wrt_moist_air_at_surface`: Specific humidity (water vapor mass mixing ratio with respect to moist air) at surface
    * `real(kind=kind_phys)`: units = kg kg-1
* `ratio_of_height_to_monin_obukhov_length`: Ratio of height to monin obukhov length
    * `real(kind=kind_phys)`: units = 1
* `air_temperature_at_2m`: Air temperature at 2m
    * `real(kind=kind_phys)`: units = K
* `surface_temperature_scale`: Surface temperature scale
    * `real(kind=kind_phys)`: units = K
* `time_since_last_snowfall`: Time since last snowfall
    * `real(kind=kind_phys)`: units = s
* `surface_snow_amount_over_ice`: Surface snow amount over ice
    * `real(kind=kind_phys)`: units = kg m-2
* `surface_snow_amount_over_land`: Surface snow amount over land
    * `real(kind=kind_phys)`: units = kg m-2
* `upper_bound_of_max_albedo_assuming_deep_snow`: Upper bound of max albedo assuming deep snow
    * `real(kind=kind_phys)`: units = fraction
* `vegetation_area_fraction`: Vegetation area fraction
    * `real(kind=kind_phys)`: units = fraction
* `canopy_temperature`: Canopy temperature
    * `real(kind=kind_phys)`: units = K
* `volume_fraction_of_frozen_soil_moisture_for_land_surface_model`: Volume fraction of frozen soil moisture for land surface model
    * `real(kind=kind_phys)`: units = fraction
* `volume_fraction_of_condensed_water_in_soil`: Volume fraction of condensed water in soil
    * `real(kind=kind_phys)`: units = fraction
* `volume_fraction_of_soil_moisture_for_land_surface_model`: Volume fraction of soil moisture for land surface model
    * `real(kind=kind_phys)`: units = fraction
* `volume_fraction_of_unfrozen_water_in_soil`: Volume fraction of unfrozen water in soil
    * `real(kind=kind_phys)`: units = fraction
* `volume_fraction_of_unfrozen_soil_moisture_for_land_surface_model`: Volume fraction of unfrozen soil moisture for land surface model
    * `real(kind=kind_phys)`: units = fraction
* `lwe_thickness_of_surface_snow_amount`: Lwe thickness of surface snow amount
    * `real(kind=kind_phys)`: units = mm
* `water_storage_in_aquifer`: Water storage in aquifer
    * `real(kind=kind_phys)`: units = mm
* `water_storage_in_aquifer_and_saturated_soil`: Water storage in aquifer and saturated soil
    * `real(kind=kind_phys)`: units = mm
* `water_table_depth`: Water table depth
    * `real(kind=kind_phys)`: units = m
* `water_table_recharge_assuming_deep`: Water table recharge assuming deep
    * `real(kind=kind_phys)`: units = m
* `water_table_recharge_assuming_shallow`: Water table recharge assuming shallow
    * `real(kind=kind_phys)`: units = m
* `water_vapor_mixing_ratio_wrt_moist_air_at_surface_over_ice`: Specific humidity (water vapor mass mixing ratio with respect to moist air) at surface over ice
    * `real(kind=kind_phys)`: units = kg kg-1
* `water_vapor_mixing_ratio_wrt_moist_air_at_surface_over_land`: Specific humidity (water vapor mass mixing ratio with respect to moist air) at surface over land
    * `real(kind=kind_phys)`: units = kg kg-1
* `wood_mass_content`: Wood mass content
    * `real(kind=kind_phys)`: units = g m-2
## GFS_typedefs_GFS_coupling_type
* `cellular_automata_global_pattern_from_coupled_process`: Cellular automata global pattern from coupled process
    * `real(kind=kind_phys)`: units = 1
* `convective_cloud_condensate_after_rainout`: Convective cloud condensate after rainout
    * `real(kind=kind_phys)`: units = kg kg-1
* `cumulative_downwelling_diffuse_nir_shortwave_flux_at_surface_for_coupling_multiplied_by_timestep`: cumulative downwelling diffuse near-infrared shortwave flux at the surface level for coupling multiplied by the duration of the timestep
    * `real(kind=kind_phys)`: units = J m-2
* `cumulative_downwelling_diffuse_uv_and_vis_shortwave_flux_at_surface_for_coupling_multiplied_by_timestep`: cumulative downwelling diffuse ultraviolet and visible shortwave flux at the surface level for coupling multiplied by the duration of the timestep
    * `real(kind=kind_phys)`: units = J m-2
* `cumulative_downwelling_direct_nir_shortwave_flux_at_surface_for_coupling_multiplied_by_timestep`: cumulative downwelling direct near-infrared shortwave flux at the surface level for coupling multiplied by the duration of the timestep
    * `real(kind=kind_phys)`: units = J m-2
* `cumulative_downwelling_direct_uv_and_vis_shortwave_flux_at_surface_for_coupling_multiplied_by_timestep`: cumulative downwelling direct ultraviolet and visible shortwave flux at the surface level for coupling multiplied by the duration of the timestep
    * `real(kind=kind_phys)`: units = J m-2
* `cumulative_downwelling_longwave_flux_at_surface_for_coupling_multiplied_by_timestep`: Cumulative downwelling longwave flux at surface for coupling multiplied by timestep
    * `real(kind=kind_phys)`: units = J m-2
* `cumulative_downwelling_shortwave_flux_at_surface_for_coupling_multiplied_by_timestep`: Cumulative downwelling shortwave flux at surface for coupling multiplied by timestep
    * `real(kind=kind_phys)`: units = J m-2
* `cumulative_net_downwelling_diffuse_nir_shortwave_flux_at_surface_for_coupling_multiplied_by_timestep`: cumulative net downwelling diffuse near-infrared shortwave flux at the surface level for coupling multiplied by the duration of the timestep
    * `real(kind=kind_phys)`: units = J m-2
* `cumulative_net_downwelling_diffuse_uv_and_vis_shortwave_flux_at_surface_for_coupling_multiplied_by_timestep`: cumulative net downwelling diffuse ultraviolet and visible shortwave flux at the surface level for coupling multiplied by the duration of the timestep
    * `real(kind=kind_phys)`: units = J m-2
* `cumulative_net_downwelling_direct_nir_shortwave_flux_at_surface_for_coupling_multiplied_by_timestep`: cumulative net downwelling direct near-infrared shortwave flux at the surface level for coupling multiplied by the duration of the timestep
    * `real(kind=kind_phys)`: units = J m-2
* `cumulative_net_downwelling_direct_uv_and_vis_shortwave_flux_at_surface_for_coupling_multiplied_by_timestep`: cumulative net downwelling direct ultraviolet and visible shortwave flux at the surface level for coupling multiplied by the duration of the timestep
    * `real(kind=kind_phys)`: units = J m-2
* `cumulative_net_downwelling_longwave_flux_at_surface_for_coupling_multiplied_by_timestep`: Cumulative net downwelling longwave flux at surface for coupling multiplied by timestep
    * `real(kind=kind_phys)`: units = J m-2
* `cumulative_net_downwelling_shortwave_flux_at_surface_for_coupling_multiplied_by_timestep`: Cumulative net downwelling shortwave flux at surface for coupling multiplied by timestep
    * `real(kind=kind_phys)`: units = J m-2
* `cumulative_upward_latent_heat_flux_at_surface_for_coupling_multiplied_by_timestep`: Cumulative upward latent heat flux at surface for coupling multiplied by timestep
    * `real(kind=kind_phys)`: units = J m-2
* `cumulative_upward_sensible_heat_flux_at_surface_for_coupling_multiplied_by_timestep`: Cumulative upward sensible heat flux at surface for coupling multiplied by timestep
    * `real(kind=kind_phys)`: units = J m-2
* `cumulative_x_momentum_flux_at_surface_for_coupling_multiplied_by_timestep`: Cumulative x momentum flux at surface for coupling multiplied by timestep
    * `real(kind=kind_phys)`: units = Pa s
* `cumulative_y_momentum_flux_at_surface_for_coupling_multiplied_by_timestep`: Cumulative y momentum flux at surface for coupling multiplied by timestep
    * `real(kind=kind_phys)`: units = Pa s
* `cellular_automata_area_fraction_for_deep_convection_from_coupled_process`: Cellular automata area fraction for deep convection from coupled process
    * `real(kind=kind_phys)`: units = fraction
* `atmosphere_heat_diffusivity_for_chemistry_coupling`: Atmosphere heat diffusivity for chemistry coupling
    * `real(kind=kind_phys)`: units = m2 s-1
* `water_vapor_mixing_ratio_wrt_moist_air_at_2m_for_coupling`: Specific humidity (water vapor mass mixing ratio with respect to moist air) at 2 meters above surface used for coupling
    * `real(kind=kind_phys)`: units = kg kg-1
* `air_pressure_at_surface_for_coupling`: Air pressure at surface for coupling
    * `real(kind=kind_phys)`: units = Pa
* `downwelling_diffuse_nir_shortwave_flux_at_surface_for_coupling`: downwelling diffuse near-infrared shortwave flux at the surface level for coupling
    * `real(kind=kind_phys)`: units = W m-2
* `downwelling_diffuse_uv_and_vis_shortwave_flux_at_surface_for_coupling`: downwelling diffuse ultraviolet and visible shortwave flux at the surface level for coupling
    * `real(kind=kind_phys)`: units = W m-2
* `downwelling_direct_nir_shortwave_flux_at_surface_for_coupling`: downwelling direct near-infrared shortwave flux at the surface level for coupling
    * `real(kind=kind_phys)`: units = W m-2
* `downwelling_direct_uv_and_vis_shortwave_flux_at_surface_for_coupling`: downwelling direct ultraviolet and visible shortwave flux at the surface level for coupling
    * `real(kind=kind_phys)`: units = W m-2
* `downwelling_longwave_flux_at_surface_for_coupling`: Downwelling longwave flux at surface for coupling
    * `real(kind=kind_phys)`: units = W m-2
* `downwelling_shortwave_flux_at_surface_for_coupling`: Downwelling shortwave flux at surface for coupling
    * `real(kind=kind_phys)`: units = W m-2
* `net_downwelling_diffuse_nir_shortwave_flux_at_surface_for_coupling`: net downwelling diffuse near-infrared shortwave flux at the surface level for coupling
    * `real(kind=kind_phys)`: units = W m-2
* `net_downwelling_diffuse_uv_and_vis_shortwave_flux_at_surface_for_coupling`: net downwelling diffuse ultraviolet and visible shortwave flux at the surface level for coupling
    * `real(kind=kind_phys)`: units = W m-2
* `net_downwelling_direct_nir_shortwave_flux_at_surface_for_coupling`: net downwelling direct near-infrared shortwave flux at the surface level for coupling
    * `real(kind=kind_phys)`: units = W m-2
* `net_downwelling_direct_uv_and_vis_shortwave_flux_at_surface_for_coupling`: downwelling direct ultraviolet and visible shortwave flux at the surface level for coupling
    * `real(kind=kind_phys)`: units = W m-2
* `net_downwelling_longwave_flux_at_surface_for_coupling`: Net downwelling longwave flux at surface for coupling
    * `real(kind=kind_phys)`: units = W m-2
* `net_downwelling_shortwave_flux_at_surface_for_coupling`: Net downwelling shortwave flux at surface for coupling
    * `real(kind=kind_phys)`: units = W m-2
* `surface_skin_temperature_for_coupling`: Surface skin temperature for coupling
    * `real(kind=kind_phys)`: units = K
* `upward_latent_heat_flux_at_surface_for_coupling`: Upward latent heat flux at surface for coupling
    * `real(kind=kind_phys)`: units = W m-2
* `upward_sensible_heat_flux_at_surface_for_chemistry_coupling`: Upward sensible heat flux at surface for chemistry coupling
    * `real(kind=kind_phys)`: units = W m-2
* `upward_sensible_heat_flux_at_surface_for_coupling`: Upward sensible heat flux at surface for coupling
    * `real(kind=kind_phys)`: units = W m-2
* `x_momentum_flux_at_surface_for_coupling`: X momentum flux at surface for coupling
    * `real(kind=kind_phys)`: units = Pa
* `y_momentum_flux_at_surface_for_coupling`: Y momentum flux at surface for coupling
    * `real(kind=kind_phys)`: units = Pa
* `temperature_at_2m_for_coupling`: Temperature at 2m for coupling
    * `real(kind=kind_phys)`: units = K
* `tendency_of_water_vapor_mixing_ratio_wrt_moist_air_due_to_moist_convection_for_coupling`: Tendency of water vapor mixing ratio wrt moist air due to moist convection for coupling
    * `real(kind=kind_phys)`: units = kg kg-1 s-1
* `x_wind_at_10m_for_coupling`: X wind at 10m for coupling
    * `real(kind=kind_phys)`: units = m s-1
* `y_wind_at_10m_for_coupling`: Y wind at 10m for coupling
    * `real(kind=kind_phys)`: units = m s-1
* `cumulative_lwe_thickness_of_convective_precipitation_amount_for_coupling`: Cumulative lwe thickness of convective precipitation amount for coupling
    * `real(kind=kind_phys)`: units = m
* `cumulative_lwe_thickness_of_precipitation_amount_for_coupling`: Cumulative lwe thickness of precipitation amount for coupling
    * `real(kind=kind_phys)`: units = m
* `cumulative_lwe_thickness_of_snow_amount_for_coupling`: Cumulative lwe thickness of snow amount for coupling
    * `real(kind=kind_phys)`: units = m
* `physics_field_for_coupling`: Physics field for coupling
    * `real(kind=kind_phys)`: units = m2 s-2
* `rrtmgp_jacobian_of_lw_flux_upward`: Rrtmgp jacobian of lw flux upward
    * `real(kind=kind_phys)`: units = W m-2 K-1
* `rrtmgp_lw_flux_profile_downward_allsky`: Rrtmgp lw flux profile downward allsky
    * `real(kind=kind_phys)`: units = W m-2
* `rrtmgp_lw_flux_profile_upward_allsky`: Rrtmgp lw flux profile upward allsky
    * `real(kind=kind_phys)`: units = W m-2
* `area_type_from_coupled_process`: Area type from coupled process
    * `real(kind=kind_phys)`: units = 1
* `downwelling_diffuse_nir_shortwave_flux_at_surface_on_radiation_timestep`: downwelling diffuse near-infrared shortwave flux at the surface level on the radiation timestep
    * `real(kind=kind_phys)`: units = W m-2
* `downwelling_diffuse_uv_and_vis_shortwave_flux_at_surface_on_radiation_timestep`: downwelling diffuse ultraviolet and visible shortwave flux at the surface level on the radiation timestep
    * `real(kind=kind_phys)`: units = W m-2
* `downwelling_direct_nir_shortwave_flux_at_surface_on_radiation_timestep`: downwelling direct near-infrared shortwave flux at the surface level on the radiation timestep
    * `real(kind=kind_phys)`: units = W m-2
* `downwelling_direct_uv_and_vis_shortwave_flux_at_surface_on_radiation_timestep`: downwelling direct ultraviolet and visible shortwave flux at the surface level on the radiation timestep
    * `real(kind=kind_phys)`: units = W m-2
* `downwelling_longwave_flux_at_surface_on_radiation_timestep`: Downwelling longwave flux at surface on radiation timestep
    * `real(kind=kind_phys)`: units = W m-2
* `downwelling_shortwave_flux_at_surface_on_radiation_timestep`: Downwelling shortwave flux at surface on radiation timestep
    * `real(kind=kind_phys)`: units = W m-2
* `net_downwelling_shortwave_flux_at_surface_on_radiation_timestep`: Net downwelling shortwave flux at surface on radiation timestep
    * `real(kind=kind_phys)`: units = W m-2
* `diffuse_nir_albedo_for_coupling`: surface albedo for diffuse near-infrared radiation for coupling
    * `real(kind=kind_phys)`: units = fraction
* `direct_nir_albedo_for_coupling`: surface albedo for direct near-infrared radiation for coupling
    * `real(kind=kind_phys)`: units = fraction
* `lwe_surface_snow_from_coupled_process`: Lwe surface snow from coupled process
    * `real(kind=kind_phys)`: units = m
* `upward_latent_heat_flux_at_surface_from_coupled_process`: Upward latent heat flux at surface from coupled process
    * `real(kind=kind_phys)`: units = W m-2
* `upward_sensible_heat_flux_at_surface_from_coupled_process`: Upward sensible heat flux at surface from coupled process
    * `real(kind=kind_phys)`: units = W m-2
* `upwelling_diffuse_nir_shortwave_flux_at_surface_on_radiation_timestep`: upwelling diffuse near-infrared shortwave flux at the surface level on the radiation timestep
    * `real(kind=kind_phys)`: units = W m-2
* `upwelling_diffuse_uv_and_vis_shortwave_flux_at_surface_on_radiation_timestep`: upwelling diffuse ultraviolet and visible shortwave flux at the surface level on the radiation timestep
    * `real(kind=kind_phys)`: units = W m-2
* `upwelling_direct_nir_shortwave_flux_at_surface_on_radiation_timestep`: upwelling direct near-infrared shortwave flux at the surface level on the radiation timestep
    * `real(kind=kind_phys)`: units = W m-2
* `upwelling_direct_uv_and_vis_shortwave_flux_at_surface_on_radiation_timestep`: upwelling direct ultraviolet and visible shortwave flux at the surface level on the radiation timestep
    * `real(kind=kind_phys)`: units = W m-2
* `upwelling_longwave_flux_at_surface_from_coupled_process`: Upwelling longwave flux at surface from coupled process
    * `real(kind=kind_phys)`: units = W m-2
* `upwelling_longwave_flux_at_surface_on_radiation_timestep`: Upwelling longwave flux at surface on radiation timestep
    * `real(kind=kind_phys)`: units = W m-2
* `diffuse_vis_albedo_for_coupling`: surface albedo for diffuse visible radiation for coupling
    * `real(kind=kind_phys)`: units = fraction
* `direct_vis_albedo_for_coupling`: surface albedo for direct visible radiation for coupling
    * `real(kind=kind_phys)`: units = fraction
* `x_momentum_flux_at_surface_from_coupled_process`: X momentum flux at surface from coupled process
    * `real(kind=kind_phys)`: units = Pa
* `y_momentum_flux_at_surface_from_coupled_process`: Y momentum flux at surface from coupled process
    * `real(kind=kind_phys)`: units = Pa
* `tendency_of_nonhygroscopic_ice_nucleating_aerosols_at_surface_adjacent_layer`: Tendency of nonhygroscopic ice nucleating aerosols at surface adjacent layer
    * `real(kind=kind_phys)`: units = kg-1 s-1
* `tendency_of_hygroscopic_aerosols_at_surface_adjacent_layer`: Tendency of hygroscopic aerosols at surface adjacent layer
    * `real(kind=kind_phys)`: units = kg-1 s-1
* `updated_tendency_of_air_temperature_due_to_longwave_heating_on_physics_timestep`: Updated tendency of air temperature due to longwave heating on physics timestep
    * `real(kind=kind_phys)`: units = K s-1
* `cellular_automata_vertical_weight`: Cellular automata vertical weight
    * `real(kind=kind_phys)`: units = fraction
* `shum_weights_from_coupled_process`: Shum weights from coupled process
    * `real(kind=kind_phys)`: units = 1
* `skeb_x_wind_weights_from_coupled_process`: Skeb x wind weights from coupled process
    * `real(kind=kind_phys)`: units = 1
* `skeb_y_wind_weights_from_coupled_process`: Skeb y wind weights from coupled process
    * `real(kind=kind_phys)`: units = 1
* `sppt_weights_from_coupled_process`: Sppt weights from coupled process
    * `real(kind=kind_phys)`: units = 1
* `surface_stochastic_weights_from_coupled_process`: Surface stochastic weights from coupled process
    * `real(kind=kind_phys)`: units = 1
## GFS_typedefs_GFS_statein_type
* `air_pressure_at_lowest_model_interface`: Air pressure at lowest model interface
    * `real(kind=kind_phys)`: units = Pa
* `air_pressure_at_surface_adjacent_layer`: Air pressure at surface adjacent layer
    * `real(kind=kind_phys)`: units = Pa
* `air_temperature_at_surface_adjacent_layer`: Air temperature at surface adjacent layer
    * `real(kind=kind_phys)`: units = K
* `cloud_liquid_water_mixing_ratio_wrt_moist_air_at_surface_adjacent_layer`: Cloud liquid water mass mixing ratio with respect to moist air at surface-adjacent layer
    * `real(kind=kind_phys)`: units = kg kg-1
* `mass_number_concentration_of_cloud_liquid_water_particles_in_air`: Mass number concentration of cloud liquid water particles in air
    * `real(kind=kind_phys)`: units = kg-1
* `exner_function_wrt_surface_pressure`: exner function w.r.t. surface pressure, (p/ps)^(Rd/cp)
    * `real(kind=kind_phys)`: units = 1
* `exner_function_at_surface_adjacent_layer`: exner function (p/p0)^(Rd/cp), where p0 is 1000 hPa and p is the pressure at the surface adjacent layer
    * `real(kind=kind_phys)`: units = 1
* `exner_function_at_interfaces`: exner function (p/p0)^(Rd/cp), where p0 is 1000 hPa and p is the pressure at vertical layer interfaces
    * `real(kind=kind_phys)`: units = 1
* `dissipation_estimate_of_air_temperature_at_model_layers`: Dissipation estimate of air temperature at model layers
    * `real(kind=kind_phys)`: units = K
* `geopotential`: Geopotential
    * `real(kind=kind_phys)`: units = m2 s-2
* `geopotential_at_interfaces`: Geopotential at interfaces
    * `real(kind=kind_phys)`: units = m2 s-2
* `graupel_mixing_ratio_wrt_moist_air`: Graupel mass mixing ratio with respect to moist air
    * `real(kind=kind_phys)`: units = kg kg-1
* `mass_number_concentration_of_graupel_in_air`: Mass number concentration of graupel in air
    * `real(kind=kind_phys)`: units = kg-1
* `mass_number_concentration_of_nonhygroscopic_ice_nucleating_aerosols`: Mass number concentration of nonhygroscopic ice nucleating aerosols
    * `real(kind=kind_phys)`: units = kg-1
* `mass_number_concentration_of_cloud_ice_water_crystals_in_air`: Mass number concentration of cloud ice water crystals in air
    * `real(kind=kind_phys)`: units = kg-1
* `ozone_mixing_ratio_wrt_moist_air`: Ozone mass mixing ratio with respect to moist air
    * `real(kind=kind_phys)`: units = kg kg-1
* `mass_number_concentration_of_rain_water_in_air`: Mass number concentration of rain water in air
    * `real(kind=kind_phys)`: units = kg-1
* `mass_number_concentration_of_snow_in_air`: Mass number concentration of snow in air
    * `real(kind=kind_phys)`: units = kg-1
* `snow_mixing_ratio_wrt_moist_air`: Snow mass mixing ratio with respect to moist air
    * `real(kind=kind_phys)`: units = kg kg-1
* `tracer_concentration`: Tracer concentration
    * `real(kind=kind_phys)`: units = kg kg-1
* `turbulent_kinetic_energy`: Turbulent kinetic energy
    * `real(kind=kind_phys)`: units = J
* `mass_number_concentration_of_hygroscopic_aerosols`: Mass number concentration of hygroscopic aerosols
    * `real(kind=kind_phys)`: units = kg-1
* `water_vapor_mixing_ratio_wrt_moist_air_at_surface_adjacent_layer`: Specific humidity (water vapor mass mixing ratio with respect to moist air) at surface-adjacent layer
    * `real(kind=kind_phys)`: units = kg kg-1
* `x_wind_at_surface_adjacent_layer`: X wind at surface adjacent layer
    * `real(kind=kind_phys)`: units = m s-1
* `y_wind_at_surface_adjacent_layer`: Y wind at surface adjacent layer
    * `real(kind=kind_phys)`: units = m s-1
## GFS_typedefs_GFS_cldprop_type
* `convective_cloud_area_fraction_between_sw_radiation_calls_from_cnvc90`: Convective cloud area fraction between sw radiation calls from cnvc90
    * `real(kind=kind_phys)`: units = fraction
* `pressure_at_convective_cloud_base_between_sw_radiation_calls_from_cnvc90`: Pressure at convective cloud base between sw radiation calls from cnvc90
    * `real(kind=kind_phys)`: units = Pa
* `pressure_at_convective_cloud_top_between_sw_radiation_calls_from_cnvc90`: Pressure at convective cloud top between sw radiation calls from cnvc90
    * `real(kind=kind_phys)`: units = Pa
## GFS_typedefs_GFS_radtend_type
* `cosine_of_solar_zenith_angle_for_daytime_points_on_radiation_timestep`: Cosine of solar zenith angle for daytime points on radiation timestep
    * `real(kind=kind_phys)`: units = 1
* `cosine_of_solar_zenith_angle_on_radiation_timestep`: Cosine of solar zenith angle on radiation timestep
    * `real(kind=kind_phys)`: units = 1
* `surface_lw_fluxes_assuming_total_and_clear_sky_on_radiation_timestep`: Surface lw fluxes assuming total and clear sky on radiation timestep
    * `sfcflw_type(kind=)`: units = W m-2
* `diffuse_shortwave_albedo_on_radiation_timestep`: surface albedo for diffuse shortwave radiation on the timestep for radiation physics
    * `real(kind=kind_phys)`: units = fraction
* `surface_longwave_emissivity`: Surface longwave emissivity
    * `real(kind=kind_phys)`: units = fraction
* `air_temperature_at_surface_adjacent_layer_on_radiation_timestep`: Air temperature at surface adjacent layer on radiation timestep
    * `real(kind=kind_phys)`: units = K
* `surface_sw_fluxes_assuming_total_and_clear_sky_on_radiation_timestep`: Surface sw fluxes assuming total and clear sky on radiation timestep
    * `sfcfsw_type(kind=)`: units = W m-2
* `tendency_of_air_temperature_due_to_longwave_heating_assuming_clear_sky_on_radiation_timestep`: Tendency of air temperature due to longwave heating assuming clear sky on radiation timestep
    * `real(kind=kind_phys)`: units = K s-1
* `tendency_of_air_temperature_due_to_integrated_dynamics_through_earths_atmosphere`: Tendency of air temperature due to integrated dynamics through earths atmosphere
    * `real(kind=kind_phys)`: units = K s-1
* `tendency_of_air_temperature_due_to_longwave_heating_on_radiation_timestep`: Tendency of air temperature due to longwave heating on radiation timestep
    * `real(kind=kind_phys)`: units = K s-1
* `tendency_of_air_temperature_due_to_shortwave_heating_assuming_clear_sky_on_radiation_timestep`: Tendency of air temperature due to shortwave heating assuming clear sky on radiation timestep
    * `real(kind=kind_phys)`: units = K s-1
* `tendency_of_air_temperature_due_to_shortwave_heating_on_radiation_timestep`: Tendency of air temperature due to shortwave heating on radiation timestep
    * `real(kind=kind_phys)`: units = K s-1
## GFS_typedefs_GFS_grid_type
* `longitude_interpolation_weight_for_aerosol_forcing`: Longitude interpolation weight for aerosol forcing
    * `real(kind=kind_phys)`: units = 1
* `latitude_interpolation_weight_for_aerosol_forcing`: Latitude interpolation weight for aerosol forcing
    * `real(kind=kind_phys)`: units = 1
* `characteristic_grid_lengthscale`: Characteristic grid lengthscale
    * `real(kind=kind_phys)`: units = m
* `longitude_interpolation_weight_for_cloud_nuclei_forcing`: Longitude interpolation weight for cloud nuclei forcing
    * `real(kind=kind_phys)`: units = 1
* `latitude_interpolation_weight_for_cloud_nuclei_forcing`: Latitude interpolation weight for cloud nuclei forcing
    * `real(kind=kind_phys)`: units = 1
* `cosine_of_latitude`: Cosine of latitude
    * `real(kind=kind_phys)`: units = 1
* `latitude_interpolation_weight_complement_for_absolute_momentum_flux_due_to_nonorographic_gravity_wave_drag`: Latitude interpolation weight complement for absolute momentum flux due to nonorographic gravity wave drag
    * `real(kind=kind_phys)`: units = 1
* `latitude_interpolation_weight_for_absolute_momentum_flux_due_to_nonorographic_gravity_wave_drag`: Latitude interpolation weight for absolute momentum flux due to nonorographic gravity wave drag
    * `real(kind=kind_phys)`: units = 1
* `lower_longitude_index_of_aerosol_forcing_for_interpolation`: Lower longitude index of aerosol forcing for interpolation
    * `integer(kind=)`: units = index
* `lower_latitude_index_of_aerosol_forcing_for_interpolation`: Lower latitude index of aerosol forcing for interpolation
    * `integer(kind=)`: units = index
* `lower_longitude_index_of_cloud_nuclei_forcing_for_interpolation`: Lower longitude index of cloud nuclei forcing for interpolation
    * `integer(kind=)`: units = index
* `lower_latitude_index_of_cloud_nuclei_forcing_for_interpolation`: Lower latitude index of cloud nuclei forcing for interpolation
    * `integer(kind=)`: units = index
* `lower_latitude_index_of_absolute_momentum_flux_due_to_nonorographic_gravity_wave_drag_for_interpolation`: Lower latitude index of absolute momentum flux due to nonorographic gravity wave drag for interpolation
    * `integer(kind=)`: units = index
* `lower_latitude_index_of_ozone_forcing_for_interpolation`: Lower latitude index of ozone forcing for interpolation
    * `integer(kind=)`: units = index
* `lower_latitude_index_of_stratospheric_water_vapor_forcing_for_interpolation`: Lower latitude index of stratospheric water vapor forcing for interpolation
    * `integer(kind=)`: units = index
* `latitude_interpolation_weight_for_ozone_forcing`: Latitude interpolation weight for ozone forcing
    * `real(kind=kind_phys)`: units = 1
* `sine_of_latitude`: Sine of latitude
    * `real(kind=kind_phys)`: units = 1
* `upper_longitude_index_of_aerosol_forcing_for_interpolation`: Upper longitude index of aerosol forcing for interpolation
    * `integer(kind=)`: units = index
* `upper_latitude_index_of_aerosol_forcing_for_interpolation`: Upper latitude index of aerosol forcing for interpolation
    * `integer(kind=)`: units = index
* `upper_longitude_index_of_cloud_nuclei_forcing_for_interpolation`: Upper longitude index of cloud nuclei forcing for interpolation
    * `integer(kind=)`: units = index
* `upper_latitude_index_of_cloud_nuclei_forcing_for_interpolation`: Upper latitude index of cloud nuclei forcing for interpolation
    * `integer(kind=)`: units = index
* `upper_latitude_index_of_absolute_momentum_flux_due_to_nonorographic_gravity_wave_drag_for_interpolation`: Upper latitude index of absolute momentum flux due to nonorographic gravity wave drag for interpolation
    * `integer(kind=)`: units = index
* `upper_latitude_index_of_ozone_forcing_for_interpolation`: Upper latitude index of ozone forcing for interpolation
    * `integer(kind=)`: units = index
* `upper_latitude_index_of_stratospheric_water_vapor_forcing_for_interpolation`: Upper latitude index of stratospheric water vapor forcing for interpolation
    * `integer(kind=)`: units = index
* `latitude_interpolation_weight_for_stratospheric_water_vapor_forcing`: Latitude interpolation weight for stratospheric water vapor forcing
    * `real(kind=kind_phys)`: units = 1
## GFS_typedefs_GFS_stateout_type
* `air_temperature_of_new_state_at_surface_adjacent_layer`: Air temperature of new state at surface adjacent layer
    * `real(kind=kind_phys)`: units = K
* `air_temperature_of_new_state`: Air temperature of new state
    * `real(kind=kind_phys)`: units = K
* `cloud_liquid_water_mixing_ratio_wrt_moist_air_of_new_state`: Cloud liquid water mass mixing ratio with respect to moist air of new state
    * `real(kind=kind_phys)`: units = kg kg-1
* `mass_number_concentration_of_cloud_liquid_water_particles_in_air_of_new_state`: Mass number concentration of cloud liquid water particles in air of new state
    * `real(kind=kind_phys)`: units = kg-1
* `nonconvective_cloud_area_fraction_in_atmosphere_layer_of_new_state`: Nonconvective cloud area fraction in atmosphere layer of new state
    * `real(kind=kind_phys)`: units = fraction
* `graupel_mixing_ratio_wrt_moist_air_of_new_state`: Graupel mass mixing ratio with respect to moist air of new state
    * `real(kind=kind_phys)`: units = kg kg-1
* `mass_number_concentration_of_graupel_of_new_state`: Mass number concentration of graupel of new state
    * `real(kind=kind_phys)`: units = kg-1
* `mass_number_concentration_of_nonhygroscopic_ice_nucleating_aerosols_of_new_state`: Mass number concentration of nonhygroscopic ice nucleating aerosols of new state
    * `real(kind=kind_phys)`: units = kg-1
* `mass_number_concentration_of_cloud_ice_water_crystals_in_air_of_new_state`: Mass number concentration of cloud ice water crystals in air of new state
    * `real(kind=kind_phys)`: units = kg-1
* `cloud_ice_mixing_ratio_wrt_moist_air_of_new_state`: Cloud ice mass mixing ratio with respect to moist air of new state
    * `real(kind=kind_phys)`: units = kg kg-1
* `mass_weighted_rime_factor_of_new_state`: Mass weighted rime factor of new state
    * `real(kind=kind_phys)`: units = kg kg-1
* `ozone_concentration_of_new_state`: Ozone concentration of new state
    * `real(kind=kind_phys)`: units = kg kg-1
* `mass_number_concentration_of_rain_of_new_state`: Mass number concentration of rain of new state
    * `real(kind=kind_phys)`: units = kg-1
* `rain_mixing_ratio_wrt_moist_air_of_new_state`: Rain mass mixing ratio with respect to moist air of new state
    * `real(kind=kind_phys)`: units = kg kg-1
* `mass_number_concentration_of_snow_of_new_state`: Mass number concentration of snow of new state
    * `real(kind=kind_phys)`: units = kg-1
* `snow_mixing_ratio_wrt_moist_air_of_new_state`: Snow mass mixing ratio with respect to moist air of new state
    * `real(kind=kind_phys)`: units = kg kg-1
* `tracer_concentration_of_new_state`: Tracer concentration of new state
    * `real(kind=kind_phys)`: units = kg kg-1
* `mass_number_concentration_of_hygroscopic_aerosols_of_new_state`: Mass number concentration of hygroscopic aerosols of new state
    * `real(kind=kind_phys)`: units = kg-1
* `water_vapor_mixing_ratio_wrt_moist_air_of_new_state_at_surface_adjacent_layer`: Specific humidity (water vapor mass mixing ratio with respect to moist air) of new state at surface-adjacent layer
    * `real(kind=kind_phys)`: units = kg kg-1
* `water_vapor_mixing_ratio_wrt_moist_air_of_new_state`: Specific humidity (water vapor mass mixing ratio with respect to moist air) of new state
    * `real(kind=kind_phys)`: units = kg kg-1
* `x_wind_of_new_state_at_surface_adjacent_layer`: X wind of new state at surface adjacent layer
    * `real(kind=kind_phys)`: units = m s-1
* `x_wind_of_new_state`: X wind of new state
    * `real(kind=kind_phys)`: units = m s-1
* `y_wind_of_new_state_at_surface_adjacent_layer`: Y wind of new state at surface adjacent layer
    * `real(kind=kind_phys)`: units = m s-1
* `y_wind_of_new_state`: Y wind of new state
    * `real(kind=kind_phys)`: units = m s-1
