from config.db import conn
from index import students

s = students.select().where(students.c.id > 2)
result = conn.execute(s)

for i in result:
    print(i)

# row = result.fetchone()
# print(row)