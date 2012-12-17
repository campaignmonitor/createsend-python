import urllib
try:
***REMOVED***import json
except ImportError:
***REMOVED***import simplejson as json
from createsend import CreateSendBase
from utils import json_to_py

class List(CreateSendBase):
***REMOVED***"""Represents a subscriber list and associated functionality."""

***REMOVED***def __init__(self, list_id=None):
***REMOVED******REMOVED***self.list_id = list_id
***REMOVED******REMOVED***super(List, self).__init__()

***REMOVED***def create(self, client_id, title, unsubscribe_page, confirmed_opt_in,
***REMOVED******REMOVED***confirmation_success_page, unsubscribe_setting="AllClientLists"):
***REMOVED******REMOVED***"""Creates a new list for a client."""
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"Title": title,
***REMOVED******REMOVED******REMOVED***"UnsubscribePage": unsubscribe_page,
***REMOVED******REMOVED******REMOVED***"ConfirmedOptIn": confirmed_opt_in,
***REMOVED******REMOVED******REMOVED***"ConfirmationSuccessPage": confirmation_success_page,
***REMOVED******REMOVED******REMOVED***"UnsubscribeSetting": unsubscribe_setting }
***REMOVED******REMOVED***response = self._post("/lists/%s.json" % client_id, json.dumps(body))
***REMOVED******REMOVED***self.list_id = json_to_py(response)
***REMOVED******REMOVED***return self.list_id

***REMOVED***def delete(self):
***REMOVED******REMOVED***"""Deletes this list."""
***REMOVED******REMOVED***response = self._delete("/lists/%s.json" % self.list_id)

***REMOVED***def create_custom_field(self, field_name, data_type, options=[],
***REMOVED******REMOVED***visible_in_preference_center=True):
***REMOVED******REMOVED***"""Creates a new custom field for this list."""
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"FieldName": field_name,
***REMOVED******REMOVED******REMOVED***"DataType": data_type,
***REMOVED******REMOVED******REMOVED***"Options": options,
***REMOVED******REMOVED******REMOVED***"VisibleInPreferenceCenter": visible_in_preference_center }
***REMOVED******REMOVED***response = self._post(self.uri_for("customfields"), json.dumps(body))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def update_custom_field(self, custom_field_key, field_name,
***REMOVED******REMOVED***visible_in_preference_center):
***REMOVED******REMOVED***"""Updates a custom field belonging to this list."""
***REMOVED******REMOVED***custom_field_key = urllib.quote(custom_field_key, '')
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"FieldName": field_name,
***REMOVED******REMOVED******REMOVED***"VisibleInPreferenceCenter": visible_in_preference_center }
***REMOVED******REMOVED***response = self._put(self.uri_for("customfields/%s" % custom_field_key), json.dumps(body))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def delete_custom_field(self, custom_field_key):
***REMOVED******REMOVED***"""Deletes a custom field associated with this list."""
***REMOVED******REMOVED***custom_field_key = urllib.quote(custom_field_key, '')
***REMOVED******REMOVED***response = self._delete("/lists/%s/customfields/%s.json" %
***REMOVED******REMOVED***(self.list_id, custom_field_key))

***REMOVED***def update_custom_field_options(self, custom_field_key, new_options,
***REMOVED******REMOVED***keep_existing_options):
***REMOVED******REMOVED***"""Updates the options of a multi-optioned custom field on this list."""
***REMOVED******REMOVED***custom_field_key = urllib.quote(custom_field_key, '')
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"Options": new_options,
***REMOVED******REMOVED******REMOVED***"KeepExistingOptions": keep_existing_options }
***REMOVED******REMOVED***response = self._put(self.uri_for("customfields/%s/options" % custom_field_key), json.dumps(body))

