from . import ma
from marshmallow import fields

class ProductSchema(ma.Schema):
    id = fields.Integer(required=False) #will auto increment
    product_name = fields.String(required=True)
    price = fields.String(required=True)
    
        
    class Meta:
        fields = ('id', 'product_name', 'price') #fields coming into product schema
            
product_schema = ProductSchema() #instantiating our product schema
products_schema = ProductSchema(many=True) # returns a list of products
