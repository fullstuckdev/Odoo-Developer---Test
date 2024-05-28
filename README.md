# Material Management Module for Odoo 14

## Overview

The Material Management module is a project test for Odoo developers, designed to assess their skills in managing materials and their associated suppliers within Odoo 14. This module provides RESTful API endpoints to create, read, update, and delete materials.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/fullstuckdev/Odoo-Developer-Test

2. Update the Odoo Configuration:
   Ensure the Odoo configuration file (odoo.conf) includes the path to the custom_addons directory:
   ```bash
   [options]
   addons_path = addons_path,custom_addons

3. Restart Odoo:
   Restart your Odoo server to load the new module:
   ```bash
   odoo-bin -c /etc/odoo/odoo.conf

4. Install the Module:
   Go to the Apps menu in Odoo, search for Material Management, and install it.

5. Models: <br>
  Material (table) <br>
 
  ```bash
  material_code: String (required) 
  material_name: String (required) 
  material_type: Selection (required: Fabric, Jeans, Cotton) 
  material_buy_price: Float (required, must be ≥ 100) 
  related_supplier_id: Many2one (required, relation to Supplier)
  ```

  Supplier (table) <br>
 
  ```bash
  name: String (required)
  ```

6. API Endpoints: <br>
  - List Materials <br>
  URL: /materials <br>
  Method: GET <br>
  Response: JSON array of material objects <br>

  Example Request: <br>
  ```bash
  curl -X GET http://localhost:8069/materials
  ```
  Example Response:
  ```
  [
  {
    "id": 1,
    "material_code": "MAT001",
    "material_name": "Sample Material",
    "material_type": "fabric",
    "material_buy_price": 150.0,
    "related_supplier_id": [1, "Sample Supplier"]
  },
  {
    "id": 2,
    "material_code": "MAT002",
    "material_name": "Another Material",
    "material_type": "cotton",
    "material_buy_price": 200.0,
    "related_supplier_id": [2, "Another Supplier"]
  }
]
```
- Create Material <br>
URL: /materials <br>
Method: POST <br>
Request Body: JSON object with material details <br>
Response: JSON object of the created material <br>

Example Request: <br> 
```
curl -X POST http://localhost:8069/materials -H "Content-Type: application/json" -d '{
    "material_code": "MAT001",
    "material_name": "Sample Material",
    "material_type": "fabric",
    "material_buy_price": 150,
    "related_supplier_id": 1
}'
```


- Update Material <br>
URL: /materials/<material_id> <br>
Method: PUT <br>
Request Body: JSON object with updated material details <br>
Response: JSON object of the updated material <br>

Example Request: <br> 
```
curl -X PUT http://localhost:8069/materials/1 -H "Content-Type: application/json" -d '{
    "material_code": "MAT001",
    "material_name": "Updated Material",
    "material_type": "jeans",
    "material_buy_price": 200,
    "related_supplier_id": 1
}'
```

- Delete Material <br>
URL: /materials/<material_id> <br>
Method: DELETE <br>
Response: JSON object with status <br>

Example Request: <br>
```
curl -X DELETE http://localhost:8069/materials/1
```

Example Response: <br>
```
{
  "status": "success"
}
```








