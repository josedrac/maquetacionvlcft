var gridList = function($) {

    var list = $('#list');
    var grid = $('#grid');
    var newBlog = $('.list-group .new-blog');

    list.click(setListMode);
    grid.click(setGridMode);

    function setListMode(event) {
        event.preventDefault();
        newBlog.removeClass('col-sm-6 col-lg-3').addClass('list-group-elem');
        newBlog.find('.img-content').addClass('col-sm-5 col-lg-4');
        newBlog.find('.content-new').addClass('col-sm-7 col-lg-8');
        newBlog.find('.content-new .description').show();
        list.addClass('active');
        grid.removeClass('active');
    }

    function setGridMode(event) {
        event.preventDefault();
        newBlog.removeClass('list-group-elem').addClass('col-sm-6 col-lg-3');
        newBlog.find('.img-content').removeClass('col-sm-5 col-lg-4');
        newBlog.find('.content-new').removeClass('col-sm-7 col-lg-8');
        newBlog.find('.content-new .description').hide();
        grid.addClass('active');
        list.removeClass('active');
    }

    newBlog.addClass('wow fadeIn');
};
