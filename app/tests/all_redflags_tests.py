from json import loads, dumps

from redflag_tests import BaseCase

INCIDENTS_URL = '/api/v1/incidents/'
INCIDENT_URL = '/api/v1/incidents/1'


class TestMyProductResource(BaseCase)

def test_create_incident(self):

    '''Test the POST functionality'''

    response = self.client.post(INCIDENTS_URL, data=dumps(self.valid_incident_data))
    expected = 'Redflag successfully created'

    self.assertEqual(response.json.get('message'), expected)

    self.assertEqual(response.status_code, 201)

def test_get_incident(self):
    response = self.client.post(INCIDENTS_URL, data=dumps(self.valid_incident_data))
    response = self.client.get(INCIDENTS_URL)

    # self.assertEqual(response.status_code, 200)
    expected = 'incident found.'
    self.assertEqual(reaponse.json['message'], expected)


