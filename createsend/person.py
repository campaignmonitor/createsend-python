try:
***REMOVED***import json
except ImportError:
***REMOVED***import simplejson as json
from createsend import CreateSendBase, BadRequest
from utils import json_to_py

class Person(CreateSendBase):
***REMOVED***"""Represents a person and associated functionality."""

***REMOVED***def __init__(self, auth=None, client_id=None, email_address=None):
***REMOVED******REMOVED***self.client_id = client_id
***REMOVED******REMOVED***self.email_address = email_address
***REMOVED******REMOVED***super(Person, self).__init__(auth)

***REMOVED***def get(self, client_id=None, email_address=None):
***REMOVED******REMOVED***"""Gets a person by client ID and email address."""
***REMOVED******REMOVED***params = { "email": email_address or self.email_address }
***REMOVED******REMOVED***response = self._get("/clients/%s/people.json" % (client_id or self.client_id), params=params)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def add(self, client_id, email_address, name, access_level, password):
***REMOVED******REMOVED***"""Adds a person to a client. Password is optional and if not supplied, an invitation will be emailed to the person"""
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"EmailAddress": email_address,
***REMOVED******REMOVED******REMOVED***"Name": name,
***REMOVED******REMOVED******REMOVED***"AccessLevel": access_level,
***REMOVED******REMOVED******REMOVED***"Password": password}
***REMOVED******REMOVED***response = self._post("/clients/%s/people.json" % client_id, json.dumps(body))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def update(self, new_email_address, name, access_level, password = None):
***REMOVED******REMOVED***"""Updates the details for a person. Password is optional and is only updated if supplied."""
***REMOVED******REMOVED***params = { "email": self.email_address }
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"EmailAddress": new_email_address,
***REMOVED******REMOVED******REMOVED***"Name": name,
***REMOVED******REMOVED******REMOVED***"AccessLevel": access_level,
***REMOVED******REMOVED******REMOVED***"Password": password}
***REMOVED******REMOVED***response = self._put("/clients/%s/people.json" % self.client_id,
***REMOVED******REMOVED******REMOVED***body=json.dumps(body), params=params)
***REMOVED******REMOVED***# Update self.email_address, so this object can continue to be used reliably
***REMOVED******REMOVED***self.email_address = new_email_address

***REMOVED***def delete(self):
***REMOVED******REMOVED***"""Deletes the person from the client."""
***REMOVED******REMOVED***params = { "email": self.email_address }
***REMOVED******REMOVED***response = self._delete("/clients/%s/people.json" % self.client_id, params=params)
