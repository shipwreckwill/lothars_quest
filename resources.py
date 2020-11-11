from falcon_autocrud.resource import CollectionResource, SingleResource
from models import *
import random

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

class ButtResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        thing = {'message': 'Buttt'}
        resp.body = json.dumps(thing)

    def on_post(self, req, resp):
        butt = req.get_param("name", required=True)
        message = {'message': butt}
        resp.status = falcon.HTTP_200
        # resp.content_type = falcon.MEDIA_TEXT
        resp.body = json.dumps(message)

class DiceResource:
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
        diceBag = [4,6,8,10,12,20]
        die = req.get_param("die", required=True)
        resp.status = falcon.HTTP_200
        print(f"The dice rolled is: {die}")
        if die in diceBag:
            roll = random.randrange(int(die))
            message = {'roll': roll}
            resp.body = json.dumps(message)
        else:
            message = { 'error' : 'You do not have that die in your Dice Bag...'}
            resp.body = json.dumps(message)