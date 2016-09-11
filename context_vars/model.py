import context_vars.navbar as navbar

def get_vars():
    return {
        'navbar'        : navbar.get_navbar(),
        'page_name'     : 'known',
        'subpage_name'  : 'model',
        'primary_title' : 'Modelo Mercadona',
        'image_header'      : 'images/header/model/image_header.jpg',
        'image_header_480'  : 'images/header/model/image_header_480.jpg',
        'image_header_1200' : 'images/header/model/image_header_1200.jpg',
        'textBox'       : [{
            'img'   : 'images/textbox/1.jpeg',
            'alt'   : '. . .',
            'title' : 'El Jefe',
            'text'  : '“Jefe” (Cliente): Mercadona se esfuerza día a día para satisfacer a sus Jefes, prescribiendo soluciones con la mejor relación calidad-precio del mercado para que los clientes se fabriquen su Compra Total.'
        },
        {
            'img'   : 'images/advantages/textbox/3.jpg',
            'alt'   : '. . .',
            'title' : 'El trabajador',
            'text'  : 'Para poder satisfacer a sus clientes, Mercadona también busca satisfacer a sus Trabajadores y Trabajadoras. Para ello, aplica un modelo de Recursos Humanos basado en el liderazgo, el esfuerzo y la satisfacción personal de la plantilla.'
        },
        {
            'img'   : 'images/advantages/textbox/2.jpg',
            'alt'   : '. . .',
            'title' : 'El proveedor',
            'text'  : 'Mercadona también persigue establecer relaciones estables con los Proveedores para conseguir un objetivo común: la satisfacción de nuestros clientes. En esta línea Mercadona ha iniciado los últimos años una apuesta por el sector primario para construir una Cadena Agroalimentaria Sostenible en la que todos los eslabones se vean beneficiados.'
        },
        {
            'img'   : 'images/advantages/textbox/1.jpg',
            'alt'   : '. . .',
            'title' : 'La sociedad',
            'text'  : 'Mercadona también persigue establecer relaciones estables con los Proveedores para conseguir un objetivo común: la satisfacción de nuestros clientes. En esta línea Mercadona ha iniciado los últimos años una apuesta por el sector primario para construir una Cadena Agroalimentaria Sostenible en la que todos los eslabones se vean beneficiados.'
        },
        {
            'img'   : 'images/advantages/textbox/4.jpg',
            'alt'   : '. . .',
            'title' : 'El capital',
            'text'  : 'Mercadona también persigue establecer relaciones estables con los Proveedores para conseguir un objetivo común: la satisfacción de nuestros clientes. En esta línea Mercadona ha iniciado los últimos años una apuesta por el sector primario para construir una Cadena Agroalimentaria Sostenible en la que todos los eslabones se vean beneficiados.'
        }],
        'breadcrumbs'   : [
            {'label': 'Inicio', 'url': 'index.html'},
            {'label': 'Conócenos', 'url': 'known.html'},
            {'label': 'Modelo Mercadona'}
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
        ]
    }
