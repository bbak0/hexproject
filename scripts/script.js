$('.arrow').click(function() {
    
    $('html, body').animate({
        scrollTop: $("#features").offset().top
    }, 300);

    return false;
});

// $('.more-btn').click(function() {
//     $(this).parents('.over').find('.full-article').css('margin-top', '0');
//     $(this).parents('.over').find('.article-top').css('visibility', 'hidden');
//     $(this).parents('.over').find('.article-bot').css('visibility', 'hidden');

//     $(this).parents('.over').find('.more-btn').css('visibility', 'hidden');
//     $(this).parents('.over').find('.close-btn').css('visibility', 'visible');
// });

// $('.close-btn').click(function() {
//     $(this).parents('.over').find('.full-article').css('margin-top', '-375px');
//     $(this).parents('.over').find('.article-top').css('visibility', 'visible');
//     $(this).parents('.over').find('.article-bot').css('visibility', 'visible');

//     $(this).parents('.over').find('.more-btn').css('visibility', 'visible');
//     $(this).parents('.over').find('.close-btn').css('visibility', 'hidden');
// });


// function toggleSignup() {
//     document.getElementById("login-toggle").style.backgroundColor = "#fff";
//     document.getElementById("login-toggle").style.color = "#434A54";
//     document.getElementById("signup-toggle").style.backgroundColor = "#0099d0";
//     document.getElementById("signup-toggle").style.color = "#fff";
//     document.getElementById("login-form").style.display = "none";
//     document.getElementById("signup-form").style.display = "block";

//     document.getElementById("cross").style.color = "#fff";
// }
  
// function toggleLogin() {
//     document.getElementById("login-toggle").style.backgroundColor = "#0099d0";
//     document.getElementById("login-toggle").style.color = "#fff";
//     document.getElementById("signup-toggle").style.backgroundColor = "#fff";
//     document.getElementById("signup-toggle").style.color = "#434A54";
//     document.getElementById("signup-form").style.display = "none";
//     document.getElementById("login-form").style.display = "block";

//     document.getElementById("cross").style.color = "#434A54";
// }
  
// $('#nav-login').click(function() {
//     document.getElementById("modal-absolute").style.display = "block";

//     document.getElementById("login-toggle").style.backgroundColor = "#0099d0";
//     document.getElementById("login-toggle").style.color = "#fff";
//     document.getElementById("signup-toggle").style.backgroundColor = "#fff";
//     document.getElementById("signup-toggle").style.color = "#434A54";
//     document.getElementById("signup-form").style.display = "none";
//     document.getElementById("login-form").style.display = "block";

//     document.getElementById("cross").style.color = "#434A54";
// });

// $('#nav-signup').click(function() {
//     document.getElementById("modal-absolute").style.display = "block";

//     document.getElementById("login-toggle").style.backgroundColor = "#fff";
//     document.getElementById("login-toggle").style.color = "#434A54";
//     document.getElementById("signup-toggle").style.backgroundColor = "#0099d0";
//     document.getElementById("signup-toggle").style.color = "#fff";
//     document.getElementById("login-form").style.display = "none";
//     document.getElementById("signup-form").style.display = "block";

//     document.getElementById("cross").style.color = "#fff";
// });

// $('#ready').click(function() {
//     document.getElementById("modal-absolute").style.display = "block";

//     document.getElementById("login-toggle").style.backgroundColor = "#0099d0";
//     document.getElementById("login-toggle").style.color = "#fff";
//     document.getElementById("signup-toggle").style.backgroundColor = "#fff";
//     document.getElementById("signup-toggle").style.color = "#434A54";
//     document.getElementById("signup-form").style.display = "none";
//     document.getElementById("login-form").style.display = "block";
// });

// $('#cross').click(function() {
//     document.getElementById("modal-absolute").style.display = "none";
// });


