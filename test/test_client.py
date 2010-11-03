import unittest

from createsend import Client

class CreateSendTestCase(unittest.TestCase):

***REMOVED***def setUp(self):
***REMOVED******REMOVED***self.cl = Client()

***REMOVED***def test_create_client(self):
***REMOVED******REMOVED***self.cl.stub_request("create_client.json")
***REMOVED******REMOVED***client_id = self.cl.create("Client Company Name", "Client Contact Name", "client@example.com", "(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")
***REMOVED******REMOVED***self.assertEquals("32a381c49a2df99f1d0c6f3c112352b9", client_id)
