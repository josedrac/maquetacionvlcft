import context_vars.navbar as navbar

def get_vars():
    return {
        'navbar'        : navbar.get_navbar(),
        'page_name'     : 'known',
        'subpage_name'  : 'history',
        'primary_title' : 'Historia',
        'image_header'      : 'images/header/history/image_header.jpg',
        'image_header_480'  : 'images/header/history/image_header_480.jpg',
        'image_header_1200' : 'images/header/history/image_header_1200.jpg',
        'breadcrumbs'   : [
            {'label': 'Inicio', 'url': 'index.html'},
            {'label': 'Conócenos', 'url': 'known.html'},
            {'label': 'Historia'}
        ],
        'timeline'      : [
            {
                'date'  : '1977',
                'text'  : 'El matrimonio formado por D. Francisco Roig Ballester (1912-2003) y Da Trinidad Alfonso Mocholí (1911- 2006) inicia la actividad de Mercadona dentro del Grupo Cárnicas Roig. Las entonces carnicerías del negocio familiar se transforman en ultramarinos.',
                'img'   : 'images/timeline/1977.jpg'
            },
            {
                'date'  : '1981',
                'text'  : 'Juan Roig y su esposa, junto a sus hermanos Fernando, Trinidad y Amparo, compran Mercadona a su padre. La empresa cuenta con 8 tiendas de aproximadamente 300 m2 de sala de ventas. Juan Roig asume la dirección de la compañía, que inicia su actividad como empresa independiente.'
            },
            {
                'date'  : '1982',
                'text'  : 'Primera empresa en España en utilizar el escáner para la lectura del código de barras en los puntos de venta.',
                'imgbg' : 'images/timeline/1982.jpg'
            },
            {
                'date'  : '1986',
                'text'  : 'Implantación de la tarjeta de compra, de uso gratuito para "El Jefe".'
            },
            {
                'date'  : '1988',
                'text'  : 'Inauguración del bloque logístico de Ribaroja de Túria (Valencia), pionero en España por estar totalmente automatizado. Adquisición de Supermercados Superette, que contaba con 22 tiendas en Valencia.'
            },
            {
                'date'  : '1989',
                'text'  : 'Adquisición de Cesta Distribución y Desarrollo de Centros Comerciales, que permite a la compañía tener presencia en Madrid.',
                'img'   : 'images/timeline/1989.jpg'
            },
            {
                'date'  : '1990',
                'text'  : 'Juan Roig y Hortensia María Herrero pasan a ostentar la mayoría del capital de la compañía.'
            },
            {
                'date'  : '1991',
                'text'  : 'Adquisición de Dinos y Super Aguilar. Se inicia el Intercambio Electrónico de Datos (EDI) con proveedores.',
                'imgbg' : 'images/timeline/1991.jpg'
            },
            {
                'date'  : '1992',
                'text'  : 'Se alcanzan las cifras de 10.000 trabajadores y 150 tiendas.'
            },
            {
                'date'  : '1993',
                'text'  : 'Implantación de la estrategia comercial SPB (Siempre Precios Bajos), que más adelante derivará en el Modelo de Calidad Total.'
            },
            {
                'date'  : '1996',
                'text'  : 'Nacimiento de las marcas Hacendado, Bosque Verde, Deliplus y Compy. Apertura del supermercado número 200, en Segorbe (Castellón). Se firma el primer convenio de empresa para todos los trabajadores.',
                'img'   : 'images/timeline/1996.jpg'
            },
            {
                'date'  : '1997',
                'text'  : 'Acuerdo de unión con Almacenes Gómez Serrano, Antequera (Málaga).'
            },
            {
                'date'  : '1998',
                'text'  : 'Adquisición de Almacenes Paquer y de Supermercados Vilaró, ambos en Cataluña.',
                'imgbg' : 'images/timeline/1998.jpg'
            },
            {
                'date'  : '1999',
                'text'  : 'Finaliza el proceso, iniciado en 1995, de convertir en fijos a todos los miembros de la plantilla, que en esos momentos era de 16.825 trabajadores. Inauguración del bloque logístico de Antequera (Málaga). Se inicia el proyecto de nuevo diseño y modelo de perfumerías.'
            },
            {
                'date'  : '2000',
                'text'  : 'Construcción del bloque logístico de Sant Sadurní d’Anoia (Barcelona). Inauguración, en Massanassa (Valencia), de la primera Tienda por Ambientes. Celebración de la primera Reunión de Interproveedores. Firma del Convenio Colectivo de Empresa (2001-2005).',
                'img'   : ''
            },
            {
                'date'  : '2001',
                'text'  : 'Inauguración del primer centro educativo infantil gratuito para los hijos de los trabajadores, en el bloque logístico de Sant Sadurní d’Anoia (Barcelona). Mercadona alcanza las 500 tiendas con la apertura de su primer supermercado en Linares (Jaén).',
                'img'   : 'images/timeline/2001.jpg'
            },
            {
                'date'  : '2003',
                'text'  : 'Primera empresa en realizar una Auditoría Ética. Inauguración del bloque logístico de San Isidro (Alicante) y del segundo centro educativo infantil de la empresa. Lanzamiento de la nueva línea de perfume Hortensia H. Inauguración de un supermercado en las instalaciones del Mercat de l’Olivar, en Palma de Mallorca.'
            },
            {
                'date'  : '2004',
                'text'  : 'Inauguración del bloque logístico de Huévar (Sevilla) y del tercer centro educativo infantil de la empresa. El Comité de Dirección decide como norma general no abrir los supermercados los domingos.',
                'imgbg' : 'images/timeline/2004.jpg'
            },
            {
                'date'  : '2005',
                'text'  : 'Implantación del nuevo uniforme Mercadona. Inauguración del bloque logístico de Granadilla de Abona (Tenerife). Firma del nuevo Convenio Colectivo de Empresa para los próximos cuatro años (2006-2009).'
            },
            {
                'date'  : '2006',
                'text'  : 'Vigésimo quinto aniversario de la compañía. Inauguración de la tienda número 1.000 de la compañía, en Calp (Alicante). Relanzamiento de la nueva imagen de la Tarjeta Mercadona.'
            },
            {
                'date'  : '2007',
                'text'  : 'Puesta en marcha de la primera fase del bloque logístico Almacén Siglo XXI de Ciempozuelos (Madrid). Cuarta empresa del mundo mejor valorada en reputa- ción corporativa, de acuerdo con el estudio del Reputa- tion Institute de Nueva York.',
                'img'   : 'images/timeline/2007.jpg'
            },
            {
                'date'  : '2008',
                'text'  : 'Realineación de Mercadona con el Modelo de Calidad Total, quince años después de su implantación. Carro Menú para ofrecer a "El Jefe" el carro de la Compra Total de mayor calidad y más barato del mercado. Inauguración del bloque logístico de Ingenio (Gran Canaria).'
            },
            {
                'date'  : '2009',
                'text'  : 'Volver a la sencillez para tener un surtido eficaz haciendo lo que añade valor a "El Jefe". Firma del nuevo Convenio Colectivo de Empresa y Plan de Igualdad (2010-2013).',
                'imgbg' : 'images/timeline/2009.jpg'
            },
            {
                'date'  : '2010',
                'text'  : 'Modelo de gestión de Recursos Humanos basado en el Liderazgo y la Cultura del Esfuerzo: claves para ser una empresa de alto rendimiento y productividad.'
            },
            {
                'date'  : '2011',
                'text'  : 'Mercadona cumple treinta años de un modelo sostenible que pasa por hacer crecer a los cinco componentes de la compañía. Se inicia el cobro de las bolsas para adaptarse al Plan Nacional Integrado de Residuos.'
            },
            {
                'date'  : '2013',
                'text'  : 'Firma del Convenio Colectivo y Plan de Igualdad 2014-2018. Reinventarnos para ser más tenderos. Implantación nuevas secciones de frescos. Iniciar el desarrollo de la Cadena Agroalimentaria Sostenible de Mercadona. Inauguración del bloque logístico de Guadix (Granada). ',
                'img'   : 'images/timeline/2013.jpg'
            },
            {
                'date'  : '2014',
                'text'  : 'Apertura del supermercado 1.500, ubicado en la ciudad de Santander, en el barrio de Cazoña. Puesta en marcha del nuevo Centro de Proceso de Datos situado en Albalat dels Sorells (Valencia).'
            },
            {
                'date'  : '2015',
                'text'  : 'Nuevo Centro de Formación y Servicios en Albalat dels Sorells (Valencia). El modelo de innovación radical de Mercadona es reconocido internacionalmente.',
                'imgbg' : 'images/timeline/2015.jpg'
            },
            {
                'date'  : '2016',
                'text'  : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut laoreet nisi vitae ligula mollis tempor. Donec auctor consectetur nunc, ut condimentum sapien bibendum ac. Nam molestie, elit vitae vulputate rutrum, ex metus sollicitudin purus, eu tempus mi orci quis diam.'
            }
        ],
        'model'   : {
            'image' : 'images/model_mercadona.jpg',
            'title' : 'Modelo Mercadona',
            'desc'  : 'Mercadona es una compañía  de supermercados, de capital 100% español y familiar, que tiene por objetivo satisfacer las necesidades de sus clientes.',
            'button': 'Saber más'
        }
    }
