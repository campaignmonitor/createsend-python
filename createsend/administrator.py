try:
  import json
except ImportError:
  import simplejson as json
from .createsend import CreateSendBase, BadRequest
from .utils import json_to_py

class Administrator(CreateSendBase):
  """Represents an administrator and associated functionality."""

  def __init__(self, auth=None, email_address=None):
    self.email_address = email_address
    super(Administrator, self).__init__(auth)

  def get(self, email_address=None):
    """Gets an administrator by  email address."""
    params = { "email": email_address or self.email_address }
    response = self._get("/admins.json", params=params)
    return json_to_py(response)

  def add(self, email_address, name):
    """Adds an administrator to an account."""
    body = {
      "EmailAddress": email_address,
      "Name": name}
    response = self._post("/admins.json", json.dumps(body))
    return json_to_py(response)

  def update(self, new_email_address, name):
    """Updates the details for an administrator."""
    params = { "email": self.email_address }
    body = {
      "EmailAddress": new_email_address,
      "Name": name}
    response = self._put("/admins.json",
      body=json.dumps(body), params=params)
    # Update self.email_address, so this object can continue to be used reliably
    self.email_address = new_email_address

  def delete(self):
    """Deletes the administrator from the account."""
    params = { "email": self.email_address }
    response = self._delete("/admins.json", params=params)
