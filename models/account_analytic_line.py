from odoo import models, fields, api
from datetime import datetime
import math

class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    # Campos para la Vista Tree
    start_stop = fields.Boolean(
        string='Start Stop'
    )
    date_start = fields.Datetime(
        string='Start Time'
    )
    date_stop = fields.Datetime(
        string='End Time'
    )
    date_reboot = fields.Datetime(
        string='Reboot Time'
    )

    @api.multi
    def action_start(self):
        if self.date_start == False: # Si la línea nunca se ha inicializado
            return self.write({'date_start': datetime.now(), 'start_stop': True})
        else: # Si la línea está pausada
            return self.write({'date_reboot': datetime.now(), 'start_stop': True})

    @api.multi
    def count_time(self):
        if self.date_reboot: # Se está parando una línea reiniciada
            datetime_diff = datetime.now() - self.date_reboot
            self.date_reboot = False
        else: # Se está parando una línea que no ha sido reiniciada
            datetime_diff = datetime.now() - self.date_start
        
        minutes, seconds = divmod(datetime_diff.total_seconds(), 60) # Convertimos los segundos en minutos
        hours, minutes = divmod(minutes, 60) # Convertimos los minutos en horas
        # Damos formato a la hora
        dur_hours = (('%0*d') % (2, hours))
        dur_minutes = (('%0*d') % (2, minutes * 1.677966102))
        duration = dur_hours + '.' + dur_minutes

        total = self.unit_amount + float(duration) # Sumamos la duración actual con la recién calculada
        return total

    @api.multi
    def action_pause(self):
        return self.write({
            'start_stop': False,
            'unit_amount': self.count_time(),
        })

    @api.multi
    def action_stop(self):
        if self.start_stop == False: # Si la línea está pausada
            return self.write({'date_stop': datetime.now(),})
        else: # Si la línea está activa
            return self.write({
                'start_stop': False,
                'date_stop': datetime.now(),
                'unit_amount': self.count_time(),
            })