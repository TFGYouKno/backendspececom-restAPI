from database import db #services interact directly with the database
from models.order import Order #need to create customer objects
from models.product import Product #need to create product objects
from sqlalchemy import select #so we can query our database
from datetime import date #so we can get the current date

def save(order_data):
    
    new_order = Order(customer_id=order_data['customer_id'], date=date.today())
    for item_id in order_data['product_ids']:
        query = select(Product).where(Product.id == item_id) #select the product with the given id
        item = db.session.execute(query).scalar()
        new_order.products.append(item) #create connection from Order to associate id, and populates our order_product table
    db.session.add(new_order) #add the new order to the session
    db.session.commit() #commit the new order to the database
    
    db.session.refresh(new_order) #refresh the session with the new order
    return new_order #return the new order

def find_all(page=1, per_page=10):
    query = select(Order) #select all orders
    all_orders = db.paginate(query, page=int(page), per_page=int(per_page)) #execute the query and get all the orders
    
    return all_orders #return all the orders
