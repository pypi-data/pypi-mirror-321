# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/AGPL).

from odoo import api, models


class ServiceQuotation(models.Model):
    _name = "service.quotation"
    _inherit = [
        "service.quotation",
        "mixin.state_change_constrain",
        "mixin.status_check",
    ]

    _status_check_create_page = True

    @api.onchange("type_id")
    def onchange_status_check_template_id(self):
        self.status_check_template_id = False
        if self.type_id:
            self.status_check_template_id = self._get_template_status_check()

    # @api.model_create_multi
    # def create(self, vals_list):
    #     _super = super(ServiceQuotation, self)
    #     quotation = _super.create(vals_list)
    #     quotation.action_reload_status_check_template()
    #     quotation.action_reload_status_check()
    #     return quotation
