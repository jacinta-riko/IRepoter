"""Docstring for views"""
from flask_restful import Resource
from flask import jsonify, make_response, request
from .models import RedFlagModule

class RedFlags(Resource):
    """This is the redflags class which we will use for post or get all redflags methods"""
    
    def __init__(self):
        self.db = RedFlagModule()

    def post(self):
        """retun redflag details created by user"""
        
        self.db.save()
        
        success_message = {
            'message' : 'Sucessfully created a red-flag'
        }

        return make_response(jsonify({
            "status" : 201,
            "data" : success_message
        }), 201)

    def get(self):
        """return all records created by specific user"""
        self.db.get_all() 
        return make_response(jsonify({
            "status" : 200,
            "data" : self.db.get_all()
        }), 200)

class RedFlag(Resource):
    """class which will be used to view, delete and edit single redflag by id""" 
    def __init__(self):
        self.db = RedFlagModule()
        

    def get(self, redflag_id):
        """return specific redflag by id"""
        incident = self.db.find(redflag_id)
        if incident == None:
            return make_response(jsonify({
                "status" : 200,
                "error" : "Red-flag does not exist"
                }), 200)
        return make_response(jsonify({
                "status" : 200,
                "data" : incident
                }), 200)
    

    def delete(self, redflag_id):
        """delete a single redflag by id"""
        incident = self.db.find(redflag_id)

        if incident == None:
            return make_response(jsonify({
                "status" : 200,
                "data" : "Red-flag record does not exist"
            }), 200)
        delete_status = self.db.delete(incident)
        if delete_status == "deleted":
            return make_response(jsonify({
                "status" : 200,
                "data" : {
                    "id" : redflag_id,
                    "message" : 'Red-flag record has been sucessfully deleted'
                 }
            }), 200)  

    def put(self, redflag_id):
        """returns updated redflag record"""
        incident = self.db.find(redflag_id)
        if incident:
                incident['createdBy'] = request.json.get('createdBy', incident['createdBy'])
                incident['location'] = request.json.get('location', incident['location'])
                incident['images'] = request.json.get('images', incident['images'])
                incident['videos'] = request.json.get('videos', incident['videos'])
                incident['title'] = request.json.get('title', incident['title'])
                incident['comment'] = request.json.get('comment', incident['comment'])

                success_message = {
                    "message" : "Red-flag has been successflly updated"
                }

                return make_response(jsonify({
                    "status" : 201,
                    "data" : success_message
                }), 201)

class UpdateLocation(Resource):
    """class that will be used to update location"""
    def __init__(self):
        self.db = RedFlagModule()


    def patch(self, redflag_id):
        """We need to get a specific redflag record by id before the user can edit"""
        
        incident = self.db.find(redflag_id)

        if incident == None:
            return make_response(jsonify({
                "status" : 200,
                "error" : "Successfully updated redflag location"
            }), 200)
        edit_status = self.db.edit_redflag_location(incident)
        if edit_status == "keyerror":
            return make_response(jsonify({
                "status" : 400,
                "data" : "Keyerror: location for the redflag not updated"
            }), 400)
        elif edit_status == "location updated":
            return make_response(jsonify({
                "status" : 200,
                "data" : {
                    "id" : redflag_id,
                    "message" : "Successfully updated redflag location"
                }
            }), 200)

class UpdateComment(Resource):
    """this class will be used to patch a comment"""
    def __init__(self):
        self.db = RedFlagModule()


    def patch(self, redflag_id):
        """"method for editing a red flag by id"""
        incident = self.db.find(redflag_id)

        if incident == None:
            return make_response(jsonify({
                "status" : 200,
                "error" : "Red flag does not exist"
            }), 200)
        edit_status = self.db.edit_redflag_comment(incident)
        if edit_status == "keyerror":
            return make_response(jsonify({
                "status" : 400,
                "data" : "Keyerror: comment for the redflag not updated"
            }), 400)
        elif edit_status == "comment updated":
            return make_response(jsonify({
                "status" : 200,
                "data" : {
                    "id" : redflag_id,
                    "message" : "Successfully updated redflag comment"
                }
            }), 200)                                                           
