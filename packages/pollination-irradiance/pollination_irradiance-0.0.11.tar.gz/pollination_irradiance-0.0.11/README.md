# Irradiance

Calculate solar irradiance (W/m2) and radiation (kWh/m2) at each time step provided by a wea file.

The fundamental calculation of this recipe is the same as that of
[Annual Daylight Enhanced](https://github.com/pollination/annual-daylight-enhanced)
in that a detailed accounting of direct sun is computed at each time step.
However, the recipe computes broadband solar irradiance in W/m2 instead of
visible illuminance in lux.

The detailed matrices of W/m2 at each time step are stored under `results/total`.
Detailed matrices of just the direct component (W/m2) are output to `results/direct`.
The following values are also recorded for each sensor point under the `metrics` folder:

* `average_irradiance`: The average irradiance in W/m2 over the Wea time period
* `peak_irradiance`: The highest irradiance value in W/m2 during the Wea time period
* `cumulative_radiation`: The cumulative radiation in kWh/m2 over the Wea time period

The `peak_irradiance` value is suitable for assessing the worst-case solar load
on cooling design days or the highest radiant temperatures that occupants might
experience in over the time period of the Wea.
