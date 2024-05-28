from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestMaterial(TransactionCase):

    def setUp(self):
        super(TestMaterial, self).setUp()
        self.supplier = self.env['supplier'].create({'name': 'Test Supplier'})
        self.material = self.env['material'].create({
            'material_code': 'TEST01',
            'material_name': 'Test Material',
            'material_type': 'fabric',
            'material_buy_price': 150,
            'related_supplier_id': self.supplier.id
        })

    def test_material_creation(self):
        self.assertEqual(self.material.material_code, 'TEST01')
        self.assertEqual(self.material.material_name, 'Test Material')
        self.assertEqual(self.material.material_type, 'fabric')
        self.assertEqual(self.material.material_buy_price, 150)
        self.assertEqual(self.material.related_supplier_id, self.supplier)

    def test_material_buy_price_constraint(self):
        with self.assertRaises(ValidationError):
            self.env['material'].create({
                'material_code': 'TEST02',
                'material_name': 'Invalid Material',
                'material_type': 'cotton',
                'material_buy_price': 50,
                'related_supplier_id': self.supplier.id
            })
