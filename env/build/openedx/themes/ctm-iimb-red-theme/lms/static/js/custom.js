$('.main-header.not_authenticated').addClass('top');
$('div.open-response-assessment-summary').addClass("table-responsive");
$('div.open-response-assessment-main-table').addClass("table-responsive");
$('div.white-listed-students').addClass("table-responsive");
$(".view-in-course.view-instructordash div.staff_info").addClass("table-responsive");
$(".view-statictab div.xblock.xblock-student_view.xblock-student_view-static_tab.xmodule_display").addClass("table-responsive");


jQuery(document).ready(function(){

    //2 lines tab script
    if($('.catalog_tabpage').length){
        var tab_height = $('.catalog_tab_header').outerHeight();
        $('.cource-section.catalog-tabs-section.catalog_tabpage').css('margin-top', '-' +  (tab_height + 6) + 'px');
        $('.catalog-tabs-section .cource-heading').css('margin-top',+ (tab_height + 6) + 'px');
         $(window).resize(function(){
            var tab_height = $('.catalog_tab_header').outerHeight();
            $('section.catalog-tabs-section').css('margin-top', '-' +  (tab_height + 6) + 'px');
            $('.catalog-tabs-section .cource-heading').css('margin-top',+ (tab_height + 6) + 'px');
        });    
    }


    if($('.contact-wrap-sec').length){
        var _left = $(".main-header .container").offset().left + 15; 
        $('.contact-wrap-sec .landing-wrap').css("left", + _left +"px");
        $(window).resize(function(){
            var _left = $(".main-header .container").offset().left + 15; 
            $('.contact-wrap-sec .landing-wrap').css("left", + _left +"px");
        }); 
    }            

    //addd script for scrollbar on right sidebar

    $('.panel-default > .panel-heading a').click(function(){
        $(this).parent('.panel-heading').toggleClass('active');
    });

    function showLess(){
        $('.show-less').show();
        $('.all-expand').hide();

        jQuery(".panel-body ul").removeClass('opensub');
        jQuery('.panel-body ul').next("ul").addClass('opensub');
        jQuery('.panel-body a.sub-list').addClass('active');
    }
    function showExpand(){

        $('.show-less').hide();
        $('.all-expand').show();

        //sub menu script
        jQuery(".panel-body ul").removeClass('opensub');
        jQuery('.panel-body ul').next("ul").addClass('opensub');
        jQuery('.panel-body a.sub-list').addClass('active');
    }

    if($('.course_accordian').length){
        $('.panel-heading').on("click",function(){
            if(jQuery(this).next(".panel-collapse").is(":visible")){
                //jQuery(".panel .panel-collapse").removeClass('opensub');
                jQuery(this).next(".panel-collapse").removeClass('opensub');
                if($(".panel-collapse").is(":visible") == false){
                    showExpand();
                    //sub menu script

                }else{
                    showLess();

                    //sub menu script
                    jQuery(".panel-body ul").addClass('opensub');
                    jQuery('.panel-body a.sub-list').addClass('active');
                }
            }
            else
            {

                jQuery(".panel .panel-collapse").removeClass('opensub');
                jQuery(this).next(".panel .panel-collapse").addClass('opensub');
                showLess();

                //sub menu script
                //jQuery(".panel-body ul").removeClass('opensub');
                jQuery('.panel-body a.sub-list').removeClass('active');
                jQuery('.panel-default .panel-heading').removeClass('active');
                jQuery(this).addClass('active');
            }
        });
    }
           
    //addd script for scrollbar on right sidebar                  
    if($('.custom-scrollbar').length){
        $('.custom-scrollbar').scrollBox();
    }

    $('.all-expand').on("click",function(e) {
        jQuery(".panel .panel-collapse").addClass('opensub');
        $('.panel-default .panel-heading').addClass('active');
        //sub menu script
        jQuery('.panel-body ul').addClass('opensub');
        jQuery('.panel-body a.sub-list').addClass('active');    

        
        $('.show-less').show();
        $('.all-expand').hide();


    });

    $('.show-less').on("click", function() {
        $('.show-less').hide();
        $('.all-expand').show();
        $(".panel .panel-collapse").removeClass('opensub');
        $('.panel-default .panel-heading').removeClass('active');
        //sub menu script
        jQuery('.panel-body ul').removeClass('opensub');
        jQuery('.panel-body a.sub-list').removeClass('active');
    });   

    //===========fixed footer
    if($('.footer_wrap').length){
        fixed_footer_function('.footer_wrap','.wrap-inner');
        $(window).resize(function(){
            fixed_footer_function('.footer_wrap','.wrap-inner');
        });
    }

    //footer fixed bottom script
    function fixed_footer_function(_footer,_maincontent){
        var _footer = $(_footer).outerHeight();
        var _window_height = $(window).height();
        var _count_height = _window_height - _footer;
        $(_maincontent).css("min-height",+ _count_height);
    }


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

    //Profile menu dropdown custom toggle script
    if($('.btn-profile').length){
        $("header .btn-profile").on('click',function(e){
            e.preventDefault();
            e.stopPropagation();
            $(this).parent('.profile-dropdown').toggleClass('open');
            $(document).one('click',function closeMenu(e){
                if($(".profile-dropdown-menu").has(e.target).length == 0)
                {
                    $(".profile-dropdown").toggleClass('open');
                }else{$(document).one('click',closeMenu);}
            });
        });
    }

    //menu custom toggle script
    if($('header').length){
        $("header .iimbx-toggle").on('click',function(e){
            e.preventDefault();
            e.stopPropagation();
            $(".iimbxCollapse-collapse").slideToggle();
            $(document).one('click',function closeMenu(e){
                if($(".iimbxCollapse-collapse").has(e.target).length == 0)
                {
                    $(".iimbxCollapse-collapse").slideUp();
                }else{$(document).one('click',closeMenu);}
            });
        });
    }


    //equal height catalog title
    if($('.catalog_grid').length){
        $('.catalog_grid .catalog_info').matchHeight();
    }
    if($('.mycourse_grid_sec').length){
        $('.mycourse_grid_sec .mycourse_block').matchHeight();
    }

    


     /*=======Yoga Page Slider Script========*/
    if($('.about_slider').length){
        $('.about_slider').slick({
            infinite: true,
            arrows:true,
            dots:true,
            fade: false,
            items:1,
            speed: 500,
            prevArrow:false,
            nextArrow:false,
            slidesToScroll:1,
            autoplay:false,
        });
    }

     //sub menu  dropdown responsive script

    if($('.main-header li.has-child').length){
        $('.main-header li.has-child a').next('ul.sub-menu').before('<i class="fa fa-angle-down"></i>');
        $(".main-header ul li > .fa").click(function(){
          $(this).next().slideToggle('slow');
          $(this).toggleClass('fa-angle-up').toggleClass('fa-angle-down');
          $(this).parent().siblings().children('.fa').next().slideUp('slow');
          $(this).parent().siblings().children('.fa').next().parents('li').find('.fa').removeClass('fa-angle-up').addClass('fa-angle-down');
        });
    }
    //script for login page half class window width height by jquery
    var _wh = $(window).height();
    if($('.landing_section').length){
        $('.col-half').css('height',+ _wh);
        $(window).resize(function(){
            var _wh = $(window).height();
            $('.col-half').css('height',+ _wh);
        });
    }       
    if($('.slider_landing').length){
        $('.slider_landing').slick({
          dots: true,
          infinite: true,
          autoplay: true,
          autoplaySpeed: 5000,
          speed: 300,
          slidesToShow: 1,
          prevArrow: false,
          nextArrow: false
        });
    }


  });
