import json

from createsend.createsend import CreateSendBase
from createsend.utils import json_to_py, validate_consent_to_track


class Transactional(CreateSendBase):
***REMOVED******REMOVED***"""Represents transactional functionality."""

***REMOVED******REMOVED***def __init__(self, auth=None, client_id=None):
***REMOVED******REMOVED******REMOVED******REMOVED***self.client_id = client_id
***REMOVED******REMOVED******REMOVED******REMOVED***super().__init__(auth)

***REMOVED******REMOVED***def smart_email_list(self, status="all", client_id=None):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets the smart email list."""
***REMOVED******REMOVED******REMOVED******REMOVED***if client_id is None:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***response = self._get(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"/transactional/smartEmail?status=%s" % status)
***REMOVED******REMOVED******REMOVED******REMOVED***else:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***response = self._get(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"/transactional/smartEmail?status={}&clientID={}".format(status, client_id))
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def smart_email_details(self, smart_email_id):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets the smart email details."""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get("/transactional/smartEmail/%s" % smart_email_id)
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def smart_email_send(self, smart_email_id, to, consent_to_track, cc=None, bcc=None, attachments=None, data=None, add_recipients_to_list=None):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Sends the smart email."""
***REMOVED******REMOVED******REMOVED******REMOVED***validate_consent_to_track(consent_to_track)
***REMOVED******REMOVED******REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"To": to,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"CC": cc,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"BCC": bcc,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Attachments": attachments,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Data": data,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"AddRecipientsToList": add_recipients_to_list,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"ConsentToTrack": consent_to_track,
***REMOVED******REMOVED******REMOVED******REMOVED***}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._post("/transactional/smartEmail/%s/send" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***smart_email_id, json.dumps(body))
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def classic_email_send(self, subject, from_address, to, consent_to_track, client_id=None, cc=None, bcc=None, html=None, text=None, attachments=None, track_opens=True, track_clicks=True, inline_css=True, group=None, add_recipients_to_list=None):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Sends a classic email."""
***REMOVED******REMOVED******REMOVED******REMOVED***validate_consent_to_track(consent_to_track)
***REMOVED******REMOVED******REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Subject": subject,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"From": from_address,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"To": to,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"CC": cc,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"BCC": bcc,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"HTML": html,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Text": text,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Attachments": attachments,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"TrackOpens": track_opens,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"TrackClicks": track_clicks,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"InlineCSS": inline_css,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Group": group,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"AddRecipientsToList": add_recipients_to_list,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"ConsentToTrack": consent_to_track,
***REMOVED******REMOVED******REMOVED******REMOVED***}
***REMOVED******REMOVED******REMOVED******REMOVED***if client_id is None:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***response = self._post(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"/transactional/classicEmail/send", json.dumps(body))
***REMOVED******REMOVED******REMOVED******REMOVED***else:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***response = self._post(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"/transactional/classicEmail/send?clientID=%s" % client_id, json.dumps(body))
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def classic_email_groups(self, client_id=None):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets the list of classic email groups."""
***REMOVED******REMOVED******REMOVED******REMOVED***if client_id is None:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***response = self._get("/transactional/classicEmail/groups")
***REMOVED******REMOVED******REMOVED******REMOVED***else:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***response = self._get(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"/transactional/classicEmail/groups?clientID=%s" % client_id)
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def statistics(self, params={}):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets the statistics according to the parameters."""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get("/transactional/statistics", params)
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def message_timeline(self, params={}):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets the messages timeline according to the parameters."""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get("/transactional/messages", params)
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def message_details(self, message_id, statistics=False, exclude_message_body=False):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets the details of this message."""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"/transactional/messages/{}?statistics={}&excludemessagebody={}".format(message_id, statistics, exclude_message_body))
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def message_resend(self, message_id):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Resend the message."""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._post("/transactional/messages/%s/resend" % message_id)
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)
