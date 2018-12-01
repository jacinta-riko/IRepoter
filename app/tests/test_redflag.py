import unittest
import json
from app import create_app


class RedFlagsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.data = {
            "id": 1,
            "createdOn" : "Tue, 27 Nov 2018 21:18:13 GMT",
            "createdBy" : "Admin",
            'type' : 'red-flags',
            "location" : "Nakuru",
            "status" : "draft",
            "images" : "",
            "videos" : "",
            "title" : "Mercury in sugar",
            "comment" : "Lorem ipsum dolor sit amet."
        }

    def test_get_all_redflags(self):
        response = self.client.get("/api/v1/red-flags")
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_post_redflag(self):
        response = self.client.post("/api/v1/red-flags", headers={'Content-Type': 'application/json'}, data = json.dumps(self.data))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)

    def test_get_specific_redflag(self):
        response = self.client.post("/api/v1/red-flags", headers={'Content-Type': 'application/json'}, data = json.dumps(self.data))
        response2 = self.client.get("/api/v1/red-flags/1")
        result = json.loads(response2.data)
        self.assertEqual(response2.status_code, 200)

    def test_redflag_not_found(self):
        response = self.client.get("/api/v1/red-flags/10")
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 404)        

    def test_delete_specific_redflag(self):
        response = self.client.post("/api/v1/red-flags", headers={'Content-Type': 'application/json'}, data = json.dumps(self.data))
        response2 = self.client.delete("/api/v1/red-flags/1")
        result = json.loads(response2.data)
        self.assertEqual(response2.status_code, 200)

    def test_update_location_of_specific_redflag(self):
        response = self.client.post("/api/v1/red-flags/1/location", headers={'Content-Type': 'application/json'}, data = json.dumps(self.data))
        response2 = self.client.patch("/api/v1/red-flags/1/location", headers={'Content-Type': 'application/json'}, data = json.dumps({"location" : "Nairobi"}))
        result = json.loads(response2.data)
        self.assertEqual(response2.status_code, 201)    

    def test_update_comment_of_specific_redflag(self):
        response = self.client.post("/api/v1/red-flags/1/comment", headers={'Content-Type': 'application/json'}, data = json.dumps(self.data))
        response2 = self.client.patch("/api/v1/red-flags/1/comment", headers={'Content-Type': 'application/json'}, data = json.dumps({"comment" : "Cartels are taking over Kenya"}))
        result = json.loads(response2.data)
        self.assertEqual(response2.status_code, 201)               

if __name__ == "__main__":
    unittest.main() 