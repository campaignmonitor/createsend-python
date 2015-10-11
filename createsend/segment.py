try:
  import json
except ImportError:
  import simplejson as json
from .createsend import CreateSendBase
from .utils import json_to_py

class Segment(CreateSendBase):
  """Represents a subscriber list segment and associated functionality."""

  def __init__(self, auth=None, segment_id=None):
    self.segment_id = segment_id
    super(Segment, self).__init__(auth)

  def create(self, list_id, title, rulegroups):
    """Creates a new segment."""
    body = {
      "Title": title,
      "RuleGroups": rulegroups }
    response = self._post("/segments/%s.json" % list_id, json.dumps(body))
    self.segment_id = json_to_py(response)
    return self.segment_id

  def update(self, title, rulegroups):
    """Updates this segment."""
    body = {
      "Title": title,
      "RuleGroups": rulegroups }
    response = self._put("/segments/%s.json" % self.segment_id, json.dumps(body))

  def add_rulegroup(self, rulegroup):
    """Adds a rulegroup to this segment."""
    body = rulegroup
    response = self._post("/segments/%s/rules.json" % self.segment_id, json.dumps(body))

  def subscribers(self, date="", page=1, page_size=1000, order_field="email", order_direction="asc"):
    """Gets the active subscribers in this segment."""
    params = {
      "date": date,
      "page": page,
      "pagesize": page_size,
      "orderfield": order_field,
      "orderdirection": order_direction }
    response = self._get(self.uri_for("active"), params=params)
    return json_to_py(response)

  def details(self):
    """Gets the details of this segment"""
    response = self._get("/segments/%s.json" % self.segment_id)
    return json_to_py(response)

  def clear_rules(self):
    """Clears all rules of this segment."""
    response = self._delete("/segments/%s/rules.json" % self.segment_id)

  def delete(self):
    """Deletes this segment."""
    response = self._delete("/segments/%s.json" % self.segment_id)

  def uri_for(self, action):
    return "/segments/%s/%s.json" % (self.segment_id, action)
