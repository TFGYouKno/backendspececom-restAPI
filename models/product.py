from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import List
from models.orderProduct import order_product

class Product(Base): #creating our product model that inherits from Base
    __tablename__ = 'products' #setting the table name in the DB

    id: Mapped[int] = mapped_column(primary_key=True) # primary key auto increment! Woo!
    product_name: Mapped[str] = mapped_column(db.String(255), nullable=False) #product name column, not nullable
    price: Mapped[str] = mapped_column(db.String, nullable=False) #price column, not nullable, 
    
    orders: Mapped[List['Order']] = db.relationship(secondary=order_product)