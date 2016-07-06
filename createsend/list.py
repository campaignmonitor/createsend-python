from six.moves.urllib.parse import quote
try:
  import json
except ImportError:
  import simplejson as json
from .createsend import CreateSendBase
from .utils import json_to_py

class List(CreateSendBase):
  """Represents a subscriber list and associated functionality."""

  def __init__(self, auth=None, list_id=None):
    self.list_id = list_id
    super(List, self).__init__(auth)

  def create(self, client_id, title, unsubscribe_page, confirmed_opt_in,
    confirmation_success_page, unsubscribe_setting="AllClientLists"):
    """Creates a new list for a client."""
    body = {
      "Title": title,
      "UnsubscribePage": unsubscribe_page,
      "ConfirmedOptIn": confirmed_opt_in,
      "ConfirmationSuccessPage": confirmation_success_page,
      "UnsubscribeSetting": unsubscribe_setting }
    response = self._post("/lists/%s.json" % client_id, json.dumps(body))
    self.list_id = json_to_py(response)
    return self.list_id

  def delete(self):
    """Deletes this list."""
    response = self._delete("/lists/%s.json" % self.list_id)

  def create_custom_field(self, field_name, data_type, options=[],
    visible_in_preference_center=True):
    """Creates a new custom field for this list."""
    body = {
      "FieldName": field_name,
      "DataType": data_type,
      "Options": options,
      "VisibleInPreferenceCenter": visible_in_preference_center }
    response = self._post(self.uri_for("customfields"), json.dumps(body))
    return json_to_py(response)

  def update_custom_field(self, custom_field_key, field_name,
    visible_in_preference_center):
    """Updates a custom field belonging to this list."""
    custom_field_key = quote(custom_field_key, '')
    body = {
      "FieldName": field_name,
      "VisibleInPreferenceCenter": visible_in_preference_center }
    response = self._put(self.uri_for("customfields/%s" % custom_field_key), json.dumps(body))
    return json_to_py(response)

  def delete_custom_field(self, custom_field_key):
    """Deletes a custom field associated with this list."""
    custom_field_key = quote(custom_field_key, '')
    response = self._delete("/lists/%s/customfields/%s.json" %
    (self.list_id, custom_field_key))

  def update_custom_field_options(self, custom_field_key, new_options,
    keep_existing_options):
    """Updates the options of a multi-optioned custom field on this list."""
    custom_field_key = quote(custom_field_key, '')
    body = {
      "Options": new_options,
      "KeepExistingOptions": keep_existing_options }
    response = self._put(self.uri_for("customfields/%s/options" % custom_field_key), json.dumps(body))

  def details(self):
    """Gets the details of this list."""
    response = self._get("/lists/%s.json" % self.list_id)
    return json_to_py(response)

  def custom_fields(self):
    """Gets the custom fields for this list."""
    response = self._get(self.uri_for("customfields"))
    return json_to_py(response)

  def segments(self):
    """Gets the segments for this list."""
    response = self._get(self.uri_for("segments"))
    return json_to_py(response)

  def stats(self):
    """Gets the stats for this list."""
    response = self._get(self.uri_for("stats"))
    return json_to_py(response)

  def active(self, date="", page=1, page_size=1000, order_field="email", order_direction="asc"):
    """Gets the active subscribers for this list."""
    params = {
      "date": date,
      "page": page,
      "pagesize": page_size,
      "orderfield": order_field,
      "orderdirection": order_direction }
    response = self._get(self.uri_for("active"), params=params)
    return json_to_py(response)

  def unconfirmed(self, date="", page=1, page_size=1000, order_field="email", order_direction="asc"):
    """Gets the unconfirmed subscribers for this list."""
    params = {
      "date": date,
      "page": page,
      "pagesize": page_size,
      "orderfield": order_field,
      "orderdirection": order_direction }
    response = self._get(self.uri_for("unconfirmed"), params=params)
    return json_to_py(response)

  def bounced(self, date="", page=1, page_size=1000, order_field="email", order_direction="asc"):
    """Gets the bounced subscribers for this list."""
    params = {
      "date": date,
      "page": page,
      "pagesize": page_size,
      "orderfield": order_field,
      "orderdirection": order_direction }
    response = self._get(self.uri_for("bounced"), params=params)
    return json_to_py(response)

  def unsubscribed(self, date="", page=1, page_size=1000, order_field="email", order_direction="asc"):
    """Gets the unsubscribed subscribers for this list."""
    params = {
      "date": date,
      "page": page,
      "pagesize": page_size,
      "orderfield": order_field,
      "orderdirection": order_direction }
    response = self._get(self.uri_for("unsubscribed"), params=params)
    return json_to_py(response)

  def deleted(self, date="", page=1, page_size=1000, order_field="email", order_direction="asc"):
    """Gets the deleted subscribers for this list."""
    params = {
      "date": date,
      "page": page,
      "pagesize": page_size,
      "orderfield": order_field,
      "orderdirection": order_direction }
    response = self._get(self.uri_for("deleted"), params=params)
    return json_to_py(response)

  def update(self, title, unsubscribe_page, confirmed_opt_in,
    confirmation_success_page, unsubscribe_setting="AllClientLists",
    add_unsubscribes_to_supp_list=False, scrub_active_with_supp_list=False):
    """Updates this list."""
    body = {
      "Title": title,
      "UnsubscribePage": unsubscribe_page,
      "ConfirmedOptIn": confirmed_opt_in,
      "ConfirmationSuccessPage": confirmation_success_page,
      "UnsubscribeSetting": unsubscribe_setting,
      "AddUnsubscribesToSuppList": add_unsubscribes_to_supp_list,
      "ScrubActiveWithSuppList": scrub_active_with_supp_list }
    response = self._put("/lists/%s.json" % self.list_id, json.dumps(body))

  def webhooks(self):
    """Gets the webhooks for this list."""
    response = self._get(self.uri_for("webhooks"))
    return json_to_py(response)

  def create_webhook(self, events, url, payload_format):
    """Creates a new webhook for the specified events (an array of strings). 
    Valid events are "Subscribe", "Deactivate", and "Update".
    Valid payload formats are "json", and "xml"."""
    body = {
      "Events": events,
      "Url": url,
      "PayloadFormat": payload_format }
    response = self._post(self.uri_for("webhooks"), json.dumps(body))
    return json_to_py(response)

  def test_webhook(self, webhook_id):
    """Tests that a post can be made to the endpoint specified for the webhook
    identified by webhook_id."""
    response = self._get(self.uri_for("webhooks/%s/test" % webhook_id))
    return True # An exception will be raised if any error occurs

  def delete_webhook(self, webhook_id):
    """Deletes a webhook associated with this list."""
    response = self._delete("/lists/%s/webhooks/%s.json" % (self.list_id, webhook_id))

  def activate_webhook(self, webhook_id):
    """Activates a webhook associated with this list."""
    response = self._put(self.uri_for("webhooks/%s/activate" % webhook_id), ' ')

  def deactivate_webhook(self, webhook_id):
    """De-activates a webhook associated with this list."""
    response = self._put(self.uri_for("webhooks/%s/deactivate" % webhook_id), ' ')

  def uri_for(self, action):
    return "/lists/%s/%s.json" % (self.list_id, action)
