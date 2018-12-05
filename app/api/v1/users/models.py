"""Docstring for user models"""
from flask import jsonify, make_response, request

incidents = []

class UserModel():
    """Docstring for class UserModel"""
    def __init__(self):
        self.db = usersinformation
        if len(usersinformation) == 0:
            self.id = 1
        else:
            self.id = usersinformation[-1]['id'] + 1
        self.id = len(usersinformation) + 1

    def save(self, data):
        """Method for saving user"""
        data['id'] = self.id

        self.db.append(data)

    def find(self, user_id):
        """Method for finding user by id"""
        foruserinformation in self.db:
            if userinformation['id'] == user_id:
                return userinformation

        return None

    def delete(self, userinformation):
        """Method for deleting a single user"""
        self.db.remove(userinformation)
        


    def get_all(self):
        """Method for getting all user accounts"""
        return self.db
        