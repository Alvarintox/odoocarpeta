# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HospitalDiagnostico(models.Model):
    _name = "hospital.diagnostico"
    _description = "Diagnostico de los pacientes"

    paciente = fields.Many2one('hospital.paciente', string="Paciente")
    medico = fields.Many2many('hospital.medico', string="Atención")
    diagnostico = fields.Text(string="Diagnostico")