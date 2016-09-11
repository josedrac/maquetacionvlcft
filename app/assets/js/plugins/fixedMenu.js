var fixedMenu = function($) {
    $(window).scroll(function () {
        var nav = $('.nav-content');
        var content = $('.contents');
        var pos = content.offset().top - nav.height();
        var isScrollDownOfNav = $(this).scrollTop() > pos;

        if (isScrollDownOfNav) {
            nav.addClass('navbar-fixed-top');
        } else {
            nav.removeClass('navbar-fixed-top');
        }
    });
};
