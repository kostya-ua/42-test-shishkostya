var reader = new FileReader();

reader.onloadend = function(e) {
    $('.preview').attr('src',  e.target.result);
};

$( document ).ready(function(){
    $('#id_photo').change(function() {
        var imageFile = document.getElementById('id_photo').files[0];
        reader.readAsDataURL(imageFile);
    });
});