# -*- coding: utf-8 -*-
from odoo import fields, models, _, api, http
import json
from requests import request, Response



class ComissoesEstagios(models.Model):
    _name="comissoes.estagios"
    _description="Estágios das comissões"
    _rec_name = "nome_estagio"
    _order = "sequencia"
    

    nome_estagio = fields.Char(string=u"Estágio")
    
    sequencia = fields.Integer(string=u"Sequência")
    
    fold = fields.Boolean(string="Aparecer no kanban")
    
    cor = fields.Selection(selection=[
        ('blocked', 'Vermelho'),
        ('normal', 'Cinza'),
        ('done', 'Verde'),
    ], copy=False, default='normal' )
    
    
    @api.constrains('cor')
    def validar_cor_nas_comissoes(self):
        import ipdb;ipdb.set_trace(context=10)
        estagio_ids = []
        estagio_ids = self.env['comissoes.estagios'].search([('name','!=',self.nome_estagio),('id','!=',self.id)])
        
        if estagio_ids:
            for estagio_id in estagio_ids:
                pass
    


class ComissoesConfiguracoes(models.Model):
    _name="comissoes.configuracoes"
    _description="Configuracao das comissões"
    _rec_name = "nivel"
    

    nivel = fields.Char(string="Nível")
    
    entidade = fields.Char(string=u"Entidade")
    
    tipo = fields.Char(string=u"Tipo")
    
    percentagem = fields.Char(string="Percentagem")
    