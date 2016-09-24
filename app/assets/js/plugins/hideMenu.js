var hideMenu = function($) {
    var webSite = $('html');
    var webSiteContent = webSite.find('body');
    var launcher = webSiteContent.find('.panel-menu');

    launcher.mouseout(function() {
        var idOpMenu = '#'+this.id;
        var idSubmenu = '#'+this.id.substring(7,this.id.length);
        var isSubmenuVisible = launcher.find(idSubmenu).is(":visible");
        var idLinkMenu = '#link-'+this.id.substring(7,this.id.length);

        if (!isSubmenuVisible) {
    //        $(idLinkMenu).removeClass('active_option');
        }

    });

    launcher.mouseenter(function() {
        console.log('over-panelmenu');

        var idOpMenu = '#'+this.id;
        var idSubmenu = '#'+this.id.substring(7,this.id.length);
        var isSubmenuVisible = launcher.find(idSubmenu).is(":visible");
        var idLinkMenu = '#link-'+this.id.substring(7,this.id.length);

        console.log('isSubmenuVisible:'+isSubmenuVisible);
        console.log(this);
        console.log('this.id:'+this.id);
        console.log('idSubmenu:'+idSubmenu);
        console.log('idLinkMenu:'+idLinkMenu);

        if (!isSubmenuVisible) {
            $(".sub-menu").collapse('hide');
        }

        $(idSubmenu).collapse('show');
        //$(idLinkMenu).addClass('active_option');

    });

};
