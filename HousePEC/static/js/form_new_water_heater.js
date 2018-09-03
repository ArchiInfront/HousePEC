function set_water_heater(hotwater_heating_system, water_heater_type, integrated_water_heater_type) {
    //給湯設備のすべてのformを非表示
    $('#id_form_water_heater_type').hide();
    $('#id_form_integrated_water_heater_type').hide();
    $('#id_form_gasoil_water_heater_efficiency_type').hide();
    $('#id_form_gasoil_water_heater_jis_efficiency_GasClassic_Mode').hide();
    $('#id_form_gasoil_heating_water_heater_jis_efficiency_IntegratedGasClassic_Mode').hide();
    $('#id_form_gasoil_water_heater_jis_efficiency_GasClassic_Other').hide();
    $('#id_form_gasoil_heating_water_heater_jis_efficiency_IntegratedGasClassic_Other').hide();
    $('#id_form_gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Mode').hide();
    $('#id_form_gasoil_heating_water_heater_jis_efficiency_IntegratedGasLatentHeatRecovery_Mode').hide();
    $('#id_form_gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Other').hide();
    $('#id_form_gasoil_heating_water_heater_jis_efficiency_IntegratedGasLatentHeatRecovery_Other').hide();
    $('#id_form_gasoil_water_heater_jis_efficiency_OilClassic_Mode').hide();
    $('#id_form_gasoil_heating_water_heater_jis_efficiency_IntegratedOil_Mode').hide();
    $('#id_form_gasoil_water_heater_jis_efficiency_OilClassic_Other').hide();
    $('#id_form_gasoil_heating_water_heater_jis_efficiency_IntegratedOil_Other').hide();
    $('#id_form_gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Mode').hide();
    $('#id_form_gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Other').hide();
    $('#id_form_heatpump_water_heater_efficiency_type').hide();
    $('#id_form_heatpump_water_heater_jis_efficiency_M1SEJISEfficiency').hide();
    $('#id_form_heatpump_water_heater_jis_efficiency_Other').hide();
    $('#id_form_water_heater_name').hide();
    $('#id_form_water_heater_heatpump_unit_input').hide();
    $('#id_form_water_heater_heatpump_unit').hide();
    $('#id_form_water_heater_heatpump_unit_coolant').hide();
    $('#id_form_water_heater_tank_unit').hide();
    $('#id_form_water_heater_backup_boiler').hide();
    $('#id_form_water_heater_tank_place').hide();
    $('#id_form_water_heater_tank_capacity').hide();
    $('#id_form_water_heater_cogeneration_info').hide();

    switch (hotwater_heating_system) {
        case 'NonIntegrated':
            //給湯熱源（給湯専用型）を表示
            $('#id_form_water_heater_type').show();
            switch (water_heater_type) {
                case 'GasClassic':
                    $('#id_form_gasoil_water_heater_efficiency_type').show();
                    switch ($('#id_gasoil_water_heater_efficiency_type').val()) {
                        case 'Mode':
                            $('#id_form_gasoil_water_heater_jis_efficiency_GasClassic_Mode').show();
                            break;
                        case 'Other':
                            $('#id_form_gasoil_water_heater_jis_efficiency_GasClassic_Other').show();
                            break;
                        case 'None':
                        default:
                            break;
                    }
                    break;
                case 'GasLatentHeatRecovery':
                    $('#id_form_gasoil_water_heater_efficiency_type').show();
                    switch ($('#id_gasoil_water_heater_efficiency_type').val()) {
                        case 'Mode':
                            $('#id_form_gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Mode').show();
                            break;
                        case 'Other':
                            $('#id_form_gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Other').show();
                            break;
                        case 'None':
                        default:
                            break;
                    }
                    break;
                case 'OilClassic':
                    $('#id_form_gasoil_water_heater_efficiency_type').show();
                    switch ($('#id_gasoil_water_heater_efficiency_type').val()) {
                        case 'Mode':
                            $('#id_form_gasoil_water_heater_jis_efficiency_OilClassic_Mode').show();
                            break;
                        case 'Other':
                            $('#id_form_gasoil_water_heater_jis_efficiency_OilClassic_Other').show();
                            break;
                        case 'None':
                        default:
                            break;
                    }
                    break;
                case 'OilLatentHeatRecovery':
                    $('#id_form_gasoil_water_heater_efficiency_type').show();
                    switch ($('#id_gasoil_water_heater_efficiency_type').val()) {
                        case 'Mode':
                            $('#id_form_gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Mode').show();
                            break;
                        case 'Other':
                            $('#id_form_gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Other').show();
                            break;
                        case 'None':
                        default:
                            break;
                    }
                    break;
                case 'ElectricHeater':
                    break;
                case 'ElectricHeatPump':
                    $('#id_form_heatpump_water_heater_efficiency_type').show();
                    switch ($('#id_heatpump_water_heater_efficiency_type').val()) {
                        case 'M1SEJISEfficiency':
                            $('#id_form_heatpump_water_heater_jis_efficiency_M1SEJISEfficiency').show();
                            $('#id_form_water_heater_name').show();
                            break;
                        case 'Other':
                            $('#id_form_heatpump_water_heater_jis_efficiency_Other').show();
                            break;
                        case 'None':
                        default:
                            break;
                    }
                    break;
                case 'Hybrid':
                    $('#id_form_water_heater_heatpump_unit_input').show();
                    if ($('#id_water_heater_heatpump_unit_input').is(':checked')) {
                        $('#id_form_water_heater_heatpump_unit').show();
                        $('#id_form_water_heater_tank_unit').show();
                        $('#id_form_water_heater_backup_boiler').show();
                    } else {
                        $('#id_form_water_heater_heatpump_unit_coolant').show();
                        switch ($('#id_water_heater_heatpump_unit_coolant').val()) {
                            case 'HFC':
                                $('#id_form_water_heater_tank_capacity').show();
                                break;
                            case 'Propane':
                            default:
                                $('#id_form_water_heater_tank_capacity').hide();
                                break;
                        }
                    }
                    break;
                case 'Cogeneration':
                    //コージェネレーションについてを表示
                    $('#id_form_water_heater_cogeneration_info').show();
                    break;
                case 'Other':
            //給湯熱源機の名前を表示
                    $('#id_form_water_heater_name').show();
                    break;
                case 'NotUsed':
                    break;
                default:
                    console.log('water_heater_type');
            }
            break;
        case 'Integrated':
            //給湯熱源（給湯・温水暖房一体型）を表示
            $('#id_form_integrated_water_heater_type').show();
            switch (integrated_water_heater_type) {
                case 'IntegratedGasClassic':
                    $('#id_form_gasoil_water_heater_efficiency_type').show();
                    switch ($('#id_gasoil_water_heater_efficiency_type').val()) {
                        case 'Mode':
                            $('#id_form_gasoil_water_heater_jis_efficiency_GasClassic_Mode').show();
                            $('#id_form_gasoil_heating_water_heater_jis_efficiency_IntegratedGasClassic_Mode').show();
                            break;
                        case 'Other':
                            $('#id_form_gasoil_water_heater_jis_efficiency_GasClassic_Other').show();
                            $('#id_form_gasoil_heating_water_heater_jis_efficiency_IntegratedGasClassic_Other').show();
                            break;
                        case 'None':
                        default:
                            break;
                    }
                    break;
                case 'IntegratedGasLatentHeatRecovery':
                    $('#id_form_gasoil_water_heater_efficiency_type').show();
                    switch ($('#id_gasoil_water_heater_efficiency_type').val()) {
                        case 'Mode':
                            $('#id_form_gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Mode').show();
                            $('#id_form_gasoil_heating_water_heater_jis_efficiency_IntegratedGasLatentHeatRecovery_Mode').show();
                            break;
                        case 'Other':
                            $('#id_form_gasoil_water_heater_jis_efficiency_GasLatentHeatRecovery_Other').show();
                            $('#id_form_gasoil_heating_water_heater_jis_efficiency_IntegratedGasLatentHeatRecovery_Other').show();
                            break;
                        case 'None':
                        default:
                            break;
                    }
                    break;
                case 'IntegratedOil':
                    $('#id_form_gasoil_water_heater_efficiency_type').show();
                    switch ($('#id_gasoil_water_heater_efficiency_type').val()) {
                        case 'Mode':
                            $('#id_form_gasoil_water_heater_jis_efficiency_OilClassic_Mode').show();
                            $('#id_form_gasoil_heating_water_heater_jis_efficiency_IntegratedOil_Mode').show();
                            break;
                        case 'Other':
                            $('#id_form_gasoil_water_heater_jis_efficiency_OilClassic_Other').show();
                            $('#id_form_gasoil_heating_water_heater_jis_efficiency_IntegratedOil_Other').show();
                            break;
                        case 'None':
                        default:
                            break;
                    }
                    break;
                case 'IntegratedOilLatentHeatRecovery':
                    $('#id_form_gasoil_water_heater_efficiency_type').show();
                    switch ($('#id_gasoil_water_heater_efficiency_type').val()) {
                        case 'Mode':
                            $('#id_form_gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Mode').show();
                            break;
                        case 'Other':
                            $('#id_form_gasoil_water_heater_jis_efficiency_OilLatentHeatRecovery_Other').show();
                            break;
                        case 'None':
                        default:
                            break;
                    }
                    break;
                case 'IntegratedElectricHeater':
                    break;
                case 'Hybrid_Gas':
                    $('#id_form_water_heater_tank_place').show();
                    break;
                case 'Hybrid_Hybrid':
                    break;
                case 'Gas_Hybrid':
                    $('#id_form_water_heater_heatpump_unit_input').show();
                    if ($('#id_water_heater_heatpump_unit_input').is(':checked')) {
                        $('#id_form_water_heater_heatpump_unit').show();
                        $('#id_form_water_heater_tank_unit').show();
                        $('#id_form_water_heater_backup_boiler').show();
                    } else {
                        $('#id_form_water_heater_heatpump_unit_coolant').show();
                        switch ($('#id_water_heater_heatpump_unit_coolant').val()) {
                            case 'HFC':
                                $('#id_form_water_heater_tank_capacity').show();
                                break;
                            case 'Propane':
                            default:
                                $('#id_form_water_heater_tank_capacity').hide();
                                break;
                        }
                    }
                    break;
                case 'Cogeneration':
                    //コージェネレーションについてを表示
                    $('#id_form_water_heater_cogeneration_info').show();
                    break;
                case 'Other':
            //給湯熱源機の名前を表示
                    $('#id_form_water_heater_name').show();
                    break;
                case 'NotUsed':
                    break;
                default:
                    console.log('integrated_water_heater_type');
            }
            break;
        case 'Cogeneration':
            //コージェネレーションについてを表示
            $('#id_form_water_heater_cogeneration_info').show();
            break;
        case 'Other':
            //給湯熱源機の名前を表示
            $('#id_form_water_heater_name').show();
            break;
        case 'NotUsed':
            //表示フォームなし
            break;
        default:
            break;
    }

    return [hotwater_heating_system, water_heater_type, integrated_water_heater_type];
}

