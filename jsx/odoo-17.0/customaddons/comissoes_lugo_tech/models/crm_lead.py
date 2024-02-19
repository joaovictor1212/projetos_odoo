# -*- coding: utf-8 -*-
from odoo import fields, models, _, api, http
import json
from requests import request, Response



class CrmLead(models.Model):
    _inherit ="crm.lead"
    
    
    comercial_interno_cir = fields.Char(string="Comercial Interno Rua (CIR)")
    comercial_interno_bo = fields.Char(string="Comercial Interno BO")
    id_proposta_edp = fields.Char(string="ID da Proposta EDP")
    id_oportunidade_edp = fields.Char(string="ID da Oportunidade EDP")
    id_cpe = fields.Char(string="ID&CPE")