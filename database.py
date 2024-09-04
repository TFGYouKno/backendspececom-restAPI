from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase): #creating our base class that all models will inherit 
    pass

db = SQLAlchemy(model_class=Base) #instantiating our DB using Base as the model class