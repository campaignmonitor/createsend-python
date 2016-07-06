try:
***REMOVED***import json
except ImportError:
***REMOVED***import simplejson as json
from .createsend import CreateSendBase
from .utils import json_to_py

class Campaign(CreateSendBase):
***REMOVED***"""Represents a campaign and provides associated functionality."""

***REMOVED***def __init__(self, auth=None, campaign_id=None):
***REMOVED******REMOVED***self.campaign_id = campaign_id
***REMOVED******REMOVED***super(Campaign, self).__init__(auth)

***REMOVED***def create(self, client_id, subject, name, from_name, from_email, reply_to, html_url,
***REMOVED******REMOVED***text_url, list_ids, segment_ids):
***REMOVED******REMOVED***"""Creates a new campaign for a client.

***REMOVED******REMOVED***:param client_id: String representing the ID of the client for whom the
***REMOVED******REMOVED******REMOVED***campaign will be created.
***REMOVED******REMOVED***:param subject: String representing the subject of the campaign.
***REMOVED******REMOVED***:param name: String representing the name of the campaign.
***REMOVED******REMOVED***:param from_name: String representing the from name for the campaign.
***REMOVED******REMOVED***:param from_email: String representing the from address for the campaign.
***REMOVED******REMOVED***:param reply_to: String representing the reply-to address for the campaign.
***REMOVED******REMOVED***:param html_url: String representing the URL for the campaign HTML content.
***REMOVED******REMOVED***:param text_url: String representing the URL for the campaign text content.
***REMOVED******REMOVED******REMOVED***Note that text_url is optional and if None or an empty string, text
***REMOVED******REMOVED******REMOVED***content will be automatically generated from the HTML content.
***REMOVED******REMOVED***:param list_ids: Array of Strings representing the IDs of the lists to
***REMOVED******REMOVED******REMOVED***which the campaign will be sent.
***REMOVED******REMOVED***:param segment_ids: Array of Strings representing the IDs of the segments to
***REMOVED******REMOVED******REMOVED***which the campaign will be sent.
***REMOVED******REMOVED***:returns String representing the ID of the newly created campaign.
***REMOVED******REMOVED***"""
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
***REMOVED******REMOVED***self.campaign_id = json_to_py(response)
***REMOVED******REMOVED***return self.campaign_id

***REMOVED***def create_from_template(self, client_id, subject, name, from_name,
***REMOVED******REMOVED***from_email, reply_to, list_ids, segment_ids, template_id, template_content):
***REMOVED******REMOVED***"""Creates a new campaign for a client, from a template.

***REMOVED******REMOVED***:param client_id: String representing the ID of the client for whom the
***REMOVED******REMOVED******REMOVED***campaign will be created.
***REMOVED******REMOVED***:param subject: String representing the subject of the campaign.
***REMOVED******REMOVED***:param name: String representing the name of the campaign.
***REMOVED******REMOVED***:param from_name: String representing the from name for the campaign.
***REMOVED******REMOVED***:param from_email: String representing the from address for the campaign.
***REMOVED******REMOVED***:param reply_to: String representing the reply-to address for the campaign.
***REMOVED******REMOVED***:param list_ids: Array of Strings representing the IDs of the lists to
***REMOVED******REMOVED******REMOVED***which the campaign will be sent.
***REMOVED******REMOVED***:param segment_ids: Array of Strings representing the IDs of the segments to
***REMOVED******REMOVED******REMOVED***which the campaign will be sent.
***REMOVED******REMOVED***:param template_id: String representing the ID of the template on which
***REMOVED******REMOVED******REMOVED***the campaign will be based.
***REMOVED******REMOVED***:param template_content: Hash representing the content to be used for the
***REMOVED******REMOVED******REMOVED***editable areas of the template. See documentation at
***REMOVED******REMOVED******REMOVED***campaignmonitor.com/api/campaigns/#creating_a_campaign_from_template
***REMOVED******REMOVED******REMOVED***for full details of template content format.
***REMOVED******REMOVED***:returns String representing the ID of the newly created campaign.
***REMOVED******REMOVED***"""
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"Subject": subject,
***REMOVED******REMOVED******REMOVED***"Name": name,
***REMOVED******REMOVED******REMOVED***"FromName": from_name,
***REMOVED******REMOVED******REMOVED***"FromEmail": from_email,
***REMOVED******REMOVED******REMOVED***"ReplyTo": reply_to,
***REMOVED******REMOVED******REMOVED***"ListIDs": list_ids,
***REMOVED******REMOVED******REMOVED***"SegmentIDs": segment_ids,
***REMOVED******REMOVED******REMOVED***"TemplateID": template_id,
***REMOVED******REMOVED******REMOVED***"TemplateContent": template_content }
***REMOVED******REMOVED***response = self._post("/campaigns/%s/fromtemplate.json" % client_id, json.dumps(body))
***REMOVED******REMOVED***self.campaign_id = json_to_py(response)
***REMOVED******REMOVED***return self.campaign_id

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

