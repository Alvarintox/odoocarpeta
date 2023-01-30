# -*- coding: utf-8 -*-
{
    'name': "Lista de tareas",

    'summary': """
        Esto es una lista de tareas muy sencilla-"Joan Melsion" """,

    'description': """
        Sencilla lista de tareas utilizadas para crear un nuevo modulo del odoo de los cojones con un nuevo modelos de datos-"Joan Melsion"
    """,

    'author': "Alvarinto",
    'website': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml'
    ]
}
