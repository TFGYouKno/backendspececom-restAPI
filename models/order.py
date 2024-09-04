from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
import datetime
from typing import List
from models.orderProduct import order_product

class Order(Base): #creating our order model that inherits from Base
    __tablename__ = 'orders' #setting the table name in the DB

    id: Mapped[int] = mapped_column(primary_key=True) # primary key auto increment! Woo!
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('customers.id')) 
    #customer column, not nullable
    date: Mapped[datetime.date] = mapped_column(db.Date, nullable=False) #date column, not nullable
    

    #many to one, many orders can belong to one customer
    customer: Mapped['Customer'] = db.relationship(back_populates='orders')

    #many to many relationship, many orders can have many products
    products: Mapped[List['Product']] = db.relationship(secondary=order_product)