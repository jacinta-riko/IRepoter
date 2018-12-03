import unittest
import json
from app import create_app


class RedFlagsTestCase(unittest.TestCase):
    def setUp(self):
        APP = create_app()
        self.app = APP.test_client()
        self.redflag = {
            "id": 1,
            "createdOn" : "Friday, 30 Dec 2018 22:10:33 GMT",
            "createdBy" : "Admin",
            'type' : 'red-flags',
            "location" : "Kaloleni",
            "status" : "Under investigation",
            "images" : "",
            "videos" : "",
            "title" : "Michuki seatbealts",
            "comment" : "police wanted money to pass the offense"
        }

    def test_get_all_redflags(self):
        response = self.app.get("/api/v1/red-flags")
        # result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        

    def test_post_redflag(self):
        response = self.app.post("/api/v1/red-flags", headers={'Content-Type': 'application/json'},
         data = json.dumps(self.redflag))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Created red-flag record',str(result))

    def test_get_specific_redflag(self):
        self.app.post("/api/v1/red-flags", headers={'Content-Type': 'application/json'},
         data = json.dumps(self.redflag))
        response = self.app.get("/api/v1/red-flags/1")
        json.loads(response.data)
        self.assertEqual(response.status_code, 200)     

    def test_delete_specific_redflag(self):
        self.app.post("/api/v1/red-flags", headers={'Content-Type': 'application/json'},
         data = json.dumps(self.redflag))
        response = self.app.delete("/api/v1/red-flags/1")
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Red-flag record has been sucessfully deleted',str(result))

    def test_update_location_of_specific_redflag(self):
        self.app.post("/api/v1/red-flags/1/location", headers={'Content-Type': 'application/json'},
         data = json.dumps(self.redflag))
        response = self.app.patch("/api/v1/red-flags/1/location", headers={'Content-Type': 'application/json'},
         data = json.dumps({"location" : "Kaloleni"}))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("Sucessfully updated red-flag location",str(result))
            

    def test_update_comment_of_specific_redflag(self):
        self.app.post("/api/v1/red-flags/1/comment", headers={'Content-Type': 'application/json'},
         data = json.dumps(self.redflag))
        response = self.app.patch("/api/v1/red-flags/1/comment", headers={'Content-Type': 'application/json'},
         data = json.dumps({"comment" : "police wanted money to pass the offense"}))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201) 
        self.assertIn("Successfully updated red-flag comment",
        str(result))

    # def test_redflag_not_found(self):
    #     response = self.app.get("/api/v1/red-flags/10")
    #     result = json.loads(response.data)
    #     self.assertEqual(response.status_code, 404) 
    #     self.assertIn("Red-flag does not exist",str(result))                

if __name__ == "__main__": 
    unittest.main()