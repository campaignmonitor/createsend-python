import json
from createsend import CreateSendBase
from utils import json_to_py

class Client(CreateSendBase):

  def __init__(self, client_id=None):
    self.client_id = client_id
    super(Client, self).__init__()

  def create(self, company, contact_name, email, timezone, country):
    body = { 
      "CompanyName": company, 
      "ContactName": contact_name,
      "EmailAddress": email,
      "TimeZone": timezone,
      "Country": country }
    response = self.post("/clients.json", json.dumps(body))
    return json_to_py(response)
