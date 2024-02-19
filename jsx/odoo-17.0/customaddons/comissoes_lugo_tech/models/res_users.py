# -*- coding: utf-8 -*-
from odoo import fields, models, _, api, http
import json
from requests import request, Response



class ResUsers(models.Model):
    _inherit ="res.users"
    
    codigo_edp = fields.Char(string="Código EDP")
    modelo_comissional = fields.Many2one(comodel_name='comissoes.configuracoes', string="Modelo Comissional")