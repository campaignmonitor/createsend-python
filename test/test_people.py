import unittest
import urllib

from createsend import *

class PeopleTestCase(object):

  def test_get(self):
    email = "person@example.com"
    self.person.stub_request("clients/%s/people.json?email=%s" % (self.client_id, urllib.quote(email)), "person_details.json")
    person = self.person.get(self.client_id, email)
    self.assertEquals(person.EmailAddress, email)
    self.assertEquals(person.Name, "Person One")
    self.assertEquals(person.AccessLevel, 1023)
    self.assertEquals(person.Status, "Active")    

  def test_add(self):
    self.person.stub_request("clients/%s/people.json" % self.client_id, "add_person.json")
    result = self.person.add(self.client_id, "person@example.com", "Person Name", 1023, "Password")
    self.assertEquals(result.EmailAddress, "person@example.com")
  
  def test_update(self):
    new_email = "new_email_address@example.com"
    self.person.stub_request("clients/%s/people.json?email=%s" % (self.client_id, urllib.quote(self.person.email_address)), None)
    self.person.update(new_email, "Person New Name", 31, 'blah')
    self.assertEquals(self.person.email_address, new_email)

  def test_delete(self):
    self.person.stub_request("clients/%s/people.json?email=%s" % (self.client_id, urllib.quote(self.person.email_address)), None)
    email_address = self.person.delete()

class OAuthPeopleTestCase(unittest.TestCase, PeopleTestCase):
  """Test when using OAuth to authenticate"""
  def setUp(self):
    self.client_id = "d98h2938d9283d982u3d98u88"
    self.person = Person(
      {"access_token": "98u9q8uw9ddw", "refresh_token": "9u09i02e3"},
      self.client_id, "person@example.com")

class ApiKeyPeopleTestCase(unittest.TestCase, PeopleTestCase):
  """Test when using an API key to authenticate"""
  def setUp(self):
    self.client_id = "d98h2938d9283d982u3d98u88"
    self.person = Person(
      {'api_key': '123123123123123123123'},
      self.client_id, "person@example.com")
