import urllib
import urllib2
import httplib
import base64
import gzip
from StringIO import StringIO
from urlparse import urlparse
from utils import json_to_py, get_faker

__version_info__ = ('2', '6', '0')
__version__ = '.'.join(__version_info__)

class CreateSendError(Exception):
***REMOVED***"""Represents a CreateSend API error and contains specific data about the error."""
***REMOVED***def __init__(self, data):
***REMOVED******REMOVED***self.data = data
***REMOVED***def __str__(self):
***REMOVED******REMOVED***# self.data should contain Code, Message and optionally ResultData
***REMOVED******REMOVED***extra = ("\nExtra result data: %s" % self.data.ResultData) if hasattr(self.data, 'ResultData') else ""
***REMOVED******REMOVED***return "The CreateSend API responded with the following error - %s: %s%s" % (self.data.Code, self.data.Message, extra)

class ClientError(Exception): pass
class ServerError(Exception): pass
class BadRequest(CreateSendError): pass
class Unauthorized(CreateSendError): pass
class NotFound(ClientError): pass
class Unavailable(Exception): pass

class ExpiredOAuthToken(Unauthorized):
***REMOVED***"""Raised for HTTP response code of 401, specifically when an OAuth
***REMOVED***token has expired (Code: 121, Message: 'Expired OAuth Token')"""
***REMOVED***pass

class CreateSendBase(object):
***REMOVED***authentication = None
***REMOVED***oauth = None
***REMOVED***api_key = None

***REMOVED***def __init__(self):
***REMOVED******REMOVED***self.fake_web = False

***REMOVED***def reset_auth(self):
***REMOVED******REMOVED***"""Reset the authentication which was set for this object."""
***REMOVED******REMOVED***self.oauth = None
***REMOVED******REMOVED***self.api_key = None

***REMOVED***def authorize_url(self, client_id, client_secret, redirect_uri,
***REMOVED******REMOVED***scope, state=None):
***REMOVED******REMOVED***"""Get the authorization URL for your application, given the application's
***REMOVED******REMOVED***client_id, client_secret, redirect_uri, scope, and optional state data."""
***REMOVED******REMOVED***options = [
***REMOVED******REMOVED******REMOVED***('client_id', client_id),
***REMOVED******REMOVED******REMOVED***('client_secret', client_secret),
***REMOVED******REMOVED******REMOVED***('redirect_uri', redirect_uri),
***REMOVED******REMOVED******REMOVED***('scope', scope)
***REMOVED******REMOVED***]
***REMOVED******REMOVED***if state:
***REMOVED******REMOVED******REMOVED***options.append(('state', state))
***REMOVED******REMOVED***return "%s?%s" % (CreateSend.oauth_uri, urllib.urlencode(options))

***REMOVED***def auth(self, auth):
***REMOVED******REMOVED***"""Authenticate with the Campaign Monitor API using either OAuth or
***REMOVED******REMOVED***an API key.

***REMOVED******REMOVED***:param auth: A dictionary representing the authentication scheme to use.
***REMOVED******REMOVED***This dictionary must take either of the following forms:

***REMOVED******REMOVED***{'access_token': 'your access token', 'refresh_token': 'your refresh token'}

***REMOVED******REMOVED***{'api_key': 'your api key'}

***REMOVED******REMOVED***:returns If no auth is specified, returns the current authentication
***REMOVED******REMOVED***data as a dictionary.
***REMOVED******REMOVED***"""
***REMOVED******REMOVED***if not auth:
***REMOVED******REMOVED******REMOVED***return self.authentication
***REMOVED******REMOVED***self.reset_auth()
***REMOVED******REMOVED***self.authentication = auth
***REMOVED******REMOVED***if 'api_key' in auth:
***REMOVED******REMOVED******REMOVED***self.api_key = auth['api_key']
***REMOVED******REMOVED***elif 'access_token' in auth:
***REMOVED******REMOVED******REMOVED***access_token = auth['access_token']
***REMOVED******REMOVED******REMOVED***refresh_token = None
***REMOVED******REMOVED******REMOVED***if 'refresh_token' in auth:
***REMOVED******REMOVED******REMOVED******REMOVED***refresh_token = auth['refresh_token']
***REMOVED******REMOVED******REMOVED***self.oauth = {
***REMOVED******REMOVED******REMOVED******REMOVED***'access_token': access_token,
***REMOVED******REMOVED******REMOVED******REMOVED***'refresh_token': refresh_token }

***REMOVED***def stub_request(self, expected_url, filename, status=None, body=None):
***REMOVED******REMOVED***"""Stub a web request for testing."""
***REMOVED******REMOVED***self.fake_web = True
***REMOVED******REMOVED***self.faker = get_faker(expected_url, filename, status, body)

