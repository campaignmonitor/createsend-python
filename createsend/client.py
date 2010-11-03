import json
from createsend import CreateSendBase
from utils import json_to_py

class Client(CreateSendBase):

***REMOVED***def __init__(self, client_id=None):
***REMOVED******REMOVED***self.client_id = client_id
***REMOVED******REMOVED***super(Client, self).__init__()

***REMOVED***def create(self, company, contact_name, email, timezone, country):
***REMOVED******REMOVED***body = { 
***REMOVED******REMOVED******REMOVED***"CompanyName": company, 
***REMOVED******REMOVED******REMOVED***"ContactName": contact_name,
***REMOVED******REMOVED******REMOVED***"EmailAddress": email,
***REMOVED******REMOVED******REMOVED***"TimeZone": timezone,
***REMOVED******REMOVED******REMOVED***"Country": country }
***REMOVED******REMOVED***response = self.post("/clients.json", json.dumps(body))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def details(self):
***REMOVED******REMOVED***response = self.get("/clients/%s.json" % self.client_id)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def campaigns(self):
***REMOVED******REMOVED***response = self.get(self.uri_for("campaigns"))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def drafts(self):
***REMOVED******REMOVED***response = self.get(self.uri_for("drafts"))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def lists(self):
***REMOVED******REMOVED***response = self.get(self.uri_for("lists"))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def segments(self):
***REMOVED******REMOVED***response = self.get(self.uri_for("segments"))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def suppressionlist(self, page=1, page_size=1000, order_field="email", order_direction="asc"):
***REMOVED******REMOVED***params = { 
***REMOVED******REMOVED******REMOVED***"page": page,
***REMOVED******REMOVED******REMOVED***"pagesize": page_size,
***REMOVED******REMOVED******REMOVED***"orderfield": order_field,
***REMOVED******REMOVED******REMOVED***"orderdirection": order_direction }
***REMOVED******REMOVED***response = self.get(self.uri_for("suppressionlist"), params=params)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def templates(self):
***REMOVED******REMOVED***pass
***REMOVED******REMOVED***# response = get 'templates'

***REMOVED***def uri_for(self, action):
***REMOVED******REMOVED***return "/clients/%s/%s.json" % (self.client_id, action)
