var fixedMenu = function($) {
    var pos = $('.nav-content').offset().top;
    var nav = $('.nav-content');

    $(window).scroll(function () {
        if ($(this).scrollTop() > pos) {
            nav.addClass('navbar-fixed-top');
        } else {
            nav.removeClass('navbar-fixed-top');
        }
    });
};
