from django import forms
from pecbyapi.models import HouseBuilder, HouseBasic, HouseSpec


class NewHouseForm(forms.ModelForm):
    class Meta:
        model = HouseBasic
        fields = [
            'name', 
            "ua_value", "winter_ha_value", "summer_ha_value", "total_envelope_area", 
            "total_area", "ldk_area", "oth_area", 
            'region', 'annual_solar_level', 
            ]


class NewHouseDetailForm(forms.ModelForm):
    class Meta:
        model = HouseBasic
        fields = [
            'name', 
            "ua_value", "winter_ha_value", "summer_ha_value", "total_envelope_area", 
            "total_area", "ldk_area", "oth_area", 
            'region', 'annual_solar_level', 
            'heat_storage', 'under_floor_ventilation', 'under_floor_ventilation_area_rate', 'ldk_natural_wind', 'oth_natural_wind',
            ]


class CopyHouseDetailForm(forms.ModelForm):
    class Meta:
        model = HouseBasic
        fields = [
            'name', 
            "ua_value", "winter_ha_value", "summer_ha_value", "total_envelope_area", 
            "total_area", "ldk_area", "oth_area", 
            'region', 'annual_solar_level', 
            'heat_storage', 'under_floor_ventilation', 'under_floor_ventilation_area_rate', 'ldk_natural_wind', 'oth_natural_wind',
            ]

class UpdateHouseForm(forms.ModelForm):
    class Meta:
        model = HouseBasic
        fields = [
            'name', 
            "ua_value", "winter_ha_value", "summer_ha_value", "total_envelope_area", 
            "total_area", "ldk_area", "oth_area", 
            'region', 'annual_solar_level', 
            ]

class UpdateHouseDetailForm(forms.ModelForm):
    class Meta:
        model = HouseBasic
        fields = [
            'name', 
            "ua_value", "winter_ha_value", "summer_ha_value", "total_envelope_area", 
            "total_area", "ldk_area", "oth_area", 
            'region', 'annual_solar_level', 
            'heat_storage', 'under_floor_ventilation', 'under_floor_ventilation_area_rate', 'ldk_natural_wind', 'oth_natural_wind',
            ]




