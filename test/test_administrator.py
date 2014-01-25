import unittest
import urllib

***REMOVED***

class AdministratorTestCase(object):

***REMOVED***def test_get(self):
***REMOVED******REMOVED***email = "admin@example.com"
***REMOVED******REMOVED***self.administrator.stub_request("admins.json?email=%s" %urllib.quote(email), "admin_details.json")
***REMOVED******REMOVED***administrator = self.administrator.get(email)
***REMOVED******REMOVED***self.assertEquals(administrator.EmailAddress, email)
***REMOVED******REMOVED***self.assertEquals(administrator.Name, "Admin One")
***REMOVED******REMOVED***self.assertEquals(administrator.Status, "Active")

***REMOVED***def test_get_without_args(self):
***REMOVED******REMOVED***email = "admin@example.com"
***REMOVED******REMOVED***self.administrator.stub_request("admins.json?email=%s" %urllib.quote(email), "admin_details.json")
***REMOVED******REMOVED***administrator = self.administrator.get()
***REMOVED******REMOVED***self.assertEquals(administrator.EmailAddress, email)
***REMOVED******REMOVED***self.assertEquals(administrator.Name, "Admin One")
***REMOVED******REMOVED***self.assertEquals(administrator.Status, "Active")

***REMOVED***def test_add(self):
***REMOVED******REMOVED***self.administrator.stub_request("admins.json", "add_admin.json")
***REMOVED******REMOVED***result = self.administrator.add("admin@example.com", "Admin Name")
***REMOVED******REMOVED***self.assertEquals(result.EmailAddress, "admin@example.com")

***REMOVED***def test_update(self):
***REMOVED******REMOVED***new_email = "new_email_address@example.com"
***REMOVED******REMOVED***self.administrator.stub_request("admins.json?email=%s" % urllib.quote(self.administrator.email_address), None)
***REMOVED******REMOVED***self.administrator.update(new_email, "Admin New Name")
***REMOVED******REMOVED***self.assertEquals(self.administrator.email_address, new_email)

***REMOVED***def test_delete(self):
***REMOVED******REMOVED***self.administrator.stub_request("admins.json?email=%s" % urllib.quote(self.administrator.email_address), None)
***REMOVED******REMOVED***email_address = self.administrator.delete()

class OAuthAdministatorTestCase(unittest.TestCase, AdministratorTestCase):
***REMOVED***"""Test when using OAuth to authenticate"""
***REMOVED***def setUp(self):
***REMOVED******REMOVED***self.administrator = Administrator(
***REMOVED******REMOVED******REMOVED***{"access_token": "ASP95S4aR+9KsgfHB0dapTYxNA==", "refresh_token": "5S4aASP9R+9KsgfHB0dapTYxNA=="}, "admin@example.com")

class ApiKeyAdministatorTestCase(unittest.TestCase, AdministratorTestCase):
***REMOVED***"""Test when using an API key to authenticate"""
***REMOVED***def setUp(self):
***REMOVED******REMOVED***self.administrator = Administrator(
***REMOVED******REMOVED******REMOVED***{'api_key': '123123123123123123123'}, "admin@example.com")
