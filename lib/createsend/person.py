from __future__ import absolute_import

try:
***REMOVED******REMOVED***import json
except ImportError:
***REMOVED******REMOVED***import simplejson as json
from createsend.createsend import CreateSendBase
from createsend.utils import json_to_py


class Person(CreateSendBase):
***REMOVED******REMOVED***"""Represents a person and associated functionality."""

***REMOVED******REMOVED***def __init__(self, auth=None, client_id=None, email_address=None):
***REMOVED******REMOVED******REMOVED******REMOVED***self.client_id = client_id
***REMOVED******REMOVED******REMOVED******REMOVED***self.email_address = email_address
***REMOVED******REMOVED******REMOVED******REMOVED***super(Person, self).__init__(auth)

***REMOVED******REMOVED***def get(self, client_id=None, email_address=None):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets a person by client ID and email address."""
***REMOVED******REMOVED******REMOVED******REMOVED***params = {"email": email_address or self.email_address}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get("/clients/%s/people.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (client_id or self.client_id), params=params)
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def add(self, client_id, email_address, name, access_level, password):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Adds a person to a client. Password is optional and if not supplied, an invitation will be emailed to the person"""
***REMOVED******REMOVED******REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"EmailAddress": email_address,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Name": name,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"AccessLevel": access_level,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Password": password}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._post("/clients/%s/people.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***client_id, json.dumps(body))
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def update(self, new_email_address, name, access_level, password=None):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Updates the details for a person. Password is optional and is only updated if supplied."""
***REMOVED******REMOVED******REMOVED******REMOVED***params = {"email": self.email_address}
***REMOVED******REMOVED******REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"EmailAddress": new_email_address,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Name": name,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"AccessLevel": access_level,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Password": password}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._put("/clients/%s/people.json" % self.client_id,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** body=json.dumps(body), params=params)
***REMOVED******REMOVED******REMOVED******REMOVED***# Update self.email_address, so this object can continue to be used
***REMOVED******REMOVED******REMOVED******REMOVED***# reliably
***REMOVED******REMOVED******REMOVED******REMOVED***self.email_address = new_email_address

***REMOVED******REMOVED***def delete(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Deletes the person from the client."""
***REMOVED******REMOVED******REMOVED******REMOVED***params = {"email": self.email_address}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._delete("/clients/%s/people.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.client_id, params=params)
