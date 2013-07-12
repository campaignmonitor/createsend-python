import unittest

from createsend import *

class VerifiedHTTPSConnectionTestCase(unittest.TestCase):

  def setUp(self):
    self.cs = CreateSend({'api_key': 'not an api key'})

  def test_verified_connection(self):
    # An actual (non-stubbed) unauthenticated request to test verification.
    self.assertRaises(Unauthorized, self.cs.clients)
