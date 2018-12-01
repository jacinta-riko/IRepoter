from flask import Blueprint 
from flask_restful import Api ,Resource  

from .redflags.views import RedFlag, RedFlags 

version1 = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(version1)

# The add_resource function registers the routes with the framework using the given endpoint
api.add_resource(RedFlags, '/red-flags')  #for the list of redflags
api.add_resource(RedFlag, '/red-flags/<int:redflag_id>') #for an individual red-flag