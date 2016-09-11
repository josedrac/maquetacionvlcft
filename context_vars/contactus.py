import context_vars.navbar as navbar

def get_vars():
    return {
        'navbar'    : navbar.get_navbar(),
        'recaptcha' : True,
        'page_name' : 'support',
        'primary_title' : 'Formulario de contacto',
        'image_header'      : 'images/header/contactus/image_header.jpg',
        'image_header_480'  : 'images/header/contactus/image_header_480.jpg',
        'image_header_1200' : 'images/header/contactus/image_header_1200.jpg',
        'breadcrumbs'   : [
            {'label': 'Inicio', 'url': 'index.html'},
            {'label': 'Atención al cliente', 'url': 'support.html'},
            {'label': 'Formulario de contacto'}
        ]
    }
