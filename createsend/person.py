try:
  import json
except ImportError:
  import simplejson as json
from createsend import CreateSendBase, BadRequest
from utils import json_to_py

class Person(CreateSendBase):
  """Represents a person and associated functionality."""

  def __init__(self, auth=None, client_id=None, email_address=None):
    self.client_id = client_id
    self.email_address = email_address
    super(Person, self).__init__(auth)

  def get(self, client_id=None, email_address=None):
    """Gets a person by client ID and email address."""
    params = { "email": email_address or self.email_address }
    response = self._get("/clients/%s/people.json" % (client_id or self.client_id), params=params)
    return json_to_py(response)

  def add(self, client_id, email_address, name, access_level, password):
    """Adds a person to a client. Password is optional and if not supplied, an invitation will be emailed to the person"""
    body = {
      "EmailAddress": email_address,
      "Name": name,
      "AccessLevel": access_level,
      "Password": password}
    response = self._post("/clients/%s/people.json" % client_id, json.dumps(body))
    return json_to_py(response)

  def update(self, new_email_address, name, access_level, password = None):
    """Updates the details for a person. Password is optional and is only updated if supplied."""
    params = { "email": self.email_address }
    body = {
      "EmailAddress": new_email_address,
      "Name": name,
      "AccessLevel": access_level,
      "Password": password}
    response = self._put("/clients/%s/people.json" % self.client_id,
      body=json.dumps(body), params=params)
    # Update self.email_address, so this object can continue to be used reliably
    self.email_address = new_email_address

  def delete(self):
    """Deletes the person from the client."""
    params = { "email": self.email_address }
    response = self._delete("/clients/%s/people.json" % self.client_id, params=params)
