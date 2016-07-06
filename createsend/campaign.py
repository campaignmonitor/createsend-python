try:
  import json
except ImportError:
  import simplejson as json
from .createsend import CreateSendBase
from .utils import json_to_py

class Campaign(CreateSendBase):
  """Represents a campaign and provides associated functionality."""

  def __init__(self, auth=None, campaign_id=None):
    self.campaign_id = campaign_id
    super(Campaign, self).__init__(auth)

  def create(self, client_id, subject, name, from_name, from_email, reply_to, html_url,
    text_url, list_ids, segment_ids):
    """Creates a new campaign for a client.

    :param client_id: String representing the ID of the client for whom the
      campaign will be created.
    :param subject: String representing the subject of the campaign.
    :param name: String representing the name of the campaign.
    :param from_name: String representing the from name for the campaign.
    :param from_email: String representing the from address for the campaign.
    :param reply_to: String representing the reply-to address for the campaign.
    :param html_url: String representing the URL for the campaign HTML content.
    :param text_url: String representing the URL for the campaign text content.
      Note that text_url is optional and if None or an empty string, text
      content will be automatically generated from the HTML content.
    :param list_ids: Array of Strings representing the IDs of the lists to
      which the campaign will be sent.
    :param segment_ids: Array of Strings representing the IDs of the segments to
      which the campaign will be sent.
    :returns String representing the ID of the newly created campaign.
    """
    body = {
      "Subject": subject,
      "Name": name,
      "FromName": from_name,
      "FromEmail": from_email,
      "ReplyTo": reply_to,
      "HtmlUrl": html_url,
      "TextUrl": text_url,
      "ListIDs": list_ids,
      "SegmentIDs": segment_ids }
    response = self._post("/campaigns/%s.json" % client_id, json.dumps(body))
    self.campaign_id = json_to_py(response)
    return self.campaign_id

  def create_from_template(self, client_id, subject, name, from_name,
    from_email, reply_to, list_ids, segment_ids, template_id, template_content):
    """Creates a new campaign for a client, from a template.

    :param client_id: String representing the ID of the client for whom the
      campaign will be created.
    :param subject: String representing the subject of the campaign.
    :param name: String representing the name of the campaign.
    :param from_name: String representing the from name for the campaign.
    :param from_email: String representing the from address for the campaign.
    :param reply_to: String representing the reply-to address for the campaign.
    :param list_ids: Array of Strings representing the IDs of the lists to
      which the campaign will be sent.
    :param segment_ids: Array of Strings representing the IDs of the segments to
      which the campaign will be sent.
    :param template_id: String representing the ID of the template on which
      the campaign will be based.
    :param template_content: Hash representing the content to be used for the
      editable areas of the template. See documentation at
      campaignmonitor.com/api/campaigns/#creating_a_campaign_from_template
      for full details of template content format.
    :returns String representing the ID of the newly created campaign.
    """
    body = {
      "Subject": subject,
      "Name": name,
      "FromName": from_name,
      "FromEmail": from_email,
      "ReplyTo": reply_to,
      "ListIDs": list_ids,
      "SegmentIDs": segment_ids,
      "TemplateID": template_id,
      "TemplateContent": template_content }
    response = self._post("/campaigns/%s/fromtemplate.json" % client_id, json.dumps(body))
    self.campaign_id = json_to_py(response)
    return self.campaign_id

  def send_preview(self, recipients, personalize="fallback"):
    """Sends a preview of this campaign."""
    body = {
      "PreviewRecipients": [ recipients ] if isinstance(recipients, str) else recipients,
      "Personalize": personalize }
    response = self._post(self.uri_for("sendpreview"), json.dumps(body))

  def send(self, confirmation_email, send_date="immediately"):
    """Sends this campaign."""
    body = {
      "ConfirmationEmail": confirmation_email,
      "SendDate": send_date }
    response = self._post(self.uri_for("send"), json.dumps(body))

  def unschedule(self):
    """Unschedules this campaign if it is currently scheduled."""
    response = self._post(self.uri_for("unschedule"), json.dumps({}))

  def delete(self):
    """Deletes this campaign."""
    response = self._delete("/campaigns/%s.json" % self.campaign_id)

  def summary(self):
    """Gets a summary of this campaign"""
    response = self._get(self.uri_for("summary"))
    return json_to_py(response)

  def email_client_usage(self):
    """Gets the email clients that subscribers used to open the campaign"""
    response = self._get(self.uri_for("emailclientusage"))
    return json_to_py(response)

  def lists_and_segments(self):
    """Retrieves the lists and segments to which this campaaign will be (or was) sent."""
    response = self._get(self.uri_for("listsandsegments"))
    return json_to_py(response)

  def recipients(self, page=1, page_size=1000, order_field="email", order_direction="asc"):
    """Retrieves the recipients of this campaign."""
    params = { 
      "page": page,
      "pagesize": page_size,
      "orderfield": order_field,
      "orderdirection": order_direction }
    response = self._get(self.uri_for("recipients"), params=params)
    return json_to_py(response)

  def opens(self, date="", page=1, page_size=1000, order_field="date", order_direction="asc"):
    """Retrieves the opens for this campaign."""
    params = { 
      "date": date,
      "page": page,
      "pagesize": page_size,
      "orderfield": order_field,
      "orderdirection": order_direction }
    response = self._get(self.uri_for("opens"), params=params)
    return json_to_py(response)

  def clicks(self, date="", page=1, page_size=1000, order_field="date", order_direction="asc"):
    """Retrieves the subscriber clicks for this campaign."""
    params = { 
      "date": date,
      "page": page,
      "pagesize": page_size,
      "orderfield": order_field,
      "orderdirection": order_direction }
    response = self._get(self.uri_for("clicks"), params=params)
    return json_to_py(response)

  def unsubscribes(self, date="", page=1, page_size=1000, order_field="date", order_direction="asc"):
    """Retrieves the unsubscribes for this campaign."""
    params = { 
      "date": date,
      "page": page,
      "pagesize": page_size,
      "orderfield": order_field,
      "orderdirection": order_direction }
    response = self._get(self.uri_for("unsubscribes"), params=params)
    return json_to_py(response)

  def spam(self, date="", page=1, page_size=1000, order_field="date", order_direction="asc"):
    """Retrieves the spam complaints for this campaign."""
    params = { 
      "date": date,
      "page": page,
      "pagesize": page_size,
      "orderfield": order_field,
      "orderdirection": order_direction }
    response = self._get(self.uri_for("spam"), params=params)
    return json_to_py(response)

  def bounces(self, date="", page=1, page_size=1000, order_field="date", order_direction="asc"):
    """Retrieves the bounces for this campaign."""
    params = { 
      "date": date,
      "page": page,
      "pagesize": page_size,
      "orderfield": order_field,
      "orderdirection": order_direction }
    response = self._get(self.uri_for("bounces"), params=params)
    return json_to_py(response)

  def uri_for(self, action):
    return "/campaigns/%s/%s.json" % (self.campaign_id, action)
