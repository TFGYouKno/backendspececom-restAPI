from . import ma
from marshmallow import fields

class CustomerSchema(ma.Schema):
    id = fields.Integer(required=False) #will auto increment
    name = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    admin = fields.Integer(required=True)
        
    class Meta:
        fields = ('id', 'name', 'email', 'phone', 'username', 'password', 'admin') #fields coming into customer schema
            
customer_schema = CustomerSchema() #instantiating our customer schema
customers_schema = CustomerSchema(many=True, exclude=["password"]) # returns a list of customers, excludes the password field
customer_login = CustomerSchema(exclude=["name", "phone", "username","id"]) #returns a customer object with only the username and password fields