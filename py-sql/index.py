from sqlalchemy import Column, Table, Integer, String
from config.db import conn, meta

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String(16), unique = True), 
   Column('lastname', String(16)),
)

addresses = Table(
    'addresses', meta,
    Column('id', Integer, primary_key = True),
    Column("st_id", Integer, foreign_key = True),
    Column("post_addr", String(20)),
    Column("email_addr", String(16))
)

meta.create_all(conn)