from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, ARRAY
import falcon
import json

Base = declarative_base()
DB_URI = 'postgresql:///characters.db'

class Character(Base):
    __tablename__ = 'Character'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(140))
    classType = Column(String(50))
    hitPoints = Column(Integer)
    location = Column(String(50))
    inventory = Column(ARRAY(Integer))

class Weapon(Base):
    __tablename__= 'Weapon'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    value = Column(Integer)
    damage = Column(Integer)

class Location(Base):
    __tablename__ = 'Location'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(240))
    exits = Column(ARRAY(String(20)))
    items = Column(ARRAY(Integer))

# class ButtResource:
#     def on_get(self, req, resp):
#         resp.status = falcon.HTTP_200
#         resp.content_type = falcon.MEDIA_TEXT
#         thing = {'message': 'Buttt'}
#         resp.body = json.dumps(thing)

#     def on_post(self, req, resp):
#         butt = req.get_param("name", required=True)
#         message = {'message': butt}
#         resp.status = falcon.HTTP_200
#         # resp.content_type = falcon.MEDIA_TEXT
#         resp.body = json.dumps(message)

if __name__ == "__main__":
    from sqlalchemy import create_engine

    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    