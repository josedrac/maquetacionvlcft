import context_vars.navbar as navbar

def get_vars():
    return {
        'navbar'        : navbar.get_navbar(),
        'page_name'     : 'known',
        'subpage_name'  : 'model',
        'title'         : 'Modelo Mercadona',
        'image_header'  : 'images/slider/slider2.jpg',
        'textBox'       : [{
            'img'   : 'images/textbox/1.jpeg',
            'alt'   : '. . .',
            'title' : 'El Jefe',
            'text'  : '“Jefe” (Cliente): Mercadona se esfuerza día a día para satisfacer a sus Jefes, prescribiendo soluciones con la mejor relación calidad-precio del mercado para que los clientes se fabriquen su Compra Total.'
        },
        {
            'img'   : 'images/textbox/1.jpeg',
            'alt'   : '. . .',
            'title' : 'El trabajador',
            'text'  : 'Para poder satisfacer a sus clientes, Mercadona también busca satisfacer a sus Trabajadores y Trabajadoras. Para ello, aplica un modelo de Recursos Humanos basado en el liderazgo, el esfuerzo y la satisfacción personal de la plantilla.'
        },
        {
            'img'   : 'images/textbox/1.jpeg',
            'alt'   : '. . .',
            'title' : 'El proveedor',
            'text'  : 'Mercadona también persigue establecer relaciones estables con los Proveedores para conseguir un objetivo común: la satisfacción de nuestros clientes. En esta línea Mercadona ha iniciado los últimos años una apuesta por el sector primario para construir una Cadena Agroalimentaria Sostenible en la que todos los eslabones se vean beneficiados.'
        }],
        'breadcrumbs'   : [
            'Inicio',
            'Conoce Mercadona',
            'Modelo Mercadona'
        ]
    }
