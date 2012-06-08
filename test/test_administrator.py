import unittest
import urllib

from createsend import *

class AdministratorTestCase(unittest.TestCase):

  def setUp(self):
    self.api_key = '123123123123123123123'
    CreateSend.api_key = self.api_key   
    self.administrator = Administrator("admin@example.com")

  def test_get(self):
    email = "admin@example.com"
    self.administrator.stub_request("admins.json?email=%s" %urllib.quote(email), "admin_details.json")
    administrator = self.administrator.get(email)
    self.assertEquals(administrator.EmailAddress, email)
    self.assertEquals(administrator.Name, "Admin One")
    self.assertEquals(administrator.Status, "Active")    

  def test_add(self):
    self.administrator.stub_request("admins.json", "add_admin.json")
    result = self.administrator.add("admin@example.com", "Admin Name")
    self.assertEquals(result.EmailAddress, "admin@example.com")
  
  def test_update(self):
    new_email = "new_email_address@example.com"
    self.administrator.stub_request("admins.json?email=%s" % urllib.quote(self.administrator.email_address), None)
    self.administrator.update(new_email, "Admin New Name")
    self.assertEquals(self.administrator.email_address, new_email)

  def test_delete(self):
    self.administrator.stub_request("admins.json?email=%s" % urllib.quote(self.administrator.email_address), None)
    email_address = self.administrator.delete()
    
    