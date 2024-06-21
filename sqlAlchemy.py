from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()
class Abc(Base):
    _tablename_="xyz"
    Id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)

eng=create_engine("sqlite:///mydb1.db")
Base.metadata.create_all(eng)
session=sessionmaker(bind=eng)
s=session()