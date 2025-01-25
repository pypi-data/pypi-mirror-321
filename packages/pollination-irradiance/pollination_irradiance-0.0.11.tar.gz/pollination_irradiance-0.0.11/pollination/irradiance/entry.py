from pollination_dsl.dag import Inputs, DAG, task, Outputs
from dataclasses import dataclass
from pollination.honeybee_radiance_postprocess.grid import MergeFolderData

# input/output alias
from pollination.alias.inputs.model import hbjson_model_grid_input
from pollination.alias.inputs.wea import wea_input
from pollination.alias.inputs.north import north_input
from pollination.alias.inputs.radiancepar import rad_par_annual_input
from pollination.alias.inputs.grid import grid_filter_input, \
    min_sensor_count_input, cpu_count
from pollination.alias.inputs.bool_options import visible_vs_solar_input
from pollination.alias.outputs.daylight import average_irradiance_results, \
    peak_irradiance_results, cumulative_radiation_results

from ._prepare_folder import AnnualIrradiancePrepareFolder
from ._raytracing import AnnualIrradianceRayTracing
from ._postprocess import AnnualIrradiancePostprocess


@dataclass
class AnnualIrradianceEntryPoint(DAG):
    """Annual irradiance entry point."""

    # inputs
    timestep = Inputs.int(
        description='Input wea timestep. This value will be used to compute '
        'cumulative radiation results.', default=1,
        spec={'type': 'integer', 'minimum': 1, 'maximum': 60}
    )

    output_type = Inputs.str(
        description='Text for the type of irradiance output, which can be solar '
        'or visible. Note that the output values will still be irradiance (W/m2) '
        'when visible is selected but these irradiance values will be just for '
        'the visible portion of the electromagnetic spectrum. The visible '
        'irradiance values can be converted into illuminance by multiplying them '
        'by the Radiance luminous efficacy factor of 179.', default='solar',
        spec={'type': 'string', 'enum': ['visible', 'solar']},
        alias=visible_vs_solar_input
    )

    north = Inputs.float(
        default=0,
        description='A number between -360 and 360 for the counterclockwise '
        'difference between the North and the positive Y-axis in degrees. This '
        'can also be a Vector for the direction to North. (Default: 0).',
        spec={'type': 'number', 'minimum': -360, 'maximum': 360},
        alias=north_input
    )

    cpu_count = Inputs.int(
        default=50,
        description='The maximum number of CPUs for parallel execution. This will be '
        'used to determine the number of sensors run by each worker.',
        spec={'type': 'integer', 'minimum': 1},
        alias=cpu_count
    )

    min_sensor_count = Inputs.int(
        description='The minimum number of sensors in each sensor grid after '
        'redistributing the sensors based on cpu_count. This value takes '
        'precedence over the cpu_count and can be used to ensure that '
        'the parallelization does not result in generating unnecessarily small '
        'sensor grids. The default value is set to 1, which means that the '
        'cpu_count is always respected.', default=500,
        spec={'type': 'integer', 'minimum': 1},
        alias=min_sensor_count_input
    )

    radiance_parameters = Inputs.str(
        description='Radiance parameters for ray tracing.',
        default='-ab 2 -ad 5000 -lw 2e-05 -dr 0',
        alias=rad_par_annual_input
    )

    grid_filter = Inputs.str(
        description='Text for a grid identifier or a pattern to filter the sensor grids '
        'of the model that are simulated. For instance, first_floor_* will simulate '
        'only the sensor grids that have an identifier that starts with '
        'first_floor_. By default, all grids in the model will be simulated.',
        default='*',
        alias=grid_filter_input
    )

    model = Inputs.file(
        description='A Honeybee Model JSON file (HBJSON) or a Model pkl (HBpkl) file. '
        'This can also be a zipped version of a Radiance folder, in which case this '
        'recipe will simply unzip the file and simulate it as-is.',
        extensions=['json', 'hbjson', 'pkl', 'hbpkl', 'zip'],
        alias=hbjson_model_grid_input
    )

    wea = Inputs.file(
        description='Wea file.', extensions=['wea', 'epw'], alias=wea_input
    )

    @task(template=AnnualIrradiancePrepareFolder)
    def prepare_folder_annual_irradiance(
        self, timestep=timestep, output_type=output_type, north=north,
        cpu_count=cpu_count, min_sensor_count=min_sensor_count,
        grid_filter=grid_filter, model=model, wea=wea
    ):
        return [
            {
                'from': AnnualIrradiancePrepareFolder()._outputs.model_folder,
                'to': 'model'
            },
            {
                'from': AnnualIrradiancePrepareFolder()._outputs.resources,
                'to': 'resources'
            },
            {
                'from': AnnualIrradiancePrepareFolder()._outputs.results,
                'to': 'results'
            },
            {
                'from': AnnualIrradiancePrepareFolder()._outputs.sensor_grids
            }
        ]

    @task(
        template=AnnualIrradianceRayTracing,
        needs=[prepare_folder_annual_irradiance],
        loop=prepare_folder_annual_irradiance._outputs.sensor_grids,
        # create a subfolder for each grid
        sub_folder='initial_results/{{item.full_id}}',
        # sensor_grid sub path
        sub_paths={
            'sensor_grid': '{{item.full_id}}.pts',
            'octree_file_with_suns': 'scene_with_suns.oct',
            'octree_file': 'scene.oct',
            'sensor_grid': 'grid/{{item.full_id}}.pts',
            'sky_dome': 'sky.dome',
            'sky_matrix': 'sky.mtx',
            'sky_matrix_direct': 'sky_direct.mtx',
            'sun_modifiers': 'sunpath.mod',
            'bsdfs': 'bsdf'
            }
    )
    def annual_irradiance_raytracing(
        self,
        radiance_parameters=radiance_parameters,
        octree_file_with_suns=prepare_folder_annual_irradiance._outputs.resources,
        octree_file=prepare_folder_annual_irradiance._outputs.resources,
        grid_name='{{item.full_id}}',
        sensor_grid=prepare_folder_annual_irradiance._outputs.resources,
        sensor_count='{{item.count}}',
        sky_dome=prepare_folder_annual_irradiance._outputs.resources,
        sky_matrix=prepare_folder_annual_irradiance._outputs.resources,
        sky_matrix_direct=prepare_folder_annual_irradiance._outputs.resources,
        sun_modifiers=prepare_folder_annual_irradiance._outputs.resources,
        bsdfs=prepare_folder_annual_irradiance._outputs.model_folder
    ):
        pass

    @task(
        template=MergeFolderData,
        needs=[prepare_folder_annual_irradiance, annual_irradiance_raytracing],
        sub_paths={
            'dist_info': '_redist_info.json'
        }
    )
    def restructure_total_results(
        self, input_folder='initial_results/final/total',
        extension='ill',
        dist_info=prepare_folder_annual_irradiance._outputs.resources
    ):
        return [
            {
                'from': MergeFolderData()._outputs.output_folder,
                'to': 'results/__static_apertures__/default/total'
            }
        ]

    @task(
        template=MergeFolderData,
        needs=[prepare_folder_annual_irradiance, annual_irradiance_raytracing],
        sub_paths={
            'dist_info': '_redist_info.json'
        }
    )
    def restructure_direct_results(
        self, input_folder='initial_results/final/direct',
        extension='ill',
        dist_info=prepare_folder_annual_irradiance._outputs.resources
    ):
        return [
            {
                'from': MergeFolderData()._outputs.output_folder,
                'to': 'results/__static_apertures__/default/direct'
            }
        ]

    @task(
        template=AnnualIrradiancePostprocess,
        needs=[restructure_total_results, restructure_direct_results]
    )
    def postprocess_annual_irradiance(
        self, input_folder='results'
    ):
        return [
            {
                'from': AnnualIrradiancePostprocess()._outputs.metrics,
                'to': 'metrics'
            }
        ]

    results = Outputs.folder(
        source='results', description='Folder with raw result files (.ill) that '
        'contain matrices of irradiance in W/m2 for each time step of the Wea '
        'time period.'
    )

    average_irradiance = Outputs.folder(
        source='metrics/average_irradiance', description='The average irradiance in '
        'W/m2 for each sensor over the Wea time period.',
        alias=average_irradiance_results
    )

    peak_irradiance = Outputs.folder(
        source='metrics/peak_irradiance', description='The highest irradiance value '
        'in W/m2 during the Wea time period. This is suitable for assessing the '
        'worst-case solar load on cooling design days or the highest radiant '
        'temperatures that occupants might experience in over the time period '
        'of the Wea.', alias=peak_irradiance_results
    )

    cumulative_radiation = Outputs.folder(
        source='metrics/cumulative_radiation', description='The cumulative radiation '
        'in kWh/m2 over the Wea time period.', alias=cumulative_radiation_results
    )
