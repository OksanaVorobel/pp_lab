from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *


session = sessionmaker(bind=engine)

add_order = Order(id=6, quantity=1, status='cool', User_idUser=3, Product_IdProduct = 3)
add_order2 = Order(id=4, quantity= 2, status='not cool', User_idUser=4, Product_IdProduct=4)
add_order3 = Order(id=5, quantity= 2, status='not cool', User_idUser=3, Product_IdProduct=4)
ss = session()

ss.add(add_order)
ss.add(add_order2)
ss.add(add_order3)
ss.commit()
