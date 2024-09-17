from database import db #services interact directly with the database
from models.customer import Customer #need to create customer objects
from sqlalchemy import select #so we can query our database
from utils.util import encode_role_token #to encode the token

def save(customer_data):
    
    new_customer = Customer(name=customer_data['name'], email=customer_data['email'], phone=customer_data['phone'], username=customer_data['username'], password=customer_data['password'], admin=customer_data['admin']) #create a new customer object
    db.session.add(new_customer) #add the new customer to the session
    db.session.commit() #commit the new customer to the database
    
    db.session.refresh(new_customer) #refresh the session with the new customer
    return new_customer #return the new customer

def find_all(page=1, per_page=10):
    query = select(Customer) #select all customers
    all_customers = db.paginate(query, page=int(page), per_page=int(per_page)) #execute the query and get all the customers
    
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

def login(credentials):
    query = select(Customer).where(Customer.email == credentials['email']) #select the customer with the given username and password
    customer = db.session.execute(query).scalar_one_or_none() #execute the query and get the customer with the given username and password

    if customer and customer.password == credentials['password']:
        auth_token = encode_role_token(customer.id, customer.admin) #return the customer with the given username and password
        return auth_token #return the customer with the given username and password
    
    return None #return None if the customer does not exist or the password is incorrect