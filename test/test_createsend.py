import unittest

from createsend import CreateSend

class CreateSendTestCase(unittest.TestCase):

  def setUp(self):
    self.cs = CreateSend()

  def test_apikey(self):
    self.cs.stub_request("apikey.json")
    site_url = "http://iamadesigner.createsend.com/"
    username = "myusername"
    password = "mypassword"
    apikey = self.cs.apikey(site_url, username, password)
    self.assertEquals(apikey, "981298u298ue98u219e8u2e98u2")

  def test_clients(self):
    self.cs.stub_request("clients.json")
    cl = self.cs.clients()
    self.assertEquals(2, len(cl))
    self.assertEquals("4a397ccaaa55eb4e6aa1221e1e2d7122", cl[0].ClientID)
    self.assertEquals("Client One", cl[0].Name)

  def test_countries(self):
    self.cs.stub_request("countries.json")
    countries = self.cs.countries()
    self.assertEquals(245, len(countries))
    self.assertEquals("Australia", countries[11])

  def test_systemdate(self):
    self.cs.stub_request("systemdate.json")
    systemdate = self.cs.systemdate()
    self.assertEquals(systemdate, "2010-10-15 09:27:00")
    
  def test_timezones(self):
    self.cs.stub_request("timezones.json")
    timezones = self.cs.timezones()
    self.assertEquals(97, len(timezones))
    self.assertEquals("(GMT+12:00) Fiji", timezones[61])
