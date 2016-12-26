$('button').bind('click', function(event){
  event.preventDefault();
   $(this).attr('disabled', 'disabled');
   setTimeout(enableButton, 600000);
   var element = $(this);
   var enableButton = function(){
   $('#button').removeAttr('disabled');
}


    $.ajax({
        url : '/like_art/',
        type : 'POST',
        data : { arts_id : $(this).attr("data-id")},

        success : function(data){
            element.html(' ' + data);
        }
    });
});


// You need these methods to add the CSRF token using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
