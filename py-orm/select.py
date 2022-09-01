from config.db import conn
from index import Base, session, Customers


result = session.query(Customers).all()

for i in result:
    print(i.name)