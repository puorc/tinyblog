from base import Session, engine, Base

Base.metadata.create_all(engine)
session = Session()
