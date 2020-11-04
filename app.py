from sqlalchemy import create_engine
import falcon
import json
from resources import *
from falcon_autocrud.middleware import Middleware

db_engine = create_engine('postgresql:///characters.db')

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