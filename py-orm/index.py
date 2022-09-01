from config.db import conn
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Customers(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key = True)

    name = Column(String(20))
    address = Column(String(30))
    email = Column(String(16))

class Invoices(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key = True)
    custid = Column(Integer, ForeignKey("customers.id"))
    invno = Column(Integer)
    amount = Column(Integer)
    customers = relationship("Customers", back_populates="invoices")

Customers.invoices = relationship("Invoices", order_by=Invoices.id, back_populates="customers")
Base.metadata.create_all(conn)

Session = sessionmaker(bind = conn)
session = Session()