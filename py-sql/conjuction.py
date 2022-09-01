from config.db import conn
from index import students, addresses
from sqlalchemy.sql import select
from sqlalchemy import and_, or_, asc, desc, between 

# st = select([students]).where(and_(students.c.name == "ravi", students.c.id < 6))
# st = select([students]).where(or_(students.c.name == "rajiv", students.c.id < 6))
# st = select([students]).order_by(asc(students.c.name))
# st = select([students]).order_by(desc(students.c.name))
st = select([students]).where(between(students.c.id,6,13))

result = conn.execute(st)

print(result.fetchall())