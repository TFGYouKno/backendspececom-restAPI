from database import db #services interact directly with the database
from models.product import Product #need to create product objects
from models.schema.productSchema import product_schema #need to create product objects
from sqlalchemy import select #so we can query our database
from flask import request,jsonify #to get the request data and return a response

def save(product_data):
    
    new_product = Product(product_name=product_data['product_name'], price=product_data['price']) #create a new product object
    db.session.add(new_product) #add the new product to the session
    db.session.commit() #commit the new product to the database
    
    db.session.refresh(new_product) #refresh the session with the new product
    return new_product #return the new product

def find_all(page=1, per_page=10):
    query = select(Product) #select all products
    all_products = db.paginate(query, page=int(page,), per_page=int(per_page)) 
    #to execute a query with pagination, the url model looks like this: customers/?page=1&per_page=10
    
    return all_products #return all the productss

def find_by_id(id):
    query = select(Product).where(Product.id == id) #select the product with the given id
    product = db.session.execute(query).scalars().first() #execute the query and get the product with the given id
    
    return product #return the product with the given id

def update(id, product_data):
    query = select(Product).where(Product.id == id) #select the product with the given id
    product = db.session.execute(query).scalars().first() #execute the query and get the product with the given id
    
    if not product:
        return None
    
    product.product_name = product_data['product_name']
    product.price = product_data['price']

    db.session.commit() #commit the updated product to the database
    
    db.session.refresh(product) #refresh the session with the updated product
    return product #return the updated product

def delete(id):
    query = select(Product).where(Product.id == id) #select the product with the given id
    product = db.session.execute(query).scalars().first() #execute the query and get the product with the given id
    
    if not product:
        return None
    
    db.session.delete(product) #delete the product with the given id
    db.session.commit() #commit the deletion of the product
    
    return product #return the deleted product