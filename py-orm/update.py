from index import session, Customers

x = session.query(Customers).get(2)

x.address = "Banjara Hills Secunderabad"

session.commit()