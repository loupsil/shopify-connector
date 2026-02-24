# -*- coding: utf-8 -*-
{
    'name': 'Dasolo Shopify Connector',
    'version': '18.0.1.0.0',
    'category': 'Sales',
    'summary': 'Connect your Shopify store with Odoo seamlessly',
    'description': """
Dasolo Shopify Connector
========================

Seamlessly synchronize your Shopify store with Odoo.

**Key Features:**
- Automatic product and order synchronization
- API-based architecture following Odoo & Shopify best practices
- Works with Odoo Online, Odoo.sh, and on-premise
- Upgrade resilient: updates don't break the integration
- Native Odoo interface integration

For more information, visit https://www.dasolo.ai/odoo-shopify-connector
    """,
    'author': 'Dasolo',
    'website': 'https://www.dasolo.ai/',
    'license': 'Other proprietary',
    'depends': ['base', 'web'],
    'data': [
        'views/shopify_connector_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'dasolo_shopify_connector/static/src/css/shopify_connector.css',
            'dasolo_shopify_connector/static/src/js/shopify_connector.js',
            'dasolo_shopify_connector/static/src/xml/shopify_connector.xml',
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
