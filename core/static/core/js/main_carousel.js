$(document).ready(function(){
    var owl = $('.owl-carousel');
    owl.owlCarousel({
        loop: true,
        margin:10,
        autoplay: true,
        items: 6,
        dots: false,
        autoplaySpeed: 2000,
        autoplayTimeout: 5000,
        animateOut: 'fadeOut',
        nav: true,
        responsiveClass:true,
        responsive:{
            0:{
                items:2
            },
            600:{
                items:6
            },
            1000:{
                items:9
            }
        }

    });  
});