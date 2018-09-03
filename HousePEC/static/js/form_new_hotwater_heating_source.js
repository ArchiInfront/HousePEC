function set_hotwater_heating(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system) {
    $('#id_card_hotwater_heating').hide();
    switch (ldk_heating_type) {
        case 'PanelRadiator':
        case 'HotWaterFloorHeatingRadiator':
        case 'FanConvectorRadiator':
            $('#id_card_hotwater_heating').show();
            break;
        default:
            break;
    }
    switch (oth_heating_type) {
        case 'PanelRadiator':
        case 'HotWaterFloorHeatingRadiator':
        case 'FanConvectorRadiator':
            $('#id_card_hotwater_heating').show();
            break;
        default:
            break;
    }

    //温水暖房熱源のすべてのformを非表示
    $('#id_subcard_hotwater_heating_source_type').hide();
    $('#id_form_hotwater_heating_integrated_info').hide();
    $('#id_form_hotwater_heating_cogeneration_info').hide();
    $('#id_form_hotwater_heating_source_name').hide();
    $('#id_form_hotwater_heating_source_pipe').hide();
    $('#id_form_hotwater_heating_source_saving_input').hide();
    $('#id_form_hotwater_heating_source_efficiency_OilClassic').hide();
    $('#id_form_hotwater_heating_source_efficiency_GasClassic').hide();
    $('#id_form_hotwater_heating_source_efficiency_GasLatentHeatRecovery').hide();

    switch (hotwater_heating_system) {
        case 'NonIntegrated':
            $('#id_subcard_hotwater_heating_source_type').show();
            switch ($('#id_hotwater_heating_source_type').val()) {
                case 'OilClassic':
                    $('#id_form_hotwater_heating_source_saving_input').show();
                    if ($('#id_hotwater_heating_source_saving_input').is(':checked')) {
                        $('#id_form_hotwater_heating_source_efficiency_OilClassic').show();
                    }
                    break;
                case 'GasClassic':
                    $('#id_form_hotwater_heating_source_saving_input').show();
                    if ($('#id_hotwater_heating_source_saving_input').is(':checked')) {
                        $('#id_form_hotwater_heating_source_efficiency_GasClassic').show();
                    }
                    break;
                case 'GasLatentHeatRecovery':
                    $('#id_form_hotwater_heating_source_saving_input').show();
                    if ($('#id_hotwater_heating_source_saving_input').is(':checked')) {
                        $('#id_form_hotwater_heating_source_efficiency_GasLatentHeatRecovery').show();
                    }
                    break;
                case 'OilLatentHeatRecovery':
                case 'ElectricHeatPump':
                case 'ElectricHeater':
                default:
                    break;
            }
            $('#id_form_hotwater_heating_source_pipe').show();
            break;
        case 'Integrated':
            $('#id_form_hotwater_heating_integrated_info').show();
            $('#id_form_hotwater_heating_source_pipe').show();
            break;
        case 'Cogeneration':
            $('#id_form_hotwater_heating_cogeneration_info').show();
            $('#id_form_hotwater_heating_source_pipe').show();
            break;
        case 'Other':
            $('#id_form_hotwater_heating_source_name').show();
            $('#id_form_hotwater_heating_source_pipe').show();
            break;
        case 'NotUsed':
            break;
        default:
            break;
    }

    $("#id_ldk_heating_type").val(ldk_heating_type);
    $('#id_oth_heating_type').val(oth_heating_type);
    $('#id_ldk_cooling_type').val(ldk_cooling_type);
    $('#id_oth_cooling_type').val(oth_cooling_type);
    $('#id_hotwater_heating_system').val(hotwater_heating_system);

    return [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system];
}

$("#id_hotwater_heating_system").change(function () {
    var ldk_heating_type = $('#id_ldk_heating_type').val();
    var oth_heating_type = $('#id_oth_heating_type').val();
    var ldk_cooling_type = $('#id_ldk_cooling_type').val();
    var oth_cooling_type = $('#id_oth_cooling_type').val();
    var hotwater_heating_system = $(this).val();
    var water_heater_type = $('#id_water_heater_type').val();
    var integrated_water_heater_type = $('#id_integrated_water_heater_type').val();

    //console.log(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
    console.log(hotwater_heating_system, water_heater_type, integrated_water_heater_type);

    //[ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_ldk_heating(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
    //[ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_oth_heating(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
    //[ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_ldk_cooling(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
    //[ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_oth_cooling(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
    [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_hotwater_heating(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
    [hotwater_heating_system, water_heater_type, integrated_water_heater_type] = set_water_heater(hotwater_heating_system, water_heater_type, integrated_water_heater_type);

    //console.log(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
    console.log(hotwater_heating_system, water_heater_type, integrated_water_heater_type);
});

$("#id_hotwater_heating_source_type").change(function () {
    var ldk_heating_type = $('#id_ldk_heating_type').val();
    var oth_heating_type = $('#id_oth_heating_type').val();
    var ldk_cooling_type = $('#id_ldk_cooling_type').val();
    var oth_cooling_type = $('#id_oth_cooling_type').val();
    var hotwater_heating_system = $("#id_hotwater_heating_system").val();

    [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_hotwater_heating(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);

    console.log(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
});

$('#id_hotwater_heating_source_saving_input').change(function () {
    switch ($('#id_hotwater_heating_source_type').val()) {
        case 'OilClassic':
            $('#id_form_hotwater_heating_source_saving_input').show();
            if ($('#id_hotwater_heating_source_saving_input').is(':checked')) {
                $('#id_form_hotwater_heating_source_efficiency_OilClassic').show();
            } else {
                $('#id_form_hotwater_heating_source_efficiency_OilClassic').hide();
            }
            break;
        case 'GasClassic':
            $('#id_form_hotwater_heating_source_saving_input').show();
            if ($('#id_hotwater_heating_source_saving_input').is(':checked')) {
                $('#id_form_hotwater_heating_source_efficiency_GasClassic').show();
            } else {
                $('#id_form_hotwater_heating_source_efficiency_GasClassic').hide();
            }
            break;
        case 'GasLatentHeatRecovery':
            $('#id_form_hotwater_heating_source_saving_input').show();
            if ($('#id_hotwater_heating_source_saving_input').is(':checked')) {
                $('#id_form_hotwater_heating_source_efficiency_GasLatentHeatRecovery').show();
            } else {
                $('#id_form_hotwater_heating_source_efficiency_GasLatentHeatRecovery').hide();
            }
            break;
        default:
            break;
    }
});


