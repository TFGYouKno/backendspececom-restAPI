from flask import Blueprint

from controllers.productController import save, find_all, find_by_id, update, delete

product_blueprint = Blueprint('products', __name__)

#URL prefix for this blueprint is /products

product_blueprint.route('/', methods=['POST'])(save) #when a POST request is made to /products/save, run the save function in the productController

product_blueprint.route('/', methods=['GET'])(find_all) #when a GET request is made to /products, run the find_all function in the productController

product_blueprint.route('/<int:id>', methods=['GET'])(find_by_id) #when a GET request is made to /products/<id>, run the find_by_id function in the productController

product_blueprint.route('/<int:id>', methods=['PUT'])(update) #when a PUT request is made to /products/<id>, run the update function in the productController

product_blueprint.route('/<int:id>', methods=['DELETE'])(delete) #when a DELETE request is made to /products/<id>, run the delete function in the productController