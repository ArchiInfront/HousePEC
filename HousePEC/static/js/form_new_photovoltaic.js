$(document).ready(function () {
    var photovoltaic = $("#id_photovoltaic").val();

    $('#id_form_photovoltaic_power_conditioner_efficiency_input').hide();
    $('#id_form_photovoltaic_power_conditioner_efficiency').hide();
    $('#id_card_Panel1').hide();
    $('#id_card_Panel2').hide();
    $('#id_card_Panel3').hide();
    $('#id_card_Panel4').hide();

    switch (photovoltaic) {
        case 'Panel1':
            $('#id_form_photovoltaic_power_conditioner_efficiency_input').show();
            if ($('#id_photovoltaic_power_conditioner_efficiency_input').is(':checked')) {
                $('#id_form_photovoltaic_power_conditioner_efficiency').show();
            } else {
                $('#id_form_photovoltaic_power_conditioner_efficiency').hide();
            }
            $('#id_card_Panel1').show();
            $('#id_card_Panel2').hide();
            $('#id_card_Panel3').hide();
            $('#id_card_Panel4').hide();
            break;
        case 'Panel2':
            $('#id_form_photovoltaic_power_conditioner_efficiency_input').show();
            if ($('#id_photovoltaic_power_conditioner_efficiency_input').is(':checked')) {
                $('#id_form_photovoltaic_power_conditioner_efficiency').show();
            } else {
                $('#id_form_photovoltaic_power_conditioner_efficiency').hide();
            }
            $('#id_card_Panel1').show();
            $('#id_card_Panel2').show();
            $('#id_card_Panel3').hide();
            $('#id_card_Panel4').hide();
            break;
        case 'Panel3':
            $('#id_form_photovoltaic_power_conditioner_efficiency_input').show();
            if ($('#id_photovoltaic_power_conditioner_efficiency_input').is(':checked')) {
                $('#id_form_photovoltaic_power_conditioner_efficiency').show();
            } else {
                $('#id_form_photovoltaic_power_conditioner_efficiency').hide();
            }
            $('#id_card_Panel1').show();
            $('#id_card_Panel2').show();
            $('#id_card_Panel3').show();
            $('#id_card_Panel4').hide();
            break;
        case 'Panel4':
            $('#id_form_photovoltaic_power_conditioner_efficiency_input').show();
            if ($('#id_photovoltaic_power_conditioner_efficiency_input').is(':checked')) {
                $('#id_form_photovoltaic_power_conditioner_efficiency').show();
            } else {
                $('#id_form_photovoltaic_power_conditioner_efficiency').hide();
            }
            $('#id_card_Panel1').show();
            $('#id_card_Panel2').show();
            $('#id_card_Panel3').show();
            $('#id_card_Panel4').show();
            break;
        case 'NotInstalled':
            $('#id_form_photovoltaic_power_conditioner_efficiency_input').hide();
            $('#id_form_photovoltaic_power_conditioner_efficiency').hide();
            $('#id_card_Panel1').hide();
            $('#id_card_Panel2').hide();
            $('#id_card_Panel3').hide();
            $('#id_card_Panel4').hide();
            break;
        default:
            console.log(photovoltaic);
    }

});

$("#id_photovoltaic").change(function () {
    var photovoltaic = $(this).val();

    $('#id_form_photovoltaic_power_conditioner_efficiency_input').hide();
    $('#id_form_photovoltaic_power_conditioner_efficiency').hide();
    $('#id_card_Panel1').hide();
    $('#id_card_Panel2').hide();
    $('#id_card_Panel3').hide();
    $('#id_card_Panel4').hide();

    switch (photovoltaic) {
        case 'Panel1':
            $('#id_form_photovoltaic_power_conditioner_efficiency_input').show();
            if ($('#id_photovoltaic_power_conditioner_efficiency_input').is(':checked')) {
                $('#id_form_photovoltaic_power_conditioner_efficiency').show();
            } else {
                $('#id_form_photovoltaic_power_conditioner_efficiency').hide();
            }
            $('#id_card_Panel1').show();
            $('#id_card_Panel2').hide();
            $('#id_card_Panel3').hide();
            $('#id_card_Panel4').hide();
            break;
        case 'Panel2':
            $('#id_form_photovoltaic_power_conditioner_efficiency_input').show();
            if ($('#id_photovoltaic_power_conditioner_efficiency_input').is(':checked')) {
                $('#id_form_photovoltaic_power_conditioner_efficiency').show();
            } else {
                $('#id_form_photovoltaic_power_conditioner_efficiency').hide();
            }
            $('#id_card_Panel1').show();
            $('#id_card_Panel2').show();
            $('#id_card_Panel3').hide();
            $('#id_card_Panel4').hide();
            break;
        case 'Panel3':
            $('#id_form_photovoltaic_power_conditioner_efficiency_input').show();
            if ($('#id_photovoltaic_power_conditioner_efficiency_input').is(':checked')) {
                $('#id_form_photovoltaic_power_conditioner_efficiency').show();
            } else {
                $('#id_form_photovoltaic_power_conditioner_efficiency').hide();
            }
            $('#id_card_Panel1').show();
            $('#id_card_Panel2').show();
            $('#id_card_Panel3').show();
            $('#id_card_Panel4').hide();
            break;
        case 'Panel4':
            $('#id_form_photovoltaic_power_conditioner_efficiency_input').show();
            if ($('#id_photovoltaic_power_conditioner_efficiency_input').is(':checked')) {
                $('#id_form_photovoltaic_power_conditioner_efficiency').show();
            } else {
                $('#id_form_photovoltaic_power_conditioner_efficiency').hide();
            }
            $('#id_card_Panel1').show();
            $('#id_card_Panel2').show();
            $('#id_card_Panel3').show();
            $('#id_card_Panel4').show();
            break;
        case 'NotInstalled':
            $('#id_form_photovoltaic_power_conditioner_efficiency_input').hide();
            $('#id_form_photovoltaic_power_conditioner_efficiency').hide();
            $('#id_card_Panel1').hide();
            $('#id_card_Panel2').hide();
            $('#id_card_Panel3').hide();
            $('#id_card_Panel4').hide();
            break;
        default:
            console.log(photovoltaic);
    }

});

$('#id_photovoltaic_power_conditioner_efficiency_input').change(function () {
    var efficiency_input = $(this).is(':checked');
    if (efficiency_input) {
        $('#id_form_photovoltaic_power_conditioner_efficiency').show();
    } else {
        $('#id_form_photovoltaic_power_conditioner_efficiency').hide();
    }
    //console.log(efficiency_input);
});
