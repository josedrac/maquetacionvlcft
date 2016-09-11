var timeline = function($) {
    'use strict';
    var timeline = $('.timeline');
    var launchers = timeline.find('.date');

    launchers.click(function() {
        var isPhoneSize = Modernizr.mq('(max-width: ' + xsScreenMax + 'px)');
        if (isPhoneSize) {
            var launch = $(this).find('span');
            var sectionBlock = $(this).next();
            sectionBlock.collapse('toggle');
            launch.toggleClass('fa-angle-down fa-angle-up');
        }
    });
};
