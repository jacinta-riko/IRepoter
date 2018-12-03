from flask import Blueprint 
from flask_restful import Api ,Resource  

from .redflags.views import RedFlag, RedFlags, UpdateLocation, UpdateComment

version1 = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(version1)

# The add_resource function registers the routes with the framework using the given endpoint
api.add_resource(RedFlags, '/red-flags')  #for the list of redflags
api.add_resource(RedFlag, '/red-flags/<int:redflag_id>') #for an individual red-flag
api.add_resource(UpdateLocation, '/red-flags/<int:redflag_id>/location')
api.add_resource(UpdateComment, '/red-flags/<int:redflag_id>/comment')