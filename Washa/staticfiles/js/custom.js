$(function(){
    //======================preloader================
    //preloader js
$(window).load(function(){
  $(".preloader").delay(1500).fadeOut(500);
});
    
    $Offset = $('#menu').offset().top;
$(window).scroll(function () {
    $scrolling = $(this).scrollTop();
    if ($scrolling > $Offset) {
        $('#menu').addClass('menufixed');
    } else {
        $('#menu').removeClass('menufixed');
    }
    if($scrolling >100){
      $(".back-to-top").fadeIn(500);
  }
  else{
      $(".back-to-top").fadeOut(500);
  }

});
//animation scroll js
var html_body = $('html, body');
$('nav a').on('click', function () {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
        if (target.length) {
            html_body.animate({
                scrollTop: target.offset().top - 30
            }, 2000);
            return false;
        }
    }
}); 

    
    
    //==============================banner slider=======================
    $('.banner-slider').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 2500,
        speed:1500,
        fade:true,
        arrows:true,
        prevArrow:'.left',
        nextArrow:'.right',
      });
      // isotope js
      // external js: isotope.pkgd.js


// init Isotope
var $grid = $('.grid').isotope({
  itemSelector: '.element-item',
  layoutMode: 'fitRows',
  getSortData: {
    name: '.name',
    symbol: '.symbol',
    number: '.number parseInt',
    category: '[data-category]',
    weight: function( itemElem ) {
      var weight = $( itemElem ).find('.weight').text();
      return parseFloat( weight.replace( /[\(\)]/g, '') );
    }
  }
});

// filter functions
var filterFns = {
  // show if number is greater than 50
  numberGreaterThan50: function() {
    var number = $(this).find('.number').text();
    return parseInt( number, 10 ) > 50;
  },
  // show if name ends with -ium
  ium: function() {
    var name = $(this).find('.name').text();
    return name.match( /ium$/ );
  }
};

// bind filter button click
$('#filters').on( 'click', 'button', function() {
  var filterValue = $( this ).attr('data-filter');
  // use filterFn if matches value
  filterValue = filterFns[ filterValue ] || filterValue;
  $grid.isotope({ filter: filterValue });
});

// bind sort button click
$('#sorts').on( 'click', 'button', function() {
  var sortByValue = $(this).attr('data-sort-by');
  $grid.isotope({ sortBy: sortByValue });
});

// change is-checked class on buttons
$('.button-group').each( function( i, buttonGroup ) {
  var $buttonGroup = $( buttonGroup );
  $buttonGroup.on( 'click', 'button', function() {
    $buttonGroup.find('.is-checked').removeClass('is-checked');
    $( this ).addClass('is-checked');
  });
});
     //==============================mobile-slider=======================
     $('.mobile-slide').slick({
      slidesToShow: 4,
      slidesToScroll: 1,
      autoplay: false,
      autoplaySpeed: 2000,
      arrows:true,
      prevArrow:'.left1',
        nextArrow:'.right1',
      responsive: [
        {
          breakpoint: 461,
          settings: {
            slidesToShow: 1,
            
          }
        },
        {
          breakpoint: 576,
          settings: {
            slidesToShow: 2,
            
          }
        },
        {
          breakpoint: 768,
          settings: {
            slidesToShow: 2,
            
          }
        },
        {
          breakpoint: 992,
          settings: {
            slidesToShow: 3,
            
          }
        },
        
      ]
    });


    //===========================counter timer=======================
    const second = 1000,
      minute = second * 60,
      hour = minute * 60,
      day = hour * 24;

let countDown = new Date('Jul 21, 2022 00:00:00').getTime(),
    x = setInterval(function() {

      let now = new Date().getTime(),
          distance = countDown - now;

      document.getElementById('days').innerText = Math.floor(distance / (day)),
        document.getElementById('hours').innerText = Math.floor((distance % (day)) / (hour)),
        document.getElementById('minutes').innerText = Math.floor((distance % (hour)) / (minute)),
        document.getElementById('seconds').innerText = Math.floor((distance % (minute)) / second);
      
      //do something later when date is reached
      //if (distance < 0) {
      //  clearInterval(x);
      //  
      //}

    }, second)

  

    //=============================team-slider=======================
    
$('.team-slide').slick({
  slidesToShow: 2,
  slidesToScroll: 1,
  autoplay: false,
  autoplaySpeed: 2000,
  arrows:true,
  prevArrow:'.left2',
  nextArrow:'.right2',
  responsive: [
    {
      breakpoint: 576,
      settings: {
        slidesToShow: 1,
        
      }
    },
    {
      breakpoint: 768,
      settings: {
        slidesToShow: 1,
        
      }
    },
    
    
    
  ]
});
// wow js
new WOW().init();













});