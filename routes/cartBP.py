from flask import Blueprint
from controllers.cartController import view_cart, add_to_cart, place_order, remove_item_from_cart, empty_cart

cart_blueprint = Blueprint('cart_bp', __name__)

cart_blueprint.route('/', methods =['GET'])(view_cart)
cart_blueprint.route('/', methods =['POST'])(add_to_cart)
cart_blueprint.route('/place-order', methods =['POST'])(place_order)
cart_blueprint.route('/', methods =['DELETE'])(remove_item_from_cart)
cart_blueprint.route('/empty-cart', methods =['DELETE'])(empty_cart)