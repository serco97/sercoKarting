# -*- coding: utf-8 -*-
from odoo import http

# class SercoKarting(http.Controller):
#     @http.route('/serco_karting/serco_karting/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/serco_karting/serco_karting/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('serco_karting.listing', {
#             'root': '/serco_karting/serco_karting',
#             'objects': http.request.env['serco_karting.serco_karting'].search([]),
#         })

#     @http.route('/serco_karting/serco_karting/objects/<model("serco_karting.serco_karting"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('serco_karting.object', {
#             'object': obj
#         })