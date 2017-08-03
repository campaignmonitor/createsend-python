from __future__ import absolute_import

try:
***REMOVED******REMOVED***import json
except ImportError:
***REMOVED******REMOVED***import simplejson as json
from createsend.createsend import CreateSendBase
from createsend.utils import json_to_py


class Client(CreateSendBase):
***REMOVED******REMOVED***"""Represents a client and associated functionality."""

***REMOVED******REMOVED***def __init__(self, auth=None, client_id=None):
***REMOVED******REMOVED******REMOVED******REMOVED***self.client_id = client_id
***REMOVED******REMOVED******REMOVED******REMOVED***super(Client, self).__init__(auth)

***REMOVED******REMOVED***def create(self, company, timezone, country):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Creates a client."""

***REMOVED******REMOVED******REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"CompanyName": company,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"TimeZone": timezone,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Country": country}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._post("/clients.json", json.dumps(body))
***REMOVED******REMOVED******REMOVED******REMOVED***self.client_id = json_to_py(response)
***REMOVED******REMOVED******REMOVED******REMOVED***return self.client_id

***REMOVED******REMOVED***def details(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets the details of this client."""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get("/clients/%s.json" % self.client_id)
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def campaigns(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets the sent campaigns belonging to this client."""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get(self.uri_for("campaigns"))
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def scheduled(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets the currently scheduled campaigns belonging to this client."""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get(self.uri_for("scheduled"))
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def drafts(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets the draft campaigns belonging to this client."""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get(self.uri_for("drafts"))
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def lists(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets the subscriber lists belonging to this client."""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get(self.uri_for("lists"))
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def lists_for_email(self, email_address):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets the lists across a client to which a subscriber with a particular
***REMOVED******REMOVED******REMOVED******REMOVED***email address belongs."""
***REMOVED******REMOVED******REMOVED******REMOVED***params = {"email": email_address}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get(self.uri_for("listsforemail"), params=params)
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def segments(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets the segments belonging to this client."""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get(self.uri_for("segments"))
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def suppressionlist(self, page=1, page_size=1000, order_field="email", order_direction="asc"):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets this client's suppression list."""
***REMOVED******REMOVED******REMOVED******REMOVED***params = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"page": page,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"pagesize": page_size,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"orderfield": order_field,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"orderdirection": order_direction}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get(self.uri_for("suppressionlist"), params=params)
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def suppress(self, email):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Adds email addresses to a client's suppression list"""
***REMOVED******REMOVED******REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"EmailAddresses": [email] if isinstance(email, str) else email}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._post(self.uri_for("suppress"), json.dumps(body))

***REMOVED******REMOVED***def unsuppress(self, email):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Unsuppresses an email address by removing it from the the client's
***REMOVED******REMOVED******REMOVED******REMOVED***suppression list"""
***REMOVED******REMOVED******REMOVED******REMOVED***params = {"email": email}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._put(self.uri_for("unsuppress"),
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** body=" ", params=params)

***REMOVED******REMOVED***def templates(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets the templates belonging to this client."""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get(self.uri_for("templates"))
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def set_basics(self, company, timezone, country):
***REMOVED******REMOVED******REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"CompanyName": company,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"TimeZone": timezone,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Country": country}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._put(self.uri_for('setbasics'), json.dumps(body))

***REMOVED******REMOVED***def set_payg_billing(self, currency, can_purchase_credits, client_pays, markup_percentage,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** markup_on_delivery=0, markup_per_recipient=0, markup_on_design_spam_test=0):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Sets the PAYG billing settings for this client."""
***REMOVED******REMOVED******REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Currency": currency,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"CanPurchaseCredits": can_purchase_credits,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"ClientPays": client_pays,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"MarkupPercentage": markup_percentage,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"MarkupOnDelivery": markup_on_delivery,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"MarkupPerRecipient": markup_per_recipient,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"MarkupOnDesignSpamTest": markup_on_design_spam_test}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._put(self.uri_for('setpaygbilling'), json.dumps(body))

***REMOVED******REMOVED***def set_monthly_billing(self, currency, client_pays, markup_percentage, monthly_scheme=None):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Sets the monthly billing settings for this client."""
***REMOVED******REMOVED******REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Currency": currency,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"ClientPays": client_pays,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"MarkupPercentage": markup_percentage}

***REMOVED******REMOVED******REMOVED******REMOVED***if monthly_scheme is not None:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***body["MonthlyScheme"] = monthly_scheme

***REMOVED******REMOVED******REMOVED******REMOVED***response = self._put(self.uri_for(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***'setmonthlybilling'), json.dumps(body))

***REMOVED******REMOVED***def transfer_credits(self, credits, can_use_my_credits_when_they_run_out):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Transfer credits to or from this client.

***REMOVED******REMOVED******REMOVED******REMOVED***:param credits: An Integer representing the number of credits to transfer.
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***This value may be either positive if you want to allocate credits from
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***your account to the client, or negative if you want to deduct credits
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***from the client back into your account.
***REMOVED******REMOVED******REMOVED******REMOVED***:param can_use_my_credits_when_they_run_out: A Boolean value representing
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***which, if set to true, will allow the client to continue sending using
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***your credits or payment details once they run out of credits, and if
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***set to false, will prevent the client from using your credits to
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***continue sending until you allocate more credits to them.
***REMOVED******REMOVED******REMOVED******REMOVED***:returns: An object of the following form representing the result:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***AccountCredits # Integer representing credits in your account now
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***ClientCredits # Integer representing credits in this client's
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***account now
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***}
***REMOVED******REMOVED******REMOVED******REMOVED***"""
***REMOVED******REMOVED******REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Credits": credits,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"CanUseMyCreditsWhenTheyRunOut": can_use_my_credits_when_they_run_out}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._post(self.uri_for('credits'), json.dumps(body))
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def people(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""gets people associated with the client"""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get(self.uri_for('people'))
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def get_primary_contact(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""retrieves the primary contact for this client"""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get(self.uri_for('primarycontact'))
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def set_primary_contact(self, email):
***REMOVED******REMOVED******REMOVED******REMOVED***"""assigns the primary contact for this client"""
***REMOVED******REMOVED******REMOVED******REMOVED***params = {"email": email}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._put(self.uri_for('primarycontact'), params=params)
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def delete(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Deletes this client."""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._delete("/clients/%s.json" % self.client_id)

***REMOVED******REMOVED***def uri_for(self, action):
***REMOVED******REMOVED******REMOVED******REMOVED***return "/clients/%s/%s.json" % (self.client_id, action)
