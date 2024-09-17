from flask import Blueprint

from controllers.orderController import save, find_all, find_by_id, find_by_customer_id, find_by_email

order_blueprint = Blueprint('orders', __name__)

#URL prefix for this blueprint is /orders

order_blueprint.route('/', methods=['POST'])(save) #when a POST request is made to /orders/save, run the save function in the orderController

order_blueprint.route('/', methods=['GET'])(find_all) #when a GET request is made to /orders, run the find_all function in the orderController

order_blueprint.route('/<int:order_id>', methods=['GET'])(find_by_id) #when a GET request is made to /orders/<order_id>, run the find_by_id function in the orderController

order_blueprint.route('customer/<int:customer_id>', methods=['GET'])(find_by_customer_id) #when a GET request is made to /orders/customer/<customer_id>, run the find_by_customer_id function in the orderController

order_blueprint.route('/customer-email', methods=['POST'])(find_by_email) #when a POST request is made to /orders/customer-email, run the find_by_email function in the orderController