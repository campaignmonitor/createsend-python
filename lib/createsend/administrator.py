import json

from createsend.createsend import CreateSendBase
from createsend.utils import json_to_py


class Administrator(CreateSendBase):
***REMOVED******REMOVED***"""Represents an administrator and associated functionality."""

***REMOVED******REMOVED***def __init__(self, auth=None, email_address=None):
***REMOVED******REMOVED******REMOVED******REMOVED***self.email_address = email_address
***REMOVED******REMOVED******REMOVED******REMOVED***super().__init__(auth)

***REMOVED******REMOVED***def get(self, email_address=None):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets an administrator by***REMOVED***email address."""
***REMOVED******REMOVED******REMOVED******REMOVED***params = {"email": email_address or self.email_address}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get("/admins.json", params=params)
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def add(self, email_address, name):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Adds an administrator to an account."""
***REMOVED******REMOVED******REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"EmailAddress": email_address,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Name": name}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._post("/admins.json", json.dumps(body))
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def update(self, new_email_address, name):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Updates the details for an administrator."""
***REMOVED******REMOVED******REMOVED******REMOVED***params = {"email": self.email_address}
***REMOVED******REMOVED******REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"EmailAddress": new_email_address,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Name": name}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._put("/admins.json",
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** body=json.dumps(body), params=params)
***REMOVED******REMOVED******REMOVED******REMOVED***# Update self.email_address, so this object can continue to be used
***REMOVED******REMOVED******REMOVED******REMOVED***# reliably
***REMOVED******REMOVED******REMOVED******REMOVED***self.email_address = new_email_address

***REMOVED******REMOVED***def delete(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Deletes the administrator from the account."""
***REMOVED******REMOVED******REMOVED******REMOVED***params = {"email": self.email_address}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._delete("/admins.json", params=params)