function set_bathroom(bathroom) {
    var bath_function_list = {
        'SingleFunction': '給湯単機能',
        'BathNoReheating': 'ふろ給湯器(追い焚きなし)',
        'BathReheating': 'ふろ給湯器(追い焚きあり)',
    };

    switch (bathroom) {
        case 'TapAndBath':
            $('#id_bath_function').empty();
            $('#id_bath_function').append($('<option>').val('BathReheating').text('ふろ給湯器(追い焚きあり)'));
            $('#id_bath_function').append($('<option>').val('BathNoReheating').text('ふろ給湯器(追い焚きなし)'));
            $('#id_bath_function').append($('<option>').val('SingleFunction').text('給湯単機能'));
            $('#id_card_water_heater').show();
            $('#id_form_bath_function').show();
            $('#id_card_pipe_type').show();
            $('#id_card_tap_saving').show();
            $('#id_form_bath_shower_tap_saving').show();
            $('#id_card_bath_insulation').show();
            break;
        case 'TapOnly':
            $('#id_bath_function').empty();
            $('#id_bath_function').append($('<option>').val('SingleFunction').text('給湯単機能'));
            $('#id_card_water_heater').show();
            $('#id_form_bath_function').show();
            $('#id_card_pipe_type').show();
            $('#id_card_tap_saving').show();
            $('#id_form_bath_shower_tap_saving').hide();
            $('#id_card_bath_insulation').hide();
            break;
        case 'NA':
        default:
            $('#id_card_water_heater').hide();
            $('#id_form_bath_function').hide();
            $('#id_card_pipe_type').hide();
            $('#id_card_tap_saving').hide();
            $('#id_card_bath_insulation').hide();
    }
}

