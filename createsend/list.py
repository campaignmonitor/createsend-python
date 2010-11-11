import urllib
import json
from createsend import CreateSendBase
from utils import json_to_py

class List(CreateSendBase):
  """Represents a subscriber list and associated functionality."""

  def __init__(self, list_id=None):
    self.list_id = list_id
    super(List, self).__init__()

  def create(self, client_id, title, unsubscribe_page, confirmed_opt_in, confirmation_success_page):
    """Creates a new list for a client."""
    body = { 
      "Title": title,
      "UnsubscribePage": unsubscribe_page,
      "ConfirmedOptIn": confirmed_opt_in,
      "ConfirmationSuccessPage": confirmation_success_page }
    response = self._post("/lists/%s.json" % client_id, json.dumps(body))
    return json_to_py(response)

  def delete(self):
    """Deletes this list."""
    response = self._delete("/lists/%s.json" % self.list_id)

  def create_custom_field(self, field_name, data_type, options=[]):
    """Creates a new custom field for this list."""
    body = {
      "FieldName": field_name,
      "DataType": data_type,
      "Options": options }
    response = self._post(self.uri_for("customfields"), json.dumps(body))
    return json_to_py(response)

  def delete_custom_field(self, custom_field_key):
    """Deletes a custom field associated with this list."""
    custom_field_key = urllib.quote(custom_field_key, '')
    response = self._delete("/lists/%s/customfields/%s.json" % (self.list_id, custom_field_key))

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

  def active(self, date, page=1, page_size=1000, order_field="email", order_direction="asc"):
    """Gets the active subscribers for this list."""
    params = {
      "date": date,
      "page": page,
      "pagesize": page_size,
      "orderfield": order_field,
      "orderdirection": order_direction }
    response = self._get(self.uri_for("active"), params=params)
    return json_to_py(response)

  def bounced(self, date, page=1, page_size=1000, order_field="email", order_direction="asc"):
    """Gets the bounced subscribers for this list."""
    params = {
      "date": date,
      "page": page,
      "pagesize": page_size,
      "orderfield": order_field,
      "orderdirection": order_direction }
    response = self._get(self.uri_for("bounced"), params=params)
    return json_to_py(response)

  def unsubscribed(self, date, page=1, page_size=1000, order_field="email", order_direction="asc"):
    """Gets the unsubscribed subscribers for this list."""
    params = {
      "date": date,
      "page": page,
      "pagesize": page_size,
      "orderfield": order_field,
      "orderdirection": order_direction }
    response = self._get(self.uri_for("unsubscribed"), params=params)
    return json_to_py(response)

  def update(self, title, unsubscribe_page, confirmed_opt_in, confirmation_success_page):
    """Updates this list."""
    body = {
      "Title": title,
      "UnsubscribePage": unsubscribe_page,
      "ConfirmedOptIn": confirmed_opt_in,
      "ConfirmationSuccessPage": confirmation_success_page }
    response = self._put("/lists/%s.json" % self.list_id, json.dumps(body))

  def uri_for(self, action):
    return "/lists/%s/%s.json" % (self.list_id, action)
