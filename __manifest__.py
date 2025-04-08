{
    'name': 'Form Action on Website',
    'version': '1.0',
    'summary': 'Trigger custom actions when a form is submitted',
    'category': 'Website',
    'depends': ['website', 'mail'],  # mail = if you want to send emails
    'data': [
    'views/contact_form_template.xml',
    'views/menu.xml',  # <== nuevo archivo
    ],
    'installable': True,
    'application': True,
}
