# -*- coding: utf-8 -*-
{
    'name': 'Library Website',
    'description': 'Create and check book checkout requests.',
    'author': 'Alan Hou',
    'depends': [
        'library_checkout',
        'website',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/library_security.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/library_member.xml',
        'security/library_security.xml',
        'views/helloworld_template.xml',
        'views/website_assets.xml',
        'views/checkout_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
