try:
***REMOVED***import json
except ImportError:
***REMOVED***import simplejson as json
from createsend import CreateSendBase
from utils import json_to_py

class Segment(CreateSendBase):
***REMOVED***"""Represents a subscriber list segment and associated functionality."""

***REMOVED***def __init__(self, auth=None, segment_id=None):
***REMOVED******REMOVED***self.segment_id = segment_id
***REMOVED******REMOVED***super(Segment, self).__init__(auth)

***REMOVED***def create(self, list_id, title, rulegroups):
***REMOVED******REMOVED***"""Creates a new segment."""
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"Title": title,
***REMOVED******REMOVED******REMOVED***"RuleGroups": rulegroups }
***REMOVED******REMOVED***response = self._post("/segments/%s.json" % list_id, json.dumps(body))
***REMOVED******REMOVED***self.segment_id = json_to_py(response)
***REMOVED******REMOVED***return self.segment_id

***REMOVED***def update(self, title, rulegroups):
***REMOVED******REMOVED***"""Updates this segment."""
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"Title": title,
***REMOVED******REMOVED******REMOVED***"RuleGroups": rulegroups }
***REMOVED******REMOVED***response = self._put("/segments/%s.json" % self.segment_id, json.dumps(body))

***REMOVED***def add_rulegroup(self, rulegroup):
***REMOVED******REMOVED***"""Adds a rulegroup to this segment."""
***REMOVED******REMOVED***body = rulegroup
***REMOVED******REMOVED***response = self._post("/segments/%s/rules.json" % self.segment_id, json.dumps(body))

***REMOVED***def subscribers(self, date="", page=1, page_size=1000, order_field="email", order_direction="asc"):
***REMOVED******REMOVED***"""Gets the active subscribers in this segment."""
***REMOVED******REMOVED***params = {
***REMOVED******REMOVED******REMOVED***"date": date,
***REMOVED******REMOVED******REMOVED***"page": page,
***REMOVED******REMOVED******REMOVED***"pagesize": page_size,
***REMOVED******REMOVED******REMOVED***"orderfield": order_field,
***REMOVED******REMOVED******REMOVED***"orderdirection": order_direction }
***REMOVED******REMOVED***response = self._get(self.uri_for("active"), params=params)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def details(self):
***REMOVED******REMOVED***"""Gets the details of this segment"""
***REMOVED******REMOVED***response = self._get("/segments/%s.json" % self.segment_id)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def clear_rules(self):
***REMOVED******REMOVED***"""Clears all rules of this segment."""
***REMOVED******REMOVED***response = self._delete("/segments/%s/rules.json" % self.segment_id)

***REMOVED***def delete(self):
***REMOVED******REMOVED***"""Deletes this segment."""
***REMOVED******REMOVED***response = self._delete("/segments/%s.json" % self.segment_id)

***REMOVED***def uri_for(self, action):
***REMOVED******REMOVED***return "/segments/%s/%s.json" % (self.segment_id, action)
