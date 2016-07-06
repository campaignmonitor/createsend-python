try:
***REMOVED***import json
except ImportError:
***REMOVED***import simplejson as json
from .createsend import CreateSendBase
from .utils import json_to_py

class Transactional(CreateSendBase):
***REMOVED***"""Represents transactional functionality."""

***REMOVED***def __init__(self, auth=None, client_id=None):
***REMOVED******REMOVED***self.client_id = client_id
***REMOVED******REMOVED***super(Transactional, self).__init__(auth)

***REMOVED***def smart_email_list(self, status="all", client_id=None):
***REMOVED******REMOVED***"""Gets the smart email list."""
***REMOVED******REMOVED***if client_id is None:
***REMOVED******REMOVED******REMOVED***response = self._get("/transactional/smartEmail?status=%s" % status)
***REMOVED******REMOVED***else:
***REMOVED******REMOVED******REMOVED***response = self._get("/transactional/smartEmail?status=%s&clientID=%s" % (status, client_id))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def smart_email_details(self, smart_email_id):
***REMOVED******REMOVED***"""Gets the smart email details."""
***REMOVED******REMOVED***response = self._get("/transactional/smartEmail/%s" % smart_email_id)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def smart_email_send(self, smart_email_id, to, cc=None, bcc=None, attachments=None, data=None, add_recipients_to_list=None):
***REMOVED******REMOVED*** """Sends the smart email."""
***REMOVED******REMOVED*** body = {
***REMOVED******REMOVED******REMOVED***"To": to,
***REMOVED******REMOVED******REMOVED***"CC": cc,
***REMOVED******REMOVED******REMOVED***"BCC": bcc,
***REMOVED******REMOVED******REMOVED***"Attachments": attachments,
***REMOVED******REMOVED******REMOVED***"Data": data,
***REMOVED******REMOVED******REMOVED***"AddRecipientsToList": add_recipients_to_list }
***REMOVED******REMOVED*** response = self._post("/transactional/smartEmail/%s/send" % smart_email_id, json.dumps(body))
***REMOVED******REMOVED*** return json_to_py(response)

***REMOVED***def classic_email_send(self, subject, from_address, to, client_id=None, cc=None, bcc=None, html=None, text=None, attachments=None, track_opens=True, track_clicks=True, inline_css=True, group=None, add_recipients_to_list=None):
***REMOVED******REMOVED*** """Sends a classic email."""
***REMOVED******REMOVED*** body = {
***REMOVED******REMOVED******REMOVED***"Subject": subject,
***REMOVED******REMOVED******REMOVED***"From": from_address,
***REMOVED******REMOVED******REMOVED***"To": to,
***REMOVED******REMOVED******REMOVED***"CC": cc,
***REMOVED******REMOVED******REMOVED***"BCC": bcc,
***REMOVED******REMOVED******REMOVED***"HTML": html,
***REMOVED******REMOVED******REMOVED***"Text": text,
***REMOVED******REMOVED******REMOVED***"Attachments": attachments,
***REMOVED******REMOVED******REMOVED***"TrackOpens": track_opens,
***REMOVED******REMOVED******REMOVED***"TrackClicks": track_clicks,
***REMOVED******REMOVED******REMOVED***"InlineCSS": inline_css,
***REMOVED******REMOVED******REMOVED***"Group": group,
***REMOVED******REMOVED******REMOVED***"AddRecipientsToList": add_recipients_to_list }
***REMOVED******REMOVED*** if client_id is None:
***REMOVED******REMOVED******REMOVED*** response = self._post("/transactional/classicEmail/send", json.dumps(body))
***REMOVED******REMOVED*** else:
***REMOVED******REMOVED******REMOVED*** response = self._post("/transactional/classicEmail/send?clientID=%s" % client_id, json.dumps(body))
***REMOVED******REMOVED*** return json_to_py(response)

***REMOVED***def classic_email_groups(self, client_id=None):
***REMOVED******REMOVED***"""Gets the list of classic email groups."""
***REMOVED******REMOVED***if client_id is None:
***REMOVED******REMOVED******REMOVED***response = self._get("/transactional/classicEmail/groups")
***REMOVED******REMOVED***else:
***REMOVED******REMOVED******REMOVED***response = self._get("/transactional/classicEmail/groups?clientID=%s" % client_id)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def statistics(self, params={}):
***REMOVED******REMOVED***"""Gets the statistics according to the parameters."""
***REMOVED******REMOVED***response = self._get("/transactional/statistics", params)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def message_timeline(self, params={}):
***REMOVED******REMOVED***"""Gets the messages timeline according to the parameters."""
***REMOVED******REMOVED***response = self._get("/transactional/messages", params)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def message_details(self, message_id, statistics=False):
***REMOVED******REMOVED***"""Gets the details of this message."""
***REMOVED******REMOVED***response = self._get("/transactional/messages/%s?statistics=%s" % (message_id, statistics))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def message_resend(self, message_id):
***REMOVED******REMOVED***"""Resend the message."""
***REMOVED******REMOVED***response = self._post("/transactional/messages/%s/resend" % message_id)
***REMOVED******REMOVED***return json_to_py(response)
