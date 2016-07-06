try:
  import json
except ImportError:
  import simplejson as json
from .createsend import CreateSendBase, BadRequest
from .utils import json_to_py

class Subscriber(CreateSendBase):
  """Represents a subscriber and associated functionality."""

  def __init__(self, auth=None, list_id=None, email_address=None):
    self.list_id = list_id
    self.email_address = email_address
    super(Subscriber, self).__init__(auth)

  def get(self, list_id=None, email_address=None):
    """Gets a subscriber by list ID and email address."""
    params = { "email": email_address or self.email_address }
    response = self._get("/subscribers/%s.json" % (list_id or self.list_id), params=params)
    return json_to_py(response)

  def add(self, list_id, email_address, name, custom_fields, resubscribe, restart_subscription_based_autoresponders=False):
    """Adds a subscriber to a subscriber list."""
    body = {
      "EmailAddress": email_address,
      "Name": name,
      "CustomFields": custom_fields,
      "Resubscribe": resubscribe,
      "RestartSubscriptionBasedAutoresponders": restart_subscription_based_autoresponders }
    response = self._post("/subscribers/%s.json" % list_id, json.dumps(body))
    return json_to_py(response)

  def update(self, new_email_address, name, custom_fields, resubscribe, restart_subscription_based_autoresponders=False):
    """Updates any aspect of a subscriber, including email address, name, and
    custom field data if supplied."""
    params = { "email": self.email_address }
    body = {
      "EmailAddress": new_email_address,
      "Name": name,
      "CustomFields": custom_fields,
      "Resubscribe": resubscribe,
      "RestartSubscriptionBasedAutoresponders": restart_subscription_based_autoresponders }
    response = self._put("/subscribers/%s.json" % self.list_id,
      body=json.dumps(body), params=params)
    # Update self.email_address, so this object can continue to be used reliably
    self.email_address = new_email_address

  def import_subscribers(self, list_id, subscribers, resubscribe, queue_subscription_based_autoresponders=False, restart_subscription_based_autoresponders=False):
    """Imports subscribers into a subscriber list."""
    body = {
      "Subscribers": subscribers,
      "Resubscribe": resubscribe,
      "QueueSubscriptionBasedAutoresponders": queue_subscription_based_autoresponders,
      "RestartSubscriptionBasedAutoresponders": restart_subscription_based_autoresponders }
    try:
      response = self._post("/subscribers/%s/import.json" % list_id, json.dumps(body))
    except BadRequest as br:
      # Subscriber import will throw BadRequest if some subscribers are not imported
      # successfully. If this occurs, we want to return the ResultData property of
      # the BadRequest exception (which is of the same "form" as the response we'd
      # receive upon a completely successful import)
      if hasattr(br.data, 'ResultData'):
        return br.data.ResultData
      else:
        raise br
    return json_to_py(response)

  def unsubscribe(self):
    """Unsubscribes this subscriber from the associated list."""
    body = {
      "EmailAddress": self.email_address }
    response = self._post("/subscribers/%s/unsubscribe.json" % self.list_id, json.dumps(body))

  def history(self):
    """Gets the historical record of this subscriber's trackable actions."""
    params = { "email": self.email_address }
    response = self._get("/subscribers/%s/history.json" % self.list_id, params=params)
    return json_to_py(response)

  def delete(self):
    """Moves this subscriber to the deleted state in the associated list."""
    params = { "email": self.email_address }
    response = self._delete("/subscribers/%s.json" % self.list_id, params=params)
