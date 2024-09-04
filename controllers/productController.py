from flask import request, jsonify
from models.schema.productSchema import product_schema, products_schema
from services import productService
from marshmallow import ValidationError
from cache import cache


def save(): #always name the controller the same as the service it recruits
    try:
        product_data = product_schema.load(request.json)
        
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    product = productService.save(product_data)
    return product_schema.jsonify(product), 201 #send them  the product object and a 201 success status code

@cache.cached(timeout=60) #caches the response for 60 seconds
def find_all():
    page= request.args.get('page')
    per_page = request.args.get('per_page')
    all_products = productService.find_all(page, per_page)
    return products_schema.jsonify(all_products), 200 #send them the list of products and a 200 success status code

def find_by_id(id):
    product = productService.find_by_id(id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    return product_schema.jsonify(product), 200

def update(id):
    try:
        product_data = product_schema.load(request.json)
        
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    product = productService.update(id, product_data)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    return product_schema.jsonify(product), 200

def delete(id):
    
    product = productService.delete(id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    return jsonify({'message': f'Product {product.id} deleted'}), 200