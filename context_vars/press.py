import context_vars.navbar as navbar

def get_vars():
    return {
        'navbar'    : navbar.get_navbar(),
        'page_name' : 'known',
        'subpage_name'  : 'press',
        'primary_title' : 'Prensa',
        'image_header'  : 'images/header/press/image_header.jpg',
        'image_header_480'  : 'images/header/press/image_header_480.jpg',
        'image_header_1200' : 'images/header/press/image_header_1200.jpg',
        'breadcrumbs'   : [
            {'label': 'Inicio', 'url': 'index.html'},
            {'label': 'Conócenos', 'url': 'known.html'},
            {'label': 'Prensa'}
        ],
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
    }
