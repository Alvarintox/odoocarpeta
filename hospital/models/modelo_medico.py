# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HospitalMedico(models.Model):
    _name = 'hospital.medico'
    _description = "Medicos del hospital"
    _rec_name = 'nombre'

    nombre = fields.Char("Nombre", required=True)
    apellidos = fields.Char("Apellidos",required=True)
    Num_colegiado = fields.Char("Num_colegiado",required=True)