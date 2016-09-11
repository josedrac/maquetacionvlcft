import context_vars.navbar as navbar

def get_vars():
    return {
        'navbar'    : navbar.get_navbar(),
        'page_name' : 'support',
        'primary_title' : 'Atención al cliente',
        'image_header'      : 'images/header/support/image_header.jpg',
        'image_header_480'  : 'images/header/support/image_header_480.jpg',
        'image_header_1200' : 'images/header/support/image_header_1200.jpg',
        'breadcrumbs'   : [
            {'label': 'Inicio', 'url': 'index.html'},
            {'label': 'Atención al cliente'}
        ]
    }
