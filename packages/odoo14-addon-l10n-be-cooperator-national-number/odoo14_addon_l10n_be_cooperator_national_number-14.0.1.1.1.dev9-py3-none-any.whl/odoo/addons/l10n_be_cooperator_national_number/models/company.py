# Copyright 2019 Coop IT Easy SCRL fs
#   Houssine Bakkali <houssine@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ResCompany(models.Model):
    _inherit = "res.company"

    display_national_number = fields.Boolean(string="Display National Number")
    require_national_number = fields.Boolean(string="Require National Number")

    @api.constrains("display_national_number", "require_national_number")
    def _check_national_number(self):
        for company in self:
            if company.require_national_number and not company.display_national_number:
                raise ValidationError(
                    _(
                        'If the "Require National Number" toggle is enabled,'
                        ' then so must the "Display National Number" toggle.'
                    )
                )

    @api.onchange("display_national_number")
    def _onchange_display_national_number(self):
        if not self.display_national_number:
            self.require_national_number = False