***REMOVED***def unschedule(self):
***REMOVED******REMOVED***"""Unschedules this campaign if it is currently scheduled."""
***REMOVED******REMOVED***response = self._post(self.uri_for("unschedule"), json.dumps({}))

***REMOVED***def delete(self):
***REMOVED******REMOVED***"""Deletes this campaign."""
***REMOVED******REMOVED***response = self._delete("/campaigns/%s.json" % self.campaign_id)

***REMOVED***def summary(self):
***REMOVED******REMOVED***"""Gets a summary of this campaign"""
***REMOVED******REMOVED***response = self._get(self.uri_for("summary"))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def email_client_usage(self):
***REMOVED******REMOVED***"""Gets the email clients that subscribers used to open the campaign"""
***REMOVED******REMOVED***response = self._get(self.uri_for("emailclientusage"))
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

***REMOVED***def opens(self, date="", page=1, page_size=1000, order_field="date", order_direction="asc"):
***REMOVED******REMOVED***"""Retrieves the opens for this campaign."""
***REMOVED******REMOVED***params = { 
***REMOVED******REMOVED******REMOVED***"date": date,
***REMOVED******REMOVED******REMOVED***"page": page,
***REMOVED******REMOVED******REMOVED***"pagesize": page_size,
***REMOVED******REMOVED******REMOVED***"orderfield": order_field,
***REMOVED******REMOVED******REMOVED***"orderdirection": order_direction }
***REMOVED******REMOVED***response = self._get(self.uri_for("opens"), params=params)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def clicks(self, date="", page=1, page_size=1000, order_field="date", order_direction="asc"):
***REMOVED******REMOVED***"""Retrieves the subscriber clicks for this campaign."""
***REMOVED******REMOVED***params = { 
***REMOVED******REMOVED******REMOVED***"date": date,
***REMOVED******REMOVED******REMOVED***"page": page,
***REMOVED******REMOVED******REMOVED***"pagesize": page_size,
***REMOVED******REMOVED******REMOVED***"orderfield": order_field,
***REMOVED******REMOVED******REMOVED***"orderdirection": order_direction }
***REMOVED******REMOVED***response = self._get(self.uri_for("clicks"), params=params)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def unsubscribes(self, date="", page=1, page_size=1000, order_field="date", order_direction="asc"):
***REMOVED******REMOVED***"""Retrieves the unsubscribes for this campaign."""
***REMOVED******REMOVED***params = { 
***REMOVED******REMOVED******REMOVED***"date": date,
***REMOVED******REMOVED******REMOVED***"page": page,
***REMOVED******REMOVED******REMOVED***"pagesize": page_size,
***REMOVED******REMOVED******REMOVED***"orderfield": order_field,
***REMOVED******REMOVED******REMOVED***"orderdirection": order_direction }
***REMOVED******REMOVED***response = self._get(self.uri_for("unsubscribes"), params=params)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def spam(self, date="", page=1, page_size=1000, order_field="date", order_direction="asc"):
***REMOVED******REMOVED***"""Retrieves the spam complaints for this campaign."""
***REMOVED******REMOVED***params = { 
***REMOVED******REMOVED******REMOVED***"date": date,
***REMOVED******REMOVED******REMOVED***"page": page,
***REMOVED******REMOVED******REMOVED***"pagesize": page_size,
***REMOVED******REMOVED******REMOVED***"orderfield": order_field,
***REMOVED******REMOVED******REMOVED***"orderdirection": order_direction }
***REMOVED******REMOVED***response = self._get(self.uri_for("spam"), params=params)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def bounces(self, date="", page=1, page_size=1000, order_field="date", order_direction="asc"):
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
