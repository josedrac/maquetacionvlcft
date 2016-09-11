import context_vars.navbar as navbar

def get_vars():
    return {
        'navbar'    : navbar.get_navbar(),
        'page_name' : 'supermarket',
        'primary_title' : 'Supermercados',
        'image_header'      : 'images/header/supermarket/image_header.jpg',
        'image_header_480'  : 'images/header/supermarket/image_header_480.jpg',
        'image_header_1200' : 'images/header/supermarket/image_header_1200.jpg',
        'breadcrumbs'   : [
            {'label': 'Inicio', 'url': 'index.html'},
            {'label': 'Supermercados'}
        ]
    }
