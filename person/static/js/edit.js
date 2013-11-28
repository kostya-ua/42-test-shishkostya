var reader = new FileReader();

reader.onloadend = function(e) {
    $('.preview').attr('src',  e.target.result);
};

$( document ).ready(function(){
    $('#id_photo').change(function() {
        var imageFile = document.getElementById('id_photo').files[0];
        reader.readAsDataURL(imageFile);
    });

    var options = {
        target:        '.output',
        beforeSubmit:  disableForm,
        success:       successResponse,
    };


    $('.edit_form').submit(function() {
        $(this).ajaxSubmit(options);

        return false;
    });
});


function disableForm(data, jqForm, options) {
    $('.edit_form input').prop('disabled', true);
    $('.edit_form textarea').prop('disabled', true);
    $('.loader').show();

    $('input').parents('p').prev().html('');
    $('textarea').parents('p').prev().html('');

    return true;
}


function successResponse(data, status, xhr, $form)  {
    $('.edit_form input').prop('disabled', false);
    $('.edit_form textarea').prop('disabled', false);
    $('.loader').hide();

    if (data.errors){
        for (field in data.errors){
            error = data.errors[field][0];
            $('#id_'+field).parents('p').prev().html('<ul class="error"><li>'+error+'</li></ul>');
        }
    }
}
