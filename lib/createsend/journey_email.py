from __future__ import absolute_import

import json

from createsend.createsend import CreateSendBase
from createsend.utils import json_to_py


class JourneyEmail(CreateSendBase):
    """Represents a journey and associated functionality"""

    def __init__(self, auth=None, journey_email_id=None):
        self.journey_email_id = journey_email_id
        super(JourneyEmail, self).__init__(auth)

    def bounces(self, date="", page=1, page_size=1000, order_field="date", order_direction="asc"):
        """Retrieves the bounces for this journey email."""
        params = {
            "date": date,
            "page": page,
            "pagesize": page_size,
            "orderfield": order_field,
            "orderdirection": order_direction}
        response = self._get(self.uri_for("bounces"), params=params)
        return json_to_py(response)

    def clicks(self, date="", page=1, page_size=1000, order_field="date", order_direction="asc"):
        """Retrieves the clicks for this journey email."""
        params = {
            "date": date,
            "page": page,
            "pagesize": page_size,
            "orderfield": order_field,
            "orderdirection": order_direction}
        response = self._get(self.uri_for("clicks"), params=params)
        return json_to_py(response)

    def opens(self, date="", page=1, page_size=1000, order_field="date", order_direction="asc"):
        """Retrieves the opens for this journey email."""
        params = {
            "date": date,
            "page": page,
            "pagesize": page_size,
            "orderfield": order_field,
            "orderdirection": order_direction}
        response = self._get(self.uri_for("opens"), params=params)
        return json_to_py(response)

    def recipients(self, date="", page=1, page_size=1000, order_field="date", order_direction="asc"):
        """Retrieves the recipients for this journey email."""
        params = {
            "date": date,
            "page": page,
            "pagesize": page_size,
            "orderfield": order_field,
            "orderdirection": order_direction}
        response = self._get(self.uri_for("recipients"), params=params)
        return json_to_py(response)

    def unsubscribes(self, date="", page=1, page_size=1000, order_field="date", order_direction="asc"):
        """Retrieves the unsubscribes for this journey email."""
        params = {
            "date": date,
            "page": page,
            "pagesize": page_size,
            "orderfield": order_field,
            "orderdirection": order_direction}
        response = self._get(self.uri_for("unsubscribes"), params=params)
        return json_to_py(response)

    def uri_for(self, action):
        return "/journeys/email/%s/%s.json" % (self.journey_email_id, action)
