import unittest

from createsend import Client

class CreateSendTestCase(unittest.TestCase):

  def setUp(self):
    self.cl = Client()

  def test_create_client(self):
    self.cl.stub_request("create_client.json")
    client_id = self.cl.create("Client Company Name", "Client Contact Name", "client@example.com", "(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")
    self.assertEquals("32a381c49a2df99f1d0c6f3c112352b9", client_id)
