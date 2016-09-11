(function($) {
    'use strict';

    var mdScreenMin = 992;

    var smScreenMax = mdScreenMin - 1;
    var smScreenMin = 768;

    var xsScreenMax = smScreenMin - 1;

    /* jshint -W117 */
    $.fn.oneSlider = function() {
        var self = this;
        var items;
        var container;
        var controllers = self.find('.slider-controller');
        var isDisableActions;
        var directions = {
            next: 'next',
            prev: 'prev'
        };

        function setTransition(item) {
            $(item).addClass(directions.next);
        }
        function removeTransition(item) {
            $(item).removeClass(directions.next);
        }
        function updateItems() {
            items = self.find('.item');
            container = self.find('.slider-content');
        }
        function moveFirstToLast() {
            var first = $(items[0]);
            var copied = first.clone();
            first.remove();

            container.append(copied);
            updateItems();
        }
        function moveLastToFirst() {
            var last = $(items[items.length -1]);
            var copied = last.clone();
            last.remove();

            container.prepend(copied);
            updateItems();
        }
        function isPhone() {
            return Modernizr.mq('(max-width: ' + xsScreenMax + 'px)');
        }
        function isTablet() {
            return Modernizr.mq('(min-width: ' + smScreenMin + 'px)' +
                                     'and (max-width: ' + smScreenMax + 'px)');
        }
        function isDesktop() {
            return Modernizr.mq('(min-width: ' + mdScreenMin + 'px)');
        }
        function getVisibles() {
            if (isTablet()) {
                return 2;
            }
            if (isDesktop()) {
                return 3;
            }
        }
        function disableActions() {
            isDisableActions = true;
        }
        function enableActions() {
            isDisableActions = false;
        }

        function showNext() {
            disableActions();
            var next = getVisibles();
            setTransition($(items[next]));

            container.animate({
                left: (-100 / next) + '%'
            }, function() {
                container.removeAttr('style');
                removeTransition($(items[next]));
                moveFirstToLast();
                enableActions();
            });
        }
        function showPrev() {
            disableActions();
            var next = getVisibles();
            moveLastToFirst();
            setTransition($(items[next]));

            container.css({
                left: (-100 / next) + '%'
            });
            container.animate({
                left: '0%'
            }, function() {
                container.removeAttr('style');
                removeTransition($(items[next]));
                enableActions();
            });
        }

        controllers.click(function() {
            if (isPhone() || isDisableActions) {
                return;
            }
            updateItems();

            var controller = $(this);
            var isNext = controller.hasClass(directions.next);
            var isPrev = controller.hasClass(directions.prev);
            if (isNext) {
                showNext();
            }
            if (isPrev) {
                showPrev();
            }
        });

        return self;
    };

    $('.one-slider').oneSlider();
})(jQuery);