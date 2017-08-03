from __future__ import absolute_import

***REMOVED***
import platform
import base64
import gzip
***REMOVED***
from six import BytesIO
from six.moves.urllib.parse import parse_qs, urlencode, urlparse
try:
***REMOVED******REMOVED***import json
except ImportError:
***REMOVED******REMOVED***import simplejson as json
from createsend.utils import VerifiedHTTPSConnection, json_to_py, get_faker

__version_info__ = ('4', '2', '2')
__version__ = '.'.join(__version_info__)


class CreateSendError(Exception):
***REMOVED******REMOVED***"""Represents a CreateSend API error and contains specific data about the error."""

***REMOVED******REMOVED***def __init__(self, data):
***REMOVED******REMOVED******REMOVED******REMOVED***self.data = data

***REMOVED******REMOVED***def __str__(self):
***REMOVED******REMOVED******REMOVED******REMOVED***# self.data should contain Code, Message and optionally ResultData
***REMOVED******REMOVED******REMOVED******REMOVED***extra = ("\nExtra result data: %s" % self.data.ResultData) if hasattr(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.data, 'ResultData') else ""
***REMOVED******REMOVED******REMOVED******REMOVED***return "The CreateSend API responded with the following error - %s: %s%s" % (self.data.Code, self.data.Message, extra)


class ClientError(Exception):
***REMOVED******REMOVED***pass


class ServerError(Exception):
***REMOVED******REMOVED***pass


class BadRequest(CreateSendError):
***REMOVED******REMOVED***pass


class Unauthorized(CreateSendError):
***REMOVED******REMOVED***pass


class NotFound(ClientError):
***REMOVED******REMOVED***pass


class Unavailable(Exception):
***REMOVED******REMOVED***pass


class ExpiredOAuthToken(Unauthorized):
***REMOVED******REMOVED***"""Raised for HTTP response code of 401, specifically when an OAuth
***REMOVED******REMOVED***token has expired (Code: 121, Message: 'Expired OAuth Token')"""
***REMOVED******REMOVED***pass


class CreateSendBase(object):
***REMOVED******REMOVED***auth_details = None

***REMOVED******REMOVED***def __init__(self, auth):
***REMOVED******REMOVED******REMOVED******REMOVED***self.fake_web = False
***REMOVED******REMOVED******REMOVED******REMOVED***self.auth(auth)

***REMOVED******REMOVED***def authorize_url(self, client_id, redirect_uri, scope, state=None):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Get the authorization URL for your application, given the application's
***REMOVED******REMOVED******REMOVED******REMOVED***client_id, redirect_uri, scope, and optional state data."""
***REMOVED******REMOVED******REMOVED******REMOVED***params = [
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***('client_id', client_id),
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***('redirect_uri', redirect_uri),
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***('scope', scope)
***REMOVED******REMOVED******REMOVED******REMOVED***]
***REMOVED******REMOVED******REMOVED******REMOVED***if state:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***params.append(('state', state))
***REMOVED******REMOVED******REMOVED******REMOVED***return "%s?%s" % (CreateSend.oauth_uri, urlencode(params))

***REMOVED******REMOVED***def exchange_token(self, client_id, client_secret, redirect_uri, code):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Exchange a provided OAuth code for an OAuth access token, 'expires in'
***REMOVED******REMOVED******REMOVED******REMOVED***value and refresh token."""
***REMOVED******REMOVED******REMOVED******REMOVED***params = [
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***('grant_type', 'authorization_code'),
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***('client_id', client_id),
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***('client_secret', client_secret),
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***('redirect_uri', redirect_uri),
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***('code', code),
***REMOVED******REMOVED******REMOVED******REMOVED***]
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._post('', urlencode(params),
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***CreateSend.oauth_token_uri, "application/x-www-form-urlencoded")
***REMOVED******REMOVED******REMOVED******REMOVED***access_token, expires_in, refresh_token = None, None, None
***REMOVED******REMOVED******REMOVED******REMOVED***r = json_to_py(response)
***REMOVED******REMOVED******REMOVED******REMOVED***if hasattr(r, 'error') and hasattr(r, 'error_description'):
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***err = "Error exchanging code for access token: "
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***err += "%s - %s" % (r.error, r.error_description)
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***raise Exception(err)
***REMOVED******REMOVED******REMOVED******REMOVED***access_token, expires_in, refresh_token = r.access_token, r.expires_in, r.refresh_token
***REMOVED******REMOVED******REMOVED******REMOVED***return [access_token, expires_in, refresh_token]

