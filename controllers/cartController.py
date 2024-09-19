from flask import request, jsonify
from models.schema.cartSchema import cart_schema, carts_schema, view_cart_schema

from services import cartService
from marshmallow import ValidationError
from utils.util import user_validation
from database import db
from models.product import Product

@user_validation
def view_cart(token_id):
    try:
        cart_items = cartService.view_cart(token_id)
        print(f"Cart items: {cart_items}")

    except Exception as e:
        return jsonify({'message': str(e)}), 400
    
    return view_cart_schema.jsonify({"products": cart_items}), 200

@user_validation
def place_order(token_id):
    try:
        new_order = cartService.place_order(token_id)

        return jsonify({
            "message": "Order placed successfully",
            "order-id": new_order.id,
            "order-date": new_order.date
        }),201
    
    except ValueError:
        return jsonify({"error": str(e)}), 404
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@user_validation
def add_to_cart(token_id):
    try:
        cart_data = cart_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    try:
        added_product = cartService.add_items_to_cart(token_id, cart_data)
        return jsonify({"message": "Added to cart!"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
@user_validation
def remove_item_from_cart(token_id):
    try:
        cart_data = request.json
        if "product_ids" not in cart_data:
            return jsonify({"error": "Product IDs are required"}), 400 
        cart_data = cart_schema.load(cart_data)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    try:
        cartService.remove_item_from_cart(token_id, cart_data)
        return jsonify({"message": "Removed from cart!"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
@user_validation
def empty_cart(token_id):
    try:
        cartService.empty_cart(token_id)
        return jsonify({"message": "Cart emptied!"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400


