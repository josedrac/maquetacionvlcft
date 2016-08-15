import context_vars.navbar as navbar

def get_vars():
    return {
        'navbar'            : navbar.get_navbar(),
        'page_name'         : 'home',
        'actuality_title': {
            'title'         : 'Actualidad Mercadona',
            'linkTitle'    : 'Ver todas las Noticias',
            'link'          : '#'
        },
        'actuality' : [
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
            },
            {
                'img'       : 'images/news/new4.png',
                'title'     : 'Mercadona amplía su colaboración a dos empresas',
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
        'tips_title': {
            'title'         : 'Consejos',
            'linkTitle'     : 'Ver todos los Consejos',
            'link'          : '#'
        },
        'tips' : [
            {
                'img'           : 'images/tips/tip1.png',
                'title'         : 'Hogar',
                'link'          : '#',
                'description'   : 'Lorem ipsum dolor sit amet, consectetur adipiscing nunc ornare leo sem, in feugiat lectus sagittis sed. '
            },
            {
                'img'           : 'images/tips/tip2.png',
                'title'         : 'Perfumería',
                'link'          : '#',
                'description'   : 'Lorem ipsum dolor sit amet, consectetur adipiscing nunc ornare leo sem, in feugiat lectus sagittis sed. '
            },
            {
                'img'           : 'images/tips/tip3.png',
                'title'         : 'Alimentación',
                'link'          : '#',
                'description'   : 'Lorem ipsum dolor sit amet, consectetur adipiscing nunc ornare leo sem, in feugiat lectus sagittis sed. '
            },
            {
                'img'           : 'images/tips/tip4.png',
                'title'         : 'Macotas',
                'link'          : '#',
                'description'   : 'Lorem ipsum dolor sit amet, consectetur adipiscing nunc ornare leo sem, in feugiat lectus sagittis sed. '
            }
        ]
    }
