# -*- coding: utf-8 -*-
{
    'name': "المواعيد والخدمات الميدانية المتقدمة",
    'summary': "",
    'description': """
        نظام شامل لإدارة مهام الخدمة الميدانية والمختبرات مع ربط المنتجات بالمواعيد:

    """,
    'author': "المهندس / صالح الحجاني",
    'website': "https://www.facebook.com/salh.alhjany/?rdid=plWVCqF0AkDERe3g",
    'category': 'Services/Appointments',
    'version': '1.0',
    'depends': ['appointment', 'product', 'website_appointment', 'website_sale', 'web', 'sale_management', 'phone_validation', 'industry_fsm', 'stock', 'quality_control'],
    'data': [
        'security/ir.model.access.csv',
        'views/appointment_product_views.xml',
        'views/appointment_products_templates.xml',
        'views/project_task_signature_views.xml',
        'views/sale_order_question_views.xml',
        'views/portal_task_extra_views.xml',
        'views/project_task_question_views.xml',
        'views/product_template_service_views.xml',
        'views/project_task_service_views.xml',
        'views/project_task_form_views.xml',
        'views/report_task_extra_views.xml',
        'views/appointment_config_settings_views.xml',
        'data/fsm_task_sequence.xml',
        'data/hide_default_reports.xml',
        'views/stock_move_line_views.xml',
        'views/project_task_buttons.xml',
        'views/stock_picking_buttons.xml',
        'views/sale_order_buttons.xml',
        'views/stock_picking_report_custom.xml',
        'views/stock_picking_signature_views.xml',
        'views/stock_move_line_signature_views.xml',
        'views/product_labels_simple_enhancement.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            ('include', 'web._assets_helpers'),
            ('include', 'web._assets_frontend_helpers'),
            'web/static/lib/bootstrap/scss/_variables.scss',
            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/jquery/jquery.js',
            'appointment_products/static/src/js/appointment_products.js',
            'appointment_products/static/src/js/appointment_cart.js',
        ],
    },
    'icon': 'appointment_products/static/description/icon.svg',
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
