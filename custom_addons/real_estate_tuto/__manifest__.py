{
    'name': 'Property Management 2',#The only required field 
    'version': '1.0',
    'category': 'custom',
    'summary': 'Manage properties',
    'description': 'A simple module to manage properties.',
    'author': 'omar',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/estate_property_views.xml'
        ],
    'installable': True,
    'application': True,
}
