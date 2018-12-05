"""Docstring for models"""
from flask import jsonify, make_response, request
import datetime

incidents = []

class RedFlagModule():
    """Docstring for class RedFlagModule"""
    def __init__(self):
        self.db = incidents
        if len(incidents) == 0:
            self.id = 1
        else:
            self.id = incidents[-1]['id'] + 1


    def save(self):
        """Method for saving redflag"""
        data = {
            'id': self.id,
            'createdOn' : datetime.datetime.utcnow(),
            'createdBy' : request.json.get('createdBy', ""),
            'type' : 'red-flags',
            'location' : request.json.get('location', ""),
            'status' : "Under Investigation",
            'images' : request.json.get('images', ""),
            'videos' : request.json.get('videos', ""),
            'title' : request.json['title'],
            'comment' : request.json.get('comment', "")
        }

        if data['createdBy'] == "createdBykeyerror":
            return "createdOnkeyerror"
        
        if data['createdOn'] == "createdOnkeyerror":
            return "createdOnkeyerror"

        if data['type'] == "typekeyerror":
            return "typekeyerror"

        if data['location'] == "lockeyerror":
            return "lockeyerror"

        if data['status'] == "statkeyerror":
            return "statkeyerror"

        if data['images'] == "imagkeyerror":
            return "imagkeyerror"

        if data['videos'] == "vidkeyerror":
            return "vidkeyerror"
    
        if data['title'] == "titkeyerror":
            return "titkeyerror"

        if data['comment'] == "comkeyerror":
            return "comkeyerror"

        self.db.append(data)
        return self.id
    

    def find(self, redflag_id):
        """Method for finding redflag by id"""
        for incident in self.db:
            if incident['id'] == redflag_id:
                return incident

        return None

    def delete(self, incident):
        """Method for deleting a single redflag"""
        self.db.remove(incident)
        return "deleted"


    def get_all(self):
        """Method for getting all redflags"""
        return self.db
        
    def edit_redflag_location(self, incident):
        incident['location'] = request.json.get('location', 'keyerror')
        if incident['location'] == 'keyerror':
            return "keyerror"
        return "location updated"

    def edit_redflag_comment(self, incident):
        incident['comment'] = request.json.get('comment', 'keyerror')
        if incident['comment'] == 'keyerror':
            return "keyerror"
        return "comment updated"

    

    