class NewSpecForm(forms.ModelForm):
    class Meta:
        model = HouseSpec
        fields = [
            #暖房方式
            'heating_system', 'ldk_heating_type', 'oth_heating_type', 
            'ldk_ac_heating_efficiency', 'ldk_ac_heating_compressor', 
            'ldk_ff_saving_input', 'ldk_ff_heating_efficiency', 
            'ldk_hotwater_floorheating_area_rate', 'ldk_hotwater_floorheating_upward_heatflow_rate', 
            'ldk_elecric_floorheating_area_rate', 'ldk_elecric_floorheating_upward_heatflow_rate', 
            'ldk_ac_floorheating_area_rate', 'ldk_ac_floorheating_upward_heatflow_rate', 'ldk_ac_floorheating_pipe', 
            'ldk_other_heating_device_name', 
            'oth_ac_heating_efficiency', 'oth_ac_heating_compressor', 
            'oth_ff_saving_input', 'oth_ff_heating_efficiency', 
            'oth_hotwater_floorheating_area_rate', 'oth_hotwater_floorheating_upward_heatflow_rate', 
            'oth_elecric_floorheating_area_rate', 'oth_elecric_floorheating_upward_heatflow_rate', 
            'oth_ac_floorheating_area_rate', 'oth_ac_floorheating_upward_heatflow_rate', 'oth_ac_floorheating_pipe', 
            'oth_other_heating_device_name', 
            'hotwater_heating_system', 'hotwater_heating_source_type', 'hotwater_heating_source_name', 
            'hotwater_heating_source_saving_input', 
            'hotwater_heating_source_efficiency_OilClassic', 'hotwater_heating_source_efficiency_GasClassic', 'hotwater_heating_source_efficiency_GasLatentHeatRecovery', 
            'hotwater_heating_source_pipe', 
            'heating_rated_input', 'heating_rated_power', 'heating_rated_capacity', 'heating_power_correction', 'heating_coefficient', 
            ##冷房方式
            'cooling_system', 'ldk_cooling_type', 'oth_cooling_type', 
            'ldk_cooling_type', 'ldk_ac_cooling_efficiency', 'ldk_ac_cooling_compressor', 
            'oth_cooling_type', 'oth_ac_cooling_efficiency', 'oth_ac_cooling_compressor', 
            'ldk_other_cooling_device_name', 
            'oth_other_cooling_device_name', 
            'cooling_rated_input', 'cooling_rated_power', 'cooling_rated_capacity', 'cooling_power_correction', 'cooling_coefficient', 
            ##換気設備
            'ventilation_type', 
            'ventilation_frequency', 
            'ventilation_saving', 'ventilation_sfp', 
            'ventilation_heatexchanger', 'ventilation_efficiency', 'ventilation_heatexchanger_efficiency', 
            'ventilation_heatexchanger_bal', 'ventilation_heatexchanger_leak', 
            #給湯設備
            'bathroom', 
            'water_heater_type', 'integrated_water_heater_type',
            'gasoil_water_heater_efficiency_type', 
            'gasoil_water_heater_jis_efficiency_GasClassic_Mode', 'gasoil_water_heater_jis_efficiency_GasClassic_Other', 
            'gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Mode', 'gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Other', 
            'gasoil_water_heater_jis_efficiency_OilClassic_Mode', 'gasoil_water_heater_jis_efficiency_OilClassic_Other', 
            'gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Mode', 'gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Other', 
            'heatpump_water_heater_efficiency_type', 'heatpump_water_heater_jis_efficiency_M1SEJISEfficiency', 'heatpump_water_heater_jis_efficiency_Other', 
            'gasoil_heating_water_heater_jis_efficiency_IntegratedGasClassic_Mode', 'gasoil_heating_water_heater_jis_efficiency_IntegratedGasClassic_Other', 
            'gasoil_heating_water_heater_jis_efficiency_IntegratedGasLatentHeatRecovery_Mode', 'gasoil_heating_water_heater_jis_efficiency_IntegratedGasLatentHeatRecovery_Other', 
            'gasoil_heating_water_heater_jis_efficiency_IntegratedOil_Mode', 'gasoil_heating_water_heater_jis_efficiency_IntegratedOil_Other', 
            'water_heater_name', 
            'water_heater_heatpump_unit_input', 'water_heater_heatpump_unit', 'water_heater_heatpump_unit_coolant', 'water_heater_tank_unit', 'water_heater_backup_boiler', 'water_heater_tank_place', 'water_heater_tank_capacity', 
            'solar_water_heater_type', 'solar_water_heater_area_type', 'solar_water_heater_area', 'solar_water_heater_direction', 'solar_water_heater_angle', 'solar_water_heater_tank_capacity', 
            'bath_function', 'bath_insulation', 'pipe_type', 'pipe_saving', 
            'kitchen_tap_saving', 'bath_shower_tap_saving', 'wash_bowl_tap_saving', 
            ##照明設備
            'ldk_lighting', 'ldk_multi', 'ldk_dimming', 
            'oth_lighting', 'oth_dimming', 
            'nonldk_lighting', 'nonldk_sensor', 
            ##太陽光発電
            'photovoltaic', 'photovoltaic_power_conditioner_efficiency_input', 'photovoltaic_power_conditioner_efficiency', 
            'photovoltaic_panel_1_cell', 'photovoltaic_panel_2_cell', 'photovoltaic_panel_3_cell', 'photovoltaic_panel_4_cell', 
            'photovol_panel_1_capacity', 'photovol_panel_2_capacity', 'photovol_panel_3_capacity', 'photovol_panel_4_capacity', 
            'photovol_panel_1_setup', 'photovol_panel_2_setup', 'photovol_panel_3_setup', 'photovol_panel_4_setup', 
            'photovol_panel_1_direction', 'photovol_panel_2_direction', 'photovol_panel_3_direction', 'photovol_panel_4_direction', 
            'photovol_panel_1_angle', 'photovol_panel_2_angle', 'photovol_panel_3_angle', 'photovol_panel_4_angle', 
            ##コージェネレーション
            'cogene', 'cogene_type', 
            'cogene_PEFC_input', 'cogene_powerunit_PEFC', 'cogene_tankunit_PEFC', 'cogene_backupboiler_PEFC', 
            'cogene_SOFC_input', 'cogene_powerunit_SOFC', 'cogene_tankunit_SOFC', 'cogene_backupboiler_SOFC', 
            'cogene_unit_powerunit_2015', 
        ]

