from flask_restful import Resource
from flask import jsonify, make_response, request, abort     

import datetime

usersinfomation = []


class usersinformation(Resource):
    """Users information"""
    
    def __init__(self):
        self.db = usersinformation
        if len(usersinfomation) == 0:
            self.id = 1
        else:
            self.id = usersinfomation[-1]['id'] + 1
        self.id = len(usersinfomation) + 1


    def get(self):

        return make_response(jsonify({
            "status" : 200,
            "data" : self.db
        }), 200) 
       
    
   


        