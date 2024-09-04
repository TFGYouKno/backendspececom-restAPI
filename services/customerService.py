from database import db #services interact directly with the database
from models.customer import Customer #need to create customer objects
from sqlalchemy import select #so we can query our database

def save(customer_data):
    
    new_customer = Customer(name=customer_data['name'], email=customer_data['email'], phone=customer_data['phone'], username=customer_data['username'], password=customer_data['password']) #create a new customer object
    db.session.add(new_customer) #add the new customer to the session
    db.session.commit() #commit the new customer to the database
    
    db.session.refresh(new_customer) #refresh the session with the new customer
    return new_customer #return the new customer

def find_all():
    query = select(Customer) #select all customers
    all_customers = db.session.execute(query).scalars().all() #execute the query and get all the customers
    
    return all_customers #return all the customers

def find_by_id(id):
    query = select(Customer).where(Customer.id == id) #select the customer with the given id
    customer = db.session.execute(query).scalars().first() #execute the query and get the customer with the given id
    
    return customer #return the customer with the given id

def update(id, customer_data):
    query = select(Customer).where(Customer.id == id) #select the customer with the given id
    customer = db.session.execute(query).scalars().first() #execute the query and get the customer with the given id
    
    if not customer:
        return None
    
    customer.name = customer_data['name']
    customer.email = customer_data['email']
    customer.phone = customer_data['phone']
    customer.username = customer_data['username']
    customer.password = customer_data['password']

    db.session.commit() #commit the updated customer to the database
    
    db.session.refresh(customer) #refresh the session with the updated customer
    
    return customer #return the updated customer

def delete(id):
    query = select(Customer).where(Customer.id == id) #select the customer with the given id
    customer = db.session.execute(query).scalars().first() #execute the query and get the customer with the given id
    
    if not customer:
        return None
    
    db.session.delete(customer) #delete the customer with the given id
    db.session.commit() #commit the deletion of the customer
    
    return customer #return the deleted customer