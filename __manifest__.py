{
    'name': 'Form Action on Website 2',
    'version': '1.0',
    'summary': 'Trigger custom actions when a form is submitted',
    'category': 'Website',
    'depends': ['website', 'mail', 'crm'],  # mail = if you want to send emails
    'data': [
        'views/contact_form_template.xml',
        'views/menu.xml',  # <== nuevo archivo
        'views/forms_action.xml',
    ],
    'installable': True,
    'application': True,
}
