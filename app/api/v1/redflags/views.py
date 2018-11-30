from flask_restful import Resource
from flask import jsonify, make_response, request, abort     

import datetime

incidents = []


class RedFlags(Resource):
    """RedFlags"""
    
    def __init__(self):
        self.db = incidents
        self.id = len(incidents) + 1

    def get(self):

        return make_response(jsonify({
            "status" : 200,
            "data" : self.db
        }), 200) 
       
    
    