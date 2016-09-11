import context_vars.navbar as navbar

def get_vars():
    return {
        'navbar'        : navbar.get_navbar(),
        'page_name'     : 'support',
        'subpage_name'  : 'questions',
        'primary_title' : 'Preguntas frecuentes',
        'image_header'      : 'images/header/questions/image_header.jpg',
        'image_header_480'  : 'images/header/questions/image_header_480.jpg',
        'image_header_1200' : 'images/header/questions/image_header_1200.jpg',
        'breadcrumbs'   : [
            {'label': 'Inicio', 'url': 'index.html'},
            {'label': 'Atención al cliente', 'url': 'support.html'},
            {'label': 'Preguntas frecuentes'}
        ]
    }
