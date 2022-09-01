from sqlalchemy import text, and_
from sqlalchemy.sql import select
from config.db import conn
from index import students

# define parma in stirng using :(name) (:x)
# t = text("select * from students where students.name between :x and :y")

t = select(students) \
.where(
    and_(
        text("students.name between :x and :y"),
        text("students.id > 2")
    )
)

# Output params value
# result = conn.execute(t, x="A", y="L") #Without fetchall() function return same data
result = conn.execute(t, x="A", y="L").fetchall()  # with fetchall() function return data

for i in result:
    print(i)