import urllib
import json
from createsend import CreateSendBase
from utils import json_to_py

class List(CreateSendBase):

***REMOVED***def __init__(self, list_id=None):
***REMOVED******REMOVED***self.list_id = list_id
***REMOVED******REMOVED***super(List, self).__init__()

***REMOVED***def create(self, client_id, title, unsubscribe_page, confirmed_opt_in, confirmation_success_page):
***REMOVED******REMOVED***body = { 
***REMOVED******REMOVED******REMOVED***"Title": title,
***REMOVED******REMOVED******REMOVED***"UnsubscribePage": unsubscribe_page,
***REMOVED******REMOVED******REMOVED***"ConfirmedOptIn": confirmed_opt_in,
***REMOVED******REMOVED******REMOVED***"ConfirmationSuccessPage": confirmation_success_page }
***REMOVED******REMOVED***response = self._post("/lists/%s.json" % client_id, json.dumps(body))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def delete(self):
***REMOVED******REMOVED***response = self._delete("/lists/%s.json" % self.list_id)

***REMOVED***def create_custom_field(self, field_name, data_type, options=[]):
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"FieldName": field_name,
***REMOVED******REMOVED******REMOVED***"DataType": data_type,
***REMOVED******REMOVED******REMOVED***"Options": options }
***REMOVED******REMOVED***response = self._post(self.uri_for("customfields"), json.dumps(body))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def delete_custom_field(self, custom_field_key):
***REMOVED******REMOVED***custom_field_key = urllib.quote(custom_field_key, '')
***REMOVED******REMOVED***response = self._delete("/lists/%s/customfields/%s.json" % (self.list_id, custom_field_key))

***REMOVED***def details(self):
***REMOVED******REMOVED***response = self._get("/lists/%s.json" % self.list_id)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def custom_fields(self):
***REMOVED******REMOVED***response = self._get(self.uri_for("customfields"))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def segments(self):
***REMOVED******REMOVED***response = self._get(self.uri_for("segments"))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def stats(self):
***REMOVED******REMOVED***response = self._get(self.uri_for("stats"))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def active(self, date, page=1, page_size=1000, order_field="email", order_direction="asc"):
***REMOVED******REMOVED***params = {
***REMOVED******REMOVED******REMOVED***"date": date,
***REMOVED******REMOVED******REMOVED***"page": page,
***REMOVED******REMOVED******REMOVED***"pagesize": page_size,
***REMOVED******REMOVED******REMOVED***"orderfield": order_field,
***REMOVED******REMOVED******REMOVED***"orderdirection": order_direction }
***REMOVED******REMOVED***response = self._get(self.uri_for("active"), params=params)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def bounced(self, date, page=1, page_size=1000, order_field="email", order_direction="asc"):
***REMOVED******REMOVED***params = {
***REMOVED******REMOVED******REMOVED***"date": date,
***REMOVED******REMOVED******REMOVED***"page": page,
***REMOVED******REMOVED******REMOVED***"pagesize": page_size,
***REMOVED******REMOVED******REMOVED***"orderfield": order_field,
***REMOVED******REMOVED******REMOVED***"orderdirection": order_direction }
***REMOVED******REMOVED***response = self._get(self.uri_for("bounced"), params=params)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def unsubscribed(self, date, page=1, page_size=1000, order_field="email", order_direction="asc"):
***REMOVED******REMOVED***params = {
***REMOVED******REMOVED******REMOVED***"date": date,
***REMOVED******REMOVED******REMOVED***"page": page,
***REMOVED******REMOVED******REMOVED***"pagesize": page_size,
***REMOVED******REMOVED******REMOVED***"orderfield": order_field,
***REMOVED******REMOVED******REMOVED***"orderdirection": order_direction }
***REMOVED******REMOVED***response = self._get(self.uri_for("unsubscribed"), params=params)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def update(self, title, unsubscribe_page, confirmed_opt_in, confirmation_success_page):
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"Title": title,
***REMOVED******REMOVED******REMOVED***"UnsubscribePage": unsubscribe_page,
***REMOVED******REMOVED******REMOVED***"ConfirmedOptIn": confirmed_opt_in,
***REMOVED******REMOVED******REMOVED***"ConfirmationSuccessPage": confirmation_success_page }
***REMOVED******REMOVED***response = self._put("/lists/%s.json" % self.list_id, json.dumps(body))

***REMOVED***def uri_for(self, action):
***REMOVED******REMOVED***return "/lists/%s/%s.json" % (self.list_id, action)