class NewSpecDetailForm(forms.ModelForm):
    class Meta:
        model = HouseSpec
        fields = [
            #暖房方式
            'heating_system', 'ldk_heating_type', 'oth_heating_type', 
            'ldk_ac_heating_efficiency', 'ldk_ac_heating_compressor', 
            'ldk_ff_saving_input', 'ldk_ff_heating_efficiency', 
            'ldk_hotwater_floorheating_area_rate', 'ldk_hotwater_floorheating_upward_heatflow_rate', 
            'ldk_elecric_floorheating_area_rate', 'ldk_elecric_floorheating_upward_heatflow_rate', 
            'ldk_ac_floorheating_area_rate', 'ldk_ac_floorheating_upward_heatflow_rate', 'ldk_ac_floorheating_pipe', 
            'ldk_other_heating_device_name', 
            'oth_ac_heating_efficiency', 'oth_ac_heating_compressor', 
            'oth_ff_saving_input', 'oth_ff_heating_efficiency', 
            'oth_hotwater_floorheating_area_rate', 'oth_hotwater_floorheating_upward_heatflow_rate', 
            'oth_elecric_floorheating_area_rate', 'oth_elecric_floorheating_upward_heatflow_rate', 
            'oth_ac_floorheating_area_rate', 'oth_ac_floorheating_upward_heatflow_rate', 'oth_ac_floorheating_pipe', 
            'oth_other_heating_device_name', 
            'hotwater_heating_system', 'hotwater_heating_source_type', 'hotwater_heating_source_name', 
            'hotwater_heating_source_saving_input', 
            'hotwater_heating_source_efficiency_OilClassic', 'hotwater_heating_source_efficiency_GasClassic', 'hotwater_heating_source_efficiency_GasLatentHeatRecovery', 
            'hotwater_heating_source_pipe', 
            'heating_rated_input', 'heating_rated_power', 'heating_rated_capacity', 'heating_power_correction', 'heating_coefficient', 
            ##冷房方式
            'cooling_system', 'ldk_cooling_type', 'oth_cooling_type', 
            'ldk_cooling_type', 'ldk_ac_cooling_efficiency', 'ldk_ac_cooling_compressor', 
            'oth_cooling_type', 'oth_ac_cooling_efficiency', 'oth_ac_cooling_compressor', 
            'ldk_other_cooling_device_name', 
            'oth_other_cooling_device_name', 
            'cooling_rated_input', 'cooling_rated_power', 'cooling_rated_capacity', 'cooling_power_correction', 'cooling_coefficient', 
            ##換気設備
            'ventilation_type', 
            'ventilation_frequency', 
            'ventilation_saving', 'ventilation_sfp', 
            'ventilation_heatexchanger', 'ventilation_efficiency', 'ventilation_heatexchanger_efficiency', 
            'ventilation_heatexchanger_bal', 'ventilation_heatexchanger_leak', 
            #給湯設備
            'bathroom', 
            'water_heater_type', 'integrated_water_heater_type',
            'gasoil_water_heater_efficiency_type', 
            'gasoil_water_heater_jis_efficiency_GasClassic_Mode', 'gasoil_water_heater_jis_efficiency_GasClassic_Other', 
            'gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Mode', 'gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Other', 
            'gasoil_water_heater_jis_efficiency_OilClassic_Mode', 'gasoil_water_heater_jis_efficiency_OilClassic_Other', 
            'gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Mode', 'gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Other', 
            'heatpump_water_heater_efficiency_type', 'heatpump_water_heater_jis_efficiency_M1SEJISEfficiency', 'heatpump_water_heater_jis_efficiency_Other', 
            'gasoil_heating_water_heater_jis_efficiency_IntegratedGasClassic_Mode', 'gasoil_heating_water_heater_jis_efficiency_IntegratedGasClassic_Other', 
            'gasoil_heating_water_heater_jis_efficiency_IntegratedGasLatentHeatRecovery_Mode', 'gasoil_heating_water_heater_jis_efficiency_IntegratedGasLatentHeatRecovery_Other', 
            'gasoil_heating_water_heater_jis_efficiency_IntegratedOil_Mode', 'gasoil_heating_water_heater_jis_efficiency_IntegratedOil_Other', 
            'water_heater_name', 
            'water_heater_heatpump_unit_input', 'water_heater_heatpump_unit', 'water_heater_heatpump_unit_coolant', 'water_heater_tank_unit', 'water_heater_backup_boiler', 'water_heater_tank_place', 'water_heater_tank_capacity', 
            'solar_water_heater_type', 'solar_water_heater_area_type', 'solar_water_heater_area', 'solar_water_heater_direction', 'solar_water_heater_angle', 'solar_water_heater_tank_capacity', 
            'bath_function', 'bath_insulation', 'pipe_type', 'pipe_saving', 
            'kitchen_tap_saving', 'bath_shower_tap_saving', 'wash_bowl_tap_saving', 
            ##照明設備
            'ldk_lighting', 'ldk_multi', 'ldk_dimming', 
            'oth_lighting', 'oth_dimming', 
            'nonldk_lighting', 'nonldk_sensor', 
            ##太陽光発電
            'photovoltaic', 'photovoltaic_power_conditioner_efficiency_input', 'photovoltaic_power_conditioner_efficiency', 
            'photovoltaic_panel_1_cell', 'photovoltaic_panel_2_cell', 'photovoltaic_panel_3_cell', 'photovoltaic_panel_4_cell', 
            'photovol_panel_1_capacity', 'photovol_panel_2_capacity', 'photovol_panel_3_capacity', 'photovol_panel_4_capacity', 
            'photovol_panel_1_setup', 'photovol_panel_2_setup', 'photovol_panel_3_setup', 'photovol_panel_4_setup', 
            'photovol_panel_1_direction', 'photovol_panel_2_direction', 'photovol_panel_3_direction', 'photovol_panel_4_direction', 
            'photovol_panel_1_angle', 'photovol_panel_2_angle', 'photovol_panel_3_angle', 'photovol_panel_4_angle', 
            ##コージェネレーション
            'cogene', 'cogene_type', 
            'cogene_PEFC_input', 'cogene_powerunit_PEFC', 'cogene_tankunit_PEFC', 'cogene_backupboiler_PEFC', 
            'cogene_SOFC_input', 'cogene_powerunit_SOFC', 'cogene_tankunit_SOFC', 'cogene_backupboiler_SOFC', 
            'cogene_unit_powerunit_2015', 
        ]

