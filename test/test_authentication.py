import unittest
import urllib
from urlparse import urlparse

from createsend import *

class AuthenticationTestCase(unittest.TestCase):

  def setUp(self):
    # The following line just resets the state of the api_key class variable
    # set by the test_deprecated_can_authenticate_by_setting_class_api_key test.
    CreateSend.api_key = None

    self.oauth_credentials = {"access_token": "98u9q8uw9ddw", "refresh_token": "9u09i02e3"}
    self.api_key = '123123123123123123123'
    self.base_uri = 'http://api.createsend.com/api/v3'
    self.cs = CreateSend()

  def test_deprecated_can_authenticate_by_setting_class_api_key(self):
    """The following line demonstrates the deprecated way in which
    authentication should be handled."""
    CreateSend.api_key = self.api_key
    self.cs.stub_request("systemdate.json", "systemdate.json")
    systemdate = self.cs.systemdate()
    self.assertEquals(self.cs.headers['Authorization'], "Basic %s" % base64.b64encode("%s:x" % self.api_key))
    self.assertEquals(systemdate, "2010-10-15 09:27:00")

  def test_deprecated_can_authenticate_by_setting_instance_api_key(self):
    """The following line demonstrates the deprecated way in which
    authentication should be handled."""
    self.cs.api_key = self.api_key
    self.cs.stub_request("systemdate.json", "systemdate.json")
    systemdate = self.cs.systemdate()
    self.assertEquals(self.cs.headers['Authorization'], "Basic %s" % base64.b64encode("%s:x" % self.api_key))
    self.assertEquals(systemdate, "2010-10-15 09:27:00")

  def test_can_authenticate_by_calling_auth_with_api_key(self):
    self.cs.auth({'api_key': self.api_key})
    self.cs.stub_request("systemdate.json", "systemdate.json")
    systemdate = self.cs.systemdate()
    self.assertEquals(self.cs.headers['Authorization'], "Basic %s" % base64.b64encode("%s:x" % self.api_key))
    self.assertEquals(systemdate, "2010-10-15 09:27:00")

  def test_can_authenticate_by_calling_auth_with_oauth_credentials(self):
    self.cs.auth(self.oauth_credentials)
    self.cs.stub_request("systemdate.json", "systemdate.json")
    systemdate = self.cs.systemdate()
    self.assertEquals(self.cs.headers['Authorization'], "Bearer %s" % self.oauth_credentials['access_token'])
    self.assertEquals(systemdate, "2010-10-15 09:27:00")

  def test_raise_error_when_authenticating_with_oauth_and_token_expired(self):
    self.cs.auth(self.oauth_credentials)
    self.cs.stub_request("systemdate.json", 'expired_oauth_token_api_error.json', status=401)
    self.assertRaises(ExpiredOAuthToken, self.cs.systemdate)
