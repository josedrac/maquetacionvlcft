import context_vars.navbar as navbar

def get_vars():
    return {
        'navbar'            : navbar.get_navbar(),
        'page_name'         : 'known',
        'primary_title'     : 'Conoce Mercadona',
        'image_header'      : 'images/header/know/image_header.jpg',
        'image_header_480'  : 'images/header/know/image_header_480.jpg',
        'image_header_992'  : 'images/header/know/image_header_992.jpg',
        'image_header_1200' : 'images/header/know/image_header_1200.jpg',
        'breadcrumbs'       : [
            {'label': 'Inicio', 'url': 'index.html'},
            {'label': 'Conócenos'}
        ],
        'model'   : {
            'image' : 'images/model_mercadona.jpg',
            'title' : 'Modelo Mercadona',
            'desc'  : 'Mercadona es una compañía  de supermercados, de capital 100% español y familiar, que tiene por objetivo satisfacer las necesidades de sus clientes.',
            'button': 'Saber más'
        }
    }
