import unittest
import urllib

***REMOVED***

class PeopleTestCase(object):

***REMOVED***def test_get(self):
***REMOVED******REMOVED***email = "person@example.com"
***REMOVED******REMOVED***self.person.stub_request("clients/%s/people.json?email=%s" % (self.client_id, urllib.quote(email)), "person_details.json")
***REMOVED******REMOVED***person = self.person.get(self.client_id, email)
***REMOVED******REMOVED***self.assertEquals(person.EmailAddress, email)
***REMOVED******REMOVED***self.assertEquals(person.Name, "Person One")
***REMOVED******REMOVED***self.assertEquals(person.AccessLevel, 1023)
***REMOVED******REMOVED***self.assertEquals(person.Status, "Active")***REMOVED******REMOVED***

***REMOVED***def test_add(self):
***REMOVED******REMOVED***self.person.stub_request("clients/%s/people.json" % self.client_id, "add_person.json")
***REMOVED******REMOVED***result = self.person.add(self.client_id, "person@example.com", "Person Name", 1023, "Password")
***REMOVED******REMOVED***self.assertEquals(result.EmailAddress, "person@example.com")
***REMOVED***
***REMOVED***def test_update(self):
***REMOVED******REMOVED***new_email = "new_email_address@example.com"
***REMOVED******REMOVED***self.person.stub_request("clients/%s/people.json?email=%s" % (self.client_id, urllib.quote(self.person.email_address)), None)
***REMOVED******REMOVED***self.person.update(new_email, "Person New Name", 31, 'blah')
***REMOVED******REMOVED***self.assertEquals(self.person.email_address, new_email)

***REMOVED***def test_delete(self):
***REMOVED******REMOVED***self.person.stub_request("clients/%s/people.json?email=%s" % (self.client_id, urllib.quote(self.person.email_address)), None)
***REMOVED******REMOVED***email_address = self.person.delete()

class OAuthPeopleTestCase(unittest.TestCase, PeopleTestCase):
***REMOVED***"""Test when using OAuth to authenticate"""
***REMOVED***def setUp(self):
***REMOVED******REMOVED***self.client_id = "d98h2938d9283d982u3d98u88"
***REMOVED******REMOVED***self.person = Person(
***REMOVED******REMOVED******REMOVED***{"access_token": "98u9q8uw9ddw", "refresh_token": "9u09i02e3"},
***REMOVED******REMOVED******REMOVED***self.client_id, "person@example.com")

class ApiKeyPeopleTestCase(unittest.TestCase, PeopleTestCase):
***REMOVED***"""Test when using an API key to authenticate"""
***REMOVED***def setUp(self):
***REMOVED******REMOVED***self.client_id = "d98h2938d9283d982u3d98u88"
***REMOVED******REMOVED***self.person = Person(
***REMOVED******REMOVED******REMOVED***{'api_key': '123123123123123123123'},
***REMOVED******REMOVED******REMOVED***self.client_id, "person@example.com")
