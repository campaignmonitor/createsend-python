import unittest

from createsend import *
from createsend.utils import match_hostname

class VerifiedHTTPSConnectionTestCase(unittest.TestCase):

  def setUp(self):
    self.cs = CreateSend({'api_key': 'not an api key'})

  def test_verified_connection_no_cert(self):
    self.assertRaises(ValueError, match_hostname, None, 'api.createsend.com')

  def test_verified_connection(self):
    # An actual (non-stubbed) unauthenticated request to test verification.
    self.assertRaises(Unauthorized, self.cs.clients)
