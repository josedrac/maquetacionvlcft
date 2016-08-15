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
