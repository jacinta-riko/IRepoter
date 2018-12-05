# """Docstring for testcases"""
# import unittest
# import json
# from app import create_app


# class UserTestCase(unittest.TestCase):
#     """Docstring for user test case"""
#     def setUp(self):
#         APP = create_app()
#         self.app = APP.test_client()
#         self.data = {
#             "firstname" : "Jacinta",
#             "lastname" : "Riko",
#             'email' : "jacintariko@yahoo.com",
#             "phonenumber" : "072222222",
#             "residence" : "Nairobi",
#             "username" : "jacinta",
#             "password" : "amani",
#             "registered" : "",
#             "isAdmin" : "True"
#         }

#     def test_get_all_users_account(self):
#         """method for testing get all users"""
#         response = self.app.get("/api/v1/users")
#         self.assertEqual(response.status_code, 200)
        

#     def test_post_user_account(self):
#         """method for testing post user"""
#         response = self.app.post("/api/v1/user", headers={'Content-Type': 'application/json'},
#          data = json.dumps(self.data))
#         result = json.loads(response.data)
#         self.assertEqual(response.status_code, 201)
#         self.assertIn('Sucessfully created new user account',str(result))

#     def test_get_specific_user_account(self):
#         """method for testing get specific user"""
#         self.app.post("/api/v1/red-flags", headers={'Content-Type': 'application/json'},
#          data = json.dumps(self.userinformation))
#         response = self.app.get("/api/v1/users/1")
#         json.loads(response.data)
#         self.assertEqual(response.status_code, 200)     

#     def test_delete_specific_user_account(self):
#         """method for testing delete a specific user account"""
#         self.app.post("/api/v1/user", headers={'Content-Type': 'application/json'},
#          data = json.dumps(self.userinformation))
#         response = self.app.delete("/api/v1/users/1")
#         result = json.loads(response.data)
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('User account has been sucessfully deleted',str(result))

#     # def test_update_location_of_specific_(self):
#     #     """method for testing update location for specific redflag"""
#     #     self.app.post("/api/v1/red-flags/1/location", headers={'Content-Type': 'application/json'},
#     #      data = json.dumps(self.redflag))
#     #     response = self.app.patch("/api/v1/red-flags/1/location", headers={'Content-Type': 'application/json'},
#     #      data = json.dumps({"location" : "Kaloleni"}))
#     #     result = json.loads(response.data)
#     #     self.assertEqual(response.status_code, 201)
#     #     self.assertIn("Sucessfully updated red-flag location",str(result))
            

#     # def test_update_comment_of_specific_redflag(self):
#     #     """method for testing update comment of specific redflag"""
#     #     self.app.post("/api/v1/red-flags/1/comment", headers={'Content-Type': 'application/json'},
#     #      data = json.dumps(self.redflag))
#     #     response = self.app.patch("/api/v1/red-flags/1/comment", headers={'Content-Type': 'application/json'},
#     #      data = json.dumps({"comment" : "police wanted money to pass the offense"}))
#     #     result = json.loads(response.data)
#     #     self.assertEqual(response.status_code, 201) 
#     #     self.assertIn("Successfully updated red-flag comment",
#     #     str(result))

#     # def test_redflag_not_found(self):
#     #     response = self.app.get("/api/v1/red-flags/10")
#     #     result = json.loads(response.data)
#     #     self.assertEqual(response.status_code, 404) 
#     #     self.assertIn("Red-flag does not exist",str(result))                

