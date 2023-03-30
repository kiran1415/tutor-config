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

  $(".link_contact").click(function () {
    $('html, body').animate({
      scrollTop: $("footer").offset().top
    }, 2000);
  });
  $(".link_iimbx").click(function () {
    var x = $('.iimbx_section').offset().top;
    $('html,body').animate({
      scrollTop: x - 100
    }, 1000);

  });

  $(".dropdown__head").click(function (event) {
    event.preventDefault();
    $(".dropdown__head").parent().removeClass('open');
    $(this).parent().toggleClass('open');
  });

  $(".dropdown__body a ").click(function (event) {
    event.preventDefault();
    var value = $(this).text();
    var hrefvalue = $(this).attr('href');
    $(this).closest('.dropdown').find(".dropdown__head").text(value);
    $(this).closest('.dropdown').removeClass('open');
    console.log(value);
    console.log(hrefvalue);
    $('.card-cont').hide();
      $(hrefvalue).show();
    
    if (hrefvalue == '#viewall') {
      $('.bx-wrapper').show();
      $('.domain-slider').show();

    } else {
      $('.bx-wrapper').hide();
    }




  });





  $(".btn-pos").on("click", function () {
    $(".btn-pos").removeClass("active");
    $(this).addClass("active");
    var position = $(this).attr("rel");

    $(".position-list .pos-all").hide();
    $(".pos-banner").hide();
    $(".pos-" + position).fadeIn();
    $(".banner-" + position).show();
  });
  $(".position-list .pos-technology").show();

  $(".position-list .pos-all").on("click", function () {
    // $(".position-list .pos-all").removeClass('open');
    $(this).toggleClass("open");


  });






});

enquire.register("screen and (min-width: 768px)", {
  setup: function () {
    // Load in content via AJAX (just the once)
  },
  match: function () {
    $('.domain-slider').bxSlider({
      // minSlides :3,
      maxSlides: 4,
      moveSlides: 1,
      slideMargin: 20,
      controls: true,
      pager: false,
      infiniteLoop: false,
      touchEnabled: false,
      hideControlOnEnd: true,
      adaptiveHeight: true,
    });

  },
  unmatch: function () {
    $('.domain-slider').destroySlider();
  }
});
