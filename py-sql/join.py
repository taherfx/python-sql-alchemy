from config.db import conn
from index import students, addresses
from sqlalchemy import join
from sqlalchemy.sql import select

st = students.join(addresses, students.c.id == addresses.c.st_id)

stmt = select([students]).select_from(st)

results = conn.execute(stmt)

for i in results:
    print(i)