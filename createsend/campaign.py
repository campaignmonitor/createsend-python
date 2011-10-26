try:
***REMOVED***import json
except ImportError:
***REMOVED***import simplejson as json
from createsend import CreateSendBase
from utils import json_to_py

class Campaign(CreateSendBase):
***REMOVED***"""Represents a campaign and provides associated funtionality."""

***REMOVED***def __init__(self, campaign_id=None):
***REMOVED******REMOVED***self.campaign_id = campaign_id
***REMOVED******REMOVED***super(Campaign, self).__init__()

***REMOVED***def create(self, client_id, subject, name, from_name, from_email, reply_to, html_url,
***REMOVED******REMOVED***text_url, list_ids, segment_ids):
***REMOVED******REMOVED***"""Creates a new campaign for a client."""
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"Subject": subject,
***REMOVED******REMOVED******REMOVED***"Name": name,
***REMOVED******REMOVED******REMOVED***"FromName": from_name,
***REMOVED******REMOVED******REMOVED***"FromEmail": from_email,
***REMOVED******REMOVED******REMOVED***"ReplyTo": reply_to,
***REMOVED******REMOVED******REMOVED***"HtmlUrl": html_url,
***REMOVED******REMOVED******REMOVED***"TextUrl": text_url,
***REMOVED******REMOVED******REMOVED***"ListIDs": list_ids,
***REMOVED******REMOVED******REMOVED***"SegmentIDs": segment_ids }
***REMOVED******REMOVED***response = self._post("/campaigns/%s.json" % client_id, json.dumps(body))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def send_preview(self, recipients, personalize="fallback"):
***REMOVED******REMOVED***"""Sends a preview of this campaign."""
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"PreviewRecipients": [ recipients ] if isinstance(recipients, str) else recipients,
***REMOVED******REMOVED******REMOVED***"Personalize": personalize }
***REMOVED******REMOVED***response = self._post(self.uri_for("sendpreview"), json.dumps(body))

***REMOVED***def send(self, confirmation_email, send_date="immediately"):
***REMOVED******REMOVED***"""Sends this campaign."""
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"ConfirmationEmail": confirmation_email,
***REMOVED******REMOVED******REMOVED***"SendDate": send_date }
***REMOVED******REMOVED***response = self._post(self.uri_for("send"), json.dumps(body))

***REMOVED***def delete(self):
***REMOVED******REMOVED***"""Deletes this campaign."""
***REMOVED******REMOVED***response = self._delete("/campaigns/%s.json" % self.campaign_id)

***REMOVED***def summary(self):
***REMOVED******REMOVED***"""Gets a summary of this campaign"""
***REMOVED******REMOVED***response = self._get(self.uri_for("summary"))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def lists_and_segments(self):
***REMOVED******REMOVED***"""Retrieves the lists and segments to which this campaaign will be (or was) sent."""
***REMOVED******REMOVED***response = self._get(self.uri_for("listsandsegments"))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def recipients(self, page=1, page_size=1000, order_field="email", order_direction="asc"):
***REMOVED******REMOVED***"""Retrieves the recipients of this campaign."""
***REMOVED******REMOVED***params = { 
***REMOVED******REMOVED******REMOVED***"page": page,
***REMOVED******REMOVED******REMOVED***"pagesize": page_size,
***REMOVED******REMOVED******REMOVED***"orderfield": order_field,
***REMOVED******REMOVED******REMOVED***"orderdirection": order_direction }
***REMOVED******REMOVED***response = self._get(self.uri_for("recipients"), params=params)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def opens(self, date, page=1, page_size=1000, order_field="date", order_direction="asc"):
***REMOVED******REMOVED***"""Retrieves the opens for this campaign."""
***REMOVED******REMOVED***params = { 
***REMOVED******REMOVED******REMOVED***"date": date,
***REMOVED******REMOVED******REMOVED***"page": page,
***REMOVED******REMOVED******REMOVED***"pagesize": page_size,
***REMOVED******REMOVED******REMOVED***"orderfield": order_field,
***REMOVED******REMOVED******REMOVED***"orderdirection": order_direction }
***REMOVED******REMOVED***response = self._get(self.uri_for("opens"), params=params)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def clicks(self, date, page=1, page_size=1000, order_field="date", order_direction="asc"):
***REMOVED******REMOVED***"""Retrieves the subscriber clicks for this campaign."""
***REMOVED******REMOVED***params = { 
***REMOVED******REMOVED******REMOVED***"date": date,
***REMOVED******REMOVED******REMOVED***"page": page,
***REMOVED******REMOVED******REMOVED***"pagesize": page_size,
***REMOVED******REMOVED******REMOVED***"orderfield": order_field,
***REMOVED******REMOVED******REMOVED***"orderdirection": order_direction }
***REMOVED******REMOVED***response = self._get(self.uri_for("clicks"), params=params)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def unsubscribes(self, date, page=1, page_size=1000, order_field="date", order_direction="asc"):
***REMOVED******REMOVED***"""Retrieves the unsubscribes for this campaign."""
***REMOVED******REMOVED***params = { 
***REMOVED******REMOVED******REMOVED***"date": date,
***REMOVED******REMOVED******REMOVED***"page": page,
***REMOVED******REMOVED******REMOVED***"pagesize": page_size,
***REMOVED******REMOVED******REMOVED***"orderfield": order_field,
***REMOVED******REMOVED******REMOVED***"orderdirection": order_direction }
***REMOVED******REMOVED***response = self._get(self.uri_for("unsubscribes"), params=params)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def bounces(self, date="1900-01-01", page=1, page_size=1000, order_field="date", order_direction="asc"):
***REMOVED******REMOVED***"""Retrieves the bounces for this campaign."""
***REMOVED******REMOVED***params = { 
***REMOVED******REMOVED******REMOVED***"date": date,
***REMOVED******REMOVED******REMOVED***"page": page,
***REMOVED******REMOVED******REMOVED***"pagesize": page_size,
***REMOVED******REMOVED******REMOVED***"orderfield": order_field,
***REMOVED******REMOVED******REMOVED***"orderdirection": order_direction }
***REMOVED******REMOVED***response = self._get(self.uri_for("bounces"), params=params)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def uri_for(self, action):
***REMOVED******REMOVED***return "/campaigns/%s/%s.json" % (self.campaign_id, action)
