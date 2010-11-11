import json
from createsend import CreateSendBase, BadRequest
from utils import json_to_py

class Subscriber(CreateSendBase):

***REMOVED***def __init__(self, list_id=None, email_address=None):
***REMOVED******REMOVED***self.list_id = list_id
***REMOVED******REMOVED***self.email_address = email_address
***REMOVED******REMOVED***super(Subscriber, self).__init__()

***REMOVED***def get(self, list_id, email_address):
***REMOVED******REMOVED***params = { "email": email_address }
***REMOVED******REMOVED***response = self._get("/subscribers/%s.json" % list_id, params=params)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def add(self, list_id, email_address, name, custom_fields, resubscribe):
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"EmailAddress": email_address,
***REMOVED******REMOVED******REMOVED***"Name": name,
***REMOVED******REMOVED******REMOVED***"CustomFields": custom_fields,
***REMOVED******REMOVED******REMOVED***"Resubscribe": resubscribe }
***REMOVED******REMOVED***response = self._post("/subscribers/%s.json" % list_id, json.dumps(body))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def import_subscribers(self, list_id, subscribers, resubscribe):
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"Subscribers": subscribers,
***REMOVED******REMOVED******REMOVED***"Resubscribe": resubscribe }
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
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"EmailAddress": self.email_address }
***REMOVED******REMOVED***response = self._post("/subscribers/%s/unsubscribe.json" % self.list_id, json.dumps(body))

***REMOVED***def history(self):
***REMOVED******REMOVED***params = { "email": self.email_address }
***REMOVED******REMOVED***response = self._get("/subscribers/%s/history.json" % self.list_id, params=params)
***REMOVED******REMOVED***return json_to_py(response)
