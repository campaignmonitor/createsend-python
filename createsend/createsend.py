import urllib
import urllib2
import base64
default_opener = urllib2.urlopen
from utils import json_to_py

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
***REMOVED***def __init__(self, opener=default_opener, fake_web=False):
***REMOVED******REMOVED***self.opener = opener
***REMOVED******REMOVED***self.fake_web = fake_web

***REMOVED***def make_request(self, path):
***REMOVED******REMOVED***if not self.fake_web:
***REMOVED******REMOVED******REMOVED***r = urllib2.Request("%s%s" % (CreateSend.base_uri, path))
***REMOVED******REMOVED******REMOVED***r.add_header('Authorization', "Basic %s" % base64.b64encode("%s:x" % CreateSend.api_key))
***REMOVED******REMOVED***# If we're in fake_web mode, assume that self.opener has been set correctly
***REMOVED******REMOVED***# (using test.helper.get_fake_opener) and expect path to be the filename
***REMOVED******REMOVED***# to the json fixture file
***REMOVED******REMOVED***return self.opener(path if self.fake_web else r).read()

***REMOVED***def get(self, path):
***REMOVED******REMOVED***return self.make_request(path)

class CreateSend(CreateSendBase):
***REMOVED***base_uri = "http://api.createsend.com/api/v3"
***REMOVED***api_key = ""

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
