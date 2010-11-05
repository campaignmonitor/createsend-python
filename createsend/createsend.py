import urllib
import urllib2
import httplib
import base64
from urlparse import urlparse
from utils import json_to_py, get_faker

__version_info__ = ('0', '0', '1')
__version__ = '.'.join(__version_info__)

class CreateSendError(Exception):
  def __init__(self, data):
    self.data = data
  def __str__(self):
    return "The CreateSend API responded with the following error - %s: %s" % (self.data.Code, self.data.Message)

class ClientError(Exception): pass
class ServerError(Exception): pass
class BadRequest(CreateSendError): pass
class Unauthorized(ClientError): pass
class NotFound(ClientError): pass
class Unavailable(Exception): pass

class CreateSendBase(object):
  def __init__(self):
    self.fake_web = False

  def stub_request(self, filename):
    self.fake_web = True
    self.faker = get_faker(filename) if filename else None

  def make_request(self, method, path, params={}, body="", username=None, password=None):
    """If in fake web mode (i.e. self.stub_request has been called), 
    self.faker should be set."""
    if self.fake_web:
      return self.faker.open() if self.faker else ''

    headers = { 'User-Agent': 'createsend-python-%s' % __version__, 'Content-Type': 'application/json' }
    """username and password should only be set when it is intended that
    the default basic authentication mechanism using the API key be 
    overridden (e.g. when using the apikey route with username and password)."""
    if username and password:
      headers['Authorization'] = "Basic %s" % base64.b64encode("%s:%s" % (username, password))
    else:
      headers['Authorization'] = "Basic %s" % base64.b64encode("%s:x" % CreateSend.api_key)
    parsed_base_uri = urlparse(CreateSend.base_uri)
    c = httplib.HTTPConnection(parsed_base_uri.netloc)
    c.request(method, self.build_url(parsed_base_uri, path, params), body, headers)
    response = c.getresponse()
    data = response.read()
    c.close()
    return self.handle_response(response.status, data)

  def build_url(self, parsed_base_uri, path, params):
    url = parsed_base_uri.path + path
    if params and len(params) > 0:
      url = (url + "?%s" % urllib.urlencode(params))
    return url

  def handle_response(self, status, data):
    if status == 400:
      raise BadRequest(json_to_py(data))
    elif status == 401:
      raise Unauthorized()
    elif status == 404:
      raise NotFound()
    elif status in range(400, 501):
      raise ClientError()
    elif status in range(500, 601):
      raise ServerError()
    return data

  def _get(self, path, params={}, username=None, password=None):
    return self.make_request(path=path, method="GET", params=params, username=username, password=password)

  def _post(self, path, body=""):
    return self.make_request(path=path, method="POST", body=body)

  def _put(self, path, body=""):
    return self.make_request(path=path, method="PUT", body=body)

  def _delete(self, path):
    return self.make_request(path=path, method="DELETE")

class CreateSend(CreateSendBase):
  base_uri = "http://api.createsend.com/api/v3"
  api_key = ""

  def apikey(self, site_url, username, password):
    site_url = urllib.quote(site_url, '')
    # The only case in which username and password are passed to self.get
    response = self._get("/apikey.json?SiteUrl=%s" % site_url, username, password)
    return json_to_py(response).ApiKey

  def clients(self):
    response = self._get('/clients.json')
    return json_to_py(response)
    
  def countries(self):
    response = self._get('/countries.json')
    return json_to_py(response)

  def systemdate(self):
    response = self._get('/systemdate.json')
    return json_to_py(response).SystemDate

  def timezones(self):
    response = self._get('/timezones.json')
    return json_to_py(response)
