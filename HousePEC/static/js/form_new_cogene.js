$(document).ready(function () {
    var cogene = $("#id_cogene").val();

    $('#id_form_cogene_type').hide();
    $('#id_card_cogene_PEFC').hide();
    $('#id_card_cogene_SOFC').hide();
    $('#id_card_cogene_unit_powerunit_2015').hide();

    switch (cogene) {
        case 'Installed':
            $('#id_form_cogene_type').show();
            $('#id_card_cogene_PEFC').hide();
            $('#id_card_cogene_SOFC').hide();
            $('#id_card_cogene_unit_powerunit_2015').show();
            break;
        case 'NotInstalled':
            $('#id_form_cogene_type').hide();
            $('#id_card_cogene_PEFC').hide();
            $('#id_card_cogene_SOFC').hide();
            $('#id_card_cogene_unit_powerunit_2015').hide();
            break;
        default:
            console.log(cogene);
    }

});

$("#id_cogene").change(function () {
    var cogene = $(this).val();

    $('#id_form_cogene_type').hide();
    $('#id_card_cogene_PEFC').hide();
    $('#id_card_cogene_SOFC').hide();
    $('#id_card_cogene_unit_powerunit_2015').hide();

    switch (cogene) {
        case 'Installed':
            $('#id_form_cogene_type').show();
            $('#id_card_cogene_PEFC').hide();
            $('#id_card_cogene_SOFC').hide();
            $('#id_card_cogene_unit_powerunit_2015').show();
            break;
        case 'NotInstalled':
            $('#id_form_cogene_type').hide();
            $('#id_card_cogene_PEFC').hide();
            $('#id_card_cogene_SOFC').hide();
            $('#id_card_cogene_unit_powerunit_2015').hide();
            break;
        default:
            console.log(cogene);
    }

});

$("#id_cogene_type").change(function () {
    var cogene_type = $(this).val();

    $('#id_card_cogene_PEFC').hide();
    $('#id_card_cogene_SOFC').hide();
    $('#id_card_cogene_unit_powerunit_2015').hide();

    switch (cogene_type) {
        case 'PEFC':
            $('#id_card_cogene_PEFC').show();
            $('#id_card_cogene_SOFC').hide();
            $('#id_card_cogene_unit_powerunit_2015').hide();
            break;
        case 'SOFC':
            $('#id_card_cogene_PEFC').hide();
            $('#id_card_cogene_SOFC').show();
            $('#id_card_cogene_unit_powerunit_2015').hide();
            break;
        case 'Before2015':
            $('#id_card_cogene_PEFC').hide();
            $('#id_card_cogene_SOFC').hide();
            $('#id_card_cogene_unit_powerunit_2015').show();
            break;
        default:
            console.log(cogene_type);
    }

});

$('#id_cogene_PEFC_input').change(function () {
    var cogene_PEFC_input = $(this).is(':checked');
    if (cogene_PEFC_input) {
        $('#id_form_cogene_powerunit_PEFC').show();
        $('#id_form_cogene_tankunit_PEFC').show();
        $('#id_form_cogene_backupboiler_PEFC').show();
    } else {
        $('#id_form_cogene_powerunit_PEFC').hide();
        $('#id_form_cogene_tankunit_PEFC').hide();
        $('#id_form_cogene_backupboiler_PEFC').hide();
    }
    //console.log(efficiency_input);
});

$('#id_cogene_SOFC_input').change(function () {
    var cogene_SOFC_input = $(this).is(':checked');
    if (cogene_SOFC_input) {
        $('#id_form_cogene_powerunit_SOFC').show();
        $('#id_form_cogene_tankunit_SOFC').show();
        $('#id_form_cogene_backupboiler_SOFC').show();
    } else {
        $('#id_form_cogene_powerunit_SOFC').hide();
        $('#id_form_cogene_tankunit_SOFC').hide();
        $('#id_form_cogene_backupboiler_SOFC').hide();
    }
    //console.log(efficiency_input);
});

