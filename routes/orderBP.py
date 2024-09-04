from flask import Blueprint

from controllers.orderController import save, find_all

order_blueprint = Blueprint('orders', __name__)

#URL prefix for this blueprint is /orders

order_blueprint.route('/', methods=['POST'])(save) #when a POST request is made to /orders/save, run the save function in the orderController

order_blueprint.route('/', methods=['GET'])(find_all) #when a GET request is made to /orders, run the find_all function in the orderController
