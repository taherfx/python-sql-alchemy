from config.db import conn
from index import students
from sqlalchemy.sql.expression import update

st = students.delete().where(students.c.id == 5)

result = conn.execute(st)