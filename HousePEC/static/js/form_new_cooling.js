$('#id_cooling_system').change(function () {
    var cooling_system = $(this).val();
    var ldk_heating_type = $("#id_ldk_heating_type").val();
    var oth_heating_type = $('#id_oth_heating_type').val();
    var ldk_cooling_type = $('#id_ldk_cooling_type').val();
    var oth_cooling_type = $('#id_oth_cooling_type').val();
    var hotwater_heating_system = $('#id_hotwater_heating_system').val();
    var water_heater_type = $('#id_water_heater_type').val();
    var integrated_water_heater_type = $('#id_integrated_water_heater_type').val();

    switch (cooling_system) {
        case 'RoomSpaceCooling':
            $('#id_card_ElectricHeatPumpCentralCooling').hide();
            $('#id_card_ldk_cooling').show();
            $('#id_card_oth_cooling').show();
            //�g�[���_�N�g���Z���g�����󒲋@�ȊO�ɕύX
            $("#id_heating_system").val('RoomSpaceHeating');
            $('#id_card_ElectricHeatPumpCentralHeating').hide();
            $('#id_card_ldk_heating').show();
            $('#id_card_oth_heating').show();
            [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_ldk_heating(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
            [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_ldk_cooling(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
            [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_hotwater_heating(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
            //�����@�̐ݒ�
            [hotwater_heating_system, water_heater_type, integrated_water_heater_type] = set_water_heater(hotwater_heating_system, water_heater_type, integrated_water_heater_type);
            break;
        case 'AllSpaceCooling':
            $('#id_card_ElectricHeatPumpCentralCooling').show();
            $('#id_card_ldk_cooling').hide();
            $('#id_card_oth_cooling').hide();
            //�g�[���_�N�g���Z���g�����󒲋@�ɕύX
            $("#id_heating_system").val('AllSpaceHeating');
            $('#id_card_ElectricHeatPumpCentralHeating').show();
            $('#id_card_ldk_heating').hide();
            $('#id_card_oth_heating').hide();
            //�����g�[�M�����\��
            $('#id_card_hotwater_heating').hide();
            //�����@�̐ݒ�
            hotwater_heating_system = 'NonIntegrated';
            [hotwater_heating_system, water_heater_type, integrated_water_heater_type] = set_water_heater(hotwater_heating_system, water_heater_type, integrated_water_heater_type);
            break;
        case 'NotInstalled':
        default:
            $('#id_card_ElectricHeatPumpCentralCooling').hide();
            $('#id_card_ldk_cooling').hide();
            $('#id_card_oth_cooling').hide();
            //�g�[���_�N�g���Z���g�����󒲋@�ȊO�ɕύX
            $("#id_heating_system").val('RoomSpaceHeating');
            $('#id_card_ElectricHeatPumpCentralHeating').hide();
            $('#id_card_ldk_heating').show();
            $('#id_card_oth_heating').show();
            [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_ldk_heating(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
            [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_ldk_cooling(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
            [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_hotwater_heating(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
            //�����@�̐ݒ�
            hotwater_heating_system = 'NonIntegrated';
            [hotwater_heating_system, water_heater_type, integrated_water_heater_type] = set_water_heater(hotwater_heating_system, water_heater_type, integrated_water_heater_type);
            break;
    }
});

$("#id_ldk_cooling_type").change(function () {
    var ldk_heating_type = $('#id_ldk_heating_type').val();
    var oth_heating_type = $('#id_oth_heating_type').val();
    var ldk_cooling_type = $(this).val();
    var oth_cooling_type = $('#id_oth_cooling_type').val();
    var hotwater_heating_system = $('#id_hotwater_heating_system').val();

    console.log(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);

    //[ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_ldk_heating(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
    //[ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_oth_heating(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
    [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_ldk_cooling(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
    //[ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_oth_cooling(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
    [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_hotwater_heating(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);

    console.log(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
});

$("#id_oth_cooling_type").change(function () {
    var ldk_heating_type = $('#id_ldk_heating_type').val();
    var oth_heating_type = $('#id_oth_heating_type').val();
    var ldk_cooling_type = $('#id_ldk_cooling_type').val();
    var oth_cooling_type = $(this).val();
    var hotwater_heating_system = $('#id_hotwater_heating_system').val();

    console.log(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);

    //[ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_ldk_heating(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
    //[ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_oth_heating(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
    //[ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_ldk_cooling(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
    [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_oth_cooling(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
    [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_hotwater_heating(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);

    console.log(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
});

$('#id_ldk_ac_cooling_efficiency').change(function () {
    $("#id_ldk_ac_heating_efficiency").val($('#id_ldk_ac_cooling_efficiency').val());
});

$('#id_ldk_ac_cooling_compressor').change(function () {
    $("#id_ldk_ac_heating_compressor").val($('#id_ldk_ac_cooling_compressor').val());
});

$('#id_oth_ac_cooling_efficiency').change(function () {
    $("#id_oth_ac_heating_efficiency").val($('#id_oth_ac_cooling_efficiency').val());
});

$('#id_oth_ac_cooling_compressor').change(function () {
    $("#id_oth_ac_heating_compressor").val($('#id_oth_ac_cooling_compressor').val());
});

$('#id_cooling_rated_input').change(function () {
    console.log($('#id_cooling_rated_input').is(':checked'))
    if ($('#id_cooling_rated_input').is(':checked')) {
        $('#id_form_ElectricHeatPumpCentralCooling_rated_capacity').show();
        $('#id_form_ElectricHeatPumpCentralCooling_rated_power').show();
    } else {
        $('#id_form_ElectricHeatPumpCentralCooling_rated_capacity').hide();
        $('#id_form_ElectricHeatPumpCentralCooling_rated_power').hide();
    }
});

$('#id_cooling_power_correction').change(function () {
    console.log($('#id_cooling_power_correction').val())
    if ($('#id_cooling_power_correction').val() === 'Correct') {
        $('#id_cooling_coefficient').val(1.40);
    } else {
        $('#id_cooling_coefficient').val(1.69);
    }
});

