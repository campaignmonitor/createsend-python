import sys
import platform
import base64
import gzip
import os
from six import BytesIO
from six.moves.urllib.parse import parse_qs, urlencode, urlparse
try:
  import json
except ImportError:
  import simplejson as json
from .utils import VerifiedHTTPSConnection, json_to_py, get_faker

__version_info__ = ('4', '2', '0')
__version__ = '.'.join(__version_info__)

class CreateSendError(Exception):
  """Represents a CreateSend API error and contains specific data about the error."""
  def __init__(self, data):
    self.data = data
  def __str__(self):
    # self.data should contain Code, Message and optionally ResultData
    extra = ("\nExtra result data: %s" % self.data.ResultData) if hasattr(self.data, 'ResultData') else ""
    return "The CreateSend API responded with the following error - %s: %s%s" % (self.data.Code, self.data.Message, extra)

class ClientError(Exception): pass
class ServerError(Exception): pass
class BadRequest(CreateSendError): pass
class Unauthorized(CreateSendError): pass
class NotFound(ClientError): pass
class Unavailable(Exception): pass

class ExpiredOAuthToken(Unauthorized):
  """Raised for HTTP response code of 401, specifically when an OAuth
  token has expired (Code: 121, Message: 'Expired OAuth Token')"""
  pass

class CreateSendBase(object):
  auth_details = None

  def __init__(self, auth):
    self.fake_web = False
    self.auth(auth)

  def authorize_url(self, client_id, redirect_uri, scope, state=None):
    """Get the authorization URL for your application, given the application's
    client_id, redirect_uri, scope, and optional state data."""
    params = [
      ('client_id', client_id),
      ('redirect_uri', redirect_uri),
      ('scope', scope)
    ]
    if state:
      params.append(('state', state))
    return "%s?%s" % (CreateSend.oauth_uri, urlencode(params))

  def exchange_token(self, client_id, client_secret, redirect_uri, code):
    """Exchange a provided OAuth code for an OAuth access token, 'expires in'
    value and refresh token."""
    params = [
      ('grant_type', 'authorization_code'),
      ('client_id', client_id),
      ('client_secret', client_secret),
      ('redirect_uri', redirect_uri),
      ('code', code),
    ]
    response = self._post('', urlencode(params),
      CreateSend.oauth_token_uri, "application/x-www-form-urlencoded")
    access_token, expires_in, refresh_token = None, None, None
    r = json_to_py(response)
    if hasattr(r, 'error') and hasattr(r, 'error_description'):
      err = "Error exchanging code for access token: "
      err += "%s - %s" % (r.error, r.error_description)
      raise Exception(err)
    access_token, expires_in, refresh_token = r.access_token, r.expires_in, r.refresh_token
    return [access_token, expires_in, refresh_token]

  def auth(self, auth):
    """Authenticate with the Campaign Monitor API using either OAuth or
    an API key.

    :param auth: A dictionary representing the authentication details to use.
    This dictionary must take either of the following forms:

    {'access_token': 'your access token', 'refresh_token': 'your refresh token'}

    {'api_key': 'your api key'}
    """
    self.auth_details = auth

  def refresh_token(self):
    """Refresh an OAuth token given a refresh token."""
    if (not self.auth_details or
      not 'refresh_token' in self.auth_details or
      not self.auth_details['refresh_token']):
      raise Exception("auth_details['refresh_token'] does not contain a refresh token.")

    refresh_token = self.auth_details['refresh_token']
    params = [
      ('grant_type', 'refresh_token'),
      ('refresh_token', refresh_token)
    ]
    response = self._post('', urlencode(params),
      CreateSend.oauth_token_uri, "application/x-www-form-urlencoded")
    new_access_token, new_expires_in, new_refresh_token = None, None, None
    r = json_to_py(response)
    new_access_token, new_expires_in, new_refresh_token = r.access_token, r.expires_in, r.refresh_token
    self.auth({
      'access_token': new_access_token,
      'refresh_token': new_refresh_token})
    return [new_access_token, new_expires_in, new_refresh_token]

  def stub_request(self, expected_url, filename, status=None, body=None):
    """Stub a web request for testing."""
    self.fake_web = True
    self.faker = get_faker(expected_url, filename, status, body)

  def make_request(self, method, path, params={}, body="", username=None,
    password=None, base_uri=None, content_type=None):
    headers = {
      'User-Agent': CreateSend.user_agent,
      'Content-Type': 'application/json; charset=utf-8',
      'Accept-Encoding' : 'gzip, deflate' }
    if content_type:
      headers['Content-Type'] = content_type
    parsed_base_uri = urlparse(CreateSend.base_uri if not base_uri else base_uri)
    """username and password should only be set when it is intended that
    the default basic authentication mechanism using the API key be
    overridden (e.g. when using the apikey route with username and password)."""
    if username and password:
      headers['Authorization'] = "Basic %s" % base64.b64encode(("%s:%s" % (username, password)).encode()).decode()
    elif self.auth_details:
      if 'api_key' in self.auth_details and self.auth_details['api_key']:
        headers['Authorization'] = "Basic %s" % base64.b64encode(("%s:x" % self.auth_details['api_key']).encode()).decode()
      elif 'access_token' in self.auth_details and self.auth_details['access_token']:
        headers['Authorization'] = "Bearer %s" % self.auth_details['access_token']
    self.headers = headers

    """If in fake web mode (i.e. self.stub_request has been called),
    self.faker should be set, and this request should be treated as a fake."""
    if self.fake_web:
      # Check that the actual url which would be requested matches self.faker.url.
      actual_url = "https://%s%s" % (parsed_base_uri.netloc, self.build_url(parsed_base_uri, path, params))
      self.faker.actual_url = actual_url
      def same_urls(url_a, url_b):
          a = urlparse(url_a)
          b = urlparse(url_b)
          return (a.scheme == b.scheme and
                  a.netloc == b.netloc and
                  a.path == b.path and
                  a.params == b.params and
                  parse_qs(a.query) == parse_qs(b.query) and
                  a.fragment == b.fragment
                  )
      if not same_urls(self.faker.url, actual_url):
        raise Exception("Faker's expected URL (%s) doesn't match actual URL (%s)" % (self.faker.url, actual_url))

      self.faker.actual_body = body
      def same_bodies(body_a, body_b):
          return json.loads(body_a) == json.loads(body_b)
      if self.faker.body is not None:
        if not same_bodies(self.faker.body, body):
          raise Exception("Faker's expected body (%s) doesn't match actual body (%s)" % (self.faker.body, body))

      data = self.faker.open() if self.faker else ''
      status = self.faker.status if (self.faker and self.faker.status) else 200
      return self.handle_response(status, data)

    c = VerifiedHTTPSConnection(parsed_base_uri.netloc)
    c.request(method, self.build_url(parsed_base_uri, path, params), body, headers)
    response = c.getresponse()
    if response.getheader('content-encoding', '') == 'gzip':
      data = gzip.GzipFile(fileobj=BytesIO(response.read())).read()
    else:
      data = response.read()
    c.close()
    return self.handle_response(response.status, data)

  def build_url(self, parsed_base_uri, path, params):
    url = parsed_base_uri.path + path
    if params and len(params) > 0:
      url = (url + "?%s" % urlencode(params))
    return url

  def handle_response(self, status, data):
    if status == 400:
      raise BadRequest(json_to_py(data))
    elif status == 401:
      json_data = json_to_py(data)
      if json_data.Code == 121:
        raise ExpiredOAuthToken(json_data)
      raise Unauthorized(json_data)
    elif status == 404:
      raise NotFound()
    elif status in range(400, 500):
      raise ClientError()
    elif status in range(500, 600):
      raise ServerError()
    return data

  def _get(self, path, params={}, username=None, password=None):
    return self.make_request(path=path, method="GET", params=params, username=username, password=password)

  def _post(self, path, body="", base_uri=None, content_type=None):
    return self.make_request(path=path, method="POST", body=body,
      base_uri=base_uri, content_type=content_type)

  def _put(self, path, body="", params={}):
    return self.make_request(path=path, method="PUT", params=params, body=body)

  def _delete(self, path, params={}):
    return self.make_request(path=path, method="DELETE", params=params)

