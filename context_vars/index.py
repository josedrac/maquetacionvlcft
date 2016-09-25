import context_vars.navbar as navbar
import context_vars.lastTestimonials as lastTestimonials

def get_vars():
    return {
        'lastTestimonials'   : lastTestimonials.get_lastTestimonials(),
        'navbar'                : navbar.get_navbar(),
        'page_name'             : 'home',
        'news_title'            :'Actualidad Mercadona',
        'news' : [
            {
                'img'       : 'images/news/new1.png',
                'title'     : 'Mercadona colabora con más de 100 comedores de colegios',
                'link'      : 'detail.html',
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
                'link'      : 'detail.html',
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
                'link'      : 'detail.html',
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
        'tips_title'  : 'Consejos',
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
        ],
        'know_us'   : {
            'image' : 'images/slider/slider1.jpg',
            'title' : 'Conócenos',
            'desc'  : 'Mercadona es una compañía  de supermercados, de capital 100% español y familiar, que tiene por objetivo satisfacer las necesidades de sus clientes',
            'button': 'Saber más'
        },
        'actuality' : [
            {
                'img'       : 'images/recursos/La-Tomatina-Buñol-Valencia-420x287.jpg',
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
                'img'       : 'images/recursos/IMG_8829-420x287.jpg',
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
                'img'       : 'images/recursos/2016-06-23-18.02.52-3-420x287.jpg',
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
                'img'       : 'images/recursos/2016-07-16-09.53.32-420x287.jpg',
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
