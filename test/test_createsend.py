import unittest

from createsend import *

class CreateSendTestCase(unittest.TestCase):

  def setUp(self):
    self.cs = CreateSend()
    # Mapping of http status codes to the exceptions expected to be raised
    self.error_responses = {
      400: BadRequest,
      401: Unauthorized,
      404: NotFound,
      500: ServerError }

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

  # Test that the corresponding exceptions are raised according to the returned http status code
  def test_bad_request_on_get(self):
    self.cs.stub_request('custom_api_error.json', status=400)
    self.assertRaises(self.error_responses[400], self.cs.countries)

  def test_unauthorized_on_get(self):
    self.cs.stub_request(None, status=401)
    self.assertRaises(self.error_responses[401], self.cs.countries)

  def test_not_found_on_get(self):
    self.cs.stub_request(None, status=404)
    self.assertRaises(self.error_responses[404], self.cs.countries)

  def test_server_error_on_get(self):
    self.cs.stub_request(None, status=500)
    self.assertRaises(self.error_responses[500], self.cs.countries)

  def test_bad_request_on_post(self):
    client = Client("uhiuhiuhiuhiuhiuhiuh")
    client.stub_request('custom_api_error.json', status=400)
    self.assertRaises(self.error_responses[400], client.create, "Client Company Name", "Client Contact Name", "client@example.com", 
      "(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")

  def test_unauthorized_on_post(self):
    client = Client("uhiuhiuhiuhiuhiuhiuh")
    client.stub_request(None, status=401)
    self.assertRaises(self.error_responses[401], client.create, "Client Company Name", "Client Contact Name", "client@example.com", 
      "(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")

  def test_not_found_on_post(self):
    client = Client("uhiuhiuhiuhiuhiuhiuh")
    client.stub_request(None, status=404)
    self.assertRaises(self.error_responses[404], client.create, "Client Company Name", "Client Contact Name", "client@example.com", 
      "(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")

  def test_server_error_on_post(self):
    client = Client("uhiuhiuhiuhiuhiuhiuh")
    client.stub_request(None, status=500)
    self.assertRaises(self.error_responses[500], client.create, "Client Company Name", "Client Contact Name", "client@example.com", 
      "(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")

  def test_bad_request_on_put(self):
    template = Template("uhiuhiuhiuhiuhiuhiuh")
    template.stub_request('custom_api_error.json', status=400)
    self.assertRaises(self.error_responses[400], template.update, "Template One Updated", "http://templates.org/index.html", 
      "http://templates.org/files.zip", "http://templates.org/screenshot.jpg")

  def test_unauthorized_on_put(self):
    template = Template("uhiuhiuhiuhiuhiuhiuh")
    template.stub_request(None, status=401)
    self.assertRaises(self.error_responses[401], template.update, "Template One Updated", "http://templates.org/index.html", 
      "http://templates.org/files.zip", "http://templates.org/screenshot.jpg")

  def test_not_found_on_put(self):
    template = Template("uhiuhiuhiuhiuhiuhiuh")
    template.stub_request(None, status=404)
    self.assertRaises(self.error_responses[404], template.update, "Template One Updated", "http://templates.org/index.html", 
      "http://templates.org/files.zip", "http://templates.org/screenshot.jpg")

  def test_server_error_on_put(self):
    template = Template("uhiuhiuhiuhiuhiuhiuh")
    template.stub_request(None, status=500)
    self.assertRaises(self.error_responses[500], template.update, "Template One Updated", "http://templates.org/index.html", 
      "http://templates.org/files.zip", "http://templates.org/screenshot.jpg")
  
  def test_bad_request_on_delete(self):
    template = Template("uhiuhiuhiuhiuhiuhiuh")
    template.stub_request('custom_api_error.json', status=400)
    self.assertRaises(self.error_responses[400], template.delete)

  def test_unauthorized_on_delete(self):
    template = Template("uhiuhiuhiuhiuhiuhiuh")
    template.stub_request(None, status=401)
    self.assertRaises(self.error_responses[401], template.delete)

  def test_not_found_on_delete(self):
    template = Template("uhiuhiuhiuhiuhiuhiuh")
    template.stub_request(None, status=404)
    self.assertRaises(self.error_responses[404], template.delete)

  def test_server_error_on_delete(self):
    template = Template("uhiuhiuhiuhiuhiuhiuh")
    template.stub_request(None, status=500)
    self.assertRaises(self.error_responses[500], template.delete)
