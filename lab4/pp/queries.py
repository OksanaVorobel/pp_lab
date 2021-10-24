from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *


session = sessionmaker(bind=engine)

add_user = User(id=1, username="Aass", email="Porebryk@gmail.com", password="1234", phone="091234")
add_user2 = User(id=2, username="Fasd", email="Vasyliev@gmail.com", password="12341234", phone="12341234")

add_product = Product(id=1, name="not coffee", category="Not food", quantity=1, status='cool')
add_product2 = Product(id=2, name="coffee", category="food", quantity=1, status='not cool')

add_order = Order(id=1, quantity=1, status='cool', User_idUser=1, Audience_idAudience=1)
add_order2 = Order(id=2, quantity= 2, status='not cool', User_idUser=2, Audience_idAudience=2)

ss = session()

ss.add(add_user)
ss.add(add_user2)
ss.add(add_product)
ss.add(add_product2)
ss.add(add_order)
ss.add(add_order2)



ss.commit
