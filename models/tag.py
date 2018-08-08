from sqlalchemy import Column, String, Integer
from base import Base


class Tag(Base):
    __tablename__ = 'tags'

    uid = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, index=True)
