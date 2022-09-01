from index import Customers, session
from sqlalchemy import text

# st = session.query(Customers).filter(text("id >= 2")).first()
# st = session.query(Customers).filter(text("id = :value")).params(value = 2).first()
# st = session.query(Customers).from_statement(text("select * from customers")).first()

stmt = text("select id, name, email from customers")
stmt = stmt.columns(Customers.id, Customers.name)
result = session.query(Customers.id, Customers.name).from_statement(stmt).all()

# print(st.name)

for i in result:
    print(i.id)