from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///rfg.db')
Session = sessionmaker(bind=engine)

Base = declarative_base()
