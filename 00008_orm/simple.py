from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, MetaData, Table
from sqlalchemy import select
engine = create_engine('sqlite:///:memory:', echo=True)

metadata = MetaData()
users = Table('users', metadata, Column(
    'id', Integer, primary_key=True), Column('name', String))

users.create(bind=engine)

insert_user = users.insert().values(name='John')
engine.execute(insert_user)

statement = select([users.c.name])
user, = engine.execute(statement).fetchone()
print(user)
