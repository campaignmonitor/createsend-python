import unittest

***REMOVED***

class CreateSendTestCase(unittest.TestCase):

***REMOVED***def setUp(self):
***REMOVED******REMOVED***self.cs = CreateSend()
***REMOVED******REMOVED***# Mapping of http status codes to the exceptions expected to be raised
***REMOVED******REMOVED***self.error_responses = {
***REMOVED******REMOVED******REMOVED***400: BadRequest,
***REMOVED******REMOVED******REMOVED***401: Unauthorized,
***REMOVED******REMOVED******REMOVED***404: NotFound,
***REMOVED******REMOVED******REMOVED***500: ServerError }

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

***REMOVED***# Test that the corresponding exceptions are raised according to the returned http status code
***REMOVED***def test_bad_request_on_get(self):
***REMOVED******REMOVED***self.cs.stub_request('custom_api_error.json', status=400)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[400], self.cs.countries)

***REMOVED***def test_unauthorized_on_get(self):
***REMOVED******REMOVED***self.cs.stub_request(None, status=401)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[401], self.cs.countries)

***REMOVED***def test_not_found_on_get(self):
***REMOVED******REMOVED***self.cs.stub_request(None, status=404)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[404], self.cs.countries)

***REMOVED***def test_server_error_on_get(self):
***REMOVED******REMOVED***self.cs.stub_request(None, status=500)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[500], self.cs.countries)

***REMOVED***def test_bad_request_on_post(self):
***REMOVED******REMOVED***client = Client("uhiuhiuhiuhiuhiuhiuh")
***REMOVED******REMOVED***client.stub_request('custom_api_error.json', status=400)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[400], client.create, "Client Company Name", "Client Contact Name", "client@example.com", 
***REMOVED******REMOVED******REMOVED***"(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")

***REMOVED***def test_unauthorized_on_post(self):
***REMOVED******REMOVED***client = Client("uhiuhiuhiuhiuhiuhiuh")
***REMOVED******REMOVED***client.stub_request(None, status=401)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[401], client.create, "Client Company Name", "Client Contact Name", "client@example.com", 
***REMOVED******REMOVED******REMOVED***"(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")

***REMOVED***def test_not_found_on_post(self):
***REMOVED******REMOVED***client = Client("uhiuhiuhiuhiuhiuhiuh")
***REMOVED******REMOVED***client.stub_request(None, status=404)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[404], client.create, "Client Company Name", "Client Contact Name", "client@example.com", 
***REMOVED******REMOVED******REMOVED***"(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")

***REMOVED***def test_server_error_on_post(self):
***REMOVED******REMOVED***client = Client("uhiuhiuhiuhiuhiuhiuh")
***REMOVED******REMOVED***client.stub_request(None, status=500)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[500], client.create, "Client Company Name", "Client Contact Name", "client@example.com", 
***REMOVED******REMOVED******REMOVED***"(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")

***REMOVED***def test_bad_request_on_put(self):
***REMOVED******REMOVED***template = Template("uhiuhiuhiuhiuhiuhiuh")
***REMOVED******REMOVED***template.stub_request('custom_api_error.json', status=400)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[400], template.update, "Template One Updated", "http://templates.org/index.html", 
***REMOVED******REMOVED******REMOVED***"http://templates.org/files.zip", "http://templates.org/screenshot.jpg")

***REMOVED***def test_unauthorized_on_put(self):
***REMOVED******REMOVED***template = Template("uhiuhiuhiuhiuhiuhiuh")
***REMOVED******REMOVED***template.stub_request(None, status=401)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[401], template.update, "Template One Updated", "http://templates.org/index.html", 
***REMOVED******REMOVED******REMOVED***"http://templates.org/files.zip", "http://templates.org/screenshot.jpg")

***REMOVED***def test_not_found_on_put(self):
***REMOVED******REMOVED***template = Template("uhiuhiuhiuhiuhiuhiuh")
***REMOVED******REMOVED***template.stub_request(None, status=404)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[404], template.update, "Template One Updated", "http://templates.org/index.html", 
***REMOVED******REMOVED******REMOVED***"http://templates.org/files.zip", "http://templates.org/screenshot.jpg")

***REMOVED***def test_server_error_on_put(self):
***REMOVED******REMOVED***template = Template("uhiuhiuhiuhiuhiuhiuh")
***REMOVED******REMOVED***template.stub_request(None, status=500)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[500], template.update, "Template One Updated", "http://templates.org/index.html", 
***REMOVED******REMOVED******REMOVED***"http://templates.org/files.zip", "http://templates.org/screenshot.jpg")
***REMOVED***
***REMOVED***def test_bad_request_on_delete(self):
***REMOVED******REMOVED***template = Template("uhiuhiuhiuhiuhiuhiuh")
***REMOVED******REMOVED***template.stub_request('custom_api_error.json', status=400)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[400], template.delete)

***REMOVED***def test_unauthorized_on_delete(self):
***REMOVED******REMOVED***template = Template("uhiuhiuhiuhiuhiuhiuh")
***REMOVED******REMOVED***template.stub_request(None, status=401)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[401], template.delete)

***REMOVED***def test_not_found_on_delete(self):
***REMOVED******REMOVED***template = Template("uhiuhiuhiuhiuhiuhiuh")
***REMOVED******REMOVED***template.stub_request(None, status=404)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[404], template.delete)

***REMOVED***def test_server_error_on_delete(self):
***REMOVED******REMOVED***template = Template("uhiuhiuhiuhiuhiuhiuh")
***REMOVED******REMOVED***template.stub_request(None, status=500)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[500], template.delete)
