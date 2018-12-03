"""Docstring for models"""
from flask import jsonify, make_response, request

incidents = []

class RedFlagModule():
    """Docstring for class RedFlagModule"""
    def __init__(self):
        self.db = incidents
        if len(incidents) == 0:
            self.id = 1
        else:
            self.id = incidents[-1]['id'] + 1
        self.id = len(incidents) + 1

    def save(self, data):
        """Method for saving redflag"""
        data['id'] = self.id

        self.db.append(data)

    def find(self, redflag_id):
        """Method for finding redflag by id"""
        for incident in self.db:
            if incident['id'] == redflag_id:
                return incident

        return None

    def delete(self, incident):
        """Method for deleting a single redflag"""
        self.db.remove(incident)


    def get_all(self):
        """Method for getting all redflags"""
        return self.db
        