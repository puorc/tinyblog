from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, Integer, Text, DateTime, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from base import Base
from comment import Comment


class Article(Base):
    __tablename__ = 'articles'

    uid = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, index=True)
    content = Column(Text)
    created_time = Column(DateTime(timezone=True), server_default=func.now())
    updated_time = Column(DateTime(timezone=True), onupdate=func.now())
    # guid = Column(String(255), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey('users.uid'))
    cate_id = Column(Integer, ForeignKey('categories.uid'))
    tags = relationship('Tag', secondary='article_tag', backref='articles')
    comments = relationship("Comment")


article_tag = Table(
    'article_tag', Base.metadata,
    Column('article_id', Integer, ForeignKey('articles.uid')),
    Column('tag_id', Integer, ForeignKey('tags.uid'))
)
