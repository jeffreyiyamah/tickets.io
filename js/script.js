document.addEventListener('DOMContentLoaded', function() {
    var swiper = new Swiper('.swiper-container', {

        loop: true,
        slidesPerView: 3,
        spaceBetween: 30,


        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },

        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },


        scrollbar: {
            el: '.swiper-scrollbar',
            hide: true,
        },
    });
});
