# -*- coding: utf-8 -*-
{
    'name': "Automatics Hours for Timesheets",
    'summary': """
       Añade la funcionalidad de play, pause and stop a los partes de horas que permiten calcular las horas de manera automática.
       """,
    'author': "Inma Sánchez",
    'website': "https://github.com/EDallas89",
    'category': 'Timesheet',
    'version': '12.0',
    'depends': ['account','simple_timesheet_helpdesk_ticket', 'helpdesk_mgmt'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/helpdesk_ticket_timesheet.xml',
    ],
    'installable': True,
    'application': True,
}