***REMOVED******REMOVED***def auth(self, auth):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Authenticate with the Campaign Monitor API using either OAuth or
***REMOVED******REMOVED******REMOVED******REMOVED***an API key.

***REMOVED******REMOVED******REMOVED******REMOVED***:param auth: A dictionary representing the authentication details to use.
***REMOVED******REMOVED******REMOVED******REMOVED***This dictionary must take either of the following forms:

***REMOVED******REMOVED******REMOVED******REMOVED***{'access_token': 'your access token', 'refresh_token': 'your refresh token'}

***REMOVED******REMOVED******REMOVED******REMOVED***{'api_key': 'your api key'}
***REMOVED******REMOVED******REMOVED******REMOVED***"""
***REMOVED******REMOVED******REMOVED******REMOVED***self.auth_details = auth

***REMOVED******REMOVED***def refresh_token(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Refresh an OAuth token given a refresh token."""
***REMOVED******REMOVED******REMOVED******REMOVED***if (not self.auth_details or
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***not 'refresh_token' in self.auth_details or
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***not self.auth_details['refresh_token']):
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***raise Exception(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"auth_details['refresh_token'] does not contain a refresh token.")

***REMOVED******REMOVED******REMOVED******REMOVED***refresh_token = self.auth_details['refresh_token']
***REMOVED******REMOVED******REMOVED******REMOVED***params = [
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***('grant_type', 'refresh_token'),
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***('refresh_token', refresh_token)
***REMOVED******REMOVED******REMOVED******REMOVED***]
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._post('', urlencode(params),
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***CreateSend.oauth_token_uri, "application/x-www-form-urlencoded")
***REMOVED******REMOVED******REMOVED******REMOVED***new_access_token, new_expires_in, new_refresh_token = None, None, None
***REMOVED******REMOVED******REMOVED******REMOVED***r = json_to_py(response)
***REMOVED******REMOVED******REMOVED******REMOVED***new_access_token, new_expires_in, new_refresh_token = r.access_token, r.expires_in, r.refresh_token
***REMOVED******REMOVED******REMOVED******REMOVED***self.auth({
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***'access_token': new_access_token,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***'refresh_token': new_refresh_token})
***REMOVED******REMOVED******REMOVED******REMOVED***return [new_access_token, new_expires_in, new_refresh_token]

