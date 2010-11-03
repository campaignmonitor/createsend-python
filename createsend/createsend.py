import urllib
import urllib2
import base64
default_opener = urllib2.urlopen
from utils import json_to_py, get_fake_opener

class CreateSendError(Exception):
  def __init__(self, data):
    self.data = data
  def __str__(self):
    return "The CreateSend API responded with the following error - %s: %s" % (data.Code, data.Message)

class ClientError(Exception): pass
class ServerError(Exception): pass
class BadRequest(CreateSendError): pass
class Unauthorized(ClientError): pass
class NotFound(ClientError): pass
class Unavailable(Exception): pass

class CreateSendBase(object):
  def __init__(self, opener=default_opener):
    self.fake_web = False
    self.opener = opener

  def stub_request(self, filename):
    self.fake_web = True
    self.opener = get_fake_opener(filename) if filename else None
    self.fake_web_filename = filename

  def make_request(self, path, username=None, password=None):
    """If in fake web mode (i.e. self.stub_request has been called), 
    self.opener should be set to return the contents of a fixture file."""
    if self.fake_web:
      return self.opener().read()

    """username and password should only be set when it is intended that
    the default basic authentication mechanism using the API key be 
    overridden (e.g. when using the apikey route with username and password)."""
    r = urllib2.Request("%s%s" % (CreateSend.base_uri, path))
    if username and password:
      r.add_header('Authorization', "Basic %s" % base64.b64encode("%s:%s" % (username, password)))
    else:
      r.add_header('Authorization', "Basic %s" % base64.b64encode("%s:x" % CreateSend.api_key))
    # TODO: Include version in user agent
    r.add_header('User-Agent', "createsend-python")
    r.add_header('Content-Type', 'application/json')
    return self.opener(r).read()

  def get(self, path, username=None, password=None):
    return self.make_request(path, username, password)

  def post(self, path):
    # TODO: Implement
    return {}

  def put(self, path):
    # TODO: Implement
    return {}

  def delete(self, path):
    # TODO: Implement
    return {}

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
