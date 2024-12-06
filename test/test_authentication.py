import base64
import unittest

from createsend.createsend import CreateSend, ExpiredOAuthToken


class AuthenticationTestCase(unittest.TestCase):

***REMOVED******REMOVED***def setUp(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.oauth_auth_details = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"access_token": "ASP95S4aR+9KsgfHB0dapTYxNA==", "refresh_token": "5S4aASP9R+9KsgfHB0dapTYxNA=="}
***REMOVED******REMOVED******REMOVED******REMOVED***self.api_key_auth_details = {'api_key': '123123123123123123123'}

***REMOVED******REMOVED***def test_authorize_url_with_state(self):
***REMOVED******REMOVED******REMOVED******REMOVED***client_id = 8998879
***REMOVED******REMOVED******REMOVED******REMOVED***redirect_uri = 'http://example.com/auth'
***REMOVED******REMOVED******REMOVED******REMOVED***scope = 'ViewReports,CreateCampaigns,SendCampaigns'
***REMOVED******REMOVED******REMOVED******REMOVED***state = 89879287

***REMOVED******REMOVED******REMOVED******REMOVED***self.cs = CreateSend(self.oauth_auth_details)
***REMOVED******REMOVED******REMOVED******REMOVED***authorize_url = self.cs.authorize_url(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***client_id=client_id,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***redirect_uri=redirect_uri,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***scope=scope,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***state=state
***REMOVED******REMOVED******REMOVED******REMOVED***)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(authorize_url,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"https://api.createsend.com/oauth?client_id=8998879&redirect_uri=http%3A%2F%2Fexample.com%2Fauth&scope=ViewReports%2CCreateCampaigns%2CSendCampaigns&state=89879287"
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***)

***REMOVED******REMOVED***def test_authorize_url_without_state(self):
***REMOVED******REMOVED******REMOVED******REMOVED***client_id = 8998879
***REMOVED******REMOVED******REMOVED******REMOVED***redirect_uri = 'http://example.com/auth'
***REMOVED******REMOVED******REMOVED******REMOVED***scope = 'ViewReports,CreateCampaigns,SendCampaigns'

***REMOVED******REMOVED******REMOVED******REMOVED***self.cs = CreateSend(self.oauth_auth_details)
***REMOVED******REMOVED******REMOVED******REMOVED***authorize_url = self.cs.authorize_url(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***client_id=client_id,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***redirect_uri=redirect_uri,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***scope=scope
***REMOVED******REMOVED******REMOVED******REMOVED***)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(authorize_url,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"https://api.createsend.com/oauth?client_id=8998879&redirect_uri=http%3A%2F%2Fexample.com%2Fauth&scope=ViewReports%2CCreateCampaigns%2CSendCampaigns"
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***)

***REMOVED******REMOVED***def test_exchange_token_success(self):
***REMOVED******REMOVED******REMOVED******REMOVED***client_id = 8998879
***REMOVED******REMOVED******REMOVED******REMOVED***client_secret = 'iou0q9wud0q9wd0q9wid0q9iwd0q9wid0q9wdqwd'
***REMOVED******REMOVED******REMOVED******REMOVED***redirect_uri = 'http://example.com/auth'
***REMOVED******REMOVED******REMOVED******REMOVED***code = '98uqw9d8qu9wdu'
***REMOVED******REMOVED******REMOVED******REMOVED***self.cs = CreateSend(self.oauth_auth_details)
***REMOVED******REMOVED******REMOVED******REMOVED***self.cs.stub_request(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"https://api.createsend.com/oauth/token", "oauth_exchange_token.json")
***REMOVED******REMOVED******REMOVED******REMOVED***access_token, expires_in, refresh_token = self.cs.exchange_token(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***client_id=client_id,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***client_secret=client_secret,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***redirect_uri=redirect_uri,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***code=code
***REMOVED******REMOVED******REMOVED******REMOVED***)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(self.cs.faker.actual_body,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"grant_type=authorization_code&client_id=8998879&client_secret=iou0q9wud0q9wd0q9wid0q9iwd0q9wid0q9wdqwd&redirect_uri=http%3A%2F%2Fexample.com%2Fauth&code=98uqw9d8qu9wdu")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(access_token, "SlAV32hkKG")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(expires_in, 1209600)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(refresh_token, "tGzv3JOkF0XG5Qx2TlKWIA")