***REMOVED******REMOVED***def stub_request(self, expected_url, filename, status=None, body=None):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Stub a web request for testing."""
***REMOVED******REMOVED******REMOVED******REMOVED***self.fake_web = True
***REMOVED******REMOVED******REMOVED******REMOVED***self.faker = get_faker(expected_url, filename, status, body)

***REMOVED******REMOVED***def make_request(self, method, path, params={}, body="", username=None,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** password=None, base_uri=None, content_type=None):
***REMOVED******REMOVED******REMOVED******REMOVED***headers = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***'User-Agent': CreateSend.user_agent,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***'Content-Type': 'application/json; charset=utf-8',
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***'Accept-Encoding': 'gzip, deflate'}
***REMOVED******REMOVED******REMOVED******REMOVED***if content_type:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***headers['Content-Type'] = content_type
***REMOVED******REMOVED******REMOVED******REMOVED***parsed_base_uri = urlparse(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***CreateSend.base_uri if not base_uri else base_uri)
***REMOVED******REMOVED******REMOVED******REMOVED***"""username and password should only be set when it is intended that
***REMOVED******REMOVED***the default basic authentication mechanism using the API key be
***REMOVED******REMOVED***overridden (e.g. when using the apikey route with username and password)."""
***REMOVED******REMOVED******REMOVED******REMOVED***if username and password:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***headers['Authorization'] = "Basic %s" % base64.b64encode(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***("%s:%s" % (username, password)).encode()).decode()
***REMOVED******REMOVED******REMOVED******REMOVED***elif self.auth_details:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***if 'api_key' in self.auth_details and self.auth_details['api_key']:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***headers['Authorization'] = "Basic %s" % base64.b64encode(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***("%s:x" % self.auth_details['api_key']).encode()).decode()
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***elif 'access_token' in self.auth_details and self.auth_details['access_token']:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***headers['Authorization'] = "Bearer %s" % self.auth_details[
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***'access_token']
***REMOVED******REMOVED******REMOVED******REMOVED***self.headers = headers

***REMOVED******REMOVED******REMOVED******REMOVED***"""If in fake web mode (i.e. self.stub_request has been called),
***REMOVED******REMOVED***self.faker should be set, and this request should be treated as a fake."""
***REMOVED******REMOVED******REMOVED******REMOVED***if self.fake_web:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***# Check that the actual url which would be requested matches
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***# self.faker.url.
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***actual_url = "https://%s%s" % (parsed_base_uri.netloc,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.build_url(parsed_base_uri, path, params))
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.faker.actual_url = actual_url

***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***def same_urls(url_a, url_b):
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***a = urlparse(url_a)
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***b = urlparse(url_b)
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***return (a.scheme == b.scheme and
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***a.netloc == b.netloc and
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***a.path == b.path and
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***a.params == b.params and
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***parse_qs(a.query) == parse_qs(b.query) and
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***a.fragment == b.fragment
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***)
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***if not same_urls(self.faker.url, actual_url):
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***raise Exception("Faker's expected URL (%s) doesn't match actual URL (%s)" % (
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.faker.url, actual_url))

***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.faker.actual_body = body

***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***def same_bodies(body_a, body_b):
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***return json.loads(body_a) == json.loads(body_b)
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***if self.faker.body is not None:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***if not same_bodies(self.faker.body, body):
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***raise Exception("Faker's expected body (%s) doesn't match actual body (%s)" % (
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.faker.body, body))

***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***data = self.faker.open() if self.faker else ''
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***status = self.faker.status if (
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.faker and self.faker.status) else 200
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***return self.handle_response(status, data)

***REMOVED******REMOVED******REMOVED******REMOVED***c = VerifiedHTTPSConnection(parsed_base_uri.netloc)
***REMOVED******REMOVED******REMOVED******REMOVED***c.request(method, self.build_url(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***parsed_base_uri, path, params), body, headers)
***REMOVED******REMOVED******REMOVED******REMOVED***response = c.getresponse()
***REMOVED******REMOVED******REMOVED******REMOVED***if response.getheader('content-encoding', '') == 'gzip':
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***data = gzip.GzipFile(fileobj=BytesIO(response.read())).read()
***REMOVED******REMOVED******REMOVED******REMOVED***else:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***data = response.read()
***REMOVED******REMOVED******REMOVED******REMOVED***c.close()
***REMOVED******REMOVED******REMOVED******REMOVED***return self.handle_response(response.status, data)

***REMOVED******REMOVED***def build_url(self, parsed_base_uri, path, params):
***REMOVED******REMOVED******REMOVED******REMOVED***url = parsed_base_uri.path + path
***REMOVED******REMOVED******REMOVED******REMOVED***if params and len(params) > 0:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***url = (url + "?%s" % urlencode(params))
***REMOVED******REMOVED******REMOVED******REMOVED***return url

***REMOVED******REMOVED***def handle_response(self, status, data):
***REMOVED******REMOVED******REMOVED******REMOVED***if status == 400:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***raise BadRequest(json_to_py(data))
***REMOVED******REMOVED******REMOVED******REMOVED***elif status == 401:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***json_data = json_to_py(data)
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***if json_data.Code == 121:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***raise ExpiredOAuthToken(json_data)
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***raise Unauthorized(json_data)
***REMOVED******REMOVED******REMOVED******REMOVED***elif status == 404:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***raise NotFound()
***REMOVED******REMOVED******REMOVED******REMOVED***elif status in range(400, 500):
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***raise ClientError()
***REMOVED******REMOVED******REMOVED******REMOVED***elif status in range(500, 600):
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***raise ServerError()
***REMOVED******REMOVED******REMOVED******REMOVED***return data

***REMOVED******REMOVED***def _get(self, path, params={}, username=None, password=None):
***REMOVED******REMOVED******REMOVED******REMOVED***return self.make_request(path=path, method="GET", params=params, username=username, password=password)

***REMOVED******REMOVED***def _post(self, path, body="", base_uri=None, content_type=None):
***REMOVED******REMOVED******REMOVED******REMOVED***return self.make_request(path=path, method="POST", body=body,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** base_uri=base_uri, content_type=content_type)

***REMOVED******REMOVED***def _put(self, path, body="", params={}):
***REMOVED******REMOVED******REMOVED******REMOVED***return self.make_request(path=path, method="PUT", params=params, body=body)

***REMOVED******REMOVED***def _delete(self, path, params={}):
***REMOVED******REMOVED******REMOVED******REMOVED***return self.make_request(path=path, method="DELETE", params=params)


class CreateSend(CreateSendBase):
***REMOVED******REMOVED***"""Provides high level CreateSend functionality/data you'll probably need."""
***REMOVED******REMOVED***base_uri = "https://api.createsend.com/api/v3.1"
***REMOVED******REMOVED***oauth_uri = "https://api.createsend.com/oauth"
***REMOVED******REMOVED***oauth_token_uri = "%s/token" % oauth_uri
***REMOVED******REMOVED***platform = os.getenv('SERVER_SOFTWARE') or platform.platform()
***REMOVED******REMOVED***default_user_agent = 'createsend-python-%s-%d.%d.%d-%s' % (
***REMOVED******REMOVED******REMOVED******REMOVED***__version__, sys.version_info[0], sys.version_info[1],
***REMOVED******REMOVED******REMOVED******REMOVED***sys.version_info[2], platform)
***REMOVED******REMOVED***# You can use `CreateSend.user_agent = "my user agent"` to override the
***REMOVED******REMOVED***# default user agent string (CreateSend.default_user_agent) used when
***REMOVED******REMOVED***# making API calls.
***REMOVED******REMOVED***user_agent = default_user_agent

