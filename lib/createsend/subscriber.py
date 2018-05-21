from __future__ import absolute_import

import json

from createsend.createsend import CreateSendBase, BadRequest
from createsend.utils import json_to_py, validate_consent_to_track


class Subscriber(CreateSendBase):
***REMOVED******REMOVED***"""Represents a subscriber and associated functionality."""

***REMOVED******REMOVED***def __init__(self, auth=None, list_id=None, email_address=None):
***REMOVED******REMOVED******REMOVED******REMOVED***self.list_id = list_id
***REMOVED******REMOVED******REMOVED******REMOVED***self.email_address = email_address
***REMOVED******REMOVED******REMOVED******REMOVED***super(Subscriber, self).__init__(auth)

***REMOVED******REMOVED***def get(self, list_id=None, email_address=None, include_tracking_preference=False):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets a subscriber by list ID and email address."""
***REMOVED******REMOVED******REMOVED******REMOVED***params = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"email": email_address or self.email_address,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"includetrackingpreference": include_tracking_preference,
***REMOVED******REMOVED******REMOVED******REMOVED***}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get("/subscribers/%s.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (list_id or self.list_id), params=params)
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def add(self, list_id, email_address, name, custom_fields, resubscribe, consent_to_track, restart_subscription_based_autoresponders=False):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Adds a subscriber to a subscriber list."""
***REMOVED******REMOVED******REMOVED******REMOVED***validate_consent_to_track(consent_to_track)
***REMOVED******REMOVED******REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"EmailAddress": email_address,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Name": name,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"CustomFields": custom_fields,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Resubscribe": resubscribe,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"ConsentToTrack": consent_to_track,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"RestartSubscriptionBasedAutoresponders": restart_subscription_based_autoresponders}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._post("/subscribers/%s.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***list_id, json.dumps(body))
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def update(self, new_email_address, name, custom_fields, resubscribe, consent_to_track, restart_subscription_based_autoresponders=False):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Updates any aspect of a subscriber, including email address, name, and
***REMOVED******REMOVED******REMOVED******REMOVED***custom field data if supplied."""
***REMOVED******REMOVED******REMOVED******REMOVED***validate_consent_to_track(consent_to_track)
***REMOVED******REMOVED******REMOVED******REMOVED***params = {"email": self.email_address}
***REMOVED******REMOVED******REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"EmailAddress": new_email_address,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Name": name,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"CustomFields": custom_fields,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Resubscribe": resubscribe,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"ConsentToTrack": consent_to_track,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"RestartSubscriptionBasedAutoresponders": restart_subscription_based_autoresponders}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._put("/subscribers/%s.json" % self.list_id,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** body=json.dumps(body), params=params)
***REMOVED******REMOVED******REMOVED******REMOVED***# Update self.email_address, so this object can continue to be used
***REMOVED******REMOVED******REMOVED******REMOVED***# reliably
***REMOVED******REMOVED******REMOVED******REMOVED***self.email_address = new_email_address

***REMOVED******REMOVED***def import_subscribers(self, list_id, subscribers, resubscribe, queue_subscription_based_autoresponders=False, restart_subscription_based_autoresponders=False):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Imports subscribers into a subscriber list."""
***REMOVED******REMOVED******REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Subscribers": subscribers,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Resubscribe": resubscribe,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"QueueSubscriptionBasedAutoresponders": queue_subscription_based_autoresponders,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"RestartSubscriptionBasedAutoresponders": restart_subscription_based_autoresponders}
***REMOVED******REMOVED******REMOVED******REMOVED***try:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***response = self._post("/subscribers/%s/import.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***list_id, json.dumps(body))
***REMOVED******REMOVED******REMOVED******REMOVED***except BadRequest as br:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***# Subscriber import will throw BadRequest if some subscribers are not imported
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***# successfully. If this occurs, we want to return the ResultData property of
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***# the BadRequest exception (which is of the same "form" as the response we'd
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***# receive upon a completely successful import)
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***if hasattr(br.data, 'ResultData'):
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***return br.data.ResultData
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***else:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***raise br
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def unsubscribe(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Unsubscribes this subscriber from the associated list."""
***REMOVED******REMOVED******REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"EmailAddress": self.email_address}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._post("/subscribers/%s/unsubscribe.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.list_id, json.dumps(body))

***REMOVED******REMOVED***def history(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets the historical record of this subscriber's trackable actions."""
***REMOVED******REMOVED******REMOVED******REMOVED***params = {"email": self.email_address}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get("/subscribers/%s/history.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.list_id, params=params)
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def delete(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Moves this subscriber to the deleted state in the associated list."""
***REMOVED******REMOVED******REMOVED******REMOVED***params = {"email": self.email_address}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._delete("/subscribers/%s.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.list_id, params=params)
