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
    response = self._post("/clients.json", json.dumps(body))
    return json_to_py(response)

  def details(self):
    response = self._get("/clients/%s.json" % self.client_id)
    return json_to_py(response)

  def campaigns(self):
    response = self._get(self.uri_for("campaigns"))
    return json_to_py(response)

  def drafts(self):
    response = self._get(self.uri_for("drafts"))
    return json_to_py(response)

  def lists(self):
    response = self._get(self.uri_for("lists"))
    return json_to_py(response)

  def segments(self):
    response = self._get(self.uri_for("segments"))
    return json_to_py(response)

  def suppressionlist(self, page=1, page_size=1000, order_field="email", order_direction="asc"):
    params = { 
      "page": page,
      "pagesize": page_size,
      "orderfield": order_field,
      "orderdirection": order_direction }
    response = self._get(self.uri_for("suppressionlist"), params=params)
    return json_to_py(response)

  def templates(self):
    response = self._get(self.uri_for("templates"))
    return json_to_py(response)

  def set_basics(self, company, contact_name, email, timezone, country):
    body = {
      "CompanyName": company, 
      "ContactName": contact_name,
      "EmailAddress": email,
      "TimeZone": timezone,
      "Country": country }
    response = self._put(self.uri_for('setbasics'), json.dumps(body))

  def set_access(self, username, password, access_level):
    body = {
      "Username": username, 
      "Password": password, 
      "AccessLevel": access_level }
    response = self._put(self.uri_for('setaccess'), json.dumps(body))

  def set_payg_billing(self, currency, can_purchase_credits, client_pays, markup_percentage, 
    markup_on_delivery=0, markup_per_recipient=0, markup_on_design_spam_test=0):
    body = {
      "Currency": currency,
      "CanPurchaseCredits": can_purchase_credits,
      "ClientPays": client_pays,
      "MarkupPercentage": markup_percentage,
      "MarkupOnDelivery": markup_on_delivery,
      "MarkupPerRecipient": markup_per_recipient,
      "MarkupOnDesignSpamTest": markup_on_design_spam_test }
    response = self._put(self.uri_for('setpaygbilling'), json.dumps(body))

  def set_monthly_billing(self, currency, can_purchase_credits, client_pays, markup_percentage):
    body = {
      "Currency": currency,
      "CanPurchaseCredits": can_purchase_credits,
      "ClientPays": client_pays,
      "MarkupPercentage": markup_percentage }
    response = self._put(self.uri_for('setmonthlybilling'), json.dumps(body))

  def delete(self):
    response = self._delete("/clients/%s.json" % self.client_id)

  def uri_for(self, action):
    return "/clients/%s/%s.json" % (self.client_id, action)