***REMOVED***def make_request(self, method, path, params={}, body="", username=None,
***REMOVED******REMOVED***password=None, base_uri=None, content_type=None, no_auth=None):
***REMOVED******REMOVED***headers = {
***REMOVED******REMOVED******REMOVED***'User-Agent': 'createsend-python-%s' % __version__,
***REMOVED******REMOVED******REMOVED***'Content-Type': 'application/json; charset=utf-8',
***REMOVED******REMOVED******REMOVED***'Accept-Encoding' : 'gzip, deflate' }
***REMOVED******REMOVED***if content_type:
***REMOVED******REMOVED******REMOVED***headers['Content-Type'] = content_type
***REMOVED******REMOVED***parsed_base_uri = urlparse(CreateSend.base_uri if not base_uri else base_uri)
***REMOVED******REMOVED***"""username and password should only be set when it is intended that
***REMOVED******REMOVED***the default basic authentication mechanism using the API key be 
***REMOVED******REMOVED***overridden (e.g. when using the apikey route with username and password)."""
***REMOVED******REMOVED***if username and password:
***REMOVED******REMOVED******REMOVED***headers['Authorization'] = "Basic %s" % base64.b64encode("%s:%s" % (username, password))
***REMOVED******REMOVED***elif (CreateSend.api_key or self.api_key):
***REMOVED******REMOVED******REMOVED***# Allow api_key to be set for a CreateSend instance.
***REMOVED******REMOVED******REMOVED***headers['Authorization'] = "Basic %s" % base64.b64encode("%s:x" % (CreateSend.api_key or self.api_key))
***REMOVED******REMOVED***elif (self.oauth):
***REMOVED******REMOVED******REMOVED***headers['Authorization'] = "Bearer %s" % self.oauth["access_token"]
***REMOVED******REMOVED***if no_auth:
***REMOVED******REMOVED******REMOVED***del headers['Authorization']
***REMOVED******REMOVED***self.headers = headers

***REMOVED******REMOVED***"""If in fake web mode (i.e. self.stub_request has been called), 
***REMOVED******REMOVED***self.faker should be set, and this request should be treated as a fake."""
***REMOVED******REMOVED***if self.fake_web:
***REMOVED******REMOVED******REMOVED***# Check that the actual url which would be requested matches self.faker.url. 
***REMOVED******REMOVED******REMOVED***actual_url = "https://%s%s" % (parsed_base_uri.netloc, self.build_url(parsed_base_uri, path, params))
***REMOVED******REMOVED******REMOVED***self.faker.actual_url = actual_url
***REMOVED******REMOVED******REMOVED***if self.faker.url != actual_url:
***REMOVED******REMOVED******REMOVED******REMOVED***raise Exception("Faker's expected URL (%s) doesn't match actual URL (%s)" % (self.faker.url, actual_url))

***REMOVED******REMOVED******REMOVED***self.faker.actual_body = body
***REMOVED******REMOVED******REMOVED***if self.faker.body is not None:
***REMOVED******REMOVED******REMOVED******REMOVED***if self.faker.body != body:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***raise Exception("Faker's expected body (%s) doesn't match actual body (%s)" % (self.faker.body, body))

***REMOVED******REMOVED******REMOVED***data = self.faker.open() if self.faker else ''
***REMOVED******REMOVED******REMOVED***status = self.faker.status if (self.faker and self.faker.status) else 200
***REMOVED******REMOVED******REMOVED***return self.handle_response(status, data)

***REMOVED******REMOVED***c = httplib.HTTPConnection(parsed_base_uri.netloc)
***REMOVED******REMOVED***c.request(method, self.build_url(parsed_base_uri, path, params), body, headers)
***REMOVED******REMOVED***response = c.getresponse()
***REMOVED******REMOVED***if response.getheader('content-encoding', '') == 'gzip':
***REMOVED******REMOVED******REMOVED***data = gzip.GzipFile(fileobj=StringIO(response.read())).read()
***REMOVED******REMOVED***else:
***REMOVED******REMOVED******REMOVED***data = response.read()
***REMOVED******REMOVED***c.close()
***REMOVED******REMOVED***return self.handle_response(response.status, data)

***REMOVED***def build_url(self, parsed_base_uri, path, params):
***REMOVED******REMOVED***url = parsed_base_uri.path + path
***REMOVED******REMOVED***if params and len(params) > 0:
***REMOVED******REMOVED******REMOVED***url = (url + "?%s" % urllib.urlencode(params))
***REMOVED******REMOVED***return url

