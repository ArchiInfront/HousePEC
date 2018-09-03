$("#id_bathroom").change(function () {
    var bathroom = $(this).val();
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
});

$("#id_integrated_water_heater_type").change(function () {
    var hotwater_heat_source_type = $('#id_hotwater_heat_source_type').val();
    var bathroom = $('#id_bathroom').val();
    var water_heater_type = $('#id_water_heater_type').val();
    var integrated_water_heater_type = $(this).val();

    $('#id_form_water_heater_type').hide();
    $('#id_form_integrated_water_heater_type').show();
    $('#id_form_gasoil_water_heater_efficiency_type').hide();
    $('#id_form_heating_water_heater_jis_efficiency').hide();
    $('#id_form_gasoil_water_heater_efficiency').hide();
    $('#id_form_heatpump_water_heater_efficiency_type').hide();
    $('#id_form_heatpump_water_heater_jis_efficiency').hide();
    $('#id_form_water_heater_name').hide();
    $('#id_form_water_heater_heatpump_unit_input').hide();
    $('#id_form_water_heater_heatpump_unit').hide();
    $('#id_form_water_heater_heatpump_unit_coolant').hide();
    $('#id_form_water_heater_tank_unit').hide();
    $('#id_form_water_heater_backup_boiler').hide();
    $('#id_form_water_heater_tank_place').hide();
    $('#id_form_water_heater_tank_capacity').hide();

    console.log(integrated_water_heater_type);
    switch (integrated_water_heater_type) {
        case 'IntegratedGasClassic':
            $('#id_form_gasoil_water_heater_efficiency_type').show();
            switch ($('#id_gasoil_water_heater_efficiency_type').val()) {
                case 'Mode':
                case 'Other':
                    $('#id_heating_water_heater_jis_efficiency').val(81.0);
                    $('#id_gasoil_water_heater_jis_efficiency').val(70.4);
                    $('#id_form_gasoil_water_heater_jis_efficiency_GasClassic_Mode').show();
                    $('#id_form_gasoil_water_heater_jis_efficiency_OilClassic_Mode').show();
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
                case 'Other':
                    $('#id_heating_water_heater_jis_efficiency').val(87.0);
                    $('#id_gasoil_water_heater_jis_efficiency').val(83.6);
                    $('#id_form_heating_water_heater_jis_efficiency').show();
                    $('#id_form_gasoil_water_heater_efficiency').show();
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
                case 'Other':
                    $('#id_heating_water_heater_jis_efficiency').val(82.0);
                    $('#id_gasoil_water_heater_jis_efficiency').val(77.9);
                    $('#id_form_heating_water_heater_jis_efficiency').show();
                    $('#id_form_gasoil_water_heater_efficiency').show();
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
                case 'Other':
                    $('#id_gasoil_water_heater_jis_efficiency').val(81.9);
                    $('#id_form_heating_water_heater_jis_efficiency').hide();
                    $('#id_form_gasoil_water_heater_efficiency').show();
                    break;
                default:
                    break;
            }
            break;
        case 'IntegratedElectricHeater':
            break;
        case 'Hybrid_Gas':
            $('#id_form_water_heater_heatpump_unit_input').hide();
            $('#id_form_water_heater_heatpump_unit').hide();
            $('#id_form_water_heater_heatpump_unit_coolant').hide();
            $('#id_form_water_heater_tank_unit').hide();
            $('#id_form_water_heater_backup_boiler').hide();
            $('#id_form_water_heater_tank_place').show();
            $('#id_form_water_heater_tank_capacity').hide();
            break;
        case 'Hybrid_Hybrid':
            $('#id_form_water_heater_heatpump_unit_input').hide();
            $('#id_form_water_heater_heatpump_unit').hide();
            $('#id_form_water_heater_heatpump_unit_coolant').hide();
            $('#id_form_water_heater_tank_unit').hide();
            $('#id_form_water_heater_backup_boiler').hide();
            $('#id_form_water_heater_tank_place').hide();
            $('#id_form_water_heater_tank_capacity').hide();
            break;
        case 'Gas_Hybrid':
            $('#id_form_water_heater_heatpump_unit_input').show();
            $('#id_form_water_heater_heatpump_unit').hide();
            $('#id_form_water_heater_heatpump_unit_coolant').hide();
            $('#id_form_water_heater_tank_unit').hide();
            $('#id_form_water_heater_backup_boiler').hide();
            $('#id_form_water_heater_tank_place').hide();
            $('#id_form_water_heater_tank_capacity').hide();
            if ($('#id_water_heater_heatpump_unit_input').is(':checked')) {
                $('#id_form_water_heater_heatpump_unit').show();
                $('#id_form_water_heater_heatpump_unit_coolant').hide();
                $('#id_form_water_heater_tank_unit').show();
                $('#id_form_water_heater_backup_boiler').show();
                $('#id_form_water_heater_tank_place').hide();
                $('#id_form_water_heater_tank_capacity').hide();
            } else {
                $('#id_form_water_heater_heatpump_unit').hide();
                $('#id_form_water_heater_heatpump_unit_coolant').show();
                $('#id_form_water_heater_tank_unit').hide();
                $('#id_form_water_heater_backup_boiler').hide();
                $('#id_form_water_heater_tank_place').hide();
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
            break;
        case 'Other':
            $('#id_form_water_heater_name').show();
            break;
        case 'NotUsed':
            break;
        default:
            console.log('Null');
    }
});

$('#id_gasoil_water_heater_efficiency_type').change(function () {
    var gasoil_water_heater_efficiency_type = $(this).val();

    switch (gasoil_water_heater_efficiency_type) {
        case 'Mode':
        case 'Other':
            $('#id_form_heating_water_heater_jis_efficiency').show();
            $('#id_form_gasoil_water_heater_efficiency').show();
            break;
        case 'None':
        default:
            $('#id_form_heating_water_heater_jis_efficiency').hide();
            $('#id_form_gasoil_water_heater_efficiency').hide();
        //console.log('null');
    }
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

