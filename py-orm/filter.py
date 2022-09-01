from index import Customers, session

# st = session.query(Customers).filter(Customers.id>2)
# st = session.query(Customers).filter(Customers.id == 2)
# st = session.query(Customers).filter(Customers.id != 2)
# st = session.query(Customers).filter(Customers.name.like("ra%"))
st = session.query(Customers).filter(Customers.id.in_([2,3])).first()
# st = session.query(Customers).filter(Customers.id > 2, Customers.name.like("ra%")).all()

# for i in st:
#     print(i.name)
print(st.name)
