import json
from createsend import CreateSendBase, BadRequest
from utils import json_to_py

class Subscriber(CreateSendBase):

  def __init__(self, list_id=None, email_address=None):
    self.list_id = list_id
    self.email_address = email_address
    super(Subscriber, self).__init__()

  def get(self, list_id, email_address):
    params = { "email": email_address }
    response = self._get("/subscribers/%s.json" % list_id, params=params)
    return json_to_py(response)

  def add(self, list_id, email_address, name, custom_fields, resubscribe):
    body = {
      "EmailAddress": email_address,
      "Name": name,
      "CustomFields": custom_fields,
      "Resubscribe": resubscribe }
    response = self._post("/subscribers/%s.json" % list_id, json.dumps(body))
    return json_to_py(response)

  def import_subscribers(self, list_id, subscribers, resubscribe):
    body = {
      "Subscribers": subscribers,
      "Resubscribe": resubscribe }
    try:
      response = self._post("/subscribers/%s/import.json" % list_id, json.dumps(body))
    except BadRequest as br:
      # Subscriber import will throw BadRequest if some subscribers are not imported
      # successfully. If this occurs, we want to return the ResultData property of
      # the BadRequest exception (which is of the same "form" as the response we'd 
      # receive upon a completely successful import)
      if hasattr(br.data, 'ResultData'):
        return br.data.ResultData
      else:
        raise br
    return json_to_py(response)

  def unsubscribe(self):
    body = {
      "EmailAddress": self.email_address }
    response = self._post("/subscribers/%s/unsubscribe.json" % self.list_id, json.dumps(body))

  def history(self):
    params = { "email": self.email_address }
    response = self._get("/subscribers/%s/history.json" % self.list_id, params=params)
    return json_to_py(response)
