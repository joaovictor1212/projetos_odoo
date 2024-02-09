{
    "name": "Assinaturas",
    "description": "Assinaturas",
    "summary": "Assinaturas",
    "author": "DevFazer",
    "depends": [
        'base',
        'account',
        'analytic'
    ],
    "data": [
        'data/purchase_contract_data.xml',
        'security/purchase_subscription_security.xml',
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/res_partner_views.xml',
        'views/purchase_subscription_views.xml',
        'views/account_invoice_views.xml',
    ],    
    "installable": True,
    "application": True
}
