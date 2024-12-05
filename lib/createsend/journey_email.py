from createsend.createsend import CreateSendBase
from createsend.utils import json_to_py


class JourneyEmail(CreateSendBase):
    """Represents a journey and associated functionality"""

    def __init__(self, auth=None, journey_email_id=None):
        self.journey_email_id = journey_email_id
        super().__init__(auth)

    def bounces(self, date=None, page=None, page_size=None, order_direction=None):
        """Retrieves the bounces for this journey email."""
        return self.get_journey_email_response(date, page, page_size, order_direction, "bounces")

    def clicks(self, date=None, page=None, page_size=None, order_direction=None):
        """Retrieves the clicks for this journey email."""
        return self.get_journey_email_response(date, page, page_size, order_direction, "clicks")

    def opens(self, date=None, page=None, page_size=None, order_direction=None):
        """Retrieves the opens for this journey email."""
        return self.get_journey_email_response(date, page, page_size, order_direction, "opens")

    def recipients(self, date=None, page=None, page_size=None, order_direction=None):
        """Retrieves the recipients for this journey email."""
        return self.get_journey_email_response(date, page, page_size, order_direction, "recipients")

    def unsubscribes(self, date=None, page=None, page_size=None, order_direction=None):
        """Retrieves the unsubscribes for this journey email."""
        return self.get_journey_email_response(date, page, page_size, order_direction, "unsubscribes")

    def get_journey_email_response(self, date, page, page_size, order_direction, uri):
        """Retrieves information for the journey email - based on theuri"""
        params = {}
        if date is not None:
            params["date"] = date
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pagesize"] = page_size
        if order_direction is not None:
            params["orderdirection"] = order_direction
        response = self._get(self.uri_for(uri), params=params)
        return json_to_py(response)

    def uri_for(self, action):
        return "/journeys/email/{}/{}.json".format(self.journey_email_id, action)

