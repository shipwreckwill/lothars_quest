from falcon_autocrud.resource import CollectionResource, SingleResource
from models import *

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