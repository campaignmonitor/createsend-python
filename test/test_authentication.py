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
    self.cs = CreateSend()

  def test_authorize_url_with_state(self):
    client_id = 8998879
    client_secret = 'iou0q9wud0q9wd0q9wid0q9iwd0q9wid0q9wdqwd'
    redirect_uri = 'http://example.com/auth'
    scope = 'ViewReports,CreateCampaigns,SendCampaigns'
    state = 89879287

    self.cs.auth(self.oauth_credentials)
    authorize_url = self.cs.authorize_url(
      client_id=client_id,
      client_secret=client_secret,
      redirect_uri=redirect_uri,
      scope=scope,
      state=state)
    self.assertEquals(authorize_url,
      "https://api.createsend.com/oauth?client_id=8998879&client_secret=iou0q9wud0q9wd0q9wid0q9iwd0q9wid0q9wdqwd&redirect_uri=http%3A%2F%2Fexample.com%2Fauth&scope=ViewReports%2CCreateCampaigns%2CSendCampaigns&state=89879287"
    )

  def test_authorize_url_without_state(self):
    client_id = 8998879
    client_secret = 'iou0q9wud0q9wd0q9wid0q9iwd0q9wid0q9wdqwd'
    redirect_uri = 'http://example.com/auth'
    scope = 'ViewReports,CreateCampaigns,SendCampaigns'

    self.cs.auth(self.oauth_credentials)
    authorize_url = self.cs.authorize_url(
      client_id=client_id,
      client_secret=client_secret,
      redirect_uri=redirect_uri,
      scope=scope)
    self.assertEquals(authorize_url,
      "https://api.createsend.com/oauth?client_id=8998879&client_secret=iou0q9wud0q9wd0q9wid0q9iwd0q9wid0q9wdqwd&redirect_uri=http%3A%2F%2Fexample.com%2Fauth&scope=ViewReports%2CCreateCampaigns%2CSendCampaigns"
    )

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

  def test_refresh_token(self):
    self.cs.auth(self.oauth_credentials)
    self.cs.stub_request("https://api.createsend.com/oauth/token", "refresh_oauth_token.json")
    new_access_token, new_refresh_token = self.cs.refresh_token()
    self.assertEquals(new_access_token, "SlAV32hkKG2e12e")
    self.assertEquals(new_refresh_token, "tGzv3JOkF0XG5Qx2TlKWIA")
    self.assertEquals(self.cs.authentication,
      { 'access_token': new_access_token, 'refresh_token': new_refresh_token })

  # Tests for the deprecated method of authenticating.
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
