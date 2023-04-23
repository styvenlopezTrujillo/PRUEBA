# -*- coding: utf-8 -*-
# from odoo import http


# class Develoger(http.Controller):
#     @http.route('/develoger/develoger', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/develoger/develoger/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('develoger.listing', {
#             'root': '/develoger/develoger',
#             'objects': http.request.env['develoger.develoger'].search([]),
#         })

#     @http.route('/develoger/develoger/objects/<model("develoger.develoger"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('develoger.object', {
#             'object': obj
#         })
