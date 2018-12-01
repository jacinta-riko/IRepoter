from unittest import TestCase

from json import dumps



from app.api.v1.models import db.incident

from app import create_app

class redflag(TestCase):





    def setup(self):

        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.valid_incident_data = {
            "title" : 'corruption',
            "type" : 'intervention'
        }

def tearDown(self):

    db.drop()
    self.app_context.pop()