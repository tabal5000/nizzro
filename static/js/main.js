$(document).ready(function () {

    // Najbl nagravÅ¾na koda, ki sem jo sproduciral. Ne preveÄ spreminjat xD
    eventTarget = null;

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
        $(".add-modal").modal('show');     
    });


    // $(".edit_computer").click(function() {
    //     $(".edit-modal").modal('show'); 
    //     eventTarget = $(event.relatedTarget);
    //     console.log(eventTarget);
    //     var computer_id = $(event.relatedTarget).data('id');
    //     var url = 'api/computer/' + computer_id;
    //     $("#edit_form").attr("action", url);
    //     $.get(url, function () {})
    //         .done(function (response) {
    //             data = response;
    //             console.log(data);
    //             // var letnik = parseInt(data['letnik'])
    //             // if (letnik == 3) {
    //             //     $("[id=id_pravica_izbire]:eq(1)").css("display", "block");
    //             //     $("[id=pravicaLabel]:eq(1)").css("display", "block");
    //             //     if (data['pravica_izbire'] == true) {
    //             //         $("[id=id_pravica_izbire]:eq(1)").prop('checked', true);
    //             //     }
    //             // } else {
    //             //     $("[id=id_pravica_izbire]:eq(1)").css("display", "none");
    //             //     $("[id=pravicaLabel]:eq(1)").css("display", "none");
    //             //     $("[id=id_pravica_izbire]:eq(1)").prop('checked', false);
    //             // }
    //             // $("[id=id_smer]:eq(1)").val(data['smer']);
    //             // $("[id=id_letnik]:eq(1)").val(letnik);
    //             // $("[id=id_vrsta]:eq(1)").val(data['vrsta']);
    //             // $("[id=id_nacin]:eq(1)").val(data['nacin']);
    //             // $("[id=id_oblika]:eq(1)").val(data['oblika']);
    //         })
    //         .fail(function () {
    //             console.log('boo');
    //             // $("#id_smer option")[0].selected = true;
    //             // $('#id_letnik option')[0].selected = true;
    //             // $("#id_letnik option")[0].selected = true;
    //             // $("#id_vrsta option")[0].selected = true;
    //             // $("#id_nacin option")[0].selected = true;
    //             // $("#id_oblika option")[0].selected = true;
    //             // $("#pravicaLabel").css("display", "none");
    //             // $("#id_pravica_izbire").css("display", "none");
    //         });
    // });

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