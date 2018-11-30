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

    def post(self):

        data = {
            'id' : self.id,
            'createdOn' : datetime.datetime.utcnow(),
            'createdBy' : request.json['createdBy'],
            'type' : 'red-flags',
            'location' : request.json['location'],
            'status' : "Under Investigation",
            'images' : request.json['images'],
            'videos' : request.json['videos'],
            'title' : request.json['title'],
            'comment' : request.json['comment']
            }

            self.db.append(data)success_message = {
                'id' : self.id,
                'message' : 'Thank you for creating a Red-Flag'
                }

            return make_response(jsonify({
                "status" : 201,
                "data" : success_message
                }), 201)

class RedFlag(Resource):
"""docstring of RedFlag"""
    def __init__(self):
        self.db = incidents
        self.id = len(incidents) + 1


    def get(self, redflag_id):

        for incident in incidents:
            if incident['id'] == redflag_id:
                return make_response(jsonify({
                    "status" : 200,
                    "data" : incident
                }), 200)

    
    def delete(self, redflag_id):

        for incident in incidents:
            if incident['id'] == redflag_id:incidents.pop(redflag_id - 1)
                success_message = {
                    'id' : self.id,
                    'message' : 'Red-Flag Deleted successfully'
                    }


                    return make_response(jsonify({
                        "status" : 204,
                        "data" : success_message
                        }), 204)


     def put(self, redflag_id):

        for incident in incidents:
             if incident['id'] == redflag_id: 
                incident['createdOn'] = request.json.get('createdOn', incident['createdOn'])
                incident['createdBy'] = request.json.get('createdBy', incident['createdBy'])
                incident['type'] = request.json.get('type', incident['type'])
                incident['location'] = request.json.get ('location', incident['location']) 
                incident['status'] = request.json.get('status', incident['status'])
                incident['images'] = request.json.get('images', incident['images'])
                incident['videos'] = request.json.get('videos', incodent['videos'])
                incident['title'] = request.json.get('title', incident['title'])
                incident['comment'] = request.json.get('comment', incident['comment'])

                    success_message = {
                        "id" : redflag_id,
                        "message" : "User record has been successfully updated"
                        }

                        return make_response(jsonify({
                            "status" : 201,
                            "data" : success_message
                        }), 201)

                        return make_response(jsonify({
                            "status" : 404,
                            "error" : "User record does not exist"
                        }), 404)


    

