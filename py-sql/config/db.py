from sqlalchemy import create_engine, MetaData
import pymysql

conn = create_engine("mysql+pymysql://root:password@localhost:3306/college", echo = True)
meta = MetaData()