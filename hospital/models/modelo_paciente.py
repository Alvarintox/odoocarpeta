# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HospitalPaciente(models.Model):
    _name = 'hospital.paciente'
    _description = "Paciente del hospital"
    _rec_name = 'nombre'

    nombre = fields.Char("Nombre", required=True)
    apellidos = fields.Char("Apellidos",required=True)
    sintomas = fields.Char("sintomas",required=True)