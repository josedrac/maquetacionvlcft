import context_vars.navbar as navbar

def get_vars():
    return {
        'navbar'        : navbar.get_navbar(),
        'page_name'     : 'known',
        'subpage_name'  : 'service',
        'primary_title' : 'Servicios',
        'image_header'      : 'images/header/services/image_header.jpg',
        'image_header_480'  : 'images/header/services/image_header_480.jpg',
        'image_header_992'  : 'images/header/services/image_header_992.jpg',
        'image_header_1200' : 'images/header/services/image_header_1200.jpg',
        'breadcrumbs'   : [
            {'label': 'Inicio', 'url': 'index.html'},
            {'label': 'Conócenos', 'url': 'known.html'},
            {'label': 'Servicios'}
        ],
        'textBox'   : [{
            'img'   : 'images/advantages/textbox/1.jpg',
            'alt'   : '. . .',
            'title' : 'Siempre precios bajos',
            'text'  : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin non eleifend velit. In tempus eros tortor, ac finibus tellus condimentum id. Etiam a ullamcorper augue. Vivamus sollicitudin, velit eu sodales rhoncus, ipsum magna faucibus nunc, eget dictum lectus nunc id lorem.'
        },
        {
            'img'   : 'images/advantages/textbox/2.jpg',
            'alt'   : '. . .',
            'title' : 'Surtido eficaz',
            'text'  : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin non eleifend velit. In tempus eros tortor, ac finibus tellus condimentum id. Etiam a ullamcorper augue. Vivamus sollicitudin, velit eu sodales rhoncus, ipsum magna faucibus nunc, eget dictum lectus nunc id lorem.'
        },
        {
            'img'   : 'images/advantages/textbox/3.jpg',
            'alt'   : '. . .',
            'title' : 'Productos nacionales',
            'text'  : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin non eleifend velit. In tempus eros tortor, ac finibus tellus condimentum id. Etiam a ullamcorper augue. Vivamus sollicitudin, velit eu sodales rhoncus, ipsum magna faucibus nunc, eget dictum lectus nunc id lorem.'
        },
        {
            'img'   : 'images/advantages/textbox/4.jpg',
            'alt'   : '. . .',
            'title' : 'Servicios',
            'text'  : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin non eleifend velit. In tempus eros tortor, ac finibus tellus condimentum id. Etiam a ullamcorper augue. Vivamus sollicitudin, velit eu sodales rhoncus, ipsum magna faucibus nunc, eget dictum lectus nunc id lorem.'
        },
        {
            'img'   : 'images/advantages/textbox/5.jpg',
            'alt'   : '. . .',
            'title' : 'Innovación',
            'text'  : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin non eleifend velit. In tempus eros tortor, ac finibus tellus condimentum id. Etiam a ullamcorper augue. Vivamus sollicitudin, velit eu sodales rhoncus, ipsum magna faucibus nunc, eget dictum lectus nunc id lorem.'
        }],
        'invoice'   : {
            'image' : 'images/advantages/invoice.jpg',
            'title' : 'Factura online',
            'desc'  : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin non eleifend velit. In tempus eros tortor, ac finibus tellus condimentum id.',
            'button': 'Saber más'
        },
        'target'   : {
            'image' : 'images/advantages/target.jpg',
            'title' : 'Tarjeta Mercadona',
            'desc'  : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin non eleifend velit. In tempus eros tortor, ac finibus tellus condimentum id.',
            'button': 'Saber más'
        }
    }
