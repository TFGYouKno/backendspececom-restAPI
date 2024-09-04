from flask import request, jsonify
from models.schema.orderSchema import order_schema, orders_schema
from services import orderService
from marshmallow import ValidationError
from cache import cache


def save(): #always name the controller the same as the service it recruits
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    new_order = orderService.save(order_data)
    return order_schema.jsonify(new_order), 201 #send them  the customer object and a 201 success status code

@cache.cached(timeout=60) #caches the response for 60 seconds
def find_all():
    all_orders = orderService.find_all()
    return orders_schema.jsonify(all_orders), 200 #send them the list of customers and a 200 success status code