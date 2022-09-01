from sqlalchemy.sql import alias, select
from index import students
from config.db import conn


st = students.alias("a")

s = select([st]).where(st.c.id > 2)

result = conn.execute(s)

for i in result:
    print(i)
