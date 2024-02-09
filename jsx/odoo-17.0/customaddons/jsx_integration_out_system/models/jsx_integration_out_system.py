# -*- coding: utf-8 -*-
from odoo import fields, models, _, api, http
import json
from requests import request, Response



class JsxIntegrationOutSystemConfiguration(models.Model):
    _name="jsx.integration.configuration"
    _description="Modulo de configuracao da integracao"
    _rec_name = "server"
    
    
    
    database = fields.Char(string="Banco de dados")
    server = fields.Char(string="Servidor")
    door = fields.Char(string="Porta")
    user = fields.Char(string="Usuário")
    password = fields.Char(string="Senha")
    
    
    
class JsxIntegrationOutSystemLogs(models.Model):
    _name="jsx.integration.logs"
    _description="Modulo de configuracao da integracao"
    
    
    body = fields.Char(string="Corpo")
    message = fields.Text(string="Mensagem")
    code = fields.Char(string="Código")
    
    
    def function_request_integration(self):
        response = None
        
        # ESCREVER REQUISIÇÃO PARA PREENCHER OS CAMPOS
        
        # ===================================
        self.env['jsx.integration.logs'].create({
            'body':response.body,
            'code': response.code,
            'message':response.message,
        })
    
    


