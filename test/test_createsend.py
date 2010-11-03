import unittest

from createsend import CreateSend

class CreateSendTestCase(unittest.TestCase):

***REMOVED***def setUp(self):
***REMOVED******REMOVED***self.cs = CreateSend()

***REMOVED***def test_apikey(self):
***REMOVED******REMOVED***self.cs.stub_request("apikey.json")
***REMOVED******REMOVED***site_url = "http://iamadesigner.createsend.com/"
***REMOVED******REMOVED***username = "myusername"
***REMOVED******REMOVED***password = "mypassword"
***REMOVED******REMOVED***apikey = self.cs.apikey(site_url, username, password)
***REMOVED******REMOVED***self.assertEquals(apikey, "981298u298ue98u219e8u2e98u2")

***REMOVED***def test_clients(self):
***REMOVED******REMOVED***self.cs.stub_request("clients.json")
***REMOVED******REMOVED***cl = self.cs.clients()
***REMOVED******REMOVED***self.assertEquals(2, len(cl))
***REMOVED******REMOVED***self.assertEquals("4a397ccaaa55eb4e6aa1221e1e2d7122", cl[0].ClientID)
***REMOVED******REMOVED***self.assertEquals("Client One", cl[0].Name)

***REMOVED***def test_countries(self):
***REMOVED******REMOVED***self.cs.stub_request("countries.json")
***REMOVED******REMOVED***countries = self.cs.countries()
***REMOVED******REMOVED***self.assertEquals(245, len(countries))
***REMOVED******REMOVED***self.assertEquals("Australia", countries[11])

***REMOVED***def test_systemdate(self):
***REMOVED******REMOVED***self.cs.stub_request("systemdate.json")
***REMOVED******REMOVED***systemdate = self.cs.systemdate()
***REMOVED******REMOVED***self.assertEquals(systemdate, "2010-10-15 09:27:00")
***REMOVED******REMOVED***
***REMOVED***def test_timezones(self):
***REMOVED******REMOVED***self.cs.stub_request("timezones.json")
***REMOVED******REMOVED***timezones = self.cs.timezones()
***REMOVED******REMOVED***self.assertEquals(97, len(timezones))
***REMOVED******REMOVED***self.assertEquals("(GMT+12:00) Fiji", timezones[61])
