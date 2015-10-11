try:
  import json
except ImportError:
  import simplejson as json
from .createsend import CreateSendBase
from .utils import json_to_py

class Transactional(CreateSendBase):
  """Represents transactional functionality."""

  def __init__(self, auth=None, client_id=None):
    self.client_id = client_id
    super(Transactional, self).__init__(auth)

  def smart_email_list(self, status="all", client_id=None):
    """Gets the smart email list."""
    if client_id is None:
      response = self._get("/transactional/smartEmail?status=%s" % status)
    else:
      response = self._get("/transactional/smartEmail?status=%s&clientID=%s" % (status, client_id))
    return json_to_py(response)

  def smart_email_details(self, smart_email_id):
    """Gets the smart email details."""
    response = self._get("/transactional/smartEmail/%s" % smart_email_id)
    return json_to_py(response)

  def smart_email_send(self, smart_email_id, to, cc=None, bcc=None, attachments=None, data=None, add_recipients_to_list=None):
     """Sends the smart email."""
     body = {
      "To": to,
      "CC": cc,
      "BCC": bcc,
      "Attachments": attachments,
      "Data": data,
      "AddRecipientsToList": add_recipients_to_list }
     response = self._post("/transactional/smartEmail/%s/send" % smart_email_id, json.dumps(body))
     return json_to_py(response)

  def classic_email_send(self, subject, from_address, to, client_id=None, cc=None, bcc=None, html=None, text=None, attachments=None, track_opens=True, track_clicks=True, inline_css=True, group=None, add_recipients_to_list=None):
     """Sends a classic email."""
     body = {
      "Subject": subject,
      "From": from_address,
      "To": to,
      "CC": cc,
      "BCC": bcc,
      "HTML": html,
      "Text": text,
      "Attachments": attachments,
      "TrackOpens": track_opens,
      "TrackClicks": track_clicks,
      "InlineCSS": inline_css,
      "Group": group,
      "AddRecipientsToList": add_recipients_to_list }
     if client_id is None:
       response = self._post("/transactional/classicEmail/send", json.dumps(body))
     else:
       response = self._post("/transactional/classicEmail/send?clientID=%s" % client_id, json.dumps(body))
     return json_to_py(response)

  def classic_email_groups(self, client_id=None):
    """Gets the list of classic email groups."""
    if client_id is None:
      response = self._get("/transactional/classicEmail/groups")
    else:
      response = self._get("/transactional/classicEmail/groups?clientID=%s" % client_id)
    return json_to_py(response)

  def statistics(self, params={}):
    """Gets the statistics according to the parameters."""
    response = self._get("/transactional/statistics", params)
    return json_to_py(response)

  def message_timeline(self, params={}):
    """Gets the messages timeline according to the parameters."""
    response = self._get("/transactional/messages", params)
    return json_to_py(response)

  def message_details(self, message_id, statistics=False):
    """Gets the details of this message."""
    response = self._get("/transactional/messages/%s?statistics=%s" % (message_id, statistics))
    return json_to_py(response)

  def message_resend(self, message_id):
    """Resend the message."""
    response = self._post("/transactional/messages/%s/resend" % message_id)
    return json_to_py(response)
