$(document).ready(function(){
    // To add forbidden message on login page (in the end).
    var login_message = '<section class="outside-app error-page login-message">' +
              '<div class="error-content">' +
              '<p>Currently IIMBx allows login access only using credentials provided by IIMBx to your email. If you are interested to know more or have not received your credentials please write to us at ' +
              '<a href="mailto:digital.learning@iimbx.edu.in">digital.learning@iimbx.edu.in</a></p>'+
              '<p>Go back to the <a href="/">IIMBx homepage.</a></p>' +
            '</div>' +
          '</section>';
    
    $("#login-tpl").append(login_message);

    
    // To add forbidden message register page.
    var reg_message = '<section class="outside-app error-page">' +
        '<div class="error-content">' +
        '<h1>Account creation not allowed.</h1>' +
        '<p>Currently IIMBx allows login access only using credentials provided by IIMBx to your email. If you are interested to know more or have not received your credentials please write to us at' +
        '<a href="mailto:digital.learning@iimbx.edu.in">digital.learning@iimbx.edu.in</a></p>'+
        '<p>Go back to the <a href="/">IIMBx homepage.</a></p>' +
      '</div>' +
    '</section>';
    
    $("#register-tpl").prepend(reg_message);
});