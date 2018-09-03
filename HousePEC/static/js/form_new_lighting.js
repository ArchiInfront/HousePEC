
$(document).ready(function () {
    var ldk_lighting = $("#id_ldk_lighting").val();

    switch (ldk_lighting) {
        case 'LowEfficiency':
            $('#id_form_ldk_multi').hide();
            $('#id_form_ldk_dimming').show();
            break;
        case 'HighEfficiency':
        case 'LED':
            $('#id_form_ldk_multi').show();
            $('#id_form_ldk_dimming').show();
            break;
        case 'NotInstalled':
            $('#id_form_ldk_multi').hide();
            $('#id_form_ldk_dimming').hide();
            break;
        default:
            console.log(ldk_lighting);
    }

    var oth_lighting = $("#id_oth_lighting").val();

    switch (oth_lighting) {
        case 'LowEfficiency':
        case 'HighEfficiency':
        case 'LED':
            $('#id_form_oth_dimming').show();
            break;
        case 'NotInstalled':
            $('#id_form_oth_dimming').hide();
            break;
        default:
            console.log(oth_lighting);
    }

    var nonldk_lighting = $("#id_nonldk_lighting").val();

    switch (nonldk_lighting) {
        case 'LowEfficiency':
        case 'HighEfficiency':
        case 'LED':
            $('#id_form_nonldk_sensor').show();
            break;
        case 'NotInstalled':
            $('#id_form_nonldk_sensor').hide();
            break;
        default:
            console.log(nonldk_lighting);
    }

});

$("#id_ldk_lighting").change(function () {
    var ldk_lighting = $(this).val();

    switch (ldk_lighting) {
        case 'LowEfficiency':
            $('#id_form_ldk_multi').hide();
            $('#id_form_ldk_dimming').show();
            break;
        case 'HighEfficiency':
        case 'LED':
            $('#id_form_ldk_multi').show();
            $('#id_form_ldk_dimming').show();
            break;
        case 'NotInstalled':
            $('#id_form_ldk_multi').hide();
            $('#id_form_ldk_dimming').hide();
            break;
        default:
            console.log(ldk_lighting);
    }

});

$("#id_oth_lighting").change(function () {
    var oth_lighting = $(this).val();

    switch (oth_lighting) {
        case 'LowEfficiency':
        case 'HighEfficiency':
        case 'LED':
            $('#id_form_oth_dimming').show();
            break;
        case 'NotInstalled':
            $('#id_form_oth_dimming').hide();
            break;
        default:
            console.log(oth_lighting);
    }

});

$("#id_nonldk_lighting").change(function () {
    var nonldk_lighting = $(this).val();

    switch (nonldk_lighting) {
        case 'LowEfficiency':
        case 'HighEfficiency':
        case 'LED':
            $('#id_form_nonldk_sensor').show();
            break;
        case 'NotInstalled':
            $('#id_form_nonldk_sensor').hide();
            break;
        default:
            console.log(nonldk_lighting);
    }

});

