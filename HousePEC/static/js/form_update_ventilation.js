$(document).ready(function () {
    var ventilation_type = $('#id_ventilation_type').val();

    $('#id_form_ventilation_sfp').hide();
    $('#id_form_ventilation_efficiency').hide();
    $('#id_form_ventilation_heatexchanger').hide();
    $('#id_form_ventilation_heatexchanger_efficiency').hide();
    $('#id_form_ventilation_heatexchanger_bal').hide();
    $('#id_form_ventilation_heatexchanger_leak').hide();

    switch (ventilation_type) {
        case 'DuctVenitlation1':
            $('#id_ventilation_saving').empty();
            $('#id_ventilation_saving').append($('<option>').val('ThickDuctOnly').text('�a�̑����_�N�g���g�p����'));
            $('#id_ventilation_saving').append($('<option>').val('ThickDuctAndDCMotor').text('�a�̑����_�N�g���g�p���A����DC���[�^�[���̗p����'));
            $('#id_ventilation_saving').append($('<option>').val('SFP').text('�����d�͂���͂���'));
            $('#id_ventilation_saving').append($('<option>').val('None').text('�G�l���M�[�΍���w�肵�Ȃ�'));
            $('#id_ventilation_saving').val('ThickDuctAndDCMotor');
            $('#id_form_ventilation_efficiency').show();
            $('#id_form_ventilation_saving').show();
            $('#id_ventilation_heatexchanger').val('HeatExchanger')
            $('#id_form_ventilation_heatexchanger').show();
            $('#id_form_ventilation_heatexchanger_efficiency').show();
            $('#id_form_ventilation_heatexchanger_bal').show();
            $('#id_form_ventilation_heatexchanger_leak').show();
            break;
        case 'DuctVentilation2or3':
            $('#id_ventilation_saving').empty();
            $('#id_ventilation_saving').append($('<option>').val('ThickDuctOnly').text('�a�̑����_�N�g���g�p����'));
            $('#id_ventilation_saving').append($('<option>').val('ThickDuctAndDCMotor').text('�a�̑����_�N�g���g�p���A����DC���[�^�[���̗p����'));
            $('#id_ventilation_saving').append($('<option>').val('SFP').text('�����d�͂���͂���'));
            $('#id_ventilation_saving').append($('<option>').val('None').text('�G�l���M�[�΍���w�肵�Ȃ�'));
            $('#id_ventilation_saving').val('ThickDuctAndDCMotor');
            $('#id_form_ventilation_efficiency').hide();
            $('#id_form_ventilation_saving').show();
            break;
        case 'WallMount1':
            $('#id_ventilation_saving').empty();
            $('#id_ventilation_saving').append($('<option>').val('SFP').text('�����d�͂���͂���'));
            $('#id_ventilation_saving').append($('<option>').val('None').text('�G�l���M�[�΍���w�肵�Ȃ�'));
            $('#id_ventilation_saving').val('None');
            $('#id_form_ventilation_saving').show();
            $('#id_form_ventilation_efficiency').show();
            $('#id_ventilation_heatexchanger').val('HeatExchanger')
            $('#id_form_ventilation_heatexchanger').show();
            $('#id_form_ventilation_heatexchanger_efficiency').show();
            $('#id_form_ventilation_heatexchanger_bal').show();
            $('#id_form_ventilation_heatexchanger_leak').show();
            break;
        case 'WallMount2or3':
            $('#id_ventilation_saving').empty();
            $('#id_ventilation_saving').append($('<option>').val('SFP').text('�����d�͂���͂���'));
            $('#id_ventilation_saving').append($('<option>').val('None').text('�G�l���M�[�΍���w�肵�Ȃ�'));
            $('#id_ventilation_saving').val('None');
            $('#id_form_ventilation_efficiency').hide();
            $('#id_form_ventilation_saving').show();
            break;
        default:
            console.log(ventilation_type);
    }

});

