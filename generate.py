import random
from faker import Factory
from models.main import session
from models.article import Article
from models.category import Category
from models.comment import Comment
from models.tag import Tag
from models.user import User
from models.base import Session, engine, Base

if __name__ == '__main__': 
    Base.metadata.create_all(engine)
    session = Session()
    faker = Factory.create()
    faker_users = [User(
        username=faker.name(),
        password=faker.word(),
        email=faker.email(),
    ) for i in range(10)]
    session.add_all(faker_users)

    faker_comments = [Comment(
        author=faker.name(),
        email=faker.email(),
        content=faker.sentence()
    ) for i in range(10)]
    session.add_all(faker_comments)

    faker_categories = [Category(name=faker.word()) for i in range(5)]
    session.add_all(faker_categories)

    faker_tags = [Tag(name=faker.word()) for i in range(20)]
    session.add_all(faker_tags)

    for i in range(100):
        article = Article(
            title=faker.sentence(),
            content=' '.join(faker.sentences(nb=random.randint(10, 20))),
            author=random.choice(faker_users),
            category=random.choice(faker_categories)
        )
        for tag in random.sample(faker_tags, random.randint(2, 5)):
            article.tags.append(tag)
        for comment in random.sample(faker_comments, random.randint(2, 5)):
            article.comments.append(comment)
        session.add(article)

    session.commit()