***REMOVED******REMOVED***def __init__(self, auth=None):
***REMOVED******REMOVED******REMOVED******REMOVED***super(CreateSend, self).__init__(auth)

***REMOVED******REMOVED***def clients(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets your clients."""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get('/clients.json')
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def billing_details(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets your billing details."""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get('/billingdetails.json')
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def countries(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets valid countries."""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get('/countries.json')
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def systemdate(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets the current date in your account's timezone."""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get('/systemdate.json')
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response).SystemDate

***REMOVED******REMOVED***def timezones(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets valid timezones."""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get('/timezones.json')
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def administrators(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets administrators associated with the account"""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get('/admins.json')
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def get_primary_contact(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Retrieves the primary contact for this account"""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get('/primarycontact.json')
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def set_primary_contact(self, email):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Assigns the primary contact for this account"""
***REMOVED******REMOVED******REMOVED******REMOVED***params = {"email": email}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._put('/primarycontact.json', params=params)
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def external_session_url(self, email, chrome, url, integrator_id, client_id):
***REMOVED******REMOVED******REMOVED******REMOVED***"""
***REMOVED******REMOVED******REMOVED******REMOVED***Get a URL which initiates a new external session for the user with the
***REMOVED******REMOVED******REMOVED******REMOVED***given email.
***REMOVED******REMOVED******REMOVED******REMOVED***Full details: http://www.campaignmonitor.com/api/account/#single_sign_on

***REMOVED******REMOVED******REMOVED******REMOVED***:param email: String The representing the email address of the
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***Campaign Monitor user for whom the login session should be created.
***REMOVED******REMOVED******REMOVED******REMOVED***:param chrome: String representing which 'chrome' to display - Must be
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***either "all", "tabs", or "none".
***REMOVED******REMOVED******REMOVED******REMOVED***:param url: String representing the URL to display once logged in.
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***e.g. "/subscribers/"
***REMOVED******REMOVED******REMOVED******REMOVED***:param integrator_id: String representing the Integrator ID. You need to
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***contact Campaign Monitor support to get an Integrator ID.
***REMOVED******REMOVED******REMOVED******REMOVED***:param client_id: String representing the Client ID of the client which
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***should be active once logged in to the Campaign Monitor account.

***REMOVED******REMOVED******REMOVED******REMOVED***:returns Object containing a single field SessionUrl which represents
***REMOVED******REMOVED******REMOVED******REMOVED***the URL to initiate the external Campaign Monitor session.
***REMOVED******REMOVED******REMOVED******REMOVED***"""
***REMOVED******REMOVED******REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Email": email,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Chrome": chrome,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Url": url,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"IntegratorID": integrator_id,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"ClientID": client_id}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._put('/externalsession.json', json.dumps(body))
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)
