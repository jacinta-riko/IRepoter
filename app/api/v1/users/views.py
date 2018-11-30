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
       
    
    def post(self):
        
        data = {
            'id' : self.id,
            'firstname' : request.json['firstname'],
            'lastname' : request.json['lastname'],
            'email' : request.json['email'],
            'phonenumber' : request.json['phonenumber'],
            'residence' : request.json['residence'],
            'username' : request.json['username'],
            'password' : request.json['password'],
            'registered' : datetime.datetime.utcnow(),
            'isAdmin' : request.json['isAdmin']
        }
        self.db.append(data)
        
        success_message = {
            'id' : self.id,
            'message' : 'User account successfully added'
        }

        return make_response(jsonify({
            "status" : 201,
            "data" : success_message
        }), 201)
    
class user(Resource):
    """user docstring"""
    def __init__(self):
        self.db = usersinfomation
        
    def get(self, user_id):

        for userinformation in usersinfomations:
            if usersinfomation['id'] == user_id:
                return make_response(jsonify({
                    "status" : 200,
                    "data" : usersinfomation
                }), 200)
                return make_response(jsonify({
                    "status" : 404,
                    "error" : "User account does not exist"
                }), 404)
          
    def delete(self, user_id):
         for userinformation in usersinfomation:
            if usersinfomation['id'] == userinformation_id:
                user.remove(userinformation)
                success_message = {
                'id' : self.id,
                'message' : 'User record deleted successfully'
                }
                return make_response(jsonify({
                "status" : 204,
                "data" : success_message
                }))
                return make_response(jsonify({
                    "status" : 404,
                    "error" : "User account does not exist"
                }))
        

    def put(self, userinformation_id):
        for userinformation in usersinfomation:
            if userinformation['id'] == userinformation_id:   
            userinformation['firstname'] = request.json.get('firstname', userinformation['firstname'])
            userinformation['lastname'] = request.json.get('lastname', userinformation['lastname'])
            userinformation['email'] = request.json.get('email', userinformation['email'])
            userinformation['phonenumber'] = request.json.get('phonenumber', userinformation['phonenumber'])
            userinformation['residence'] = request.json.get('residence', userinformation['residence'])
            userinformation['username'] = request.json.get('username', userinformation['username'])
            userinformation['password'] = request.json.get('password', userinformation['password'])
            userinformation['registered'] = request.json.get('registered', userinformation['registered'])
            userinformation['isAdmin'] = request.json.get('isAdmin', userinformation['isAdmin'])

            success_message = {
                "id" : userinformation_id,
                "message" : "User account has been updated"
            }

                return make_response(jsonify({
                    "status" : 201,
                    "data" : success_message
                }), 201)

                return make_response(jsonify({
                    "status" : 404,
                    "error" : "User account does not exist"
                }), 404)
        



        