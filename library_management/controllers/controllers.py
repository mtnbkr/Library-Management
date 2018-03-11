# -*- coding: utf-8 -*-
from odoo import http

# class /home/darren/libraryManagement(http.Controller):
#     @http.route('//home/darren/library_management//home/darren/library_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//home/darren/library_management//home/darren/library_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/home/darren/library_management.listing', {
#             'root': '//home/darren/library_management//home/darren/library_management',
#             'objects': http.request.env['/home/darren/library_management./home/darren/library_management'].search([]),
#         })

#     @http.route('//home/darren/library_management//home/darren/library_management/objects/<model("/home/darren/library_management./home/darren/library_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/home/darren/library_management.object', {
#             'object': obj
#         })