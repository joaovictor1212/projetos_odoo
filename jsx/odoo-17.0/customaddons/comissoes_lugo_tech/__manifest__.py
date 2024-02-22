{
    'name': 'Autos Lugo.tech', 
    'summary': 'Modulo para controle de comissões',
    'description': '''
        Módulo de controle de comissões
    ''',
    'version': '1.0.0', 
    'category': 'Tools/UI',
    'license': 'LGPL-3', 
    'author': 'Typing Solutions',
    'depends': [
        'base',
        'crm',
        'web'
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/comissoes.xml',
        'views/configuracoes.xml',
        'views/res_users.xml',
        'views/crm_lead.xml',
        'views/menu_item.xml',
    ],
    # 'qweb': [
    #     'static/src/xml/radio_button_widget.xml',
    # ],
    'installable': True,
    'application': True,
    # 'assets': {
    #     'web.assets_backend': [
    #         'comissoes_lugo_tech/static/src/js/assets.xml',
    #     ],
    # },
}