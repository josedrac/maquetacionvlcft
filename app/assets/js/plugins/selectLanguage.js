var selectLanguage = function($) {
    'use strict';
    $('.selectpicker')
        .selectpicker({
            width: '160px',
            style: null
        });
    $('.selectpicker-form').selectpicker({
        style: null
    });

    var menuMobile = $('.languages-menu-mobile');

    menuMobile.on('click', 'dd', function() {
        menuMobile.find('dd').removeClass('active');
        $(this).addClass('active');
        var selected = $(this).find('a');
        var language = selected.text();
        var country = selected.attr('data-subtext');

        var text = country + ' ' + language;
        $('.languages-mobile-button .language').html(text);
        menuMobile.toggleClass('closed');
    });

    $('.languages-mobile-button, .close-languages').click(function() {
        menuMobile.toggleClass('closed');
    });

    $('.languages-menu .open').addClass('animated fadeInDown infinite');
};
