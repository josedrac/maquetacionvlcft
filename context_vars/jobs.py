import context_vars.navbar as navbar

def get_vars():
    return {
        'navbar'            : navbar.get_navbar(),
        'page_name'         : 'known',
        'subpage_name'      : 'job',
        'primary_title'     : 'Empleo',
        'image_header'      : 'images/header/jobs/image_header.jpg',
        'image_header_480'  : 'images/header/jobs/image_header_480.jpg',
        'image_header_1200' : 'images/header/jobs/image_header_1200.jpg',
        'breadcrumbs'   : [
            {'label': 'Inicio', 'url': 'index.html'},
            {'label': 'Conócenos', 'url': 'known.html'},
            {'label': 'Empleo'}
        ],
        'know_us'   : {
            'image' : 'images/slider/slider1.jpg',
            'title' : 'Ofertas de empleo',
            'desc'  : 'Mercadona tiene por objetivo disponer de una plantilla altamente comprometida, motivada y alineada con la visión de la compañía',
            'button': 'Ver ofertas'
        }
    }
