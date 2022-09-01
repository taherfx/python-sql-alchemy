from index import students
from config.db import conn
from sqlalchemy.sql import and_

stmt = students.update().where(
    and_(
        (students.c.lastname == "Kapoor"),
        (students.c.name == "Rajiv")        
    )
).values(lastname = "Khanna")

result = conn.execute(stmt)

print(result)