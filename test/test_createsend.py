import unittest
import urllib
from urlparse import urlparse

***REMOVED***

class CreateSendTestCase(object):
***REMOVED***"""CreateSend tests to be run in the context of both using an API key 
***REMOVED***and using OAuth."""

***REMOVED***def test_that_default_user_agent_is_set(self):
***REMOVED******REMOVED***self.cs.stub_request("clients.json", "clients.json")
***REMOVED******REMOVED***cl = self.cs.clients()
***REMOVED******REMOVED***self.assertEquals(self.cs.headers['User-Agent'], CreateSend.default_user_agent)
***REMOVED******REMOVED***self.assertEquals(2, len(cl))

***REMOVED***def test_that_custom_user_agent_can_be_set(self):
***REMOVED******REMOVED***CreateSend.user_agent = "custom user agent"
***REMOVED******REMOVED***self.cs.stub_request("clients.json", "clients.json")
***REMOVED******REMOVED***cl = self.cs.clients()
***REMOVED******REMOVED***self.assertEquals(self.cs.headers['User-Agent'], "custom user agent")
***REMOVED******REMOVED***self.assertEquals(2, len(cl))
***REMOVED******REMOVED***CreateSend.user_agent = CreateSend.default_user_agent

***REMOVED***def test_apikey(self):
***REMOVED******REMOVED***site_url = "http://iamadesigner.createsend.com"
***REMOVED******REMOVED***username = "myusername"
***REMOVED******REMOVED***password = "mypassword"
***REMOVED******REMOVED***self.cs.stub_request("apikey.json?SiteUrl=%s" % urllib.quote(site_url, ''), "apikey.json")
***REMOVED******REMOVED***apikey = self.cs.apikey(site_url, username, password)
***REMOVED******REMOVED***self.assertEquals(apikey, "981298u298ue98u219e8u2e98u2")

***REMOVED***def test_clients(self):
***REMOVED******REMOVED***self.cs.stub_request("clients.json", "clients.json")
***REMOVED******REMOVED***cl = self.cs.clients()
***REMOVED******REMOVED***self.assertEquals(2, len(cl))
***REMOVED******REMOVED***self.assertEquals("4a397ccaaa55eb4e6aa1221e1e2d7122", cl[0].ClientID)
***REMOVED******REMOVED***self.assertEquals("Client One", cl[0].Name)

***REMOVED***def test_billing_details(self):
***REMOVED******REMOVED***self.cs.stub_request("billingdetails.json", "billingdetails.json")
***REMOVED******REMOVED***bd = self.cs.billing_details()
***REMOVED******REMOVED***self.assertEquals(3021, bd.Credits)

***REMOVED***def test_countries(self):
***REMOVED******REMOVED***self.cs.stub_request("countries.json", "countries.json")
***REMOVED******REMOVED***countries = self.cs.countries()
***REMOVED******REMOVED***self.assertEquals(245, len(countries))
***REMOVED******REMOVED***self.assertEquals("Australia", countries[11])

***REMOVED***def test_systemdate(self):
***REMOVED******REMOVED***self.cs.stub_request("systemdate.json", "systemdate.json")
***REMOVED******REMOVED***systemdate = self.cs.systemdate()
***REMOVED******REMOVED***self.assertEquals(systemdate, "2010-10-15 09:27:00")
***REMOVED******REMOVED***
***REMOVED***def test_timezones(self):
***REMOVED******REMOVED***self.cs.stub_request("timezones.json", "timezones.json")
***REMOVED******REMOVED***timezones = self.cs.timezones()
***REMOVED******REMOVED***self.assertEquals(97, len(timezones))
***REMOVED******REMOVED***self.assertEquals("(GMT+12:00) Fiji", timezones[61])
***REMOVED******REMOVED***
***REMOVED***def test_administrators(self):
***REMOVED***	self.cs.stub_request("admins.json", "administrators.json")
***REMOVED***	administrators = self.cs.administrators()
***REMOVED***	self.assertEquals(2, len(administrators))
***REMOVED***	self.assertEquals('admin1@blackhole.com', administrators[0].EmailAddress)
***REMOVED***	self.assertEquals('Admin One', administrators[0].Name)
***REMOVED***	self.assertEquals('Active', administrators[0].Status)***REMOVED***

***REMOVED***def test_get_primary_contact(self):
***REMOVED***	self.cs.stub_request("primarycontact.json", "admin_get_primary_contact.json")
***REMOVED***	primary_contact = self.cs.get_primary_contact()
***REMOVED***	self.assertEquals('admin@blackhole.com', primary_contact.EmailAddress)
***REMOVED***	
***REMOVED***def test_set_primary_contact(self):
***REMOVED******REMOVED***email = 'admin@blackhole.com'
***REMOVED******REMOVED***self.cs.stub_request('primarycontact.json?email=%s' % urllib.quote(email, ''), 'admin_set_primary_contact.json')
***REMOVED******REMOVED***result = self.cs.set_primary_contact(email)
***REMOVED******REMOVED***self.assertEquals(email, result.EmailAddress)

