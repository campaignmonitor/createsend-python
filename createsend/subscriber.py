try:
***REMOVED***import json
except ImportError:
***REMOVED***import simplejson as json
from .createsend import CreateSendBase, BadRequest
from .utils import json_to_py

class Subscriber(CreateSendBase):
***REMOVED***"""Represents a subscriber and associated functionality."""

***REMOVED***def __init__(self, auth=None, list_id=None, email_address=None):
***REMOVED******REMOVED***self.list_id = list_id
***REMOVED******REMOVED***self.email_address = email_address
***REMOVED******REMOVED***super(Subscriber, self).__init__(auth)

***REMOVED***def get(self, list_id=None, email_address=None):
***REMOVED******REMOVED***"""Gets a subscriber by list ID and email address."""
***REMOVED******REMOVED***params = { "email": email_address or self.email_address }
***REMOVED******REMOVED***response = self._get("/subscribers/%s.json" % (list_id or self.list_id), params=params)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def add(self, list_id, email_address, name, custom_fields, resubscribe, restart_subscription_based_autoresponders=False):
***REMOVED******REMOVED***"""Adds a subscriber to a subscriber list."""
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"EmailAddress": email_address,
***REMOVED******REMOVED******REMOVED***"Name": name,
***REMOVED******REMOVED******REMOVED***"CustomFields": custom_fields,
***REMOVED******REMOVED******REMOVED***"Resubscribe": resubscribe,
***REMOVED******REMOVED******REMOVED***"RestartSubscriptionBasedAutoresponders": restart_subscription_based_autoresponders }
***REMOVED******REMOVED***response = self._post("/subscribers/%s.json" % list_id, json.dumps(body))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def update(self, new_email_address, name, custom_fields, resubscribe, restart_subscription_based_autoresponders=False):
***REMOVED******REMOVED***"""Updates any aspect of a subscriber, including email address, name, and
***REMOVED******REMOVED***custom field data if supplied."""
***REMOVED******REMOVED***params = { "email": self.email_address }
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"EmailAddress": new_email_address,
***REMOVED******REMOVED******REMOVED***"Name": name,
***REMOVED******REMOVED******REMOVED***"CustomFields": custom_fields,
***REMOVED******REMOVED******REMOVED***"Resubscribe": resubscribe,
***REMOVED******REMOVED******REMOVED***"RestartSubscriptionBasedAutoresponders": restart_subscription_based_autoresponders }
***REMOVED******REMOVED***response = self._put("/subscribers/%s.json" % self.list_id,
***REMOVED******REMOVED******REMOVED***body=json.dumps(body), params=params)
***REMOVED******REMOVED***# Update self.email_address, so this object can continue to be used reliably
***REMOVED******REMOVED***self.email_address = new_email_address

***REMOVED***def import_subscribers(self, list_id, subscribers, resubscribe, queue_subscription_based_autoresponders=False, restart_subscription_based_autoresponders=False):
***REMOVED******REMOVED***"""Imports subscribers into a subscriber list."""
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"Subscribers": subscribers,
***REMOVED******REMOVED******REMOVED***"Resubscribe": resubscribe,
***REMOVED******REMOVED******REMOVED***"QueueSubscriptionBasedAutoresponders": queue_subscription_based_autoresponders,
***REMOVED******REMOVED******REMOVED***"RestartSubscriptionBasedAutoresponders": restart_subscription_based_autoresponders }
***REMOVED******REMOVED***try:
***REMOVED******REMOVED******REMOVED***response = self._post("/subscribers/%s/import.json" % list_id, json.dumps(body))
***REMOVED******REMOVED***except BadRequest as br:
***REMOVED******REMOVED******REMOVED***# Subscriber import will throw BadRequest if some subscribers are not imported
***REMOVED******REMOVED******REMOVED***# successfully. If this occurs, we want to return the ResultData property of
***REMOVED******REMOVED******REMOVED***# the BadRequest exception (which is of the same "form" as the response we'd
***REMOVED******REMOVED******REMOVED***# receive upon a completely successful import)
***REMOVED******REMOVED******REMOVED***if hasattr(br.data, 'ResultData'):
***REMOVED******REMOVED******REMOVED******REMOVED***return br.data.ResultData
***REMOVED******REMOVED******REMOVED***else:
***REMOVED******REMOVED******REMOVED******REMOVED***raise br
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def unsubscribe(self):
***REMOVED******REMOVED***"""Unsubscribes this subscriber from the associated list."""
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"EmailAddress": self.email_address }
***REMOVED******REMOVED***response = self._post("/subscribers/%s/unsubscribe.json" % self.list_id, json.dumps(body))

***REMOVED***def history(self):
***REMOVED******REMOVED***"""Gets the historical record of this subscriber's trackable actions."""
***REMOVED******REMOVED***params = { "email": self.email_address }
***REMOVED******REMOVED***response = self._get("/subscribers/%s/history.json" % self.list_id, params=params)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def delete(self):
***REMOVED******REMOVED***"""Moves this subscriber to the deleted state in the associated list."""
***REMOVED******REMOVED***params = { "email": self.email_address }
***REMOVED******REMOVED***response = self._delete("/subscribers/%s.json" % self.list_id, params=params)
