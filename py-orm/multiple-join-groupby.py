from index import session, Customers, Invoices
from sqlalchemy.sql import func

stmt = session.query(
    Invoices.custid, func.count('*').label('invoice_count')
).group_by(Invoices.custid).subquery()

st = session.query(Customers, stmt.c.invoice_count).outerjoin(stmt, Customers.id == stmt.c.custid).order_by(Customers.id)

for u, count in st:
    print(u.name, count)