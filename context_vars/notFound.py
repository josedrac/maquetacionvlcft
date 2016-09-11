import context_vars.navbar as navbar

def get_vars():
    return {
        'navbar'        : navbar.get_navbar(),
        'primary_title' : '404 - Página no encontrada',
        'image_header'  : 'images/advantages/invoice.jpg'
    }
