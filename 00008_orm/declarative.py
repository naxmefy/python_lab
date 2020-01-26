from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<User(id='%s', name='%s')>" % (self.id, self.name)


Base.metadata.create_all(engine)

user = User(name='John')
print("user before save", user)


Session = sessionmaker(bind=engine)
session = Session()

session.add(user)
session.commit()

query = session.query(User)
instance = query.first()
print("from query", instance)
