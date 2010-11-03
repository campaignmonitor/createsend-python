import urllib
import urllib2
import httplib
import base64
from urlparse import urlparse
from utils import json_to_py, get_faker

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

    headers = { 'User-Agent': 'createsend-python', 'Content-Type': 'application/json' }
    """username and password should only be set when it is intended that
    the default basic authentication mechanism using the API key be 
    overridden (e.g. when using the apikey route with username and password)."""
    if username and password:
      headers['Authorization'] = "Basic %s" % base64.b64encode("%s:%s" % (username, password))
    else:
      headers['Authorization'] = "Basic %s" % base64.b64encode("%s:x" % CreateSend.api_key)
    parsed_url = urlparse(CreateSend.base_uri)
    c = httplib.HTTPConnection(parsed_url.netloc)
    c.request(method, parsed_url.path + path, body, headers)
    response = c.getresponse()
    data = response.read()
    c.close()
    return self.handle_response(response.status, data)

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

  def get(self, path, params={}, username=None, password=None):
    return self.make_request(path=path, method="GET", params=params, username=username, password=password)

  def post(self, path, body=""):
    return self.make_request(path=path, method="POST", params={}, body=body)

  def put(self, path):
    # TODO: Implement
    return ""

  def delete(self, path):
    # TODO: Implement
    return ""

class CreateSend(CreateSendBase):
  base_uri = "http://api.createsend.com/api/v3"
  api_key = ""

  def apikey(self, site_url, username, password):
    site_url = urllib.quote(site_url, '')
    # The only case in which username and password are passed to self.get
    response = self.get("/apikey.json?SiteUrl=%s" % site_url, username, password)
    return json_to_py(response).ApiKey

  def clients(self):
    response = self.get('/clients.json')
    return json_to_py(response)
    
  def countries(self):
    response = self.get('/countries.json')
    return json_to_py(response)

  def systemdate(self):
    response = self.get('/systemdate.json')
    return json_to_py(response).SystemDate

  def timezones(self):
    response = self.get('/timezones.json')
    return json_to_py(response)
