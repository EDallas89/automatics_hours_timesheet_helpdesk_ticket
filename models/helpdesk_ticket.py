from odoo import models, fields, api

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    timesheet_ids = fields.One2many(
        comodel_name='account.analytic.line',
        inverse_name='ticket_id',
        string='Timesheet',
    )

#    total_computed_hours_ticket = fields.Float(
#        compute='compute_hours',
#        string='Computed Hours'
#    )
#
#    def compute_hours(self):
#        for record in self:
#            record.total_computed_hours_ticket = \
#                sum(record.mapped('timesheet_ids.computed_hours'))