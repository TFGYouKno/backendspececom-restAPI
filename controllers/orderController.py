from flask import request, jsonify
from models.schema.orderSchema import order_schema, orders_schema
from services import orderService
from marshmallow import ValidationError
from cache import cache
from utils.util import user_validation, admin_required

@user_validation
def save(token_id): #always name the controller the same as the service it recruits
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    if token_id == order_data['customer_id']:
        new_order = orderService.save(order_data)
        return order_schema.jsonify(new_order), 201
    else:
        return jsonify({'message': 'You are not authorized to create an order for another user'}), 401

#@cache.cached(timeout=60) #caches the response for 60 seconds
@admin_required
def find_all():
    page= request.args.get('page')
    per_page = request.args.get('per_page')
    all_orders = orderService.find_all(page, per_page)
    return orders_schema.jsonify(all_orders), 200 #send them the list of customers and a 200 success status code

def find_by_id(order_id): #dynamic route takes in parameters
    
    order = orderService.find_by_id(order_id)
    
    return order_schema.jsonify(order), 200
@user_validation
def find_by_customer_id(customer_id, token_id): #dynamic route takes in parameters
    if customer_id == token_id:
        orders = orderService.find_by_customer_id(customer_id)
        return orders_schema.jsonify(orders), 200
    else:
        return jsonify({'message': 'You are not authorized to view another user\'s orders, you snoop'}), 401

def find_by_email(): #dynamic route takes in parameters
    email = request.json['email']
    if email:
        orders = orderService.find_by_email(email)
        return orders_schema.jsonify(orders), 200
    else:
        return jsonify({'message': 'Please input a valid e-mail'}), 404