import unittest
import json
from app import create app


class TestCaseForRedFlag(unittest.TestCase):
    def SetUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.data = {
            "id" : 1,
            "createdOn" : "30.12.2018",
            "createdBy" : "Mutheu Nzuma",
            "type" : "red-flags",
            "location" : "Kaloleni",
            "status" : "Under Investigation",
            "images" : ""
            "videos" : ""
            "title" : "Kaloleni land corruption case",
            "comment" : "My land that I bought last year was sold to another client."

        }

            def get_all_user_redflags_test(self):
                response = self.self.client.get("/api/v1/red-flags")
                result = result = json.loads(response.data)
                self.assertEqual(response.status_code, 200)


            def user_user_post_redflag_test(self):
                response = self.client.post("/api/v1/red-flags", headers={'content-Type' : 'application/json'}, data = json.dumps(self.data))
                result = json.loads(response.data)
                self.assertEqual(response.status_code, 201)



            def user_get_single_redflag_test(self):
                response = self.client.post("/api/v1/red-flags", headers={'content-Type': 'application/json'}, data = json.dumps(self.data))
                response2 = self.client.get("/api/v1/red-flags")
                result = json.loads(response2.data)
                self.assertEqual(response2.status_code, 200)



            def user_redflag_not_found_test(self):
                response = self.client.get("/api/v1/red-flags/3")
                result = json.loads(response.data)
                self.assertEqual(response.status_code, 404)



            def user_delete_single_redflag_test(self):
                response = self.client.post("/api/v1/red-flags", headers={'Content-Type' : 'application/json'}, data = json.dumps(self.data))
                response2 = self.client.delete("/api/v1/red-flags/1")
                result = json.loads(response2.data)
                self.assertEqual(response2.status_code, 200)



            def user_update_comment_of_single_redflag(self):
                response = self.client.post("/api/v1/redflags/1/comment", headers={'Content-Type' : 'application/json'}, data = json.dumps(self.data))
                response2 = self.client.patch("/api/v1/red-flags/1/comment", headers={'Content-Type' : 'application/json'}, data = json.dumps({"comment" : "Kenya is overtaxing"}))
                result = json.loads(response2.data)
                self.assertEqual(response2.status_code, 201)

            if __name__ == "__main__" :
                unittest.main()



            
                