$("#id_ventilation_type").change(function () {
    var ventilation_type = $(this).val();

    $('#id_form_ventilation_sfp').hide();
    $('#id_form_ventilation_efficiency').hide();
    $('#id_form_ventilation_heatexchanger').hide();
    $('#id_form_ventilation_heatexchanger_efficiency').hide();
    $('#id_form_ventilation_heatexchanger_bal').hide();
    $('#id_form_ventilation_heatexchanger_leak').hide();

    switch (ventilation_type) {
        case 'DuctVenitlation1':
            $('#id_ventilation_saving').empty();
            $('#id_ventilation_saving').append($('<option>').val('ThickDuctOnly').text('�a�̑����_�N�g���g�p����'));
            $('#id_ventilation_saving').append($('<option>').val('ThickDuctAndDCMotor').text('�a�̑����_�N�g���g�p���A����DC���[�^�[���̗p����'));
            $('#id_ventilation_saving').append($('<option>').val('SFP').text('�����d�͂���͂���'));
            $('#id_ventilation_saving').append($('<option>').val('None').text('�G�l���M�[�΍���w�肵�Ȃ�'));
            $('#id_ventilation_saving').val('ThickDuctAndDCMotor');
            $('#id_form_ventilation_efficiency').show();
            $('#id_form_ventilation_saving').show();
            $('#id_ventilation_heatexchanger').val('HeatExchanger')
            $('#id_form_ventilation_heatexchanger').show();
            $('#id_form_ventilation_heatexchanger_efficiency').show();
            $('#id_form_ventilation_heatexchanger_bal').show();
            $('#id_form_ventilation_heatexchanger_leak').show();
            break;
        case 'DuctVentilation2or3':
            $('#id_ventilation_saving').empty();
            $('#id_ventilation_saving').append($('<option>').val('ThickDuctOnly').text('�a�̑����_�N�g���g�p����'));
            $('#id_ventilation_saving').append($('<option>').val('ThickDuctAndDCMotor').text('�a�̑����_�N�g���g�p���A����DC���[�^�[���̗p����'));
            $('#id_ventilation_saving').append($('<option>').val('SFP').text('�����d�͂���͂���'));
            $('#id_ventilation_saving').append($('<option>').val('None').text('�G�l���M�[�΍���w�肵�Ȃ�'));
            $('#id_ventilation_saving').val('ThickDuctAndDCMotor');
            $('#id_form_ventilation_efficiency').hide();
            $('#id_form_ventilation_saving').show();
            break;
        case 'WallMount1':
            $('#id_ventilation_saving').empty();
            $('#id_ventilation_saving').append($('<option>').val('SFP').text('�����d�͂���͂���'));
            $('#id_ventilation_saving').append($('<option>').val('None').text('�G�l���M�[�΍���w�肵�Ȃ�'));
            $('#id_ventilation_saving').val('None');
            $('#id_form_ventilation_saving').show();
            $('#id_form_ventilation_efficiency').show();
            $('#id_ventilation_heatexchanger').val('HeatExchanger')
            $('#id_form_ventilation_heatexchanger').show();
            $('#id_form_ventilation_heatexchanger_efficiency').show();
            $('#id_form_ventilation_heatexchanger_bal').show();
            $('#id_form_ventilation_heatexchanger_leak').show();
            break;
        case 'WallMount2or3':
            $('#id_ventilation_saving').empty();
            $('#id_ventilation_saving').append($('<option>').val('SFP').text('�����d�͂���͂���'));
            $('#id_ventilation_saving').append($('<option>').val('None').text('�G�l���M�[�΍���w�肵�Ȃ�'));
            $('#id_ventilation_saving').val('None');
            $('#id_form_ventilation_efficiency').hide();
            $('#id_form_ventilation_saving').show();
            break;
        default:
            console.log(ventilation_type);
    }

});

$("#id_ventilation_saving").change(function () {
    var ventilation_saving = $(this).val();

    $('#id_form_ventilation_sfp').hide();
    if (ventilation_saving === 'SFP') {
        $('#id_form_ventilation_sfp').show();
    }

});

$("#id_ventilation_heatexchanger").change(function () {
    var ventilation_heatexchanger = $(this).val();

    switch (ventilation_heatexchanger) {
        case 'HeatExchanger':
            $('#id_form_ventilation_heatexchanger').show();
            $('#id_form_ventilation_heatexchanger_efficiency').show();
            $('#id_form_ventilation_heatexchanger_bal').show();
            $('#id_form_ventilation_heatexchanger_leak').show();
            break;
        case 'None':
            $('#id_form_ventilation_heatexchanger').show();
            $('#id_form_ventilation_heatexchanger_efficiency').hide();
            $('#id_form_ventilation_heatexchanger_bal').hide();
            $('#id_form_ventilation_heatexchanger_leak').hide();
            break;
        default:
            console.log(ventilation_heatexchanger);
    }

});

