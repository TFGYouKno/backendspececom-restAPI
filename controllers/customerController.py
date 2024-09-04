from flask import request, jsonify
from models.schema.customerSchema import customer_schema, customers_schema
from services import customerService
from marshmallow import ValidationError
from cache import cache


def save(): #always name the controller the same as the service it recruits
    try:
        customer_data = customer_schema.load(request.json)
        
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    customer = customerService.save(customer_data)
    return customer_schema.jsonify(customer), 201 #send them  the customer object and a 201 success status code

@cache.cached(timeout=60) #caches the response for 60 seconds
def find_all():
    page = request.args.get('page')
    per_page = request.args.get('per_page')
    all_customers = customerService.find_all(page, per_page)
    return customers_schema.jsonify(all_customers), 200


def find_by_id(id):
    customer = customerService.find_by_id(id)
    if not customer:
        return jsonify({'message': 'Customer not found'}), 404
    return customer_schema.jsonify(customer), 200

def update(id):
    try:
        customer_data = customer_schema.load(request.json)
        
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    customer = customerService.update(id, customer_data)
    if not customer:
        return jsonify({'message': 'Customer not found'}), 404
    return customer_schema.jsonify(customer), 200

def delete(id):
    customer = customerService.delete(id)
    if not customer:
        return jsonify({'message': 'Customer not found'}), 404
    return jsonify({'message': 'Customer deleted'}), 200