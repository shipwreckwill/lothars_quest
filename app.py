from sqlalchemy import create_engine
import falcon
import json
from resources import *
from falcon_autocrud.middleware import Middleware

db_engine = create_engine('postgresql:///characters.db')

app = falcon.API(
    middleware=[
        Middleware()
        ]
)


app.req_options.auto_parse_form_urlencoded=True

butt = ButtResource()
dice = DiceResource()

app.add_route('/dice', dice)
app.add_route('/butt', butt)
app.add_route('/character', CharacterCollectionResource(db_engine))
app.add_route('/character/{id}', CharacterResource(db_engine))
app.add_route('/character/{id}/{classType}', CharacterResource(db_engine))
app.add_route('/weapon', WeaponCollectionResource(db_engine))
app.add_route('/weapon/{id}', WeaponResource(db_engine))
