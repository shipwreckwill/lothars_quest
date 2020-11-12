from falcon_autocrud.resource import CollectionResource, SingleResource
from models import *
from game import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine,select

db_engine = create_engine('postgresql:///characters.db')


game = Game()

class CharacterCollectionResource(CollectionResource):
    model = Character
    methods = ['GET', 'POST', 'PUT']

class CharacterResource(SingleResource):
    model = Character

class WeaponCollectionResource(CollectionResource):
    model = Weapon
    methods = ['GET', 'POST', 'PUT']

class WeaponResource(SingleResource):
    model = Weapon

class LocationCollectionResource(CollectionResource):
    model = Location
    methods = ['GET', 'POST', 'PUT']

class LocationResource(SingleResource):
    model = Location

class LocalItemsResource(SingleResource):
    model = Location
    def on_post(self,req, resp):
        things = int(req.get_param("location", required=True))
        Session = sessionmaker(db_engine)
        with Session.begin() as session:
            result = session.query(Location.inventory).all()
            print(result)
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(result)
        

class ButtResource:
    """
    ButtResource:
        On Get - Says 'Buttt', three t's makes it funny.
        On Post - Parrot Function, just repeats input of "Name" param
    """
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        thing = {'message': 'Buttt'}
        resp.body = json.dumps(thing)

    def on_post(self, req, resp):
        butt = req.get_param("name", required=True)
        message = {'message': butt}
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(message)

class DiceResource:
    """
    DiceResource: Let player cast dice for checks, attacks, etc...
        On Get - Returns Available Dice that may be Cast
        On Pull - Accepts dN as parameter, N being number of sides on die,
           returns result of casting die.
    """
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.body = ('\n AVAILABLE ROLLS'
                    '\n\n --D20'
                    '\n --D12'
                    '\n --D10'
                    '\n --D08'
                    '\n --D06'
                    '\n --D04\n\n')
    
    def on_post(self, req, resp):
        die = int(req.get_param("die", required=True))
        resp.status = falcon.HTTP_200
        print(f"The dice rolled is: {die}")
        message = game.rollDice(die)
        resp.body = json.dumps(message)