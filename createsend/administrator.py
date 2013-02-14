try:
***REMOVED***import json
except ImportError:
***REMOVED***import simplejson as json
from createsend import CreateSendBase, BadRequest
from utils import json_to_py

class Administrator(CreateSendBase):
***REMOVED***"""Represents an administrator and associated functionality."""

***REMOVED***def __init__(self, auth=None, email_address=None):
***REMOVED******REMOVED***self.email_address = email_address
***REMOVED******REMOVED***super(Administrator, self).__init__(auth)

***REMOVED***def get(self, email_address):
***REMOVED******REMOVED***"""Gets an administrator by***REMOVED***email address."""
***REMOVED******REMOVED***params = { "email": email_address }
***REMOVED******REMOVED***response = self._get("/admins.json", params=params)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def add(self, email_address, name):
***REMOVED******REMOVED***"""Adds an administrator to an account."""
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"EmailAddress": email_address,
***REMOVED******REMOVED******REMOVED***"Name": name}
***REMOVED******REMOVED***response = self._post("/admins.json", json.dumps(body))
***REMOVED******REMOVED***return json_to_py(response)
***REMOVED***
***REMOVED***def update(self, new_email_address, name):
***REMOVED******REMOVED***"""Updates the details for an administrator."""
***REMOVED******REMOVED***params = { "email": self.email_address }
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"EmailAddress": new_email_address,
***REMOVED******REMOVED******REMOVED***"Name": name}
***REMOVED******REMOVED***response = self._put("/admins.json", 
***REMOVED******REMOVED******REMOVED***body=json.dumps(body), params=params)
***REMOVED******REMOVED***# Update self.email_address, so this object can continue to be used reliably
***REMOVED******REMOVED***self.email_address = new_email_address***REMOVED***

***REMOVED***def delete(self):
***REMOVED******REMOVED***"""Deletes the administrator from the account."""
***REMOVED******REMOVED***params = { "email": self.email_address }
***REMOVED******REMOVED***response = self._delete("/admins.json", params=params)
