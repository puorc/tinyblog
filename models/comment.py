from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, Integer, Text, DateTime
from sqlalchemy.sql import func
from base import Base


class Comment(Base):
    __tablename__ = 'comments'

    uid = Column(Integer, primary_key=True)
    author = Column(String(64), nullable=False, index=True)
    email = Column(String(64), nullable=False, index=True)
    content = Column(Text)
    created_time = Column(DateTime(timezone=True), server_default=func.now())
    article_id = Column(Integer, ForeignKey('articles.uid'))
