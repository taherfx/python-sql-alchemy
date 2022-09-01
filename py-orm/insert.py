from config.db import conn
from index import Base, session, Customers

# c1= Customers(name="Ravi", address = 'Station Road Nanded', email = 'ravi@gmail.com')

# session.add(c1)
session.add_all([
   Customers(name = 'Komal Pande', address = 'Koti, Hyderabad', email = 'komal@gmail.com'), 
   Customers(name = 'Rajender Nath', address = 'Sector 40, Gurgaon', email = 'nath@gmail.com'), 
   Customers(name = 'S.M.Krishna', address = 'Budhwar Peth, Pune', email = 'smk@gmail.com')]
)
session.commit()