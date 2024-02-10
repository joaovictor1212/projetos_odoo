{
    'name': 'Autos Lugo.tech', 
    'summary': 'Modulo para controle de comissões',
    'description': '''
        
    ''',
    'version': '1.0.0', 
    'category': 'Tools/UI',
    'license': 'LGPL-3', 
    'author': 'João Victor',
    'depends': [
        'base', 
        'crm',
    ],
    'data': [
        
        'security/ir.model.access.csv',
        
        
        'views/comissoes.xml',
        'views/configuracoes.xml',
        'views/menu_item.xml',
        
    ],
   
    'installable': True,
    'application': False,
    'assets': {
        'web.assets_backend': [
            'comissoes_lugo_tech/static/src/js/assets.xml',
        ],
    },
}
