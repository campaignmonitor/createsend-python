import unittest

from createsend.createsend import CreateSend, Unauthorized
from createsend.createsend.utils import match_hostname


class VerifiedHTTPSConnectionTestCase(unittest.TestCase):

***REMOVED******REMOVED***def setUp(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cs = CreateSend({'api_key': 'not an api key'})

***REMOVED******REMOVED***def test_verified_connection_no_cert(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertRaises(ValueError, match_hostname,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***None, 'api.createsend.com')

***REMOVED******REMOVED***def test_verified_connection(self):
***REMOVED******REMOVED******REMOVED******REMOVED***# An actual (non-stubbed) unauthenticated request to test verification.
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertRaises(Unauthorized, self.cs.clients)
