from index import session, Customers, Invoices
from sqlalchemy.sql import func

# st = session.query(Customers, Invoices).filter(Customers.id == Invoices.custid).all()
# st = session.query(Customers).join(Invoices).filter(Invoices.amount > 10000).all()
st = session.query(Customers).outerjoin(Customers.invoices).filter(Invoices.amount > 10000).all()

# for c, i in st:
#     print(c.name, i.invno)

for c in st:
    for i in c.invoices:
        print(c.name, i.amount)