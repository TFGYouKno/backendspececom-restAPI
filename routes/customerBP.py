from flask import Blueprint

from controllers.customerController import save, find_all, find_by_id, update, delete, login

customer_blueprint = Blueprint('customer', __name__)

#URL prefix for this blueprint is /customers

customer_blueprint.route('/', methods=['POST'])(save) #when a POST request is made to /customers/save, run the save function in the customerController

customer_blueprint.route('/', methods=['GET'])(find_all) #when a GET request is made to /customers, run the find_all function in the customerController

customer_blueprint.route('/<int:id>', methods=['GET'])(find_by_id) #when a GET request is made to /customers/<id>, run the find_by_id function in the customerController

customer_blueprint.route('/<int:id>', methods=['PUT'])(update) #when a PUT request is made to /customers/<id>, run the update function in the customerController

customer_blueprint.route('/<int:id>', methods=['DELETE'])(delete) #when a DELETE request is made to /customers/<id>, run the delete function in the customerController

customer_blueprint.route('/login', methods=['POST'])(login) #when a POST request is made to /customers/login, run the login function in the customerController