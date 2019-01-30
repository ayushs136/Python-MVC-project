$(document).ready(function () {
    console.log("loaded");
    $.material.init();
    $(document).on("submit", "#registration-form", function (e) {
        e.preventDefault();
        var form = $('#registration-form').serialize();
        $.ajax({
            url: '/postregistration',
            type: 'POST',
            data: form,
            success: function (response) {
                console.log(response);
                alert("Registration Successful!")
            }
        });
    });


    $(document).on('submit', '#login-form', function (e) {
       e.preventDefault();

       var form = $(this).serialize();
       $.ajax({
           url: '/check-login',
           type: 'POST',
           data: form,
           success: function (res) {
               if(res == "error"){
                   alert("Could not log in...");
               }else{
                   console.log("logged in as ", res);
                   window.location.href = '/'
               }
           }
       })
    });

    $(document).on('click', '#logout-link', function (e) {
       e.preventDefault();
       $.ajax({
           url: '/logout',
           type: 'GET',
           success: function (res) {
               if (res == "Logout Success"){
                   window.location.href = '/login';
               }else{
                   alert("Something went Wrong...");
               }

           }
       })
    });

});