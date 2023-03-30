jQuery(document).ready(function() {

  // To apply margin top to body as per header size
  if ($('.main-header').length) {
    $(window).resize(function() {
      $(document.body).css("margin-top", $(".main-header").outerHeight());
    }).resize();
  }

});