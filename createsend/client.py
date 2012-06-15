try:
***REMOVED***import json
except ImportError:
***REMOVED***import simplejson as json
from createsend import CreateSendBase
from utils import json_to_py
import warnings

class Client(CreateSendBase):
***REMOVED***"""Represents a client and associated functionality."""

***REMOVED***def __init__(self, client_id=None):
***REMOVED******REMOVED***self.client_id = client_id
***REMOVED******REMOVED***super(Client, self).__init__()

***REMOVED***def create(self, company, contact_name, email, timezone, country):
***REMOVED******REMOVED***"""Creates a client."""
***REMOVED******REMOVED***if not (contact_name is None or contact_name == ""):
***REMOVED******REMOVED***	warnings.warn("[DEPRECATION] create used in this way has been deprecated. Instead, set contact_name on persons in this client using person.add or person.update")
	if not (email is None or email == ""):
		warnings.warn("[DEPRECATION] create used in this way has been deprecated. Instead, set email on persons in this client using person.add or person.update")
***REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED***body = { 
***REMOVED******REMOVED******REMOVED***"CompanyName": company, 
***REMOVED******REMOVED******REMOVED***"ContactName": contact_name,
***REMOVED******REMOVED******REMOVED***"EmailAddress": email,
***REMOVED******REMOVED******REMOVED***"TimeZone": timezone,
***REMOVED******REMOVED******REMOVED***"Country": country }
***REMOVED******REMOVED***response = self._post("/clients.json", json.dumps(body))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def details(self):
***REMOVED******REMOVED***"""Gets the details of this client."""
***REMOVED******REMOVED***response = self._get("/clients/%s.json" % self.client_id)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def campaigns(self):
***REMOVED******REMOVED***"""Gets the sent campaigns belonging to this client."""
***REMOVED******REMOVED***response = self._get(self.uri_for("campaigns"))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def scheduled(self):
***REMOVED******REMOVED***"""Gets the currently scheduled campaigns belonging to this client."""
***REMOVED******REMOVED***response = self._get(self.uri_for("scheduled"))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def drafts(self):
***REMOVED******REMOVED***"""Gets the draft campaigns belonging to this client."""
***REMOVED******REMOVED***response = self._get(self.uri_for("drafts"))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def lists(self):
***REMOVED******REMOVED***"""Gets the subscriber lists belonging to this client."""
***REMOVED******REMOVED***response = self._get(self.uri_for("lists"))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def segments(self):
***REMOVED******REMOVED***"""Gets the segments belonging to this client."""
***REMOVED******REMOVED***response = self._get(self.uri_for("segments"))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def suppressionlist(self, page=1, page_size=1000, order_field="email", order_direction="asc"):
***REMOVED******REMOVED***"""Gets this client's suppression list."""
***REMOVED******REMOVED***params = { 
***REMOVED******REMOVED******REMOVED***"page": page,
***REMOVED******REMOVED******REMOVED***"pagesize": page_size,
***REMOVED******REMOVED******REMOVED***"orderfield": order_field,
***REMOVED******REMOVED******REMOVED***"orderdirection": order_direction }
***REMOVED******REMOVED***response = self._get(self.uri_for("suppressionlist"), params=params)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def templates(self):
***REMOVED******REMOVED***"""Gets the templates belonging to this client."""
***REMOVED******REMOVED***response = self._get(self.uri_for("templates"))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def set_basics(self, company, contact_name, email, timezone, country):
***REMOVED******REMOVED***"""Sets the basic details for this client."""
***REMOVED******REMOVED***if not (contact_name is None or contact_name == ""):
***REMOVED******REMOVED***	warnings.warn("[DEPRECATION] set_basics used in this way has been deprecated. Instead, set contact_name on persons in this client using person.add or person.update")
***REMOVED*** 	if not (email is None or email == ""):
***REMOVED*** 		warnings.warn("[DEPRECATION] set_basics used in this way has been deprecated. Instead, set email on persons in this client using person.add or person.update")
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"CompanyName": company, 
***REMOVED******REMOVED******REMOVED***"ContactName": contact_name,
***REMOVED******REMOVED******REMOVED***"EmailAddress": email,
***REMOVED******REMOVED******REMOVED***"TimeZone": timezone,
***REMOVED******REMOVED******REMOVED***"Country": country }
***REMOVED******REMOVED***response = self._put(self.uri_for('setbasics'), json.dumps(body))

***REMOVED***def set_access(self, username, password, access_level):
***REMOVED******REMOVED***"""Sets the access settings for this client."""
***REMOVED******REMOVED***warnings.warn("[DEPRECATION] set_access has been deprecated. Instead, set access on persons in this client using person.add or person.update")
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"Username": username, 
***REMOVED******REMOVED******REMOVED***"Password": password, 
***REMOVED******REMOVED******REMOVED***"AccessLevel": access_level }
***REMOVED******REMOVED***response = self._put(self.uri_for('setaccess'), json.dumps(body))

***REMOVED***def set_payg_billing(self, currency, can_purchase_credits, client_pays, markup_percentage, 
***REMOVED******REMOVED***markup_on_delivery=0, markup_per_recipient=0, markup_on_design_spam_test=0):
***REMOVED******REMOVED***"""Sets the PAYG billing settings for this client."""
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"Currency": currency,
***REMOVED******REMOVED******REMOVED***"CanPurchaseCredits": can_purchase_credits,
***REMOVED******REMOVED******REMOVED***"ClientPays": client_pays,
***REMOVED******REMOVED******REMOVED***"MarkupPercentage": markup_percentage,
***REMOVED******REMOVED******REMOVED***"MarkupOnDelivery": markup_on_delivery,
***REMOVED******REMOVED******REMOVED***"MarkupPerRecipient": markup_per_recipient,
***REMOVED******REMOVED******REMOVED***"MarkupOnDesignSpamTest": markup_on_design_spam_test }
***REMOVED******REMOVED***response = self._put(self.uri_for('setpaygbilling'), json.dumps(body))

***REMOVED***def set_monthly_billing(self, currency, client_pays, markup_percentage):
***REMOVED******REMOVED***"""Sets the monthly billing settings for this client."""
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"Currency": currency,
***REMOVED******REMOVED******REMOVED***"ClientPays": client_pays,
***REMOVED******REMOVED******REMOVED***"MarkupPercentage": markup_percentage }
***REMOVED******REMOVED***response = self._put(self.uri_for('setmonthlybilling'), json.dumps(body))
***REMOVED******REMOVED***
***REMOVED***def people(self):
***REMOVED***	"""gets people associated with the client"""
***REMOVED***	response = self._get(self.uri_for('people'))
***REMOVED***	return json_to_py(response)
***REMOVED***
***REMOVED***def get_primary_contact(self):
***REMOVED***	"""retrieves the primary contact for this client"""
***REMOVED***	response = self._get(self.uri_for('primarycontact'))
***REMOVED***	return json_to_py(response)
***REMOVED***
***REMOVED***def set_primary_contact(self, email):
***REMOVED***	"""assigns the primary contact for this client"""
	params = { "email": email }
	response = self._put(self.uri_for('primarycontact'), params = params)
	return json_to_py(response)***REMOVED******REMOVED***

***REMOVED***def delete(self):
***REMOVED******REMOVED***"""Deletes this client."""
***REMOVED******REMOVED***response = self._delete("/clients/%s.json" % self.client_id)

***REMOVED***def uri_for(self, action):
***REMOVED******REMOVED***return "/clients/%s/%s.json" % (self.client_id, action)
