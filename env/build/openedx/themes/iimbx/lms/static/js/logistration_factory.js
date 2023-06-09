(function(define) {
    'use strict';
    define([
        'jquery',
        currentTheme + 'js/student_account/views/AccessView'
    ],
        function($, AccessView) {
            return function(options) {
                var $logistrationElement = $('#login-and-registration-container');

                new AccessView(_.extend(options, {el: $logistrationElement}));
            };
        }
    );
}).call(this, define || RequireJS.define);
