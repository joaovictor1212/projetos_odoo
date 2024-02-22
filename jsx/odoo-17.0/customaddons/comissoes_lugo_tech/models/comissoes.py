# -*- coding: utf-8 -*-
from odoo import fields, models, _, api, http, SUPERUSER_ID
import json
from requests import request, Response





class Comissoes(models.Model):
    _name="comissoes"
    _description="Registros Comissões"
    _rec_name = "nome_venda"
    
    
    nome_venda = fields.Char(string=u"Venda")
    
    id_oportunidade = fields.Many2one(comodel_name='crm.lead', string="Id da oportunidade")
    
    id_proposta = fields.Char(string="Id da proposta")
    
    id_cpe = fields.Char(string=u"ID&CPE")
    
    canal_angariacao = fields.Char(string=u"Canal de Angariação")
    
    cpe = fields.Char(string="CPE")
    
    segmento = fields.Char(string="Segmento")
    
    nipc = fields.Char(string="NIPC")
    
    tipo_comissao = fields.Char(string=u"Tipo de comissão")
    
    ciclo = fields.Char(string=u"Ciclo")
    
    comissao_lugo_tech = fields.Float(string=u"Comissão LugoTech")
    
    comissao_interno = fields.Float(string=u"Comissão Interno")
    
    comissao_parceiro = fields.Float(string=u"Comissão Parceiro")
    
    def default_id_estagio(self):
        filtered_id_estagio = self.env['comissoes.estagios'].search([], order="sequencia", limit=1)
        return filtered_id_estagio and filtered_id_estagio.id or False

    id_estagio = fields.Many2one(comodel_name='comissoes.estagios', string="Estagio", default=default_id_estagio, group_expand='_read_group_id_estagio_ids', tracking=1)

    @api.model
    def _read_group_id_estagio_ids(self, id_estagio, domain, order):
        search_domain = []
        stage_ids = id_estagio._search(search_domain, order='sequencia', access_rights_uid=SUPERUSER_ID)
        return id_estagio.browse(stage_ids)

    cor = fields.Selection(selection=[
        ('blocked', 'Vermelho'),
        ('normal', 'Cinza'),
        ('done', 'Verde'),
    ], copy=False, default='normal' )
    
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'High'),
    ], default='0', index=True, string="Priority", tracking=True)
    
    arquivo = fields.Binary(attachment=True, string="Arquivo")
    
    
    @api.onchange('id_estagio')
    def change_status_kanban(self):
        if self.id_estagio.cor == 'blocked':
            self.cor = 'blocked'
        elif self.id_estagio.cor == 'done':
            self.cor = 'done'
        else:
            self.cor = 'normal'
            
    
    