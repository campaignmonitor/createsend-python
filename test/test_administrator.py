from six.moves.urllib.parse import quote
import unittest

from createsend.administrator import Administrator


class AdministratorTestCase(object):

***REMOVED******REMOVED***def test_get(self):
***REMOVED******REMOVED******REMOVED******REMOVED***email = "admin@example.com"
***REMOVED******REMOVED******REMOVED******REMOVED***self.administrator.stub_request(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"admins.json?email=%s" % quote(email), "admin_details.json")
***REMOVED******REMOVED******REMOVED******REMOVED***administrator = self.administrator.get(email)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(administrator.EmailAddress, email)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(administrator.Name, "Admin One")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(administrator.Status, "Active")

***REMOVED******REMOVED***def test_get_without_args(self):
***REMOVED******REMOVED******REMOVED******REMOVED***email = "admin@example.com"
***REMOVED******REMOVED******REMOVED******REMOVED***self.administrator.stub_request(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"admins.json?email=%s" % quote(email), "admin_details.json")
***REMOVED******REMOVED******REMOVED******REMOVED***administrator = self.administrator.get()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(administrator.EmailAddress, email)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(administrator.Name, "Admin One")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(administrator.Status, "Active")

***REMOVED******REMOVED***def test_add(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.administrator.stub_request("admins.json", "add_admin.json")
***REMOVED******REMOVED******REMOVED******REMOVED***result = self.administrator.add("admin@example.com", "Admin Name")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(result.EmailAddress, "admin@example.com")

***REMOVED******REMOVED***def test_update(self):
***REMOVED******REMOVED******REMOVED******REMOVED***new_email = "new_email_address@example.com"
***REMOVED******REMOVED******REMOVED******REMOVED***self.administrator.stub_request("admins.json?email=%s" % quote(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.administrator.email_address), None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.administrator.update(new_email, "Admin New Name")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(self.administrator.email_address, new_email)

***REMOVED******REMOVED***def test_delete(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.administrator.stub_request("admins.json?email=%s" % quote(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.administrator.email_address), None)
***REMOVED******REMOVED******REMOVED******REMOVED***email_address = self.administrator.delete()


class OAuthAdministatorTestCase(unittest.TestCase, AdministratorTestCase):
***REMOVED******REMOVED***"""Test when using OAuth to authenticate"""

***REMOVED******REMOVED***def setUp(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.administrator = Administrator(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{"access_token": "ASP95S4aR+9KsgfHB0dapTYxNA==", "refresh_token": "5S4aASP9R+9KsgfHB0dapTYxNA=="}, "admin@example.com")


class ApiKeyAdministatorTestCase(unittest.TestCase, AdministratorTestCase):
***REMOVED******REMOVED***"""Test when using an API key to authenticate"""

***REMOVED******REMOVED***def setUp(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.administrator = Administrator(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{'api_key': '123123123123123123123'}, "admin@example.com")
