from flask import Flask, Blueprint
from database import db
from models.schema import ma
from limiter import limiter
from cache import cache


#models
from models.customer import Customer
from models.order import Order
from models.product import Product
from models.orderProduct import order_product

#blueprints
from routes.customerBP import customer_blueprint
from routes.orderBP import order_blueprint
from routes.productBP import product_blueprint

def create_app(config_name):

    app = Flask(__name__) #instantiate the flask app
    app.config.from_object(f'config.{config_name}') #load the config file into the app
    db.init_app(app) #initialize the db with the app
    ma.init_app(app) #initialize the marshmallow with the app
    blueprint_config(app) #configure the blueprints
    rate_limiter_config(app) #configure the rate limiter
    cache.init_app(app) #initialize the cache with the app

    return app

def blueprint_config(app):
    app.register_blueprint(customer_blueprint, url_prefix="/customers") #register the customer blueprint
    app.register_blueprint(order_blueprint, url_prefix="/orders") #register the order blueprint
    app.register_blueprint(product_blueprint, url_prefix="/products") #register the product blueprint

def rate_limiter_config(app):
    limiter.init_app(app) #initialize the limiter with the app
    limiter.limit("500 per hour")(customer_blueprint) #limit the customer blueprint to 500 requests per hour

#create runner
if __name__ == '__main__': #if this file is run as the main file
    app = create_app('DevelopmentConfig') #create the app using the DevelopmentConfig
    
    with app.app_context(): #create a context for the app
        db.create_all()

    app.run(debug=True) #run the app