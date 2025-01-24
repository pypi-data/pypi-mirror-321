from cosmicfrog import FrogModel

def main():
    # frog_model = FrogModel(app_key=app_key, model_name="IKEATEST")

    # abc = frog_model.read_sql("SELECT * FROM optimizationproductionsummary WHERE productname LIKE 'fg_%%';")

    # print(abc)

    # EXAMPLE: Init model class
    # Need an app_key and name of the model
    # frog_model = FrogModel(app_key=app_key, model_name="IKEATEST")

    # Get All Model Templates - static
    # abc = FrogModel.all_available_model_templates(app_key=app_key)
    # print(abc)

    # Get All Models - static
    # res = FrogModel.all_models(app_key=app_key)
    # print(res)

    # New Model - static
    # res = FrogModel.create_model(app_key=app_key, name="IKEATEST12322")
    # print('res', res)

    # Edit Model
    # frog_model = FrogModel(app_key=app_key, model_name="IKEATEST12322")
    # res = frog_model.edit_model(new_name="IKEATEST111")
    # print('res', res)

    # Delete Model
    # frog_model = FrogModel(app_key=app_key, model_name="IKEATEST111")
    # res = frog_model.delete_model()
    # print('res', res)

    # Share model
    # frog_model = FrogModel(app_key=app_key, model_name="IKEATEST")
    # res = frog_model.share(target_user="mr-cf-test-main")
    # print('res', res)
    
    # Remove Share access
    # frog_model = FrogModel(app_key=app_key, model_name="IKEATEST")
    # res = frog_model.remove_share_access(target_user="mr-cf-test-main")
    # print('res', res)

    # Clone model
    # frog_model = FrogModel(app_key=app_key, model_name="IKEATEST")
    # res = frog_model.clone("IKEATEST2")
    # print('res', res)

    # archive a model
    # frog_model = FrogModel(app_key=app_key, model_name="IKEATEST2")
    # res = frog_model.archive()
    # print(res)

    # archive restore
    # res = FrogModel.archive_restore(app_key=app_key, model_name="IKEATEST2")
    # print(res)

    # Get all archived models
    # res = FrogModel.archived_models(app_key=app_key)
    # print(res)

    # EXAMPLE: Simple Scenario Run
    # def run_scenario(
    #     scenario_name: str = "Baseline",
    #     wksp: [str] = "Studio",
    #     engine: [ENGINES] = "neo",
    #     resource_size: [RESOURCE_SIZES] = "s",
    #     tags: [str] = "",
    #     version: [str] = "",
    #     fire_and_forget: bool = False,
    #     correlation_id: str = None,
    #     check_configuration_before_run: bool = False
    # )

    # frog_model = FrogModel(app_key=app_key, model_name="IKEATEST")
    # scenarios = frog_model.all_scenarios_preview()
    # print(scenarios)
    # run = frog_model.run_scenario()
    # run = frog_model.run_scenario(['No Detroit DC', 'GF 9 Facilities', 'Throg Example', 'Hopper Example', 'No Flow Constraints', 'GF 10 Facilities']) # Run Baseline

    # run = frog_model.run_scenario(['No Flow Constraints','GF 9 Facilities'], check_configuration_before_run = True)

    # run = frog_model.run_scenario(['All'], check_configuration_before_run = True)
    # run = frog_model.run_scenario(['No Detroit DC'])

    # run = frog_model.run_scenario("No Detroit DC", fire_and_forget=True) # Run specific scenario
    # run = frog_model.run_scenario(["No Detroit DC"], engine="throg") # Run specific scenario with specific engine
    # run = frog_model.run_scenario(resource_size="4xs", fire_and_forget=True) # Run specific scenario with specific engine and resource size
    # print('scenarioRunFinished', run)

    # EXAMPLE Stop a scenario
    # frog_model = FrogModel(app_key=app_key, model_name="IKEATEST")
    # stop = frog_model.stop_scenario(scenario_name="Baseline")
    # stop = frog_model.stop_scenario(job_key="No Detroit DC")
    # print('stop', stop)

    # EXAMPLE Check scenario status
    # frog_model = FrogModel(app_key=app_key, model_name="IKEATEST")
    # status = frog_model.check_scenario_status(scenario_name="Baseline")
    # print('status', status)

    # status = frog_model.check_scenario_status(job_key="2ed63b69-907a-4c96-8efe-b9127041233f")
    # print('status', status)

    # EXAMPLE: check scenario logs
    # frog_model = FrogModel(app_key=app_key, model_name="IKEATEST")
    # logs = frog_model.get_job_logs(job_key="249c404d-2834-4e9c-8f56-f6e154aa2beb")
    # print('logs', logs)

    # EXAMPLE: MRO tables
    # frog_model = FrogModel(app_key=app_key, model_name="IKEATEST")
    # all_parameters = frog_model.get_all_run_parameters()
    # all_parameters = frog_model.get_all_run_parameters(engine="neo") # related to specific engine
    # print('all_parameters', all_parameters)

    # EXAMPLE: Want to update a parameter value before running the scenario
    # frog_model = FrogModel(app_key=app_key, model_name="IKEATEST")
    # update_run_parameter_value = frog_model.update_run_parameter_value("LaneCreationRule", "Transportation Policy Lanes Only")
    # update_run_parameter_value = frog_model.update_run_parameter_value("IKEATEST", "NumberOfReplications", "1")
    # print('update_run_parameter_value', update_run_parameter_value)

    # EXAMPLE: Want to create a new parameter
    # def add_run_parameter(self, model_name: str, model_run_option: ModelRunOption, correlation_id = None) -> dict:
    # abc = frog_model.add_run_parameter( {"option": "bbb", "value": 'ccc'})
    # print('abc', abc)

    # EXAMPLE: Want to delete a parameter
    # def delete_run_parameter(self, model_name: str, parameter_name: str, correlation_id = None) -> dict:
    # res = frog_model.delete_run_parameter("bbb")
    # print('res', res)

    # EXAMPLE: Wait for geocode to finish
    # def geocode_table(
    #     self,
    #     table_name: str,
    #     geoprovider: str = "MapBox",
    #     geoapikey: str = None,
    #     ignore_low_confidence: bool = True,
    #     fire_and_forget: bool = True,
    # )
    # frog_model = FrogModel(app_key=app_key, model_name="IKEATEST")
    # abc = frog_model.geocode_table('facilities', fire_and_forget=False)
    # print('abc', abc)

    # Custom table/column CRUD
    # frog_model = FrogModel(app_key=app_key, model_name="IKEATEST")
    # frog_model = FrogModel(connection_string='postgresql://685ba205-712a-47af-81ad-9264d757f3ce_03415342db99:FByF11RmXw3PKMSH@685ba205-712a-47af-81ad-9264d757f3ce-0d1f55075408.database.optilogic.app:6432/685ba205-712a-47af-81ad-9264d757f3ce-0d1f55075408?sslmode=require&fallback_application_name=optilogic_sqlalchemy')

    # Create custom table
    # cde = frog_model.create_table("aaaaaab")
    # print(cde)

    # all custom tables
    # cde = frog_model.get_all_custom_tables()
    # print(cde)


    # delete custom table
    # cde = frog_model.delete_table("aaaaaab")
    # print(cde)

    # rename custom table
    # cde = frog_model.rename_table("ooooo", "eee")
    # print(cde)

    # create custom column
    # cde = frog_model.create_custom_column('newtable', 'new_column4', 'integer', True, False)
    # print(cde)

    # update custom column
    # def edit_custom_column(self, table_name: str, column_name: str, new_column_name: str = None, data_type: str = None, key_column: bool = None):
    # cde = frog_model.edit_custom_column('newtable', 'new_column4', data_type='text', key_column=False)
    # print(cde)

    # delete custom column
    cde = frog_model.delete_custom_column('newtable', 'new_column4')
    print(cde)


    # all custom columns
    # cde = frog_model.get_all_custom_columns('newtable')
    # print(cde)



if __name__ == "__main__":
    main()