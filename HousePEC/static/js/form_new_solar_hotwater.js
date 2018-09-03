$(document).ready(function () {
    var solar_water_heater_type = $(id_solar_water_heater_type).val();

    $('#id_card_solar_water_heater_area_type').hide();
    $('#id_card_solar_water_heater_system1').hide();
    $('#id_card_solar_water_heater_system2').hide();

    switch (solar_water_heater_type) {
        case 'System1':
            $('#id_card_solar_water_heater_area_type').show();
            $('#id_card_solar_water_heater_system1').show();
            break;
        case 'System2':
            $('#id_card_solar_water_heater_area_type').show();
            $('#id_card_solar_water_heater_system2').show();
            break;
        default:
            $('#id_card_solar_water_heater_area_type').hide();
            $('#id_card_solar_water_heater_system1').hide();
            $('#id_card_solar_water_heater_system2').hide();
    }

});

$("#id_solar_water_heater_type").change(function () {
    var solar_water_heater_type = $(this).val();

    $('#id_card_solar_water_heater_area_type').hide();
    $('#id_card_solar_water_heater_system1').hide();
    $('#id_card_solar_water_heater_system2').hide();

    switch (solar_water_heater_type) {
        case 'System1':
            $('#id_card_solar_water_heater_area_type').show();
            $('#id_card_solar_water_heater_system1').show();
            break;
        case 'System2':
            $('#id_card_solar_water_heater_area_type').show();
            $('#id_card_solar_water_heater_system2').show();
            break;
        default:
            $('#id_card_solar_water_heater_area_type').hide();
            $('#id_card_solar_water_heater_system1').hide();
            $('#id_card_solar_water_heater_system2').hide();
    }

});


