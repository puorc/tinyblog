from sqlalchemy import Column, Integer, String
from base import Base


class Option(Base):
    __tablename__ = 'options'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    val = Column(String(64), nullable=False)
