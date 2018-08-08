from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from base import Base


class User(Base):
    __tablename__ = 'users'

    uid = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False, index=True)
    password = Column(String(64), nullable=False)
    nickname = Column(String(64), index=True)
    email = Column(String(64), nullable=False, index=True)
    created_time = Column(DateTime(timezone=True), server_default=func.now())
    articles = relationship('Article', backref='author')
