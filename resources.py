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