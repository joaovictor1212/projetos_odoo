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
    


class ComissoesConfiguracoes(models.Model):
    _name="comissoes.configuracoes"
    _description="Configuracao das comissões"
    _rec_name = "nivel"
    

    nivel = fields.Char(string="Nível")
    
    entidade = fields.Char(string=u"Entidade")
    
    tipo = fields.Char(string=u"Tipo")
    
    percentagem = fields.Char(string="Percentagem")
    