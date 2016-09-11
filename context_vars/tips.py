import context_vars.navbar as navbar

def get_vars():
    return {
        'navbar'    : navbar.get_navbar(),
        'page_name' : 'tips',
        'primary_title' : 'Consejos',
        'image_header'      : 'images/header/tips/image_header.jpg',
        'image_header_768'  : 'images/header/tips/image_header_768.jpg',
        'breadcrumbs'   : [
            {'label': 'Inicio', 'url': 'index.html'},
            {'label': 'Consejos'}
        ],
        'list' : [
            {
                'img'       : 'images/pets/pet1.png',
                'title'     : 'Pienso para Gatos Compy: ¿Qué nutrientes necesita mi gato?',
                'link'      : '#',
                'date'      : '12 de Julio de 2016',
                'desc'      : 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
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
                'img'       : 'images/pets/pet2.jpg',
                'title'     : 'Collar para perros de Mercadona',
                'link'      : '#',
                'date'      : '14 de Julio de 2016',
                'desc'      : 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                'tags'   : [
                    {
                        'title' : 'Etiqueta',
                        'link'  : '#'
                    }
                ]
            },
            {
                'img'       : 'images/pets/pet3.png',
                'title'     : 'Comida para pequeñas mascotas en Mercadona',
                'link'      : '#',
                'date'      : '20 de Mayo de 2016',
                'desc'      : 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
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
        'headerFood'        : {
            'title'         : 'Alimentación',
            'image'         : 'images/tips1.jpg',
            'alt'           : '. . .'
        },
        'headerPerfumery'   : {
            'title'         : 'Perfumería',
            'image'         : 'images/tips2.jpg',
            'alt'           : '. . .'
        },
        'headerHouse'       : {
            'title'         : 'Hogar',
            'image'         : 'images/tips3.jpg',
            'alt'           : '. . .'
        },
        'headerPets'        : {
            'title'         : 'Mascotas',
            'image'         : 'images/pets/header_pet.png',
            'alt'           : '. . .'
        }
    }
