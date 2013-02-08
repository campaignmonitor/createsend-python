import unittest
import urllib
from urlparse import urlparse

***REMOVED***

class AuthenticationTestCase(unittest.TestCase):

***REMOVED***def setUp(self):
***REMOVED******REMOVED***# The following line just resets the state of the api_key class variable
***REMOVED******REMOVED***# set by the test_deprecated_can_authenticate_by_setting_class_api_key test.
***REMOVED******REMOVED***CreateSend.api_key = None

***REMOVED******REMOVED***self.oauth_credentials = {"access_token": "98u9q8uw9ddw", "refresh_token": "9u09i02e3"}
***REMOVED******REMOVED***self.api_key = '123123123123123123123'
***REMOVED******REMOVED***self.cs = CreateSend()

***REMOVED***def test_deprecated_can_authenticate_by_setting_class_api_key(self):
***REMOVED******REMOVED***"""The following line demonstrates the deprecated way in which
***REMOVED******REMOVED***authentication should be handled."""
***REMOVED******REMOVED***CreateSend.api_key = self.api_key
***REMOVED******REMOVED***self.cs.stub_request("systemdate.json", "systemdate.json")
***REMOVED******REMOVED***systemdate = self.cs.systemdate()
***REMOVED******REMOVED***self.assertEquals(self.cs.headers['Authorization'], "Basic %s" % base64.b64encode("%s:x" % self.api_key))
***REMOVED******REMOVED***self.assertEquals(systemdate, "2010-10-15 09:27:00")

***REMOVED***def test_deprecated_can_authenticate_by_setting_instance_api_key(self):
***REMOVED******REMOVED***"""The following line demonstrates the deprecated way in which
***REMOVED******REMOVED***authentication should be handled."""
***REMOVED******REMOVED***self.cs.api_key = self.api_key
***REMOVED******REMOVED***self.cs.stub_request("systemdate.json", "systemdate.json")
***REMOVED******REMOVED***systemdate = self.cs.systemdate()
***REMOVED******REMOVED***self.assertEquals(self.cs.headers['Authorization'], "Basic %s" % base64.b64encode("%s:x" % self.api_key))
***REMOVED******REMOVED***self.assertEquals(systemdate, "2010-10-15 09:27:00")

***REMOVED***def test_can_authenticate_by_calling_auth_with_api_key(self):
***REMOVED******REMOVED***self.cs.auth({'api_key': self.api_key})
***REMOVED******REMOVED***self.cs.stub_request("systemdate.json", "systemdate.json")
***REMOVED******REMOVED***systemdate = self.cs.systemdate()
***REMOVED******REMOVED***self.assertEquals(self.cs.headers['Authorization'], "Basic %s" % base64.b64encode("%s:x" % self.api_key))
***REMOVED******REMOVED***self.assertEquals(systemdate, "2010-10-15 09:27:00")

***REMOVED***def test_can_authenticate_by_calling_auth_with_oauth_credentials(self):
***REMOVED******REMOVED***self.cs.auth(self.oauth_credentials)
***REMOVED******REMOVED***self.cs.stub_request("systemdate.json", "systemdate.json")
***REMOVED******REMOVED***systemdate = self.cs.systemdate()
***REMOVED******REMOVED***self.assertEquals(self.cs.headers['Authorization'], "Bearer %s" % self.oauth_credentials['access_token'])
***REMOVED******REMOVED***self.assertEquals(systemdate, "2010-10-15 09:27:00")

***REMOVED***def test_raise_error_when_authenticating_with_oauth_and_token_expired(self):
***REMOVED******REMOVED***self.cs.auth(self.oauth_credentials)
***REMOVED******REMOVED***self.cs.stub_request("systemdate.json", 'expired_oauth_token_api_error.json', status=401)
***REMOVED******REMOVED***self.assertRaises(ExpiredOAuthToken, self.cs.systemdate)

***REMOVED***def test_refresh_token(self):
***REMOVED******REMOVED***self.cs.auth(self.oauth_credentials)
***REMOVED******REMOVED***self.cs.stub_request("https://api.createsend.com/oauth/token", "refresh_oauth_token.json")
***REMOVED******REMOVED***new_access_token, new_refresh_token = self.cs.refresh_token()
***REMOVED******REMOVED***self.assertEquals(new_access_token, "SlAV32hkKG2e12e")
***REMOVED******REMOVED***self.assertEquals(new_refresh_token, "tGzv3JOkF0XG5Qx2TlKWIA")
***REMOVED******REMOVED***self.assertEquals(self.cs.authentication,
***REMOVED******REMOVED******REMOVED***{ 'access_token': new_access_token, 'refresh_token': new_refresh_token })
