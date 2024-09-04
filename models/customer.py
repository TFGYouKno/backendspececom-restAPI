from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import List

class Customer(Base): #creating our customer model that inherits from Base
    __tablename__ = 'customers' #setting the table name in the DB

    id: Mapped[int] = mapped_column(primary_key=True) # primary key auto increment! Woo!
    name: Mapped[str] = mapped_column(db.String(255), nullable=False) #name column, not nullable
    email: Mapped[str] = mapped_column(db.String(255), nullable=False, unique=True) #email column, not nullable, must be unique
    phone: Mapped[str] = mapped_column(db.String(25), nullable=False) #phone column, not nullable
    username: Mapped[str] = mapped_column(db.String(50), nullable=False, unique=True) #username column, not nullable, must be unique
    password: Mapped[str] = mapped_column(db.String(255), nullable=False) #password column, not nullable

    #one to many relationship, one customer can have many orders
    orders: Mapped[List['Order']] = db.relationship(back_populates='customer')