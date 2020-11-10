from sqlalchemy import create_engine
import falcon
import json
from resources import *
from falcon_autocrud.middleware import Middleware

db_engine = create_engine('postgresql://127.0.0.1:5432/characters.db')

app = falcon.API(
    middleware=[
        Middleware()
        ]
)
app.req_options.auto_parse_form_urlencoded=True

butt = ButtResource()

app.add_route('/butt', butt)
app.add_route('/character', CharacterCollectionResource(db_engine))
app.add_route('/character/{id}', CharacterResource(db_engine))
app.add_route('/weapon', WeaponCollectionResource(db_engine))
app.add_route('/weapon/{id}', WeaponResource(db_engine))