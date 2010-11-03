import urllib
import urllib2
import httplib
import base64
from urlparse import urlparse
from utils import json_to_py, get_faker

class CreateSendError(Exception):
***REMOVED***def __init__(self, data):
***REMOVED******REMOVED***self.data = data
***REMOVED***def __str__(self):
***REMOVED******REMOVED***return "The CreateSend API responded with the following error - %s: %s" % (self.data.Code, self.data.Message)

class ClientError(Exception): pass
class ServerError(Exception): pass
class BadRequest(CreateSendError): pass
class Unauthorized(ClientError): pass
class NotFound(ClientError): pass
class Unavailable(Exception): pass

class CreateSendBase(object):
***REMOVED***def __init__(self):
***REMOVED******REMOVED***self.fake_web = False

***REMOVED***def stub_request(self, filename):
***REMOVED******REMOVED***self.fake_web = True
***REMOVED******REMOVED***self.faker = get_faker(filename) if filename else None

***REMOVED***def make_request(self, method, path, params={}, body="", username=None, password=None):
***REMOVED******REMOVED***"""If in fake web mode (i.e. self.stub_request has been called), 
***REMOVED******REMOVED***self.faker should be set."""
***REMOVED******REMOVED***if self.fake_web:
***REMOVED******REMOVED******REMOVED***return self.faker.open() if self.faker else ''

***REMOVED******REMOVED***headers = { 'User-Agent': 'createsend-python', 'Content-Type': 'application/json' }
***REMOVED******REMOVED***"""username and password should only be set when it is intended that
***REMOVED******REMOVED***the default basic authentication mechanism using the API key be 
***REMOVED******REMOVED***overridden (e.g. when using the apikey route with username and password)."""
***REMOVED******REMOVED***if username and password:
***REMOVED******REMOVED******REMOVED***headers['Authorization'] = "Basic %s" % base64.b64encode("%s:%s" % (username, password))
***REMOVED******REMOVED***else:
***REMOVED******REMOVED******REMOVED***headers['Authorization'] = "Basic %s" % base64.b64encode("%s:x" % CreateSend.api_key)
***REMOVED******REMOVED***parsed_base_uri = urlparse(CreateSend.base_uri)
***REMOVED******REMOVED***c = httplib.HTTPConnection(parsed_base_uri.netloc)
***REMOVED******REMOVED***c.request(method, self.build_url(parsed_base_uri, path, params), body, headers)
***REMOVED******REMOVED***response = c.getresponse()
***REMOVED******REMOVED***data = response.read()
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
***REMOVED******REMOVED******REMOVED***raise Unauthorized()
***REMOVED******REMOVED***elif status == 404:
***REMOVED******REMOVED******REMOVED***raise NotFound()
***REMOVED******REMOVED***elif status in range(400, 501):
***REMOVED******REMOVED******REMOVED***raise ClientError()
***REMOVED******REMOVED***elif status in range(500, 601):
***REMOVED******REMOVED******REMOVED***raise ServerError()
***REMOVED******REMOVED***return data

***REMOVED***def get(self, path, params={}, username=None, password=None):
***REMOVED******REMOVED***return self.make_request(path=path, method="GET", params=params, username=username, password=password)

***REMOVED***def post(self, path, body=""):
***REMOVED******REMOVED***return self.make_request(path=path, method="POST", params={}, body=body)

***REMOVED***def put(self, path):
***REMOVED******REMOVED***# TODO: Implement
***REMOVED******REMOVED***return ""

***REMOVED***def delete(self, path):
***REMOVED******REMOVED***# TODO: Implement
***REMOVED******REMOVED***return ""

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
