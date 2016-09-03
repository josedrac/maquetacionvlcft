var hideMenu = function($) {
    $(window).click(function() {
        var isSubmenuVisible = $('.sub-menu').is(":visible");
        console.log(isSubmenuVisible);
        if(isSubmenuVisible) {
            $(".sub-menu").collapse('hide');
        }
    });
};