class CreateSend(CreateSendBase):
  """Provides high level CreateSend functionality/data you'll probably need."""
  base_uri = "https://api.createsend.com/api/v3.1"
  oauth_uri = "https://api.createsend.com/oauth"
  oauth_token_uri = "%s/token" % oauth_uri
  platform = os.getenv('SERVER_SOFTWARE') or platform.platform()
  default_user_agent = 'createsend-python-%s-%d.%d.%d-%s' % (
    __version__, sys.version_info[0], sys.version_info[1],
    sys.version_info[2], platform)
  # You can use `CreateSend.user_agent = "my user agent"` to override the
  # default user agent string (CreateSend.default_user_agent) used when
  # making API calls.
  user_agent = default_user_agent

  def __init__(self, auth=None):
    super(CreateSend, self).__init__(auth)

  def clients(self):
    """Gets your clients."""
    response = self._get('/clients.json')
    return json_to_py(response)

  def billing_details(self):
    """Gets your billing details."""
    response = self._get('/billingdetails.json')
    return json_to_py(response)

  def countries(self):
    """Gets valid countries."""
    response = self._get('/countries.json')
    return json_to_py(response)

  def systemdate(self):
    """Gets the current date in your account's timezone."""
    response = self._get('/systemdate.json')
    return json_to_py(response).SystemDate

  def timezones(self):
    """Gets valid timezones."""
    response = self._get('/timezones.json')
    return json_to_py(response)

  def administrators(self):
  	"""Gets administrators associated with the account"""
  	response = self._get('/admins.json')
  	return json_to_py(response)

  def get_primary_contact(self):
  	"""Retrieves the primary contact for this account"""
  	response = self._get('/primarycontact.json')
  	return json_to_py(response)

  def set_primary_contact(self, email):
    """Assigns the primary contact for this account"""
    params = { "email": email }
    response = self._put('/primarycontact.json', params = params)
    return json_to_py(response)

  def external_session_url(self, email, chrome, url, integrator_id, client_id):
    """
    Get a URL which initiates a new external session for the user with the
    given email.
    Full details: http://www.campaignmonitor.com/api/account/#single_sign_on

    :param email: String The representing the email address of the
      Campaign Monitor user for whom the login session should be created.
    :param chrome: String representing which 'chrome' to display - Must be
      either "all", "tabs", or "none".
    :param url: String representing the URL to display once logged in.
      e.g. "/subscribers/"
    :param integrator_id: String representing the Integrator ID. You need to
      contact Campaign Monitor support to get an Integrator ID.
    :param client_id: String representing the Client ID of the client which
      should be active once logged in to the Campaign Monitor account.

    :returns Object containing a single field SessionUrl which represents
    the URL to initiate the external Campaign Monitor session.
    """
    body = {
      "Email": email,
      "Chrome": chrome,
      "Url": url,
      "IntegratorID": integrator_id,
      "ClientID": client_id }
    response = self._put('/externalsession.json', json.dumps(body))
    return json_to_py(response)
