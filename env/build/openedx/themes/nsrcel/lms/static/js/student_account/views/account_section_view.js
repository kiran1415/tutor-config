(function(define, undefined) {
    'use strict';
    define([
        'gettext',
        'jquery',
        'underscore',
        'backbone',
        'edx-ui-toolkit/js/utils/html-utils',
        'text!' + currentTheme + 'templates/student_account/account_settings_section.underscore'
    ], function(gettext, $, _, Backbone, HtmlUtils, sectionTemplate) {
        var AccountSectionView = Backbone.View.extend({

            initialize: function(options) {
                this.options = options;
                _.bindAll(this, 'render', 'renderFields');
            },

            render: function() {
                this.$el.html(_.template(sectionTemplate)({
                    HtmlUtils: HtmlUtils,
                    sections: this.options.sections,
                    tabName: this.options.tabName,
                    tabLabel: this.options.tabLabel
                }));

                this.renderFields();
            },

            renderFields: function() {
                var view = this;

                _.each(view.$('.' + view.options.tabName + '-section-body'), function(sectionEl, index) {
                    _.each(view.options.sections[index].fields, function(field) {
                        $(sectionEl).append(field.view.render().el);
                    });
                });
                this.postRender();
                return this;
            },
            postRender: function(){
                //script for floating label on input enter
             	var $inputItem = $(".input-label");
                $inputItem.length && $inputItem.each(function() {
                    var $this = $(this),
                    $input = $this.find(".form-control"),
                    placeholderTxt = $input.attr("placeholder"),
                    $placeholder;

                    $input.after('<span class="placeholder">' + placeholderTxt + "</span>"),
                    $input.attr("placeholder", ""),
                    $placeholder = $this.find(".placeholder"),
                    $input.val().length ? $this.addClass("active") : $this.removeClass("active"),
                    $input.on("focusout", function() {
                        $input.val().length ? $this.addClass("active") : $this.removeClass("active");
                    }).on("focus", function() {
                        $this.addClass("active");
                    });
                });
            }
        });

        return AccountSectionView;
    });
}).call(this, define || RequireJS.define);
