from . import ma
from marshmallow import fields

class OrderSchema(ma.Schema):
    id = fields.Integer(required=False) #will auto increment
    date = fields.Date(required=False)
    customer_id = fields.Integer(required=True)
    products = fields.Nested('ProductSchema', many=True)
    
    
        
    class Meta:
        fields = ('id', 'date',  'product_ids', 'products', 'customer_id') #fields coming into order schema
            
order_schema = OrderSchema() #instantiating our order schema
orders_schema = OrderSchema(many=True) # returns a list of orders, excludes the password field
