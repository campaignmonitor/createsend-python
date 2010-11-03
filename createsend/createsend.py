import urllib
import urllib2
import base64
default_opener = urllib2.urlopen
from utils import json_to_py

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
  def __init__(self, opener=default_opener, fake_web=False):
    self.opener = opener
    self.fake_web = fake_web

  def make_request(self, path):
    if not self.fake_web:
      r = urllib2.Request("%s%s" % (CreateSend.base_uri, path))
      r.add_header('Authorization', "Basic %s" % base64.b64encode("%s:x" % CreateSend.api_key))
    # If we're in fake_web mode, assume that self.opener has been set correctly
    # (using test.helper.get_fake_opener) and expect path to be the filename
    # to the json fixture file
    return self.opener(path if self.fake_web else r).read()

  def get(self, path):
    return self.make_request(path)

class CreateSend(CreateSendBase):
  base_uri = "http://api.createsend.com/api/v3"
  api_key = ""

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
