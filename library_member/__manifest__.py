# -*- coding: utf-8 -*-
{
    'name': "Library Members",
    'description': "Manage people who will be able to borrow books.",
    'author': "Alan Hou",
    'depends': ['library_app', 'mail'],
    # always loaded
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/book_view.xml',
        'views/library_menu.xml',
        'views/member_view.xml',
        'views/book_list_template.xml',
        'data/book_demo.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
