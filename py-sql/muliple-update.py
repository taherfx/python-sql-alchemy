from config.db import conn
from index import students, addresses

st = students.update().values({
        students.c.name: "xyz",
        addresses.c.email_addr: "xyz@gmail.com"
}).\
where(students.c.id == "Abdul")

results = conn.execute(st)

for i in results:
    print(i)