***REMOVED***def test_external_session_url(self):
***REMOVED******REMOVED***email = "exammple@example.com"
***REMOVED******REMOVED***chrome = "None"
***REMOVED******REMOVED***url = "/subscribers"
***REMOVED******REMOVED***integrator_id = "qw989q8wud98qwyd"
***REMOVED******REMOVED***client_id = "9q8uw9d8u9wud"
***REMOVED******REMOVED***self.cs.stub_request('externalsession.json', 'external_session.json')
***REMOVED******REMOVED***result = self.cs.external_session_url(email, chrome, url, integrator_id, client_id)
***REMOVED******REMOVED***self.assertEquals("https://external1.createsend.com/cd/create/ABCDEF12/DEADBEEF?url=FEEDDAD1", result.SessionUrl)

***REMOVED***# Test fake web mode
***REMOVED***def test_make_request_fails_when_unexpected_request_url_is_faked(self):
***REMOVED******REMOVED***self.cs.stub_request("unexpected/url.json", "clients.json")
***REMOVED******REMOVED***self.assertRaises(Exception, self.cs.clients)

***REMOVED***def test_make_request_fails_when_unexpected_request_body_is_faked(self):
***REMOVED******REMOVED***c = Client()
***REMOVED******REMOVED***c.stub_request("clients.json", "create_client.json", 201, "unexpected request body")
***REMOVED******REMOVED***self.assertRaises(Exception, c.create, "Client Company Name", "(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")

***REMOVED***# Test functionality of exceptions inheriting from CreateSendError
***REMOVED***def test_bad_request(self):
***REMOVED******REMOVED***c = Client()
***REMOVED******REMOVED***c.stub_request("clients.json", "custom_api_error.json", 400)
***REMOVED******REMOVED***try:
***REMOVED******REMOVED******REMOVED***c.create("", "", "")
***REMOVED******REMOVED***except BadRequest as br:
***REMOVED******REMOVED******REMOVED***self.assertEquals(98798, br.data.Code)
***REMOVED******REMOVED******REMOVED***self.assertEquals('A crazy API error', br.data.Message)
***REMOVED******REMOVED******REMOVED***self.assertEquals('The CreateSend API responded with the following error - 98798: A crazy API error', "%s" % br)

***REMOVED***def test_unauthorized(self):
***REMOVED******REMOVED***c = Client()
***REMOVED******REMOVED***c.stub_request("clients.json", "custom_api_error.json", 401)
***REMOVED******REMOVED***try:
***REMOVED******REMOVED******REMOVED***c.create("", "", "")
***REMOVED******REMOVED***except Unauthorized as ua:
***REMOVED******REMOVED******REMOVED***self.assertEquals(98798, ua.data.Code)
***REMOVED******REMOVED******REMOVED***self.assertEquals('A crazy API error', ua.data.Message)
***REMOVED******REMOVED******REMOVED***self.assertEquals('The CreateSend API responded with the following error - 98798: A crazy API error', "%s" % ua)

***REMOVED***# Test that the corresponding exceptions are raised according to the returned http status code
***REMOVED***def test_bad_request_on_get(self):
***REMOVED******REMOVED***self.cs.stub_request('countries.json', 'custom_api_error.json', status=400)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[400], self.cs.countries)

***REMOVED***def test_unauthorized_on_get(self):
***REMOVED******REMOVED***self.cs.stub_request('countries.json', 'custom_api_error.json', status=401)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[401], self.cs.countries)

***REMOVED***def test_not_found_on_get(self):
***REMOVED******REMOVED***self.cs.stub_request('countries.json', None, status=404)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[404], self.cs.countries)

***REMOVED***def test_other_client_error_on_get(self):
***REMOVED******REMOVED***self.cs.stub_request('countries.json', None, status=418)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[418], self.cs.countries)

***REMOVED***def test_server_error_on_get(self):
***REMOVED******REMOVED***self.cs.stub_request('countries.json', None, status=500)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[500], self.cs.countries)

***REMOVED***def test_bad_request_on_post(self):
***REMOVED******REMOVED***client = Client(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
***REMOVED******REMOVED***client.stub_request('clients.json', 'custom_api_error.json', status=400)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[400], client.create, "Client Company Name",
***REMOVED******REMOVED******REMOVED***"(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")

***REMOVED***def test_unauthorized_on_post(self):
***REMOVED******REMOVED***client = Client(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
***REMOVED******REMOVED***client.stub_request('clients.json', 'custom_api_error.json', status=401)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[401], client.create, "Client Company Name",
***REMOVED******REMOVED******REMOVED***"(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")

***REMOVED***def test_not_found_on_post(self):
***REMOVED******REMOVED***client = Client(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
***REMOVED******REMOVED***client.stub_request('clients.json', None, status=404)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[404], client.create, "Client Company Name",
***REMOVED******REMOVED******REMOVED***"(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")

***REMOVED***def test_other_client_error_on_post(self):
***REMOVED******REMOVED***client = Client(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
***REMOVED******REMOVED***client.stub_request('clients.json', None, status=418)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[418], client.create, "Client Company Name",
***REMOVED******REMOVED******REMOVED***"(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")

