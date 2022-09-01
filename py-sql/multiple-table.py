from soupsieve import select
from config.db import conn
from index import students, addresses
from sqlalchemy.sql import select

st = select([students, addresses]).where(students.c.id == addresses.c.st_id)

results = conn.execute(st)

for i in results:
    print(i)