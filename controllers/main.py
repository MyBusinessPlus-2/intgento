from odoo import http
from odoo.http import request

class ContactFormController(http.Controller):

    @http.route('/contact-me', type='http', auth='public', website=True)
    def contact_form(self, **kw):
        return request.render('form_action_website.contact_form_template', {})

    @http.route('/submit-contact-form', type='http', auth='public', methods=['POST'], csrf=False)
    def submit_form(self, **post):
        name = post.get('name')
        email = post.get('email')
        message = post.get('message')

        # Example Action: Create a lead (CRM must be installed)
        request.env['crm.lead'].sudo().create({
            'name': f"Website Inquiry from {name}",
            'contact_name': name,
            'email_from': email,
            'description': message,
        })

        # You can also send an email, create records, etc.

        return request.redirect('/thanks')  # Create a /thanks page if you want
