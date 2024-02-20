from sqlalchemy import Column, Integer, String, BigInteger, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Estate(Base):
    __tablename__ = 'estates'
    

    hash_id = Column(BigInteger, primary_key=True, autoincrement=False)
    title = Column(String)
    price = Column(Numeric)
    image_url = Column(String)