$(document).ready(function () {
    var bathroom = $("#id_bathroom").val();
    var hotwater_heating_system = $('#id_hotwater_heating_system').val();
    var water_heater_type = $("#id_water_heater_type").val();
    var integrated_water_heater_type = $('#id_integrated_water_heater_type').val();

    bathroom = set_bathroom(bathroom);
    [hotwater_heating_system, water_heater_type, integrated_water_heater_type] = set_water_heater(hotwater_heating_system, water_heater_type, integrated_water_heater_type);
    console.log(hotwater_heating_system, water_heater_type, integrated_water_heater_type);
});

$("#id_bathroom").change(function () {
    var bathroom = $(this).val();

    bathroom = set_bathroom(bathroom);

    console.log(bathroom);
});

$("#id_water_heater_type").change(function () {
    var hotwater_heating_system = $('#id_hotwater_heating_system').val();
    var water_heater_type = $(this).val();
    var integrated_water_heater_type = $('#id_integrated_water_heater_type').val();

    [hotwater_heating_system, water_heater_type, integrated_water_heater_type] = set_water_heater(hotwater_heating_system, water_heater_type, integrated_water_heater_type);

    console.log(hotwater_heating_system, water_heater_type, integrated_water_heater_type);
});

$("#id_integrated_water_heater_type").change(function () {
    var hotwater_heating_system = $('#id_hotwater_heating_system').val();
    var water_heater_type = $('#id_water_heater_type').val();
    var integrated_water_heater_type = $(this).val();

    [hotwater_heating_system, water_heater_type, integrated_water_heater_type] = set_water_heater(hotwater_heating_system, water_heater_type, integrated_water_heater_type);

    console.log(hotwater_heating_system, water_heater_type, integrated_water_heater_type);
});

