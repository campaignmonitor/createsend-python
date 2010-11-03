import urllib
import urllib2
import base64
default_opener = urllib2.urlopen
from utils import json_to_py, get_fake_opener

class CreateSendError(Exception):
***REMOVED***def __init__(self, data):
***REMOVED******REMOVED***self.data = data
***REMOVED***def __str__(self):
***REMOVED******REMOVED***return "The CreateSend API responded with the following error - %s: %s" % (data.Code, data.Message)

class ClientError(Exception): pass
class ServerError(Exception): pass
class BadRequest(CreateSendError): pass
class Unauthorized(ClientError): pass
class NotFound(ClientError): pass
class Unavailable(Exception): pass

class CreateSendBase(object):
***REMOVED***def __init__(self, opener=default_opener):
***REMOVED******REMOVED***self.fake_web = False
***REMOVED******REMOVED***self.opener = opener

***REMOVED***def stub_request(self, filename):
***REMOVED******REMOVED***self.fake_web = True
***REMOVED******REMOVED***self.opener = get_fake_opener(filename) if filename else None
***REMOVED******REMOVED***self.fake_web_filename = filename

***REMOVED***def make_request(self, path, username=None, password=None):
***REMOVED******REMOVED***"""If in fake web mode (i.e. self.stub_request has been called), 
***REMOVED******REMOVED***self.opener should be set to return the contents of a fixture file."""
***REMOVED******REMOVED***if self.fake_web:
***REMOVED******REMOVED******REMOVED***return self.opener().read()

***REMOVED******REMOVED***"""username and password should only be set when it is intended that
***REMOVED******REMOVED***the default basic authentication mechanism using the API key be 
***REMOVED******REMOVED***overridden (e.g. when using the apikey route with username and password)."""
***REMOVED******REMOVED***r = urllib2.Request("%s%s" % (CreateSend.base_uri, path))
***REMOVED******REMOVED***if username and password:
***REMOVED******REMOVED******REMOVED***r.add_header('Authorization', "Basic %s" % base64.b64encode("%s:%s" % (username, password)))
***REMOVED******REMOVED***else:
***REMOVED******REMOVED******REMOVED***r.add_header('Authorization', "Basic %s" % base64.b64encode("%s:x" % CreateSend.api_key))
***REMOVED******REMOVED***# TODO: Include version in user agent
***REMOVED******REMOVED***r.add_header('User-Agent', "createsend-python")
***REMOVED******REMOVED***r.add_header('Content-Type', 'application/json')
***REMOVED******REMOVED***return self.opener(r).read()

***REMOVED***def get(self, path, username=None, password=None):
***REMOVED******REMOVED***return self.make_request(path, username, password)

***REMOVED***def post(self, path):
***REMOVED******REMOVED***# TODO: Implement
***REMOVED******REMOVED***return {}

***REMOVED***def put(self, path):
***REMOVED******REMOVED***# TODO: Implement
***REMOVED******REMOVED***return {}

***REMOVED***def delete(self, path):
***REMOVED******REMOVED***# TODO: Implement
***REMOVED******REMOVED***return {}

class CreateSend(CreateSendBase):
***REMOVED***base_uri = "http://api.createsend.com/api/v3"
***REMOVED***api_key = ""

***REMOVED***def apikey(self, site_url, username, password):
***REMOVED******REMOVED***site_url = urllib.quote(site_url, '')
***REMOVED******REMOVED***# The only case in which username and password are passed to self.get
***REMOVED******REMOVED***response = self.get("/apikey.json?SiteUrl=%s" % site_url, username, password)
***REMOVED******REMOVED***return json_to_py(response).ApiKey

***REMOVED***def clients(self):
***REMOVED******REMOVED***response = self.get('/clients.json')
***REMOVED******REMOVED***return json_to_py(response)
***REMOVED******REMOVED***
***REMOVED***def countries(self):
***REMOVED******REMOVED***response = self.get('/countries.json')
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def systemdate(self):
***REMOVED******REMOVED***response = self.get('/systemdate.json')
***REMOVED******REMOVED***return json_to_py(response).SystemDate

***REMOVED***def timezones(self):
***REMOVED******REMOVED***response = self.get('/timezones.json')
***REMOVED******REMOVED***return json_to_py(response)
