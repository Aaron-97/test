# -*- coding: utf-8 -*-
{
    'name': "Library Book Borrowing",
    'description': 'Members can borrow books from the library.',
    'author': 'Alan Hou',
    'depends': ['library_member', 'mail'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/library_menu.xml',
        'views/checkout_view.xml',
        'data/library_checkout_stage.xml',
        'views/checkout_kanban_view.xml',
        'views/checkout_kanban_assets.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
