$(document).ready(function () {
    $('.navbtn').on('click', function () {
        $('.bar').toggleClass('animate');
        $('.mobile_bg').fadeToggle('fast');
    });



    $(window).scroll(function () {
        if ($(this).scrollTop() > 1) {
            $('.top').addClass("sticky");
        } else {
            $('.top').removeClass("sticky");
        }
    });

    $('.anim-banner').bxSlider({
        auto: true,
        mode: 'fade',
        pager: false,
        controls: false,

    });


    $('.video-slider').bxSlider({
        moveSlides: 1,
        controls: true,
        pager: true,
        infiniteLoop: false,
        touchEnabled: true,
    });
  
       $('.gallery_list').bxSlider({
        moveSlides: 1,
        controls: true,
        pager: true,
        infiniteLoop: false,
        touchEnabled: true,
    });

});

$(document).ready(function () {

    // Set trigger and container variables
    var trigger = $('.card , .thumbnail-trigger , #main_video'),
        container = $('.modal-content');

    // Fire on click
    trigger.on('click', function (e) {
        // Set $this for re-use. Set target from data attribute
        e.preventDefault();
        var $this = $(this),
            // target = $this.attr(id);
            target = $(this).attr('id');
        console.log(target);
        // Load target page into container
        // container.load('partials/' +target + '.html');
        container.load('static/ctm-iimb-red-theme/partials/overlay-content.html #' + target);
        $('.modal-bg').fadeIn('fast');
        $('.card_modal').fadeIn('fast');
        $('body').addClass('fixed');
        // Stop normal link behavior
        return false;
    });


    $('#videonews').on('click', function (e) {
        // Set $this for re-use. Set target from data attribute
        e.preventDefault();
        var $this = $(this),
            // target = $this.attr(id);
            target = $(this).attr('id');
        console.log(target);
        // Load target page into container
        container.load('static/ctm-iimb-red-theme/partials/video_news.html');
        $('.modal-bg').fadeIn('fast');
        $('.card_modal').fadeIn('fast');
        $('body').addClass('fixed');
        // Stop normal link behavior
        return false;
    });
    
    $('#gallery').on('click', function (e) {
        // Set $this for re-use. Set target from data attribute
        e.preventDefault();
        var $this = $(this),
            // target = $this.attr(id);
            target = $(this).attr('id');
        console.log(target);
        // Load target page into container
        container.load('static/ctm-iimb-red-theme/partials/gallery.html');
        $('.modal-bg').fadeIn('fast');
        $('.card_modal').fadeIn('fast');
        $('body').addClass('fixed');
        // Stop normal link behavior
        return false;
    });


    $(".modal_close , .modal-bg").on("click", function () {
        $('.modal-bg').hide(),
            $('.card_modal').hide(),
            $('body').removeClass('fixed');
        container.empty();
    });

    $(".info").on("click", function () {
        $('.more_info').toggle();
        $(this).toggleClass('up');

    });
    $(".question").on("click", function () {
        $(this).find('.answer').slideToggle();
        $(this).toggleClass('open');

    });
    $(".campus_connect_readmore").on("click", function (e) {
        $('.campus_connect_readmore_content').fadeToggle('fast');
        $(this).hide();
        e.preventDefault();
    });
    $(".admission_criteria_readmore").on("click", function (e) {
        $('.admission_criteria_content').fadeToggle('fast');
        e.preventDefault();
    });


    $(document).keydown(function (e) {
        if (e.keyCode == 27) {
            $('.modal-bg').fadeOut('fast');
            $('.card_modal').fadeOut('fast');
            $('body').removeClass('fixed');
            container.empty();
        }
    });

    $(".link_contact").click(function () {
        $('html, body').animate({
            scrollTop: $("footer").offset().top
        }, 2000);
    });
  
   var btn = $('#button');

  $(window).scroll(function() {
    if ($(window).scrollTop() > 300) {
      btn.addClass('show');
    } else {
      btn.removeClass('show');
    }
  });

  btn.on('click', function(e) {
    e.preventDefault();
    $('html, body').animate({scrollTop:0}, '300');
  });
  
  
  

});



enquire.register("screen and (min-width: 1025px)", {
    setup: function () {
        // Load in content via AJAX (just the once)
    },
    match: function () {
        $('.domain-slider').bxSlider({
            // minSlides :3,
            maxSlides: 4,
            moveSlides: 1,
            slideWidth: 190,
            slideMargin: 20,
            controls: true,
            pager: false,
            infiniteLoop: false,
            touchEnabled: false,
            hideControlOnEnd: true,
        });

    },
    unmatch: function () {
        // Hide sidebar
    }
});
$(document).ready(function () {
  $(".download_brochure").click(function (e) {
    e.preventDefault();
    $(".overlay").show();
    $(".overlay_bg").show();
    $("body").addClass("fixed");
  });
  $(".modal_close , .close_overlay , .btn-link").click(function () {
    $(".overlay").fadeOut();
    $(".overlay_bg").fadeOut();
    $("body").removeClass("fixed");
  });
});

