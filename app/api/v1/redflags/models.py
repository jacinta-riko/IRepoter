"""Docstring for models"""
import datetime
import re
from flask import request
import datetime
from flask_restful import reqparse


incidents = []

def validator_username_id(value):
    """method to check for integers only in user id"""
    if not re.match(r"^[0-9]+$", value):
        raise ValueError("should be integer")


def validate_coordinates(value):
    """method to check for valid coordinates in location"""
    if not re.match(r"^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$", value):
        raise ValueError("Pattern not matched")


def validate_comment(value):
    """method to check that comment only contains letters"""
    if not re.match(r"[A-Za-z1-9]", value):
        raise ValueError("should only be string")


parser = reqparse.RequestParser(bundle_errors=True)

parser.add_argument('createdBy',
                    type=validator_username_id,
                    required=True,
                    help='This field is required.and should only contain number'
                    )

parser.add_argument('location',
                    type=validate_coordinates,
                    required=True,
                    help='Please provide valid coordinates'
                    )

parser.add_argument('type',
                    type=str,
                    required=True,
                    choices=("red-flags", "intervention"),
                    help="This field is required"
                         "Blank or Bad choice: {error message}"
                    )

parser.add_argument('status',
                    type=str,
                    required=True,
                    choices=("Resolved", "Unresolved", "Rejected"),
                    help='This field is required and should only be resolved or unresolved or rejected'
                    )

parser.add_argument('images',
                    action='append',
                    help='This field is required'
                    )

parser.add_argument('videos',
                    action='append',
                    help='This field is required'
                    )

parser.add_argument('comment',
                    type=validate_comment,
                    required=True,
                    help='PLease avoid special characters i.e #$%'
                    )

parser.add_argument('title',
                    type=validate_comment,
                    required=True,
                    help='This field is required'
                    )


class RedFlagModule():
    """Docstring for class RedFlagModule"""

    def __init__(self):
        self.db = incidents
        if len(incidents) == 0:
            self.id = 1
        else:
            self.id = incidents[-1]['id'] + 1

    def save(self):
        """Method for saving a single user redflag"""
        args = parser.parse_args()
        data = {
            'id': self.id,
            'createdOn': datetime.datetime.utcnow(),
            'createdBy': request.json.get('createdBy'),
            'type': 'red-flags',
            'location': request.json.get('location'),
            'status': "Under Investigation",
            'images': request.json.get('images'),
            'videos': request.json.get('videos'),
            'title': request.json['title'],
            'comment': request.json.get('comment')
        }

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
        """Method for getting all redflag records"""
        return self.db

    def edit_redflag_location(self, incident):
        """"Method for updating a redflag location"""
        incident['location'] = request.json.get('location', 'keyerror')
        if incident['location'] == 'keyerror':
            return "keyerror"
        return "location updated"

    def edit_redflag_comment(self, incident):
        """Method for updating a redflag comment"""
        incident['comment'] = request.json.get('comment', 'keyerror')
        if incident['comment'] == 'keyerror':
            return "keyerror"
        return "comment updated"
