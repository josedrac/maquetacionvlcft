import context_vars.navbar as navbar

def get_vars():
    return {
        'navbar'        : navbar.get_navbar(),
        'page_name'     : 'known',
        'subpage_name'  : 'card',
        'primary_title' : 'Tarjeta Mercadona',
        'image_header'  : 'images/header/card/image_header.jpg',
        'image_header_480'   : 'images/header/card/image_header_480.jpg',
        'image_header_992'   : 'images/header/card/image_header_992.jpg',
        'image_header_1200'  : 'images/header/card/image_header_1200.jpg',
        'breadcrumbs'   : [
            {'label': 'Inicio', 'url': 'index.html'},
            {'label': 'Tarjeta Mercadona'}
        ],
        'textBox'   : [{
            'img'   : 'images/advantages/textbox/1.jpg',
            'alt'   : '. . .',
            'title' : 'Lorem ipsum',
            'text'  : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed laoreet tristique orci non pellentesque. Integer semper diam dolor, eu suscipit justo malesuada id. Nunc nec metus nec erat facilisis luctus. Aliquam egestas orci sed dapibus gravida.'
        },
        {
            'img'   : 'images/advantages/textbox/2.jpg',
            'alt'   : '. . .',
            'title' : 'Lorem ipsum',
            'text'  : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed laoreet tristique orci non pellentesque. Integer semper diam dolor, eu suscipit justo malesuada id. Nunc nec metus nec erat facilisis luctus. Aliquam egestas orci sed dapibus gravida.'
        },
        {
            'img'   : 'images/advantages/textbox/3.jpg',
            'alt'   : '. . .',
            'title' : 'Lorem ipsum',
            'text'  : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed laoreet tristique orci non pellentesque. Integer semper diam dolor, eu suscipit justo malesuada id. Nunc nec metus nec erat facilisis luctus. Aliquam egestas orci sed dapibus gravida.'
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