$('#id_gasoil_water_heater_efficiency_type').change(function () {
    var hotwater_heating_system = $('#id_hotwater_heating_system').val();
    var water_heater_type = $('#id_water_heater_type').val();
    var integrated_water_heater_type = $("#id_integrated_water_heater_type").val();

    [hotwater_heating_system, water_heater_type, integrated_water_heater_type] = set_water_heater(hotwater_heating_system, water_heater_type, integrated_water_heater_type);

    console.log(hotwater_heating_system, water_heater_type, integrated_water_heater_type);
});

$('#id_heatpump_water_heater_efficiency_type').change(function () {
    var hotwater_heating_system = $('#id_hotwater_heating_system').val();
    var water_heater_type = $('#id_water_heater_type').val();
    var integrated_water_heater_type = $("#id_integrated_water_heater_type").val();

    [hotwater_heating_system, water_heater_type, integrated_water_heater_type] = set_water_heater(hotwater_heating_system, water_heater_type, integrated_water_heater_type);

    console.log(hotwater_heating_system, water_heater_type, integrated_water_heater_type);
});

$('#id_water_heater_heatpump_unit_input').change(function () {
    if ($('#id_water_heater_heatpump_unit_input').is(':checked')) {
        $('#id_form_water_heater_heatpump_unit').show();
        $('#id_form_water_heater_tank_unit').show();
        $('#id_form_water_heater_backup_boiler').show();

        $('#id_form_water_heater_heatpump_unit_coolant').hide();
        $('#id_form_water_heater_tank_capacity').hide();
    } else {
        switch ($('#id_water_heater_heatpump_unit_coolant').val()) {
            case 'HFC':
                $('#id_form_water_heater_tank_capacity').show();
                break;
            case 'Propane':
                $('#id_form_water_heater_tank_capacity').hide();
                break;
            default:
                console.log('null');
        }
        $('#id_form_water_heater_heatpump_unit_coolant').show();

        $('#id_form_water_heater_heatpump_unit').hide();
        $('#id_form_water_heater_tank_unit').hide();
        $('#id_form_water_heater_backup_boiler').hide();
    }
});

$('#id_water_heater_heatpump_unit_coolant').change(function () {
    switch ($(this).val()) {
        case 'HFC':
            $('#id_form_water_heater_tank_capacity').show();
            break;
        case 'Propane':
            $('#id_form_water_heater_tank_capacity').hide();
            break;
        default:
            console.log('null');
    }
});

$('#id_pipe_type').change(function () {
    switch ($(this).val()) {
        case 'Branch':
            $('#id_form_pipe_saving').hide();
            break;
        case 'Header':
            $('#id_form_pipe_saving').show();
            break;
        default:
            console.log('null');
    }
});

