from odoo import models

class WebsiteFormActionCustom(models.Model):
    _inherit = 'website.form.builder.model'

    def _get_form_builder_models(self):
        actions = super()._get_form_builder_models()

        # Agrega tu acción personalizada al listado
        actions.append({
            'model': 'custom.form',  # Este es tu modelo (debes tenerlo creado)
            'label': 'Create Custom Form Record',
            'actions': [{
                'label': 'Create Custom Record',
                'action': 'create',
            }]
        })
        return actions
