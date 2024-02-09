# -*- coding: utf-8 -*-
from odoo import fields, models, _, api, http
import json
from requests import request, Response



class Comissoes(models.Model):
    _name="comissoes"
    _description="Registros Comissões"
    _rec_name = "nome_venda"
    
    
    nome_venda = fields.Char(string=u'Venda')
    
    id_oportunidade = fields.Char(string="Id da oportunidade")
    
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
    
    
    