***REMOVED***def details(self):
***REMOVED******REMOVED***"""Gets the details of this list."""
***REMOVED******REMOVED***response = self._get("/lists/%s.json" % self.list_id)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def custom_fields(self):
***REMOVED******REMOVED***"""Gets the custom fields for this list."""
***REMOVED******REMOVED***response = self._get(self.uri_for("customfields"))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def segments(self):
***REMOVED******REMOVED***"""Gets the segments for this list."""
***REMOVED******REMOVED***response = self._get(self.uri_for("segments"))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def stats(self):
***REMOVED******REMOVED***"""Gets the stats for this list."""
***REMOVED******REMOVED***response = self._get(self.uri_for("stats"))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def active(self, date="", page=1, page_size=1000, order_field="email", order_direction="asc"):
***REMOVED******REMOVED***"""Gets the active subscribers for this list."""
***REMOVED******REMOVED***params = {
***REMOVED******REMOVED******REMOVED***"date": date,
***REMOVED******REMOVED******REMOVED***"page": page,
***REMOVED******REMOVED******REMOVED***"pagesize": page_size,
***REMOVED******REMOVED******REMOVED***"orderfield": order_field,
***REMOVED******REMOVED******REMOVED***"orderdirection": order_direction }
***REMOVED******REMOVED***response = self._get(self.uri_for("active"), params=params)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def unconfirmed(self, date="", page=1, page_size=1000, order_field="email", order_direction="asc"):
***REMOVED******REMOVED***"""Gets the unconfirmed subscribers for this list."""
***REMOVED******REMOVED***params = {
***REMOVED******REMOVED******REMOVED***"date": date,
***REMOVED******REMOVED******REMOVED***"page": page,
***REMOVED******REMOVED******REMOVED***"pagesize": page_size,
***REMOVED******REMOVED******REMOVED***"orderfield": order_field,
***REMOVED******REMOVED******REMOVED***"orderdirection": order_direction }
***REMOVED******REMOVED***response = self._get(self.uri_for("unconfirmed"), params=params)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def bounced(self, date="", page=1, page_size=1000, order_field="email", order_direction="asc"):
***REMOVED******REMOVED***"""Gets the bounced subscribers for this list."""
***REMOVED******REMOVED***params = {
***REMOVED******REMOVED******REMOVED***"date": date,
***REMOVED******REMOVED******REMOVED***"page": page,
***REMOVED******REMOVED******REMOVED***"pagesize": page_size,
***REMOVED******REMOVED******REMOVED***"orderfield": order_field,
***REMOVED******REMOVED******REMOVED***"orderdirection": order_direction }
***REMOVED******REMOVED***response = self._get(self.uri_for("bounced"), params=params)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def unsubscribed(self, date="", page=1, page_size=1000, order_field="email", order_direction="asc"):
***REMOVED******REMOVED***"""Gets the unsubscribed subscribers for this list."""
***REMOVED******REMOVED***params = {
***REMOVED******REMOVED******REMOVED***"date": date,
***REMOVED******REMOVED******REMOVED***"page": page,
***REMOVED******REMOVED******REMOVED***"pagesize": page_size,
***REMOVED******REMOVED******REMOVED***"orderfield": order_field,
***REMOVED******REMOVED******REMOVED***"orderdirection": order_direction }
***REMOVED******REMOVED***response = self._get(self.uri_for("unsubscribed"), params=params)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def deleted(self, date="", page=1, page_size=1000, order_field="email", order_direction="asc"):
***REMOVED******REMOVED***"""Gets the deleted subscribers for this list."""
***REMOVED******REMOVED***params = {
***REMOVED******REMOVED******REMOVED***"date": date,
***REMOVED******REMOVED******REMOVED***"page": page,
***REMOVED******REMOVED******REMOVED***"pagesize": page_size,
***REMOVED******REMOVED******REMOVED***"orderfield": order_field,
***REMOVED******REMOVED******REMOVED***"orderdirection": order_direction }
***REMOVED******REMOVED***response = self._get(self.uri_for("deleted"), params=params)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def update(self, title, unsubscribe_page, confirmed_opt_in,
***REMOVED******REMOVED***confirmation_success_page, unsubscribe_setting="AllClientLists",
***REMOVED******REMOVED***add_unsubscribes_to_supp_list=False, scrub_active_with_supp_list=False):
***REMOVED******REMOVED***"""Updates this list."""
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"Title": title,
***REMOVED******REMOVED******REMOVED***"UnsubscribePage": unsubscribe_page,
***REMOVED******REMOVED******REMOVED***"ConfirmedOptIn": confirmed_opt_in,
***REMOVED******REMOVED******REMOVED***"ConfirmationSuccessPage": confirmation_success_page,
***REMOVED******REMOVED******REMOVED***"UnsubscribeSetting": unsubscribe_setting,
***REMOVED******REMOVED******REMOVED***"AddUnsubscribesToSuppList": add_unsubscribes_to_supp_list,
***REMOVED******REMOVED******REMOVED***"ScrubActiveWithSuppList": scrub_active_with_supp_list }
***REMOVED******REMOVED***response = self._put("/lists/%s.json" % self.list_id, json.dumps(body))

***REMOVED***def webhooks(self):
***REMOVED******REMOVED***"""Gets the webhooks for this list."""
***REMOVED******REMOVED***response = self._get(self.uri_for("webhooks"))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def create_webhook(self, events, url, payload_format):
***REMOVED******REMOVED***"""Creates a new webhook for the specified events (an array of strings). 
***REMOVED******REMOVED***Valid events are "Subscribe", "Deactivate", and "Update".
***REMOVED******REMOVED***Valid payload formats are "json", and "xml"."""
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"Events": events,
***REMOVED******REMOVED******REMOVED***"Url": url,
***REMOVED******REMOVED******REMOVED***"PayloadFormat": payload_format }
***REMOVED******REMOVED***response = self._post(self.uri_for("webhooks"), json.dumps(body))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def test_webhook(self, webhook_id):
***REMOVED******REMOVED***"""Tests that a post can be made to the endpoint specified for the webhook
***REMOVED******REMOVED***identified by webhook_id."""
***REMOVED******REMOVED***response = self._get(self.uri_for("webhooks/%s/test" % webhook_id))
***REMOVED******REMOVED***return True # An exception will be raised if any error occurs

***REMOVED***def delete_webhook(self, webhook_id):
***REMOVED******REMOVED***"""Deletes a webhook associated with this list."""
***REMOVED******REMOVED***response = self._delete("/lists/%s/webhooks/%s.json" % (self.list_id, webhook_id))

***REMOVED***def activate_webhook(self, webhook_id):
***REMOVED******REMOVED***"""Activates a webhook associated with this list."""
***REMOVED******REMOVED***response = self._put(self.uri_for("webhooks/%s/activate" % webhook_id), ' ')

***REMOVED***def deactivate_webhook(self, webhook_id):
***REMOVED******REMOVED***"""De-activates a webhook associated with this list."""
***REMOVED******REMOVED***response = self._put(self.uri_for("webhooks/%s/deactivate" % webhook_id), ' ')

***REMOVED***def uri_for(self, action):
***REMOVED******REMOVED***return "/lists/%s/%s.json" % (self.list_id, action)