jQuery('.course_accordian_section .panel-body a.sub-list').on('click',function(e){
    e.preventDefault();
    e.stopPropagation();
    var tabClass = jQuery(this).attr('data-liid');
    var temp = tabClass + "_count";
    if(jQuery(this).parent('.small-contnet').find('.'+temp).is(':visible')){
        jQuery(this).removeClass('active');
        //jQuery('.panel-default .panel-body ul').removeClass('opensub');
        jQuery(this).parent('.small-contnet').find('.'+temp).removeClass('opensub');
    }else{       
        jQuery('.panel-default .panel-body a').removeClass('active');   
        jQuery(this).parent('.small-contnet').parent('.panel-body').find('ul').removeClass('opensub');
        jQuery(this).addClass('active');
        jQuery(this).parent('.small-contnet').find('.'+temp).addClass('opensub');
    }
}); 
    


$(window).scroll(function() {
if ($(this).scrollTop() > 1){
    $('.top').addClass("sticky");
  }
  else{
    $('.top').removeClass("sticky");
  }
});

$(document).ready(function(){
    var url = window.location.href;
    if(url.indexOf('login') != -1){
        $('header.main-header').removeClass('top');
    }
});
//For login page contact animation
$(".link_contact").click(function() {
    $('html, body').animate({
        scrollTop: $("footer").offset().top
    }, 2000);
});
