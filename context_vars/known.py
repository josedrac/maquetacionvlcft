import context_vars.navbar as navbar

def get_vars():
    return {
        'navbar'        : navbar.get_navbar(),
        'page_name'     : 'known',
        'title'         : 'Conoce Mercadona',
        'image_header'  : 'images/slider/slider2.jpg',
        'breadcrumbs'   : [
            'Inicio',
            'Conócenos'
        ]
    }
