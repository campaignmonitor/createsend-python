try:
  import json
except ImportError:
  import simplejson as json
from createsend import CreateSendBase
from utils import json_to_py

class Client(CreateSendBase):
  """Represents a client and associated functionality."""

  def __init__(self, client_id=None):
    self.client_id = client_id
    super(Client, self).__init__()

  def create(self, company, timezone, country):
    """Creates a client."""

    body = { 
      "CompanyName": company, 
      "TimeZone": timezone,
      "Country": country }
    response = self._post("/clients.json", json.dumps(body))
    return json_to_py(response)

  def details(self):
    """Gets the details of this client."""
    response = self._get("/clients/%s.json" % self.client_id)
    return json_to_py(response)

  def campaigns(self):
    """Gets the sent campaigns belonging to this client."""
    response = self._get(self.uri_for("campaigns"))
    return json_to_py(response)

  def scheduled(self):
    """Gets the currently scheduled campaigns belonging to this client."""
    response = self._get(self.uri_for("scheduled"))
    return json_to_py(response)

  def drafts(self):
    """Gets the draft campaigns belonging to this client."""
    response = self._get(self.uri_for("drafts"))
    return json_to_py(response)

  def lists(self):
    """Gets the subscriber lists belonging to this client."""
    response = self._get(self.uri_for("lists"))
    return json_to_py(response)

  def lists_for_email(self, email_address):
    """Gets the lists across a client to which a subscriber with a particular
    email address belongs."""
    params = { "email": email_address }
    response = self._get(self.uri_for("listsforemail"), params=params)
    return json_to_py(response)

  def segments(self):
    """Gets the segments belonging to this client."""
    response = self._get(self.uri_for("segments"))
    return json_to_py(response)

  def suppressionlist(self, page=1, page_size=1000, order_field="email", order_direction="asc"):
    """Gets this client's suppression list."""
    params = { 
      "page": page,
      "pagesize": page_size,
      "orderfield": order_field,
      "orderdirection": order_direction }
    response = self._get(self.uri_for("suppressionlist"), params=params)
    return json_to_py(response)

  def templates(self):
    """Gets the templates belonging to this client."""
    response = self._get(self.uri_for("templates"))
    return json_to_py(response)

  def set_basics(self, company, timezone, country):
    body = {
      "CompanyName": company, 
      "TimeZone": timezone,
      "Country": country }
    response = self._put(self.uri_for('setbasics'), json.dumps(body))

  def set_payg_billing(self, currency, can_purchase_credits, client_pays, markup_percentage, 
    markup_on_delivery=0, markup_per_recipient=0, markup_on_design_spam_test=0):
    """Sets the PAYG billing settings for this client."""
    body = {
      "Currency": currency,
      "CanPurchaseCredits": can_purchase_credits,
      "ClientPays": client_pays,
      "MarkupPercentage": markup_percentage,
      "MarkupOnDelivery": markup_on_delivery,
      "MarkupPerRecipient": markup_per_recipient,
      "MarkupOnDesignSpamTest": markup_on_design_spam_test }
    response = self._put(self.uri_for('setpaygbilling'), json.dumps(body))

  def set_monthly_billing(self, currency, client_pays, markup_percentage, monthly_scheme = None):
    """Sets the monthly billing settings for this client."""
    body = {
      "Currency": currency,
      "ClientPays": client_pays,
      "MarkupPercentage": markup_percentage }
      
    if monthly_scheme is not None:
      body["MonthlyScheme"] = monthly_scheme
      
    response = self._put(self.uri_for('setmonthlybilling'), json.dumps(body))
    
  def people(self):
  	"""gets people associated with the client"""
  	response = self._get(self.uri_for('people'))
  	return json_to_py(response)
  
  def get_primary_contact(self):
  	"""retrieves the primary contact for this client"""
  	response = self._get(self.uri_for('primarycontact'))
  	return json_to_py(response)
  
  def set_primary_contact(self, email):
  	"""assigns the primary contact for this client"""
	params = { "email": email }
	response = self._put(self.uri_for('primarycontact'), params = params)
	return json_to_py(response)    

  def delete(self):
    """Deletes this client."""
    response = self._delete("/clients/%s.json" % self.client_id)

  def uri_for(self, action):
    return "/clients/%s/%s.json" % (self.client_id, action)
