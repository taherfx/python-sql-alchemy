from index import session, Customers, Invoices


x = session.query(Customers).get(6)

session.delete(x)
count = session.query(Customers).filter_by(name = 'Govind Pant').count()
session.commit()
print(count)