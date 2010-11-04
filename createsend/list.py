import urllib
import json
from createsend import CreateSendBase
from utils import json_to_py

class List(CreateSendBase):

  def __init__(self, list_id=None):
    self.list_id = list_id
    super(List, self).__init__()

  def create(self, client_id, title, unsubscribe_page, confirmed_opt_in, confirmation_success_page):
    body = { 
      "Title": title,
      "UnsubscribePage": unsubscribe_page,
      "ConfirmedOptIn": confirmed_opt_in,
      "ConfirmationSuccessPage": confirmation_success_page }
    response = self._post("/lists/%s.json" % client_id, json.dumps(body))
    return json_to_py(response)

  def delete(self):
    response = self._delete("/lists/%s.json" % self.list_id)

  def create_custom_field(self, field_name, data_type, options=[]):
    body = {
      "FieldName": field_name,
      "DataType": data_type,
      "Options": options }
    response = self._post(self.uri_for("customfields"), json.dumps(body))
    return json_to_py(response)

  def delete_custom_field(self, custom_field_key):
    custom_field_key = urllib.quote(custom_field_key, '')
    response = self._delete("/lists/%s/customfields/%s.json" % (self.list_id, custom_field_key))

  def details(self):
    response = self._get("/lists/%s.json" % self.list_id)
    return json_to_py(response)

  def custom_fields(self):
    response = self._get(self.uri_for("customfields"))
    return json_to_py(response)

  def segments(self):
    response = self._get(self.uri_for("segments"))
    return json_to_py(response)

  def stats(self):
    response = self._get(self.uri_for("stats"))
    return json_to_py(response)

  def active(self, date, page=1, page_size=1000, order_field="email", order_direction="asc"):
    params = {
      "date": date,
      "page": page,
      "pagesize": page_size,
      "orderfield": order_field,
      "orderdirection": order_direction }
    response = self._get(self.uri_for("active"), params=params)
    return json_to_py(response)

  def bounced(self, date, page=1, page_size=1000, order_field="email", order_direction="asc"):
    params = {
      "date": date,
      "page": page,
      "pagesize": page_size,
      "orderfield": order_field,
      "orderdirection": order_direction }
    response = self._get(self.uri_for("bounced"), params=params)
    return json_to_py(response)

  def unsubscribed(self, date, page=1, page_size=1000, order_field="email", order_direction="asc"):
    params = {
      "date": date,
      "page": page,
      "pagesize": page_size,
      "orderfield": order_field,
      "orderdirection": order_direction }
    response = self._get(self.uri_for("unsubscribed"), params=params)
    return json_to_py(response)

  def update(self, title, unsubscribe_page, confirmed_opt_in, confirmation_success_page):
    body = {
      "Title": title,
      "UnsubscribePage": unsubscribe_page,
      "ConfirmedOptIn": confirmed_opt_in,
      "ConfirmationSuccessPage": confirmation_success_page }
    response = self._put("/lists/%s.json" % self.list_id, json.dumps(body))

  def uri_for(self, action):
    return "/lists/%s/%s.json" % (self.list_id, action)
