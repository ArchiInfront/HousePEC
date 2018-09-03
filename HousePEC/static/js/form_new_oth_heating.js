$("#id_oth_heating_type").change(function () {
    var ldk_heating_type = $("#id_ldk_heating_type").val();
    var oth_heating_type = $(this).val();
    var ldk_cooling_type = $('#id_ldk_cooling_type').val();
    var oth_cooling_type = $('#id_oth_cooling_type').val();
    var hotwater_heating_system = $('#id_hotwater_heating_system').val();
    var water_heater_type = $('#id_water_heater_type').val();
    var integrated_water_heater_type = $('#id_integrated_water_heater_type').val();

    [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_oth_heating(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
    [ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system] = set_hotwater_heating(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
    [hotwater_heating_system, water_heater_type, integrated_water_heater_type] = set_water_heater(hotwater_heating_system, water_heater_type, integrated_water_heater_type);

    console.log(ldk_heating_type, oth_heating_type, ldk_cooling_type, oth_cooling_type, hotwater_heating_system);
});

$('#id_oth_ac_heating_efficiency').change(function () {
    $("#id_oth_ac_cooling_efficiency").val($('#id_oth_ac_heating_efficiency').val());
});

$('#id_oth_ac_heating_compressor').change(function () {
    $("#id_oth_ac_cooling_compressor").val($('#id_oth_ac_heating_compressor').val());
});

$('#id_oth_ff_saving_input').change(function () {
    console.log($('#id_oth_ff_saving_input').is(':checked'))
    if ($('#id_oth_ff_saving_input').is(':checked')) {
        $('#id_form_oth_ff_heating_efficiency').show();
    } else {
        $('#id_form_oth_ff_heating_efficiency').hide();
    }
});

