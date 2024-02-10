# -*- coding: utf-8 -*-
from odoo import fields, models, _, api, http
import json
from requests import request, Response



class ComissoesEstagios(models.Model):
    _name="comissoes.estagios"
    _description="Estágios das comissões"
    _rec_name = "nome_estagio"
    

    nome_estagio = fields.Char(string=u"Estágio")
    
    sequencia = fields.Integer(string=u"Sequência")
    
    fold = fields.Boolean(string="Aparecer no kanban")
    