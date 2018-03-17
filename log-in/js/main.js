
(function ($) {
    "use strict";

    
    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');

    $('.validate-form').on('submit',function(){
        var check = true;

        for(var i=0; i<input.length; i++) {
            if(validate(input[i]) == false){
                showValidate(input[i]);
                check=false;
            }
        }

        return check;
    });


    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
        });
    });

    function validate (input) {
        if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        else {
            if($(input).val().trim() == ''){
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }
    
    

})(jQuery);

$("#sign").click(function() {
    var a = document.getElementById("sign-form");
    a.style.left = 'auto';

    var b = document.getElementById("log-form");
    b.style.display = 'none';
});

$("#log").click(function() {
    var a = document.getElementById("sign-form");
    a.style.left = '-960px';

    var b = document.getElementById("log-form");
    b.style.display = '';
});

$("#login-btn").click(function() {
    var a = document.getElementById("log-form");
    a.style.display = 'none';

    var c = document.getElementsByClassName("two-fact");
    c[0].style.display = 'block';
});

$("#signup-btn").click(function() {
    var a = document.getElementById("sign-form");
    a.style.display = 'none';
    
    var c = document.getElementById("sign-form-2");
    c.style.display = 'block';
});

$("#signup-btn2").click(function() {
    var a = document.getElementById("sign-form-2");
    a.style.display = 'none';

    var c = document.getElementById("sign-form-3");
    c.style.display = 'block';
});

$("#signup-btn3").click(function() {
    var a = document.getElementById("sign-form-3");
    a.style.display = 'none';

    var c = document.getElementsByClassName("two-fact");
    c[0].style.display = 'block';
});