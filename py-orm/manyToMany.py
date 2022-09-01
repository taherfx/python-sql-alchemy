from regex import W
from config.db import conn
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Department(Base):
    __tablename__ = "department"
    id = Column(Integer, primary_key= True)
    name = Column(String(16))
    employees = relationship("Employee", secondary= "link")

class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key = True)
    name = Column(String(16))
    departments = relationship(Department,secondary='link')

class Link(Base):
    __tablename__ = "link"
    department_id = Column(
      Integer, 
      ForeignKey('department.id'), 
      primary_key = True)
    employee_id = Column(
        Integer,
        ForeignKey('employee.id'),
        primary_key= True
    )

Base.metadata.create_all(conn)