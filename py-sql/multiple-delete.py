from config.db import conn
from index import students, addresses

st = students.delete().\
where(students.c.id == addresses.c.id)

conn.execute(st)