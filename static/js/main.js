$(document).ready(function () {

    // Najbl nagravÅ¾na koda, ki sem jo sproduciral. Ne preveÄ spreminjat xD

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    //console.log(csrftoken);
    var student_id = null;
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });

    $("#create_modal").click(function() {
        $(".ui.modal").modal('show');     
    });

    //pošlješ request z metodo DELETE na nek jeben naslov NAPRIMER /computer/1 
    $(".delete_computer").click(function() {
        var id = $(this).attr("data-id");
        console.log(id);
        $.ajax({
        url: '/computer/' + id,
        type: 'DELETE', 
        success: function(result)
        {
            location.reload();
        }
    });
    });
    

    
});