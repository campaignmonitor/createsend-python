import unittest

from createsend import CreateSend
from helper import get_fake_opener

class CreateSendTestCase(unittest.TestCase):

  def setUp(self):
    self.cs = CreateSend()
    self.cs.fake_web = True

  def test_clients(self):
    self.cs.opener = get_fake_opener("clients.json")
    cl = self.cs.clients()
    self.assertEquals(2, len(cl))
    self.assertEquals("4a397ccaaa55eb4e6aa1221e1e2d7122", cl[0].ClientID)
    self.assertEquals("Client One", cl[0].Name)

  def test_countries(self):
    self.cs.opener = get_fake_opener("countries.json")
    countries = self.cs.countries()
    self.assertEquals(245, len(countries))
    self.assertEquals("Australia", countries[11])

  def test_systemdate(self):
    self.cs.opener = get_fake_opener("systemdate.json")
    systemdate = self.cs.systemdate()
    self.assertEquals(systemdate, "2010-10-15 09:27:00")
    

  def test_timezones(self):
    self.cs.opener = get_fake_opener("timezones.json")
    timezones = self.cs.timezones()
    self.assertEquals(97, len(timezones))
    self.assertEquals("(GMT+12:00) Fiji", timezones[61])