***REMOVED******REMOVED***def test_echange_token_failure(self):
***REMOVED******REMOVED******REMOVED******REMOVED***client_id = 8998879
***REMOVED******REMOVED******REMOVED******REMOVED***client_secret = 'iou0q9wud0q9wd0q9wid0q9iwd0q9wid0q9wdqwd'
***REMOVED******REMOVED******REMOVED******REMOVED***redirect_uri = 'http://example.com/auth'
***REMOVED******REMOVED******REMOVED******REMOVED***code = 'invalidcode'
***REMOVED******REMOVED******REMOVED******REMOVED***self.cs = CreateSend(self.oauth_auth_details)
***REMOVED******REMOVED******REMOVED******REMOVED***self.cs.stub_request(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"https://api.createsend.com/oauth/token", "oauth_exchange_token_error.json")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertRaises(Exception, self.cs.exchange_token,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***client_id, client_secret, redirect_uri, code)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(self.cs.faker.actual_body,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"grant_type=authorization_code&client_id=8998879&client_secret=iou0q9wud0q9wd0q9wid0q9iwd0q9wid0q9wdqwd&redirect_uri=http%3A%2F%2Fexample.com%2Fauth&code=invalidcode")

***REMOVED******REMOVED***def test_can_authenticate_by_calling_auth_with_api_key(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cs = CreateSend(self.api_key_auth_details)
***REMOVED******REMOVED******REMOVED******REMOVED***self.cs.stub_request("systemdate.json", "systemdate.json")
***REMOVED******REMOVED******REMOVED******REMOVED***systemdate = self.cs.systemdate()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(self.cs.headers['Authorization'], "Basic %s" % base64.b64encode(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***("%s:x" % self.api_key_auth_details['api_key']).encode()).decode())
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(systemdate, "2010-10-15 09:27:00")

***REMOVED******REMOVED***def test_can_authenticate_by_calling_auth_with_oauth_credentials(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cs = CreateSend(self.oauth_auth_details)
***REMOVED******REMOVED******REMOVED******REMOVED***self.cs.stub_request("systemdate.json", "systemdate.json")
***REMOVED******REMOVED******REMOVED******REMOVED***systemdate = self.cs.systemdate()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(self.cs.headers[
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***'Authorization'], "Bearer %s" % self.oauth_auth_details['access_token'])
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(systemdate, "2010-10-15 09:27:00")

***REMOVED******REMOVED***def test_raise_error_when_authenticating_with_oauth_and_token_expired(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cs = CreateSend(self.oauth_auth_details)
***REMOVED******REMOVED******REMOVED******REMOVED***self.cs.stub_request(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"systemdate.json", 'expired_oauth_token_api_error.json', status=401)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertRaises(ExpiredOAuthToken, self.cs.systemdate)

***REMOVED******REMOVED***def test_refresh_token(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cs = CreateSend(self.oauth_auth_details)
***REMOVED******REMOVED******REMOVED******REMOVED***self.cs.stub_request(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"https://api.createsend.com/oauth/token", "refresh_oauth_token.json")
***REMOVED******REMOVED******REMOVED******REMOVED***new_access_token, new_expires_in, new_refresh_token = self.cs.refresh_token()

***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(self.cs.faker.actual_body,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"grant_type=refresh_token&refresh_token=5S4aASP9R%2B9KsgfHB0dapTYxNA%3D%3D")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(new_access_token, "SlAV32hkKG2e12e")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(new_expires_in, 1209600)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(new_refresh_token, "tGzv3JOkF0XG5Qx2TlKWIA")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(self.cs.auth_details,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{'access_token': new_access_token, 'refresh_token': new_refresh_token})

***REMOVED******REMOVED***def test_refresh_token_error_when_refresh_token_none(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cs = CreateSend(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{"access_token": "ASP95S4aR+9KsgfHB0dapTYxNA==", "refresh_token": None})
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertRaises(Exception, self.cs.refresh_token)

***REMOVED******REMOVED***def test_refresh_token_error_when_no_refresh_token_passed_in(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cs = CreateSend({"access_token": "ASP95S4aR+9KsgfHB0dapTYxNA=="})
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertRaises(Exception, self.cs.refresh_token)

***REMOVED******REMOVED***def test_refresh_token_error_when_no_authentication(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cs = CreateSend()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertRaises(Exception, self.cs.refresh_token)
