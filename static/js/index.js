$(document).ready(function(){

  var pathname = window.location.pathname;
  var currentURL = window.location;
  $('.nav > li > a[href="'+pathname+'"]').parent().addClass('active');

  $('.jump-to').click(function () {
    var $href = $(this).attr('href');
    console.log("hooop")
    $('body').stop().animate({
      scrollTop: $($href).offset().top
    }, 1000);
    return false;
  });

  $(".owl-carousel").owlCarousel({
            items: 1,
            autoplay:true,
            loop:true,
            margin:10,
            dots:true,
            dotData: true,
            autoplayHoverPause: true,
            thumbs: true,
            thumbImage: true,
            thumbContainerClass: 'owl-thumbs',
            thumbItemClass: 'owl-thumb-item'
            });
  $(".owl-carousel .item").on('click', function(){
          var _this = $(this).clone().find('img');
          $('.poup-viewer')
            .show()
            .html(_this)
            .on('click', function(){
              $(this)
                .html('')
                .hide();
            });

            $('.poup-viewer img').on('click', function(e){
              e.stopPropagation();
            });
        });

  $('#current-page-citation').attr('href', currentURL).text(currentURL)
  $("#twitter").html("<a href='https://twitter.com/intent/tweet?url="+ currentURL +"&text=" + document.title + "' target='_blank'>Twitter</a>")
  $("#facebook").html("<a href='https://www.facebook.com/sharer/sharer.php?u="+ currentURL + "' target='_blank'>Facebook</a>")

});
