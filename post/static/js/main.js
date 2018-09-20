(function ($) {
    $(document).on('ready', function () {

        "use strict";

        /**Preload**/
        $('#page-loader').delay(800).fadeOut(600, function () {
            $('body').fadeIn();
        });

        /**Menu Mobile**/
        $('.menu-icon').on('click', function () {
            $('body').toggleClass("open-menu");
        });
        $('.menu-res li.menu-item-has-children').on('click', function () {

            var submenu = $(this).find("ul");
            if ($(submenu).is(":visible")) {
                $(submenu).slideUp();
                $(this).removeClass("open-submenu-active");
            }
            else {
                $(submenu).slideDown();
                $(this).addClass("open-submenu-active");
            }
        });

        $('.menu-res li.menu-item-has-children > a').on('click', function () {
            return false;
        });

        /**Menu Fixed**/
        $(window).bind('scroll', function () {
            if ($(window).scrollTop() >= 250) {
                $('body.fixed-style').addClass('fixed');
            } else {
                $('body.fixed-style').removeClass('fixed');
            }

            if ($(window).scrollTop() >= 400) {
                $('body.fixed-style').addClass('show-menu-fixed');
            } else {
                $('body.fixed-style').removeClass('show-menu-fixed');
            }

            if ($(window).scrollTop() + $(window).height() > $(document).height() - 100) {
                $(".totop").addClass("show");
            }
            else {
                $(".totop").removeClass("show");
            }

        });

        /**Trend Affix**/
        $('.trend-box-affix').affix({
            offset: {
                top: 2965,
                bottom: function () {
                    return (this.bottom = $('.footer').outerHeight(true));
                }
            }
        })

        /**Back to top**/
        $(".totop").on('click', function () {
            $("html, body").animate({ scrollTop: 0 }, 2000);
        });

        /**Search Box**/
        $('body').on('click', function () {
            if ($('.search-icon').hasClass("show-search")) {
                $('.search-icon').toggleClass("show-search");
            }
        });
        $('.icon-search').on('click', function () {
            if ($(".searchbox").is(":visible")) {
                $(".searchbox").stop(true, true).slideUp();
                $(this).removeClass("show-searchbox");
            }
            else {
                $(".searchbox").stop(true, true).slideDown();
                $(this).addClass("show-searchbox");
                $(".searchbox input").focus();
            }
        });

        /**Home slider**/
        if ($('.bx-homeslider').length) {
            $('.bx-homeslider').bxSlider({
                mode: 'fade',
                captions: true,
            });
        }

        /**gallery posts slider**/
        $('.owl-gallery-posts').owlCarousel({
            loop: true,
            nav: true,
            items: 1,
            mouseDrag: false,
            navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"]
        });

        /**dailies slider**/
        $('.owl-dailies').owlCarousel({
            loop: true,
            nav: true,
            items: 1,
            mouseDrag: false,
            navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"]
        });

        /**Grid pinterest style**/
        if ($('.grid').length) {
            $('.grid').isotope({
                itemSelector: '.grid-item',
            });
        }

        /**Gallerye**/
        if ($('.fancybox').length) {
            $('.fancybox').fancybox({
                scrolling: true
            });
        }
    });
})(jQuery);