class UpdateSpecForm(forms.ModelForm):
    class Meta:
        model = HouseSpec
        fields = [
            #暖房方式
            'heating_system', 'ldk_heating_type', 'oth_heating_type', 
            'ldk_ac_heating_efficiency', 'ldk_ac_heating_compressor', 
            'ldk_ff_saving_input', 'ldk_ff_heating_efficiency', 
            'ldk_hotwater_floorheating_area_rate', 'ldk_hotwater_floorheating_upward_heatflow_rate', 
            'ldk_elecric_floorheating_area_rate', 'ldk_elecric_floorheating_upward_heatflow_rate', 
            'ldk_ac_floorheating_area_rate', 'ldk_ac_floorheating_upward_heatflow_rate', 'ldk_ac_floorheating_pipe', 
            'ldk_other_heating_device_name', 
            'oth_ac_heating_efficiency', 'oth_ac_heating_compressor', 
            'oth_ff_saving_input', 'oth_ff_heating_efficiency', 
            'oth_hotwater_floorheating_area_rate', 'oth_hotwater_floorheating_upward_heatflow_rate', 
            'oth_elecric_floorheating_area_rate', 'oth_elecric_floorheating_upward_heatflow_rate', 
            'oth_ac_floorheating_area_rate', 'oth_ac_floorheating_upward_heatflow_rate', 'oth_ac_floorheating_pipe', 
            'oth_other_heating_device_name', 
            'hotwater_heating_system', 'hotwater_heating_source_type', 'hotwater_heating_source_name', 
            'hotwater_heating_source_saving_input', 
            'hotwater_heating_source_efficiency_OilClassic', 'hotwater_heating_source_efficiency_GasClassic', 'hotwater_heating_source_efficiency_GasLatentHeatRecovery', 
            'hotwater_heating_source_pipe', 
            'heating_rated_input', 'heating_rated_power', 'heating_rated_capacity', 'heating_power_correction', 'heating_coefficient', 
            ##冷房方式
            'cooling_system', 'ldk_cooling_type', 'oth_cooling_type', 
            'ldk_cooling_type', 'ldk_ac_cooling_efficiency', 'ldk_ac_cooling_compressor', 
            'oth_cooling_type', 'oth_ac_cooling_efficiency', 'oth_ac_cooling_compressor', 
            'ldk_other_cooling_device_name', 
            'oth_other_cooling_device_name', 
            'cooling_rated_input', 'cooling_rated_power', 'cooling_rated_capacity', 'cooling_power_correction', 'cooling_coefficient', 
            ##換気設備
            'ventilation_type', 
            'ventilation_frequency', 
            'ventilation_saving', 'ventilation_sfp', 
            'ventilation_heatexchanger', 'ventilation_efficiency', 'ventilation_heatexchanger_efficiency', 
            'ventilation_heatexchanger_bal', 'ventilation_heatexchanger_leak', 
            #給湯設備
            'bathroom', 
            'water_heater_type', 'integrated_water_heater_type',
            'gasoil_water_heater_efficiency_type', 
            'gasoil_water_heater_jis_efficiency_GasClassic_Mode', 'gasoil_water_heater_jis_efficiency_GasClassic_Other', 
            'gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Mode', 'gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Other', 
            'gasoil_water_heater_jis_efficiency_OilClassic_Mode', 'gasoil_water_heater_jis_efficiency_OilClassic_Other', 
            'gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Mode', 'gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Other', 
            'heatpump_water_heater_efficiency_type', 'heatpump_water_heater_jis_efficiency_M1SEJISEfficiency', 'heatpump_water_heater_jis_efficiency_Other', 
            'gasoil_heating_water_heater_jis_efficiency_IntegratedGasClassic_Mode', 'gasoil_heating_water_heater_jis_efficiency_IntegratedGasClassic_Other', 
            'gasoil_heating_water_heater_jis_efficiency_IntegratedGasLatentHeatRecovery_Mode', 'gasoil_heating_water_heater_jis_efficiency_IntegratedGasLatentHeatRecovery_Other', 
            'gasoil_heating_water_heater_jis_efficiency_IntegratedOil_Mode', 'gasoil_heating_water_heater_jis_efficiency_IntegratedOil_Other', 
            'water_heater_name', 
            'water_heater_heatpump_unit_input', 'water_heater_heatpump_unit', 'water_heater_heatpump_unit_coolant', 'water_heater_tank_unit', 'water_heater_backup_boiler', 'water_heater_tank_place', 'water_heater_tank_capacity', 
            'solar_water_heater_type', 'solar_water_heater_area_type', 'solar_water_heater_area', 'solar_water_heater_direction', 'solar_water_heater_angle', 'solar_water_heater_tank_capacity', 
            'bath_function', 'bath_insulation', 'pipe_type', 'pipe_saving', 
            'kitchen_tap_saving', 'bath_shower_tap_saving', 'wash_bowl_tap_saving', 
            ##照明設備
            'ldk_lighting', 'ldk_multi', 'ldk_dimming', 
            'oth_lighting', 'oth_dimming', 
            'nonldk_lighting', 'nonldk_sensor', 
            ##太陽光発電
            'photovoltaic', 'photovoltaic_power_conditioner_efficiency_input', 'photovoltaic_power_conditioner_efficiency', 
            'photovoltaic_panel_1_cell', 'photovoltaic_panel_2_cell', 'photovoltaic_panel_3_cell', 'photovoltaic_panel_4_cell', 
            'photovol_panel_1_capacity', 'photovol_panel_2_capacity', 'photovol_panel_3_capacity', 'photovol_panel_4_capacity', 
            'photovol_panel_1_setup', 'photovol_panel_2_setup', 'photovol_panel_3_setup', 'photovol_panel_4_setup', 
            'photovol_panel_1_direction', 'photovol_panel_2_direction', 'photovol_panel_3_direction', 'photovol_panel_4_direction', 
            'photovol_panel_1_angle', 'photovol_panel_2_angle', 'photovol_panel_3_angle', 'photovol_panel_4_angle', 
            ##コージェネレーション
            'cogene', 'cogene_type', 
            'cogene_PEFC_input', 'cogene_powerunit_PEFC', 'cogene_tankunit_PEFC', 'cogene_backupboiler_PEFC', 
            'cogene_SOFC_input', 'cogene_powerunit_SOFC', 'cogene_tankunit_SOFC', 'cogene_backupboiler_SOFC', 
            'cogene_unit_powerunit_2015', 
        ]

