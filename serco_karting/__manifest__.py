# -*- coding: utf-8 -*-
{
    'name': "SercoKarting",

    'summary': """
        Gestion de un karting""",

    'description': """
        Modulo que nos ayudara en la gestion de nuestro karting.\n
        - Podremos manejar nuestros empleados.\n
        - Llevar el mantenimiento de nuestros vehiculos y pista.\n
        - Llevar un registro mas facil de la gestion de nuestras Compteciones y clientes mas fieles.\n
        - Una pequeña gestion de un bar en caso de que lo tengamos.\n
    """,

    'author': "Sergio Lopez",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
