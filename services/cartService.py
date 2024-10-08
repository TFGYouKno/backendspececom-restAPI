from database import db
from models.product import Product
from models.customer import Customer
from models.order import Order
from models.orderProduct import order_product
from models.cart import customer_cart
from sqlalchemy import select
from datetime import date

def get_customer(customer_id):
    customer=db.session.query(Customer).get(customer_id)
    if not customer:
        raise ValueError('Customer not found')
    return customer

def add_items_to_cart(customer_id, cart_data):
    customer = get_customer(customer_id)
    product_ids = cart_data['product_ids']

    
    for product_id in product_ids:
        product = db.session.query(Product).get(product_id)
        if not product:
            raise ValueError("Product ID: {product_id} not found")
        if product not in customer.cart:
            customer.cart.append(product)
            print(f"Product ID: {product_id} added to cart")
    db.session.add(customer)
    db.session.commit()

def remove_item_from_cart(customer_id, cart_data):
    customer = get_customer(customer_id)
    print(f"Customer ID: {customer_id}")
    product_ids = cart_data['product_ids']

    products = db.session.query(Product).filter(Product.id.in_(product_ids)).all()

    for product in products:
        if product in customer.cart:
            customer.cart.remove(product)
            print(f"Product ID: {cart_data} removed from cart")

    db.session.commit()

def view_cart(customer_id):
    query = select(Customer).where(Customer.id == customer_id)
    customer = db.session.execute(query).scalar_one_or_none()
    print(f"Query result: {customer.cart}")
    return customer.cart

    #cart_items = []
    #for row in customer:
       # item = {
            #"id": row.id, 
           # "name": row.product_name,
           # "price": row.price
          #  }
       # cart_items.append(item)
        #return cart_items
    
def empty_cart(customer_id):
    customer = get_customer(customer_id)
    customer.cart.clear()
    db.session.commit()

def place_order(customer_id):
    customer = get_customer(customer_id)

    if not customer.cart:
        raise ValueError("Cart is empty")
        
    new_order = Order(customer_id=customer_id, date=date.today())

    for product in customer.cart:
        new_order.products.append(product)

    customer.cart.clear()

    db.session.add(new_order)
    db.session.commit()

    return new_order