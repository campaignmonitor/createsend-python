try:
***REMOVED******REMOVED***import json
except ImportError:
***REMOVED******REMOVED***import simplejson as json
from createsend.createsend import CreateSendBase
from createsend.utils import json_to_py


class Segment(CreateSendBase):
***REMOVED******REMOVED***"""Represents a subscriber list segment and associated functionality."""

***REMOVED******REMOVED***def __init__(self, auth=None, segment_id=None):
***REMOVED******REMOVED******REMOVED******REMOVED***self.segment_id = segment_id
***REMOVED******REMOVED******REMOVED******REMOVED***super(Segment, self).__init__(auth)

***REMOVED******REMOVED***def create(self, list_id, title, rulegroups):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Creates a new segment."""
***REMOVED******REMOVED******REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Title": title,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"RuleGroups": rulegroups}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._post("/segments/%s.json" % list_id, json.dumps(body))
***REMOVED******REMOVED******REMOVED******REMOVED***self.segment_id = json_to_py(response)
***REMOVED******REMOVED******REMOVED******REMOVED***return self.segment_id

***REMOVED******REMOVED***def update(self, title, rulegroups):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Updates this segment."""
***REMOVED******REMOVED******REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Title": title,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"RuleGroups": rulegroups}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._put("/segments/%s.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.segment_id, json.dumps(body))

***REMOVED******REMOVED***def add_rulegroup(self, rulegroup):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Adds a rulegroup to this segment."""
***REMOVED******REMOVED******REMOVED******REMOVED***body = rulegroup
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._post("/segments/%s/rules.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.segment_id, json.dumps(body))

***REMOVED******REMOVED***def subscribers(self, date="", page=1, page_size=1000, order_field="email", order_direction="asc"):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets the active subscribers in this segment."""
***REMOVED******REMOVED******REMOVED******REMOVED***params = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"date": date,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"page": page,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"pagesize": page_size,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"orderfield": order_field,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"orderdirection": order_direction}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get(self.uri_for("active"), params=params)
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def details(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets the details of this segment"""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get("/segments/%s.json" % self.segment_id)
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def clear_rules(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Clears all rules of this segment."""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._delete("/segments/%s/rules.json" % self.segment_id)

***REMOVED******REMOVED***def delete(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Deletes this segment."""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._delete("/segments/%s.json" % self.segment_id)

***REMOVED******REMOVED***def uri_for(self, action):
***REMOVED******REMOVED******REMOVED******REMOVED***return "/segments/%s/%s.json" % (self.segment_id, action)
