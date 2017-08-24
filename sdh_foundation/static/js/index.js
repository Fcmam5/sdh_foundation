$(document).ready(function(){

$('.jump-to').click(function () {
  var $href = $(this).attr('href');
  console.log("hooop")
  $('body').stop().animate({
    scrollTop: $($href).offset().top
  }, 1000);
  return false;
});

var currentURL = window.location;
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

});