***REMOVED***def test_server_error_on_post(self):
***REMOVED******REMOVED***client = Client(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
***REMOVED******REMOVED***client.stub_request('clients.json', None, status=500)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[500], client.create, "Client Company Name", 
***REMOVED******REMOVED******REMOVED***"(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")

***REMOVED***def test_bad_request_on_put(self):
***REMOVED******REMOVED***template = Template(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
***REMOVED******REMOVED***template.stub_request('templates/uhiuhiuhiuhiuhiuhiuh.json', 'custom_api_error.json', status=400)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[400], template.update, "Template One Updated", "http://templates.org/index.html", 
***REMOVED******REMOVED******REMOVED***"http://templates.org/files.zip")

***REMOVED***def test_unauthorized_on_put(self):
***REMOVED******REMOVED***template = Template(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
***REMOVED******REMOVED***template.stub_request('templates/uhiuhiuhiuhiuhiuhiuh.json', 'custom_api_error.json', status=401)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[401], template.update, "Template One Updated", "http://templates.org/index.html", 
***REMOVED******REMOVED******REMOVED***"http://templates.org/files.zip")

***REMOVED***def test_not_found_on_put(self):
***REMOVED******REMOVED***template = Template(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
***REMOVED******REMOVED***template.stub_request('templates/uhiuhiuhiuhiuhiuhiuh.json', None, status=404)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[404], template.update, "Template One Updated", "http://templates.org/index.html", 
***REMOVED******REMOVED******REMOVED***"http://templates.org/files.zip")

***REMOVED***def test_other_client_error_on_put(self):
***REMOVED******REMOVED***template = Template(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
***REMOVED******REMOVED***template.stub_request('templates/uhiuhiuhiuhiuhiuhiuh.json', None, status=418)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[418], template.update, "Template One Updated", "http://templates.org/index.html", 
***REMOVED******REMOVED******REMOVED***"http://templates.org/files.zip")

***REMOVED***def test_server_error_on_put(self):
***REMOVED******REMOVED***template = Template(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
***REMOVED******REMOVED***template.stub_request('templates/uhiuhiuhiuhiuhiuhiuh.json', None, status=500)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[500], template.update, "Template One Updated", "http://templates.org/index.html", 
***REMOVED******REMOVED******REMOVED***"http://templates.org/files.zip")
***REMOVED***
***REMOVED***def test_bad_request_on_delete(self):
***REMOVED******REMOVED***template = Template(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
***REMOVED******REMOVED***template.stub_request('templates/uhiuhiuhiuhiuhiuhiuh.json', 'custom_api_error.json', status=400)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[400], template.delete)

***REMOVED***def test_unauthorized_on_delete(self):
***REMOVED******REMOVED***template = Template(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
***REMOVED******REMOVED***template.stub_request('templates/uhiuhiuhiuhiuhiuhiuh.json', 'custom_api_error.json', status=401)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[401], template.delete)

***REMOVED***def test_not_found_on_delete(self):
***REMOVED******REMOVED***template = Template(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
***REMOVED******REMOVED***template.stub_request('templates/uhiuhiuhiuhiuhiuhiuh.json', None, status=404)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[404], template.delete)

***REMOVED***def test_other_client_error_on_delete(self):
***REMOVED******REMOVED***template = Template(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
***REMOVED******REMOVED***template.stub_request('templates/uhiuhiuhiuhiuhiuhiuh.json', None, status=418)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[418], template.delete)

***REMOVED***def test_server_error_on_delete(self):
***REMOVED******REMOVED***template = Template(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
***REMOVED******REMOVED***template.stub_request('templates/uhiuhiuhiuhiuhiuhiuh.json', None, status=500)
***REMOVED******REMOVED***self.assertRaises(self.error_responses[500], template.delete)

class OAuthCreateSendTestCase(unittest.TestCase, CreateSendTestCase):
***REMOVED***"""Test when using OAuth to authenticate"""
***REMOVED***def setUp(self):
***REMOVED******REMOVED***self.cs = CreateSend({"access_token": "ASP95S4aR+9KsgfHB0dapTYxNA==", "refresh_token": "5S4aASP9R+9KsgfHB0dapTYxNA=="})
***REMOVED******REMOVED***# Mapping of http status codes to the exceptions expected to be raised
***REMOVED******REMOVED***self.error_responses = {
***REMOVED******REMOVED******REMOVED***400: BadRequest, 401: Unauthorized, 404: NotFound, 418: ClientError,
***REMOVED******REMOVED******REMOVED***500: ServerError }

class ApiKeyCreateSendTestCase(unittest.TestCase, CreateSendTestCase):
***REMOVED***"""Test when using an API key to authenticate"""
***REMOVED***def setUp(self):
***REMOVED******REMOVED***self.cs = CreateSend({'api_key': '123123123123123123123'})
***REMOVED******REMOVED***# Mapping of http status codes to the exceptions expected to be raised
***REMOVED******REMOVED***self.error_responses = {
***REMOVED******REMOVED******REMOVED***400: BadRequest, 401: Unauthorized, 404: NotFound, 418: ClientError,
***REMOVED******REMOVED******REMOVED***500: ServerError }
