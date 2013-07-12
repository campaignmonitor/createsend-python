import unittest

***REMOVED***
from createsend.utils import match_hostname

class VerifiedHTTPSConnectionTestCase(unittest.TestCase):

***REMOVED***def setUp(self):
***REMOVED******REMOVED***self.cs = CreateSend({'api_key': 'not an api key'})

***REMOVED***def test_verified_connection_no_cert(self):
***REMOVED******REMOVED***self.assertRaises(ValueError, match_hostname, None, 'api.createsend.com')

***REMOVED***def test_verified_connection(self):
***REMOVED******REMOVED***# An actual (non-stubbed) unauthenticated request to test verification.
***REMOVED******REMOVED***self.assertRaises(Unauthorized, self.cs.clients)
