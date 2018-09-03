function set_ldk_heating(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system) {
    //関係するすべてのformを、一旦、非表示
    $('#id_subcard_ldk_RoomAirConditioningHeating').hide();
    $('#id_subcard_ldk_FFHeating').hide();
    $('#id_subcard_ldk_HotWaterFloorHeatingRadiator').hide();
    $('#id_subcard_ldk_ElecricFloorHeating').hide();
    $('#id_subcard_ldk_FloorHeatingWithRAC').hide();
    $('#id_subcard_ldk_OtherHeatingDevice').hide();

    switch (ldk_heating_type) {
        case 'RoomAirConditioningHeating':
            $('#id_subcard_ldk_RoomAirConditioningHeating').show();
            //冷房もエアコンに変更
            ldk_cooling_type = 'RoomAirConditioningCooling';
            $("#id_ldk_ac_cooling_efficiency").val($('#id_ldk_ac_heating_efficiency').val());
            $("#id_ldk_ac_cooling_compressor").val($('#id_ldk_ac_heating_compressor').val());
            [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_ldk_cooling(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
            //給湯機の設定
            if (oth_heating_type == 'PanelRadiator' || oth_heating_type == 'HotWaterFloorHeatingRadiator' || oth_heating_type == 'FanConvectorRadiator') {
                hotwater_heating_system = 'Integrated';
            } else {
                hotwater_heating_system = 'NonIntegrated';
            }
            break;
        case 'FFHeating':
            $('#id_subcard_ldk_FFHeating').show();
            //給湯機の設定
            if (oth_heating_type == 'PanelRadiator' || oth_heating_type == 'HotWaterFloorHeatingRadiator' || oth_heating_type == 'FanConvectorRadiator') {
                hotwater_heating_system = 'Integrated';
            } else {
                hotwater_heating_system = 'NonIntegrated';
            }
            break;
        case 'PanelRadiator':
            hotwater_heating_system = 'Integrated'; //温水暖房熱源を暖給一体に変更
            break;
        case 'HotWaterFloorHeatingRadiator':
            $('#id_subcard_ldk_HotWaterFloorHeatingRadiator').show();
            hotwater_heating_system = 'Integrated'; //温水暖房熱源を暖給一体に変更
            break;
        case 'FanConvectorRadiator':
            hotwater_heating_system = 'Integrated'; //温水暖房熱源を暖給一体に変更
            break;
        case 'ElecricFloorHeating':
            $('#id_subcard_ldk_ElecricFloorHeating').show();
            //給湯機の設定
            if (oth_heating_type == 'PanelRadiator' || oth_heating_type == 'HotWaterFloorHeatingRadiator' || oth_heating_type == 'FanConvectorRadiator') {
                hotwater_heating_system = 'Integrated';
            } else {
                hotwater_heating_system = 'NonIntegrated';
            }
            break;
        case 'ElectricRoomHeaterWithThermalStorage':
            //給湯機の設定
            if (oth_heating_type == 'PanelRadiator' || oth_heating_type == 'HotWaterFloorHeatingRadiator' || oth_heating_type == 'FanConvectorRadiator') {
                hotwater_heating_system = 'Integrated';
            } else {
                hotwater_heating_system = 'NonIntegrated';
            }
            break;
        case 'FloorHeatingWithRAC':
            $('#id_subcard_ldk_FloorHeatingWithRAC').show();
            //給湯機の設定
            if (oth_heating_type == 'PanelRadiator' || oth_heating_type == 'HotWaterFloorHeatingRadiator' || oth_heating_type == 'FanConvectorRadiator') {
                hotwater_heating_system = 'Integrated';
            } else {
                hotwater_heating_system = 'NonIntegrated';
            }
            break;
        case 'OtherHeatingDevice':
            $('#id_subcard_ldk_OtherHeatingDevice').show();
            //給湯機の設定
            if (oth_heating_type == 'PanelRadiator' || oth_heating_type == 'HotWaterFloorHeatingRadiator' || oth_heating_type == 'FanConvectorRadiator') {
                hotwater_heating_system = 'Integrated';
            } else {
                hotwater_heating_system = 'NonIntegrated';
            }
            break;
        case 'NotInstalled':
            //給湯機の設定
            if (oth_heating_type == 'PanelRadiator' || oth_heating_type == 'HotWaterFloorHeatingRadiator' || oth_heating_type == 'FanConvectorRadiator') {
                hotwater_heating_system = 'Integrated';
            } else {
                hotwater_heating_system = 'NonIntegrated';
            }
            break;
        default:
            break;
    }

    //$("#id_ldk_heating_type").val(ldk_heating_type);
    $('#id_oth_heating_type').val(oth_heating_type);
    $('#id_ldk_cooling_type').val(ldk_cooling_type);
    $('#id_oth_cooling_type').val(oth_cooling_type);
    $('#id_hotwater_heating_system').val(hotwater_heating_system);

    return [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system];
}

function set_oth_heating(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system) {
    //関係するすべてのformを、一旦、非表示
    $('#id_subcard_oth_RoomAirConditioningHeating').hide();
    $('#id_subcard_oth_FFHeating').hide();
    $('#id_subcard_oth_HotWaterFloorHeatingRadiator').hide();
    $('#id_subcard_oth_ElecricFloorHeating').hide();
    $('#id_subcard_oth_FloorHeatingWithRAC').hide();
    $('#id_subcard_oth_OtherHeatingDevice').hide();

    switch (oth_heating_type) {
        case 'RoomAirConditioningHeating':
            $('#id_subcard_oth_RoomAirConditioningHeating').show();
            oth_cooling_type = 'RoomAirConditioningCooling'; //冷房もエアコンに変更
            $("#id_oth_ac_cooling_efficiency").val($('#id_oth_ac_heating_efficiency').val());
            $("#id_oth_ac_cooling_compressor").val($('#id_oth_ac_heating_compressor').val());
            [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_oth_cooling(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
            //給湯機の設定
            if (ldk_heating_type == 'PanelRadiator' || ldk_heating_type == 'HotWaterFloorHeatingRadiator' || ldk_heating_type == 'FanConvectorRadiator') {
                hotwater_heating_system = 'Integrated';
            } else {
                hotwater_heating_system = 'NonIntegrated';
            }
            break;
        case 'FFHeating':
            $('#id_subcard_oth_FFHeating').show();
            //給湯機の設定
            if (ldk_heating_type == 'PanelRadiator' || ldk_heating_type == 'HotWaterFloorHeatingRadiator' || ldk_heating_type == 'FanConvectorRadiator') {
                hotwater_heating_system = 'Integrated';
            } else {
                hotwater_heating_system = 'NonIntegrated';
            }
            break;
        case 'PanelRadiator':
            hotwater_heating_system = 'Integrated'; //温水暖房熱源を暖給一体に変更
            break;
        case 'HotWaterFloorHeatingRadiator':
            $('#id_subcard_oth_HotWaterFloorHeatingRadiator').show();
            hotwater_heating_system = 'Integrated'; //温水暖房熱源を暖給一体に変更
            break;
        case 'FanConvectorRadiator':
            hotwater_heating_system = 'Integrated'; //温水暖房熱源を暖給一体に変更
            break;
        case 'ElecricFloorHeating':
            $('#id_subcard_oth_ElecricFloorHeating').show();
            //給湯機の設定
            if (ldk_heating_type == 'PanelRadiator' || ldk_heating_type == 'HotWaterFloorHeatingRadiator' || ldk_heating_type == 'FanConvectorRadiator') {
                hotwater_heating_system = 'Integrated';
            } else {
                hotwater_heating_system = 'NonIntegrated';
            }
            break;
        case 'ElectricRoomHeaterWithThermalStorage':
            //給湯機の設定
            if (ldk_heating_type == 'PanelRadiator' || ldk_heating_type == 'HotWaterFloorHeatingRadiator' || ldk_heating_type == 'FanConvectorRadiator') {
                hotwater_heating_system = 'Integrated';
            } else {
                hotwater_heating_system = 'NonIntegrated';
            }
            break;
        case 'FloorHeatingWithRAC':
            $('#id_subcard_oth_FloorHeatingWithRAC').show();
            //給湯機の設定
            if (ldk_heating_type == 'PanelRadiator' || ldk_heating_type == 'HotWaterFloorHeatingRadiator' || ldk_heating_type == 'FanConvectorRadiator') {
                hotwater_heating_system = 'Integrated';
            } else {
                hotwater_heating_system = 'NonIntegrated';
            }
            break;
        case 'OtherHeatingDevice':
            $('#id_subcard_oth_OtherHeatingDevice').show();
            //給湯機の設定
            if (ldk_heating_type == 'PanelRadiator' || ldk_heating_type == 'HotWaterFloorHeatingRadiator' || ldk_heating_type == 'FanConvectorRadiator') {
                hotwater_heating_system = 'Integrated';
            } else {
                hotwater_heating_system = 'NonIntegrated';
            }
            break;
        case 'NotInstalled':
            //給湯機の設定
            if (ldk_heating_type == 'PanelRadiator' || ldk_heating_type == 'HotWaterFloorHeatingRadiator' || ldk_heating_type == 'FanConvectorRadiator') {
                hotwater_heating_system = 'Integrated';
            } else {
                hotwater_heating_system = 'NonIntegrated';
            }
            break;
        default:
            break;
    }

    $("#id_ldk_heating_type").val(ldk_heating_type);
    //$('#id_oth_heating_type').val(oth_heating_type);
    $('#id_ldk_cooling_type').val(ldk_cooling_type);
    $('#id_oth_cooling_type').val(oth_cooling_type);
    $('#id_hotwater_heating_system').val(hotwater_heating_system);

    return [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system];
}

function set_ldk_cooling(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system) {
    //関係するすべてのformを、一旦、非表示
    $('#id_subcard_ldk_RoomAirConditioningCooling').hide();
    $('#id_subcard_ldk_OtherCoolingDevice').hide();

    switch (ldk_cooling_type) {
        case 'RoomAirConditioningCooling':
            $('#id_subcard_ldk_RoomAirConditioningCooling').show();
            break;
        case 'OtherCoolingDevice':
            $('#id_subcard_ldk_OtherCoolingDevice').show();
            break;
        case 'NotInstalled':
            break;
        default:
            break;
    }

    $("#id_ldk_heating_type").val(ldk_heating_type);
    $('#id_oth_heating_type').val(oth_heating_type);
    //$('#id_ldk_cooling_type').val(ldk_cooling_type);
    $('#id_oth_cooling_type').val(oth_cooling_type);
    $('#id_hotwater_heating_system').val(hotwater_heating_system);

    return [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system];
}

function set_oth_cooling(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system) {
    //関係するすべてのformを、一旦、非表示
    $('#id_subcard_oth_RoomAirConditioningCooling').hide();
    $('#id_subcard_oth_OtherCoolingDevice').hide();

    switch (oth_cooling_type) {
        case 'RoomAirConditioningCooling':
            $('#id_subcard_oth_RoomAirConditioningCooling').show();
            break;
        case 'OtherCoolingDevice':
            $('#id_subcard_oth_OtherCoolingDevice').show();
            break;
        case 'NotInstalled':
            break;
        default:
            break;
    }

    $("#id_ldk_heating_type").val(ldk_heating_type);
    $('#id_oth_heating_type').val(oth_heating_type);
    $('#id_ldk_cooling_type').val(ldk_cooling_type);
    //$('#id_oth_cooling_type').val(oth_cooling_type);
    $('#id_hotwater_heating_system').val(hotwater_heating_system);

    return [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system];
}

$(document).ready(function () {
    var heating_system = $("#id_heating_system").val();
    var ldk_heating_type = $("#id_ldk_heating_type").val();
    var oth_heating_type = $('#id_oth_heating_type').val();
    var ldk_cooling_type = $('#id_ldk_cooling_type').val();
    var oth_cooling_type = $('#id_oth_cooling_type').val();
    var hotwater_heating_system = $('#id_hotwater_heating_system').val();
    var water_heater_type = $('#id_water_heater_type').val();
    var integrated_water_heater_type = $('#id_integrated_water_heater_type').val();

    switch (heating_system) {
        case 'RoomSpaceHeating':
            $('#id_card_ElectricHeatPumpCentralHeating').hide();
            $('#id_card_ldk_heating').show();
            $('#id_card_oth_heating').show();
            //冷房もダクト式セントラル空調機以外に変更
            $("#id_cooling_system").val('RoomSpaceCooling');
            $('#id_card_ElectricHeatPumpCentralCooling').hide();
            $('#id_card_ldk_cooling').show();
            $('#id_card_oth_cooling').show();
            [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_ldk_heating(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
            [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_oth_heating(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
            [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_ldk_cooling(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
            [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_oth_cooling(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
            [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_hotwater_heating(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
            [hotwater_heating_system, water_heater_type, integrated_water_heater_type] = set_water_heater(hotwater_heating_system, water_heater_type, integrated_water_heater_type);
            break;
        case 'AllSpaceHeating':
            $('#id_card_ElectricHeatPumpCentralHeating').show();
            $('#id_card_ldk_heating').hide();
            $('#id_card_oth_heating').hide();
            //冷房もダクト式セントラル空調機に変更
            $("#id_cooling_system").val('AllSpaceCooling');
            $('#id_card_ElectricHeatPumpCentralCooling').show();
            $('#id_card_ldk_cooling').hide();
            $('#id_card_oth_cooling').hide();
            //温水暖房熱源を非表示
            $('#id_card_hotwater_heating').hide();
            //給湯機の設定
            hotwater_heating_system = 'NonIntegrated';
            [hotwater_heating_system, water_heater_type, integrated_water_heater_type] = set_water_heater(hotwater_heating_system, water_heater_type, integrated_water_heater_type);
            break;
        case 'NotInstalled':
        default:
            $('#id_card_ElectricHeatPumpCentralHeating').hide();
            $('#id_card_ldk_heating').hide();
            $('#id_card_oth_heating').hide();
            //$("#id_ldk_heating_type").val('NotInstalled');
            //$("#id_oth_heating_type").val('NotInstalled');
            //冷房も設置しないに変更
            $("#id_cooling_system").val('NotInstalled');
            $('#id_card_ElectricHeatPumpCentralCooling').hide();
            $('#id_card_ldk_cooling').hide();
            $('#id_card_oth_cooling').hide();
            //$("#id_ldk_cooling_type").val('NotInstalled');
            //$("#id_oth_cooling_type").val('NotInstalled');
            //温水暖房熱源を非表示
            $('#id_card_hotwater_heating').hide();
            //給湯機の設定
            hotwater_heating_system = 'NonIntegrated';
            [hotwater_heating_system, water_heater_type, integrated_water_heater_type] = set_water_heater(hotwater_heating_system, water_heater_type, integrated_water_heater_type);
            break;
    }

    console.log(heating_system, ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system)
});

$('#id_heating_system').change(function () {
    var heating_system = $(this).val();
    var ldk_heating_type = $("#id_ldk_heating_type").val();
    var oth_heating_type = $('#id_oth_heating_type').val();
    var ldk_cooling_type = $('#id_ldk_cooling_type').val();
    var oth_cooling_type = $('#id_oth_cooling_type').val();
    var hotwater_heating_system = $('#id_hotwater_heating_system').val();
    var water_heater_type = $('#id_water_heater_type').val();
    var integrated_water_heater_type = $('#id_integrated_water_heater_type').val();

    switch (heating_system) {
        case 'RoomSpaceHeating':
            $('#id_card_ElectricHeatPumpCentralHeating').hide();
            $('#id_card_ldk_heating').show();
            $('#id_card_oth_heating').show();
            //冷房もダクト式セントラル空調機以外に変更
            $("#id_cooling_system").val('RoomSpaceCooling');
            $('#id_card_ElectricHeatPumpCentralCooling').hide();
            $('#id_card_ldk_cooling').show();
            $('#id_card_oth_cooling').show();
            [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_ldk_heating(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
            [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_oth_heating(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
            [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_ldk_cooling(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
            [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_oth_cooling(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
            [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_hotwater_heating(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
            [hotwater_heating_system, water_heater_type, integrated_water_heater_type] = set_water_heater(hotwater_heating_system, water_heater_type, integrated_water_heater_type);
            break;
        case 'AllSpaceHeating':
            $('#id_card_ElectricHeatPumpCentralHeating').show();
            $('#id_card_ldk_heating').hide();
            $('#id_card_oth_heating').hide();
            //冷房もダクト式セントラル空調機に変更
            $("#id_cooling_system").val('AllSpaceCooling');
            $('#id_card_ElectricHeatPumpCentralCooling').show();
            $('#id_card_ldk_cooling').hide();
            $('#id_card_oth_cooling').hide();
            //温水暖房熱源を非表示
            $('#id_card_hotwater_heating').hide();
            //給湯機の設定
            hotwater_heating_system = 'NonIntegrated';
            [hotwater_heating_system, water_heater_type, integrated_water_heater_type] = set_water_heater(hotwater_heating_system, water_heater_type, integrated_water_heater_type);
            break;
        case 'NotInstalled':
        default:
            $('#id_card_ElectricHeatPumpCentralHeating').hide();
            $('#id_card_ldk_heating').hide();
            $('#id_card_oth_heating').hide();
            //$("#id_ldk_heating_type").val('NotInstalled');
            //$("#id_oth_heating_type").val('NotInstalled');
            //冷房も設置しないに変更
            $("#id_cooling_system").val('NotInstalled');
            $('#id_card_ElectricHeatPumpCentralCooling').hide();
            $('#id_card_ldk_cooling').hide();
            $('#id_card_oth_cooling').hide();
            //$("#id_ldk_cooling_type").val('NotInstalled');
            //$("#id_oth_cooling_type").val('NotInstalled');
            //温水暖房熱源を非表示
            $('#id_card_hotwater_heating').hide();
            //給湯機の設定
            hotwater_heating_system = 'NonIntegrated';
            [hotwater_heating_system, water_heater_type, integrated_water_heater_type] = set_water_heater(hotwater_heating_system, water_heater_type, integrated_water_heater_type);
            break;
    }
    console.log(heating_system, hotwater_heating_system)
});

$("#id_ldk_heating_type").change(function () {
    var ldk_heating_type = $(this).val();
    var oth_heating_type = $('#id_oth_heating_type').val();
    var ldk_cooling_type = $('#id_ldk_cooling_type').val();
    var oth_cooling_type = $('#id_oth_cooling_type').val();
    var hotwater_heating_system = $('#id_hotwater_heating_system').val();
    var water_heater_type = $('#id_water_heater_type').val();
    var integrated_water_heater_type = $('#id_integrated_water_heater_type').val();
    
    [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_ldk_heating(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
    [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_hotwater_heating(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
    [hotwater_heating_system, water_heater_type, integrated_water_heater_type] = set_water_heater(hotwater_heating_system, water_heater_type, integrated_water_heater_type);

    console.log(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
});

$('#id_ldk_ac_heating_efficiency').change(function () {
    $("#id_ldk_ac_cooling_efficiency").val($('#id_ldk_ac_heating_efficiency').val());
});

$('#id_ldk_ac_heating_compressor').change(function () {
    $("#id_ldk_ac_cooling_compressor").val($('#id_ldk_ac_heating_compressor').val());
});

$('#id_ldk_ff_saving_input').change(function () {
    //console.log($('#id_ldk_ff_saving_input').is(':checked'))
    if ($('#id_ldk_ff_saving_input').is(':checked')) {
        $('#id_form_ldk_ff_heating_efficiency').show();
    } else {
        $('#id_form_ldk_ff_heating_efficiency').hide();
    }
});

$('#id_heating_rated_input').change(function () {
    //console.log($('#id_heating_rated_input').is(':checked'))
    if ($('#id_heating_rated_input').is(':checked')) {
        $('#id_form_ElectricHeatPumpCentralHeating_rated_capacity').show();
        $('#id_form_ElectricHeatPumpCentralHeating_rated_power').show();
        $('#id_cooling_rated_input').prop('checked', true)
        $('#id_form_ElectricHeatPumpCentralCooling_rated_capacity').show();
        $('#id_form_ElectricHeatPumpCentralCooling_rated_power').show();
    } else {
        $('#id_form_ElectricHeatPumpCentralHeating_rated_capacity').hide();
        $('#id_form_ElectricHeatPumpCentralHeating_rated_power').hide();
        $('#id_cooling_rated_input').prop('checked', false)
        $('#id_form_ElectricHeatPumpCentralCooling_rated_capacity').hide();
        $('#id_form_ElectricHeatPumpCentralCooling_rated_power').hide();
    }
});

$('#id_heating_power_correction').change(function () {
    //console.log($('#id_heating_power_correction').val())
    if ($('#id_heating_power_correction').val() === 'Correct') {
        $('#id_heating_coefficient').val(1.40);
        $('#id_cooling_power_correction').val('Correct')
        $('#id_cooling_coefficient').val(1.40);
    } else {
        $('#id_heating_coefficient').val(1.65);
        $('#id_cooling_power_correction').val('None')
        $('#id_cooling_coefficient').val(1.69);
    }
});

