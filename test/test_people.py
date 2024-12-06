from urllib.parse import quote
import unittest

from createsend.person import Person


class PeopleTestCase:

***REMOVED******REMOVED***def test_get(self):
***REMOVED******REMOVED******REMOVED******REMOVED***email = "person@example.com"
***REMOVED******REMOVED******REMOVED******REMOVED***self.person.stub_request("clients/%s/people.json?email=%s" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.client_id, quote(email)), "person_details.json")
***REMOVED******REMOVED******REMOVED******REMOVED***person = self.person.get(self.client_id, email)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(person.EmailAddress, email)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(person.Name, "Person One")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(person.AccessLevel, 1023)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(person.Status, "Active")

***REMOVED******REMOVED***def test_get_without_args(self):
***REMOVED******REMOVED******REMOVED******REMOVED***email = "person@example.com"
***REMOVED******REMOVED******REMOVED******REMOVED***self.person.stub_request("clients/%s/people.json?email=%s" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.client_id, quote(email)), "person_details.json")
***REMOVED******REMOVED******REMOVED******REMOVED***person = self.person.get()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(person.EmailAddress, email)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(person.Name, "Person One")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(person.AccessLevel, 1023)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(person.Status, "Active")

***REMOVED******REMOVED***def test_add(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.person.stub_request("clients/%s/people.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.client_id, "add_person.json")
***REMOVED******REMOVED******REMOVED******REMOVED***result = self.person.add(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.client_id, "person@example.com", "Person Name", 1023, "Password")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(result.EmailAddress, "person@example.com")

***REMOVED******REMOVED***def test_update(self):
***REMOVED******REMOVED******REMOVED******REMOVED***new_email = "new_email_address@example.com"
***REMOVED******REMOVED******REMOVED******REMOVED***self.person.stub_request("clients/%s/people.json?email=%s" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.client_id, quote(self.person.email_address)), None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.person.update(new_email, "Person New Name", 31, 'blah')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(self.person.email_address, new_email)

***REMOVED******REMOVED***def test_delete(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.person.stub_request("clients/%s/people.json?email=%s" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.client_id, quote(self.person.email_address)), None)
***REMOVED******REMOVED******REMOVED******REMOVED***email_address = self.person.delete()


class OAuthPeopleTestCase(unittest.TestCase, PeopleTestCase):
***REMOVED******REMOVED***"""Test when using OAuth to authenticate"""

***REMOVED******REMOVED***def setUp(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.client_id = "d98h2938d9283d982u3d98u88"
***REMOVED******REMOVED******REMOVED******REMOVED***self.person = Person(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{"access_token": "ASP95S4aR+9KsgfHB0dapTYxNA==",
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"refresh_token": "5S4aASP9R+9KsgfHB0dapTYxNA=="},
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.client_id, "person@example.com")


class ApiKeyPeopleTestCase(unittest.TestCase, PeopleTestCase):
***REMOVED******REMOVED***"""Test when using an API key to authenticate"""

***REMOVED******REMOVED***def setUp(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.client_id = "d98h2938d9283d982u3d98u88"
***REMOVED******REMOVED******REMOVED******REMOVED***self.person = Person(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{'api_key': '123123123123123123123'},
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.client_id, "person@example.com")
