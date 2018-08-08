from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from base import Base


class Category(Base):
    __tablename__ = 'categories'

    uid = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, index=True)
    articles = relationship('Article', backref='category')
