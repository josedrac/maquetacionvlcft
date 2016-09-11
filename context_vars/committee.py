import context_vars.navbar as navbar

def get_vars():
    return {
        'navbar'        : navbar.get_navbar(),
        'page_name'     : 'known',
        'subpage_name'  : 'committee',
        'primary_title' : 'Organización',
        'image_header'      : 'images/header/committee/image_header.jpg',
        'image_header_480'  : 'images/header/committee/image_header_480.jpg',
        'image_header_992'  : 'images/header/committee/image_header_992.jpg',
        'image_header_1200' : 'images/header/committee/image_header_1200.jpg',
        'breadcrumbs'   : [
            {'label': 'Inicio', 'url': 'index.html'},
            {'label': 'Conócenos', 'url': 'known.html'},
            {'label': 'Organización'}
        ],
        'committee_title': {
            'title'         : 'Comité de dirección'
        },
        'news' : [
            {
                'img'       : 'images/news/new1.png',
                'title'     : 'Mercadona colabora con más de 100 comedores de colegios',
                'link'      : '#',
                'date'      : '12 de Julio de 2016',
                'tags'   : [
                    {
                        'title' : 'Etiqueta',
                        'link'  : '#'
                    },
                    {
                        'title' : 'Etiqueta',
                        'link'  : '#'
                    }
                ]
            },
            {
                'img'       : 'images/news/new2.png',
                'title'     : 'Mercadona contrata a 600 personas hasta abril',
                'link'      : '#',
                'date'      : '14 de Julio de 2016',
                'tags'   : [
                    {
                        'title' : 'Etiqueta',
                        'link'  : '#'
                    }
                ]
            },
            {
                'img'       : 'images/news/new3.png',
                'title'     : 'Mercadona abrirá sus puertas en Lugo',
                'link'      : '#',
                'date'      : '20 de Mayo de 2016',
                'tags'   : [
                    {
                        'title' : 'Etiqueta',
                        'link'  : '#'
                    },
                    {
                        'title' : 'Etiqueta',
                        'link'  : '#'
                    }
                ]
            }
        ],
        'model'   : {
            'image' : 'images/model_mercadona.jpg',
            'title' : 'Modelo Mercadona',
            'desc'  : 'Mercadona es una compañía  de supermercados, de capital 100% español y familiar, que tiene por objetivo satisfacer las necesidades de sus clientes.',
            'button': 'Saber más'
        },
    }
