from config.db import conn
from index import students, addresses

ins = students.insert().values(name = 'janvi', lastname = 'Kapoor')
# result = conn.execute(ins)
conn.execute(students.insert(), [
    {'name':'Rajiv', 'lastname' : 'Khanna'},
    {'name':'Komal','lastname' : 'Bhandari'},
    # {'name':'Abdul','lastname' : 'Sattar'},
    # {'name':'Priya','lastname' : 'Rajhans'},
])

conn.execute(
    addresses.insert(), [
        {'st_id':1, 'post_addr':'Shivajinagar Pune', 'email_addr':'ravi@gmail.com'},
        {'st_id':1, 'post_addr':'ChurchGate Mumbai', 'email_addr':'kapoor@gmail.com'},
        {'st_id':3, 'post_addr':'Jubilee Hills Hyderabad', 'email_addr':'komal@gmail.com'},
        {'st_id':6, 'post_addr':'MG Road Bangaluru', 'email_addr':'as@yahoo.com'},
        {'st_id':4, 'post_addr':'Cannought Place new Delhi', 'email_addr':'admin@khanna.com'},
    ]
)