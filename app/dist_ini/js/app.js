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

var footerMenu = function($) {
    'use strict';
    var footerMenu = $('.footer-mercadona .footer-menu-group');
    var launchers = footerMenu.find('.title');

    launchers.click(function() {
        var isPhoneSize = Modernizr.mq('(max-width: ' + xsScreenMax + 'px)');
        if (isPhoneSize) {
            var menuBlock = $(this).next();
            menuBlock.collapse('toggle');
        }
    });
};

var gridList = function($) {

    var list = $('#list');
    var grid = $('#grid');
    var actuality = $('.list-group .actuality');

    list.click(setListMode);
    grid.click(setGridMode);

    function setListMode(event) {
        event.preventDefault();
        actuality.removeClass('col-sm-6 col-lg-3').addClass('list-group-elem');
        actuality.find('.img-content').addClass('col-sm-5 col-lg-4');
        actuality.find('.content-new').addClass('col-sm-7 col-lg-8');
        actuality.find('.content-new .description').show();
        list.addClass('active');
        grid.removeClass('active');
    }

    function setGridMode(event) {
        event.preventDefault();
        actuality.removeClass('list-group-elem').addClass('col-sm-6 col-lg-3');
        actuality.find('.img-content').removeClass('col-sm-5 col-lg-4');
        actuality.find('.content-new').removeClass('col-sm-7 col-lg-8');
        actuality.find('.content-new .description').hide();
        grid.addClass('active');
        list.removeClass('active');
    }

    actuality.addClass('wow fadeIn');
};

var hideMenu = function($) {
    $(window).click(function() {
        var isSubmenuVisible = $('.sub-menu').is(":visible");
        console.log('isSubmenuVisible='.isSubmenuVisible);
        if(isSubmenuVisible) {
            $(".sub-menu").collapse('hide');
        }
    });
};

var navPhone = function($) {
    'use strict';

    var webSite = $('html');
    var webSiteContent = webSite.find('body');
    var launcher = webSiteContent.find('.nav-phone-launch');
    var classToOpen = 'nav-phone-open';

    launcher.click(function() {
        var isOpenedMenu = webSite.hasClass(classToOpen);

        if (isOpenedMenu) {
            webSite.removeClass(classToOpen);
        } else {
            webSite.addClass(classToOpen);
        }
    });
};

var selectLanguage = function($) {
    'use strict';
    $('.selectpicker').selectpicker({
        width: '160px',
        style: null
    });
};

var animationWow = function($) {
    'use strict';
    var wow = new WOW({
        boxClass:     'wow',
        mobile:       false,
    });
    wow.init();
};

jQuery.noConflict();
jQuery(document).ready(function($) {
        'use strict';
        selectLanguage($);
        fixedMenu($);
        navPhone($);
        footerMenu($);
        gridList($);
        hideMenu($);
        animationWow($);
    });

var lgScreenMin = 1200;

var mdScreenMax = lgScreenMin - 1;
var mdScreenMin = 992;

var smScreenMax = mdScreenMin - 1;
var smScreenMin = 768;

var xsScreenMax = smScreenMin - 1;
var xsScreenMin = 480;