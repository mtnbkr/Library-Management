# -*- coding: utf-8 -*-
{
    'name': "Libary Management",

    'summary': """
        They need their books!""",

    'description': """
        Brussels' library wants to use Odoo to manage their books and customers
    """,

    'author': "Darren Klinefelter",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/librarymanagement.xml',
        'reports/report_library_management.xml',
        'reports/library_management_report.xml',
        'data/sequence_data.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
