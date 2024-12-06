from createsend.createsend import CreateSendBase
from createsend.utils import json_to_py


class Journey(CreateSendBase):
    """Represents a journey and associated functionality"""

    def __init__(self, auth=None, journey_id=None):
        self.journey_id = journey_id
        super().__init__(auth)

    def summary(self):
        """Gets the summary of the journey"""
        response = self._get("/journeys/%s.json" % self.journey_id)
        return json_to_py(response)
