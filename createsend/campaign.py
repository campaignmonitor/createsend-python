import json
from createsend import CreateSendBase
from utils import json_to_py

class Campaign(CreateSendBase):

  def __init__(self, campaign_id=None):
    self.campaign_id = campaign_id
    super(Campaign, self).__init__()

  def create(self, client_id, subject, name, from_name, from_email, reply_to, html_url,
    text_url, list_ids, segment_ids):
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
    response = self._post("/campaigns/%s.json" % self.campaign_id, json.dumps(body))
    return json_to_py(response)

  def send_preview(self, recipients, personalize="fallback"):
    body = {
      "PreviewRecipients": [ recipients ] if isinstance(recipients, str) else recipients,
      "Personalize": personalize }
    response = self._post(self.uri_for("sendpreview"), json.dumps(body))

  def send(self, confirmation_email, send_date="immediately"):
    body = {
      "ConfirmationEmail": confirmation_email,
      "SendDate": send_date }
    response = self._post(self.uri_for("send"), json.dumps(body))

  def delete(self):
    response = self._delete("/campaigns/%s.json" % self.campaign_id)

  def summary(self):
    response = self._get(self.uri_for("summary"))
    return json_to_py(response)

  def lists(self):
    response = self._get(self.uri_for("lists"))
    return json_to_py(response)

  def segments(self):
    # TODO: This needs to be implemented
    return []

  def recipients(self, page=1, page_size=1000, order_field="email", order_direction="asc"):
    params = { 
      "page": page,
      "pagesize": page_size,
      "orderfield": order_field,
      "orderdirection": order_direction }
    response = self._get(self.uri_for("recipients"), params=params)
    return json_to_py(response)

  def opens(self, date):
    params = { "date": date }
    response = self._get(self.uri_for("opens"), params=params)
    return json_to_py(response)

  def clicks(self, date):
    params = { "date": date }
    response = self._get(self.uri_for("clicks"), params=params)
    return json_to_py(response)

  def unsubscribes(self, date):
    params = { "date": date }
    response = self._get(self.uri_for("unsubscribes"), params=params)
    return json_to_py(response)

  def bounces(self):
    response = self._get(self.uri_for("bounces"))
    return json_to_py(response)

  def uri_for(self, action):
    return "/campaigns/%s/%s.json" % (self.campaign_id, action)
