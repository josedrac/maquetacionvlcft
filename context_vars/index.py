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
                'img'       : 'http://www.valenciafoodtourspain.com/wp-content/uploads/2016/08/La-Tomatina-Buñol-Valencia-420x287.jpg',
                'title'     : 'La Tomatina: A Tomato Frenzy in Buñol',
                'link'      : '#',
                'date'      : '12 de Julio de 2016',
                'desc'     : 'Every year on the last Wednesday of August (August 31st this year) the small town of Buñol (Valencian Community) puts on a tomato war...',
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
                'img'       : 'http://www.valenciafoodtourspain.com/wp-content/uploads/2016/08/IMG_8829-420x287.jpg',
                'title'     : 'The Best of Valencia in 24 Hours',
                'link'      : '#',
                'date'      : '14 de Julio de 2016',
                'desc'     : 'Every year on the last Wednesday of August (August 31st this year) the small town of Buñol (Valencian Community) puts on a tomato war...',
                'tags'   : [
                    {
                        'title' : 'Etiqueta',
                        'link'  : '#'
                    }
                ]
            },
            {
                'img'       : 'http://www.valenciafoodtourspain.com/wp-content/uploads/2016/07/2016-06-23-18.02.52-3-420x287.jpg',
                'title'     : 'Bodegas Biosca – Wine Tasting In Valencia’s Ruzafa District',
                'link'      : '#',
                'date'      : '20 de Mayo de 2016',
                'desc'     : 'Every year on the last Wednesday of August (August 31st this year) the small town of Buñol (Valencian Community) puts on a tomato war...',
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
                'img'       : 'http://www.valenciafoodtourspain.com/wp-content/uploads/2016/07/2016-07-16-09.53.32-420x287.jpg',
                'title'     : 'Snorkeling in Ambolo Beach & Seafood Paella in Moraira',
                'link'      : '#',
                'date'      : '20 de Mayo de 2016',
                'desc'     : 'Every year on the last Wednesday of August (August 31st this year) the small town of Buñol (Valencian Community) puts on a tomato war...',
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
