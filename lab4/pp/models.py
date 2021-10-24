from sqlalchemy import Column, Boolean, Integer, String, Date, ForeignKey

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+mysqlconnector://root:1111@localhost/lab6", echo=True)

Base = declarative_base()
metadata = Base.metadata

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(45))
    email = Column(String(45))
    password = Column(String(45))
    phone = Column(String(45))

    def __repr__(self):
        return f"{self.id}, {self.username}, {self.email}, {self.password}, {self.phone}"



class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    category = Column(String(45))
    quantity = Column(Integer)
    status = Column(String(45))

    def __repr__(self):
        return f"{self.id}, {self.name}, {self.category}, {self.quantity}, {self.status}"


class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    status = Column(String(45))
    User_idUser = Column(Integer, ForeignKey('user.id'))
    Audience_idAudience = Column(Integer, ForeignKey('product.id'))
    def __repr__(self):
        return f"{self.idAudience}, {self.number}, {self.amount_of_places}, {self.status}, {self.Audience_idAudience}, {self.User_idUser}"