class CopySpecForm(forms.ModelForm):
    class Meta:
        model = HouseSpec
        fields = [
            #暖房方式
            'heating_system', 'ldk_heating_type', 'oth_heating_type', 
            'ldk_ac_heating_efficiency', 'ldk_ac_heating_compressor', 
            'ldk_ff_saving_input', 'ldk_ff_heating_efficiency', 
            'ldk_hotwater_floorheating_area_rate', 'ldk_hotwater_floorheating_upward_heatflow_rate', 
            'ldk_elecric_floorheating_area_rate', 'ldk_elecric_floorheating_upward_heatflow_rate', 
            'ldk_ac_floorheating_area_rate', 'ldk_ac_floorheating_upward_heatflow_rate', 'ldk_ac_floorheating_pipe', 
            'ldk_other_heating_device_name', 
            'oth_ac_heating_efficiency', 'oth_ac_heating_compressor', 
            'oth_ff_saving_input', 'oth_ff_heating_efficiency', 
            'oth_hotwater_floorheating_area_rate', 'oth_hotwater_floorheating_upward_heatflow_rate', 
            'oth_elecric_floorheating_area_rate', 'oth_elecric_floorheating_upward_heatflow_rate', 
            'oth_ac_floorheating_area_rate', 'oth_ac_floorheating_upward_heatflow_rate', 'oth_ac_floorheating_pipe', 
            'oth_other_heating_device_name', 
            'hotwater_heating_system', 'hotwater_heating_source_type', 'hotwater_heating_source_name', 
            'hotwater_heating_source_saving_input', 
            'hotwater_heating_source_efficiency_OilClassic', 'hotwater_heating_source_efficiency_GasClassic', 'hotwater_heating_source_efficiency_GasLatentHeatRecovery', 
            'hotwater_heating_source_pipe', 
            'heating_rated_input', 'heating_rated_power', 'heating_rated_capacity', 'heating_power_correction', 'heating_coefficient', 
            ##冷房方式
            'cooling_system', 'ldk_cooling_type', 'oth_cooling_type', 
            'ldk_cooling_type', 'ldk_ac_cooling_efficiency', 'ldk_ac_cooling_compressor', 
            'oth_cooling_type', 'oth_ac_cooling_efficiency', 'oth_ac_cooling_compressor', 
            'ldk_other_cooling_device_name', 
            'oth_other_cooling_device_name', 
            'cooling_rated_input', 'cooling_rated_power', 'cooling_rated_capacity', 'cooling_power_correction', 'cooling_coefficient', 
            ##換気設備
            'ventilation_type', 
            'ventilation_frequency', 
            'ventilation_saving', 'ventilation_sfp', 
            'ventilation_heatexchanger', 'ventilation_efficiency', 'ventilation_heatexchanger_efficiency', 
            'ventilation_heatexchanger_bal', 'ventilation_heatexchanger_leak', 
            #給湯設備
            'bathroom', 
            'water_heater_type', 'integrated_water_heater_type',
            'gasoil_water_heater_efficiency_type', 
            'gasoil_water_heater_jis_efficiency_GasClassic_Mode', 'gasoil_water_heater_jis_efficiency_GasClassic_Other', 
            'gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Mode', 'gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Other', 
            'gasoil_water_heater_jis_efficiency_OilClassic_Mode', 'gasoil_water_heater_jis_efficiency_OilClassic_Other', 
            'gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Mode', 'gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Other', 
            'heatpump_water_heater_efficiency_type', 'heatpump_water_heater_jis_efficiency_M1SEJISEfficiency', 'heatpump_water_heater_jis_efficiency_Other', 
            'gasoil_heating_water_heater_jis_efficiency_IntegratedGasClassic_Mode', 'gasoil_heating_water_heater_jis_efficiency_IntegratedGasClassic_Other', 
            'gasoil_heating_water_heater_jis_efficiency_IntegratedGasLatentHeatRecovery_Mode', 'gasoil_heating_water_heater_jis_efficiency_IntegratedGasLatentHeatRecovery_Other', 
            'gasoil_heating_water_heater_jis_efficiency_IntegratedOil_Mode', 'gasoil_heating_water_heater_jis_efficiency_IntegratedOil_Other', 
            'water_heater_name', 
            'water_heater_heatpump_unit_input', 'water_heater_heatpump_unit', 'water_heater_heatpump_unit_coolant', 'water_heater_tank_unit', 'water_heater_backup_boiler', 'water_heater_tank_place', 'water_heater_tank_capacity', 
            'solar_water_heater_type', 'solar_water_heater_area_type', 'solar_water_heater_area', 'solar_water_heater_direction', 'solar_water_heater_angle', 'solar_water_heater_tank_capacity', 
            'bath_function', 'bath_insulation', 'pipe_type', 'pipe_saving', 
            'kitchen_tap_saving', 'bath_shower_tap_saving', 'wash_bowl_tap_saving', 
            ##照明設備
            'ldk_lighting', 'ldk_multi', 'ldk_dimming', 
            'oth_lighting', 'oth_dimming', 
            'nonldk_lighting', 'nonldk_sensor', 
            ##太陽光発電
            'photovoltaic', 'photovoltaic_power_conditioner_efficiency_input', 'photovoltaic_power_conditioner_efficiency', 
            'photovoltaic_panel_1_cell', 'photovoltaic_panel_2_cell', 'photovoltaic_panel_3_cell', 'photovoltaic_panel_4_cell', 
            'photovol_panel_1_capacity', 'photovol_panel_2_capacity', 'photovol_panel_3_capacity', 'photovol_panel_4_capacity', 
            'photovol_panel_1_setup', 'photovol_panel_2_setup', 'photovol_panel_3_setup', 'photovol_panel_4_setup', 
            'photovol_panel_1_direction', 'photovol_panel_2_direction', 'photovol_panel_3_direction', 'photovol_panel_4_direction', 
            'photovol_panel_1_angle', 'photovol_panel_2_angle', 'photovol_panel_3_angle', 'photovol_panel_4_angle', 
            ##コージェネレーション
            'cogene', 'cogene_type', 
            'cogene_PEFC_input', 'cogene_powerunit_PEFC', 'cogene_tankunit_PEFC', 'cogene_backupboiler_PEFC', 
            'cogene_SOFC_input', 'cogene_powerunit_SOFC', 'cogene_tankunit_SOFC', 'cogene_backupboiler_SOFC', 
            'cogene_unit_powerunit_2015', 
        ]

