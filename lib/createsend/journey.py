from __future__ import absolute_import

from createsend.createsend import CreateSendBase
from createsend.utils import json_to_py


class Journey(CreateSendBase):
***REMOVED******REMOVED***"""Represents a journey and associated functionality"""

***REMOVED******REMOVED***def __init__(self, auth=None, journey_id=None):
***REMOVED******REMOVED******REMOVED******REMOVED***self.journey_id = journey_id
***REMOVED******REMOVED******REMOVED******REMOVED***super(Journey, self).__init__(auth)

***REMOVED******REMOVED***def summary(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets the summary of the journey"""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get("/journeys/%s.json" % self.journey_id)
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)
