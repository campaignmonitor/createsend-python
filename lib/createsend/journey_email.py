from __future__ import absolute_import

from createsend.createsend import CreateSendBase
from createsend.utils import json_to_py


class JourneyEmail(CreateSendBase):
***REMOVED******REMOVED***"""Represents a journey and associated functionality"""

***REMOVED******REMOVED***def __init__(self, auth=None, journey_email_id=None):
***REMOVED******REMOVED******REMOVED******REMOVED***self.journey_email_id = journey_email_id
***REMOVED******REMOVED******REMOVED******REMOVED***super(JourneyEmail, self).__init__(auth)

***REMOVED******REMOVED***def bounces(self, date=None, page=None, page_size=None, order_direction=None):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Retrieves the bounces for this journey email."""
***REMOVED******REMOVED******REMOVED******REMOVED***return self.get_journey_email_response(date, page, page_size, order_direction, "bounces")

***REMOVED******REMOVED***def clicks(self, date=None, page=None, page_size=None, order_direction=None):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Retrieves the clicks for this journey email."""
***REMOVED******REMOVED******REMOVED******REMOVED***return self.get_journey_email_response(date, page, page_size, order_direction, "clicks")

***REMOVED******REMOVED***def opens(self, date=None, page=None, page_size=None, order_direction=None):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Retrieves the opens for this journey email."""
***REMOVED******REMOVED******REMOVED******REMOVED***return self.get_journey_email_response(date, page, page_size, order_direction, "opens")

***REMOVED******REMOVED***def recipients(self, date=None, page=None, page_size=None, order_direction=None):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Retrieves the recipients for this journey email."""
***REMOVED******REMOVED******REMOVED******REMOVED***return self.get_journey_email_response(date, page, page_size, order_direction, "recipients")

***REMOVED******REMOVED***def unsubscribes(self, date=None, page=None, page_size=None, order_direction=None):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Retrieves the unsubscribes for this journey email."""
***REMOVED******REMOVED******REMOVED******REMOVED***return self.get_journey_email_response(date, page, page_size, order_direction, "unsubscribes")

***REMOVED******REMOVED***def get_journey_email_response(self, date, page, page_size, order_direction, uri):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Retrieves information for the journey email - based on theuri"""
***REMOVED******REMOVED******REMOVED******REMOVED***params = {}
***REMOVED******REMOVED******REMOVED******REMOVED***if date is not None:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***params["date"] = date
***REMOVED******REMOVED******REMOVED******REMOVED***if page is not None:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***params["page"] = page
***REMOVED******REMOVED******REMOVED******REMOVED***if page_size is not None:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***params["pagesize"] = page_size
***REMOVED******REMOVED******REMOVED******REMOVED***if order_direction is not None:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***params["orderdirection"] = order_direction
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get(self.uri_for(uri), params=params)
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def uri_for(self, action):
***REMOVED******REMOVED******REMOVED******REMOVED***return "/journeys/email/%s/%s.json" % (self.journey_email_id, action)

