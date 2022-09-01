from config.db import conn
from index import students, addresses
from sqlalchemy.sql import select, func

st = select([func.count(students.c.id)])

results = conn.execute(st)
print(results.fetchone())