***REMOVED***def handle_response(self, status, data):
***REMOVED******REMOVED***if status == 400:
***REMOVED******REMOVED******REMOVED***raise BadRequest(json_to_py(data))
***REMOVED******REMOVED***elif status == 401:
***REMOVED******REMOVED******REMOVED***json_data = json_to_py(data)
***REMOVED******REMOVED******REMOVED***if json_data.Code == 121:
***REMOVED******REMOVED******REMOVED******REMOVED***raise ExpiredOAuthToken(json_data)
***REMOVED******REMOVED******REMOVED***raise Unauthorized(json_data)
***REMOVED******REMOVED***elif status == 404:
***REMOVED******REMOVED******REMOVED***raise NotFound()
***REMOVED******REMOVED***elif status in range(400, 500):
***REMOVED******REMOVED******REMOVED***raise ClientError()
***REMOVED******REMOVED***elif status in range(500, 600):
***REMOVED******REMOVED******REMOVED***raise ServerError()
***REMOVED******REMOVED***return data

***REMOVED***def _get(self, path, params={}, username=None, password=None):
***REMOVED******REMOVED***return self.make_request(path=path, method="GET", params=params, username=username, password=password)

***REMOVED***def _post(self, path, body="", base_uri=None, content_type=None, no_auth=None):
***REMOVED******REMOVED***return self.make_request(path=path, method="POST", body=body, 
***REMOVED******REMOVED******REMOVED***base_uri=base_uri, content_type=content_type)

***REMOVED***def _put(self, path, body="", params={}):
***REMOVED******REMOVED***return self.make_request(path=path, method="PUT", params=params, body=body)

***REMOVED***def _delete(self, path, params={}):
***REMOVED******REMOVED***return self.make_request(path=path, method="DELETE", params=params)

***REMOVED***def refresh_token(self, refresh_token=None):
***REMOVED******REMOVED***"""Refresh an OAuth token given a refresh token."""
***REMOVED******REMOVED***if (not refresh_token and 'refresh_token' in self.authentication):
***REMOVED******REMOVED******REMOVED***refresh_token = self.authentication['refresh_token']
***REMOVED******REMOVED***response = self._post(
***REMOVED******REMOVED******REMOVED***'', "grant_type=refresh_token&refresh_token=%s" % refresh_token,
***REMOVED******REMOVED******REMOVED***CreateSend.oauth_token_uri, "application/x-www-form-urlencoded", True)
***REMOVED******REMOVED***new_access_token, new_refresh_token = None, None
***REMOVED******REMOVED***r = json_to_py(response)
***REMOVED******REMOVED***new_access_token, new_refresh_token = r.access_token, r.refresh_token
***REMOVED******REMOVED***self.auth({
***REMOVED******REMOVED******REMOVED***'access_token': new_access_token,
***REMOVED******REMOVED******REMOVED***'refresh_token': new_refresh_token})
***REMOVED******REMOVED***return [new_access_token, new_refresh_token]

class CreateSend(CreateSendBase):
***REMOVED***"""Provides high level CreateSend functionality/data you'll probably need."""
***REMOVED***base_uri = "https://api.createsend.com/api/v3"
***REMOVED***oauth_uri = "https://api.createsend.com/oauth"
***REMOVED***oauth_token_uri = "%s/token" % oauth_uri

***REMOVED***def apikey(self, site_url, username, password):
***REMOVED******REMOVED***"""Gets your CreateSend API key, given your site url, username and password."""
***REMOVED******REMOVED***# The only case in which username and password are passed to self.get
***REMOVED******REMOVED***params = { "SiteUrl": site_url }
***REMOVED******REMOVED***response = self._get("/apikey.json", params, username, password)
***REMOVED******REMOVED***return json_to_py(response).ApiKey

***REMOVED***def clients(self):
***REMOVED******REMOVED***"""Gets your clients."""
***REMOVED******REMOVED***response = self._get('/clients.json')
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def billing_details(self):
***REMOVED******REMOVED***"""Gets your billing details."""
***REMOVED******REMOVED***response = self._get('/billingdetails.json')
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def countries(self):
***REMOVED******REMOVED***"""Gets valid countries."""
***REMOVED******REMOVED***response = self._get('/countries.json')
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def systemdate(self):
***REMOVED******REMOVED***"""Gets the current date in your account's timezone."""
***REMOVED******REMOVED***response = self._get('/systemdate.json')
***REMOVED******REMOVED***return json_to_py(response).SystemDate

***REMOVED***def timezones(self):
***REMOVED******REMOVED***"""Gets valid timezones."""
***REMOVED******REMOVED***response = self._get('/timezones.json')
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def administrators(self):
***REMOVED***	"""gets administrators associated with the account"""
***REMOVED***	response = self._get('/admins.json')
***REMOVED***	return json_to_py(response)
***REMOVED***
***REMOVED***def get_primary_contact(self):
***REMOVED***	"""retrieves the primary contact for this account"""
***REMOVED***	response = self._get('/primarycontact.json')
***REMOVED***	return json_to_py(response)

***REMOVED***def set_primary_contact(self, email):
***REMOVED******REMOVED***"""assigns the primary contact for this account"""
***REMOVED******REMOVED***params = { "email": email }
***REMOVED******REMOVED***response = self._put('/primarycontact.json', params = params)
***REMOVED******REMOVED***return json_to_py(response)
