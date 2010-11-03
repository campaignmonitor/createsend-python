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

  def details(self):
    response = self.get("/clients/%s.json" % self.client_id)
    return json_to_py(response)

  def campaigns(self):
    response = self.get(self.uri_for("campaigns"))
    return json_to_py(response)

  def drafts(self):
    response = self.get(self.uri_for("drafts"))
    return json_to_py(response)

  def lists(self):
    response = self.get(self.uri_for("lists"))
    return json_to_py(response)

  def segments(self):
    response = self.get(self.uri_for("segments"))
    return json_to_py(response)

  def suppressionlist(self, page=1, page_size=1000, order_field="email", order_direction="asc"):
    params = { 
      "page": page,
      "pagesize": page_size,
      "orderfield": order_field,
      "orderdirection": order_direction }
    response = self.get(self.uri_for("suppressionlist"), params=params)
    return json_to_py(response)

  def templates(self):
    pass
    # response = get 'templates'

  def uri_for(self, action):
    return "/clients/%s/%s.json" % (self.client_id, action)
