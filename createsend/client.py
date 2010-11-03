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
