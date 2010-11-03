import unittest

from createsend import CreateSend
from helper import get_fake_opener

class CreateSendTestCase(unittest.TestCase):

***REMOVED***def setUp(self):
***REMOVED******REMOVED***self.cs = CreateSend()
***REMOVED******REMOVED***self.cs.fake_web = True

***REMOVED***def test_clients(self):
***REMOVED******REMOVED***self.cs.opener = get_fake_opener("clients.json")
***REMOVED******REMOVED***cl = self.cs.clients()
***REMOVED******REMOVED***self.assertEquals(2, len(cl))
***REMOVED******REMOVED***self.assertEquals("4a397ccaaa55eb4e6aa1221e1e2d7122", cl[0].ClientID)
***REMOVED******REMOVED***self.assertEquals("Client One", cl[0].Name)

***REMOVED***def test_countries(self):
***REMOVED******REMOVED***self.cs.opener = get_fake_opener("countries.json")
***REMOVED******REMOVED***countries = self.cs.countries()
***REMOVED******REMOVED***self.assertEquals(245, len(countries))
***REMOVED******REMOVED***self.assertEquals("Australia", countries[11])

***REMOVED***def test_systemdate(self):
***REMOVED******REMOVED***self.cs.opener = get_fake_opener("systemdate.json")
***REMOVED******REMOVED***systemdate = self.cs.systemdate()
***REMOVED******REMOVED***self.assertEquals(systemdate, "2010-10-15 09:27:00")
***REMOVED******REMOVED***

***REMOVED***def test_timezones(self):
***REMOVED******REMOVED***self.cs.opener = get_fake_opener("timezones.json")
***REMOVED******REMOVED***timezones = self.cs.timezones()
***REMOVED******REMOVED***self.assertEquals(97, len(timezones))
***REMOVED******REMOVED***self.assertEquals("(GMT+12:00) Fiji", timezones[61])
