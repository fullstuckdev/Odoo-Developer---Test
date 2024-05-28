from odoo import http
from odoo.http import request

class MaterialController(http.Controller):

    @http.route('/materials', type='json', auth='user')
    def list_materials(self):
        materials = request.env['material'].search([])
        return materials.read(['material_code', 'material_name', 'material_type', 'material_buy_price', 'related_supplier_id'])

    @http.route('/materials', type='json', methods=['POST'], auth='user')
    def create_material(self, **kwargs):
        material = request.env['material'].create({
            'material_code': kwargs.get('material_code'),
            'material_name': kwargs.get('material_name'),
            'material_type': kwargs.get('material_type'),
            'material_buy_price': kwargs.get('material_buy_price'),
            'related_supplier_id': kwargs.get('related_supplier_id')
        })
        return material.read(['material_code', 'material_name', 'material_type', 'material_buy_price', 'related_supplier_id'])

    @http.route('/materials/<int:material_id>', type='json', methods=['PUT'], auth='user')
    def update_material(self, material_id, **kwargs):
        material = request.env['material'].browse(material_id)
        if material:
            material.write({
                'material_code': kwargs.get('material_code'),
                'material_name': kwargs.get('material_name'),
                'material_type': kwargs.get('material_type'),
                'material_buy_price': kwargs.get('material_buy_price'),
                'related_supplier_id': kwargs.get('related_supplier_id')
            })
        return material.read(['material_code', 'material_name', 'material_type', 'material_buy_price', 'related_supplier_id'])

    @http.route('/materials/<int:material_id>', type='json', methods=['DELETE'], auth='user')
    def delete_material(self, material_id):
        material = request.env['material'].browse(material_id)
        if material:
            material.unlink()
        return {'status': 'success'}
