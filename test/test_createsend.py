from six.moves.urllib.parse import quote, urlparse
import unittest

from createsend import *

class CreateSendTestCase(object):
  """CreateSend tests to be run in the context of both using an API key 
  and using OAuth."""

  def test_that_default_user_agent_is_set(self):
    self.cs.stub_request("clients.json", "clients.json")
    cl = self.cs.clients()
    self.assertEquals(self.cs.headers['User-Agent'], CreateSend.default_user_agent)
    self.assertEquals(2, len(cl))

  def test_that_custom_user_agent_can_be_set(self):
    CreateSend.user_agent = "custom user agent"
    self.cs.stub_request("clients.json", "clients.json")
    cl = self.cs.clients()
    self.assertEquals(self.cs.headers['User-Agent'], "custom user agent")
    self.assertEquals(2, len(cl))
    CreateSend.user_agent = CreateSend.default_user_agent

  def test_clients(self):
    self.cs.stub_request("clients.json", "clients.json")
    cl = self.cs.clients()
    self.assertEquals(2, len(cl))
    self.assertEquals("4a397ccaaa55eb4e6aa1221e1e2d7122", cl[0].ClientID)
    self.assertEquals("Client One", cl[0].Name)

  def test_billing_details(self):
    self.cs.stub_request("billingdetails.json", "billingdetails.json")
    bd = self.cs.billing_details()
    self.assertEquals(3021, bd.Credits)

  def test_countries(self):
    self.cs.stub_request("countries.json", "countries.json")
    countries = self.cs.countries()
    self.assertEquals(245, len(countries))
    self.assertEquals("Australia", countries[11])

  def test_systemdate(self):
    self.cs.stub_request("systemdate.json", "systemdate.json")
    systemdate = self.cs.systemdate()
    self.assertEquals(systemdate, "2010-10-15 09:27:00")
    
  def test_timezones(self):
    self.cs.stub_request("timezones.json", "timezones.json")
    timezones = self.cs.timezones()
    self.assertEquals(97, len(timezones))
    self.assertEquals("(GMT+12:00) Fiji", timezones[61])
    
  def test_administrators(self):
  	self.cs.stub_request("admins.json", "administrators.json")
  	administrators = self.cs.administrators()
  	self.assertEquals(2, len(administrators))
  	self.assertEquals('admin1@blackhole.com', administrators[0].EmailAddress)
  	self.assertEquals('Admin One', administrators[0].Name)
  	self.assertEquals('Active', administrators[0].Status)  

  def test_get_primary_contact(self):
  	self.cs.stub_request("primarycontact.json", "admin_get_primary_contact.json")
  	primary_contact = self.cs.get_primary_contact()
  	self.assertEquals('admin@blackhole.com', primary_contact.EmailAddress)
  	
  def test_set_primary_contact(self):
    email = 'admin@blackhole.com'
    self.cs.stub_request('primarycontact.json?email=%s' % quote(email, ''), 'admin_set_primary_contact.json')
    result = self.cs.set_primary_contact(email)
    self.assertEquals(email, result.EmailAddress)

  def test_external_session_url(self):
    email = "exammple@example.com"
    chrome = "None"
    url = "/subscribers"
    integrator_id = "qw989q8wud98qwyd"
    client_id = "9q8uw9d8u9wud"
    self.cs.stub_request('externalsession.json', 'external_session.json')
    result = self.cs.external_session_url(email, chrome, url, integrator_id, client_id)
    self.assertEquals("https://external1.createsend.com/cd/create/ABCDEF12/DEADBEEF?url=FEEDDAD1", result.SessionUrl)

  # Test fake web mode
  def test_make_request_fails_when_unexpected_request_url_is_faked(self):
    self.cs.stub_request("unexpected/url.json", "clients.json")
    self.assertRaises(Exception, self.cs.clients)

  def test_make_request_fails_when_unexpected_request_body_is_faked(self):
    c = Client()
    c.stub_request("clients.json", "create_client.json", 201, "unexpected request body")
    self.assertRaises(Exception, c.create, "Client Company Name", "(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")

  # Test functionality of exceptions inheriting from CreateSendError
  def test_bad_request(self):
    c = Client()
    c.stub_request("clients.json", "custom_api_error.json", 400)
    try:
      c.create("", "", "")
    except BadRequest as br:
      self.assertEquals(98798, br.data.Code)
      self.assertEquals('A crazy API error', br.data.Message)
      self.assertEquals('The CreateSend API responded with the following error - 98798: A crazy API error', "%s" % br)

  def test_unauthorized(self):
    c = Client()
    c.stub_request("clients.json", "custom_api_error.json", 401)
    try:
      c.create("", "", "")
    except Unauthorized as ua:
      self.assertEquals(98798, ua.data.Code)
      self.assertEquals('A crazy API error', ua.data.Message)
      self.assertEquals('The CreateSend API responded with the following error - 98798: A crazy API error', "%s" % ua)

  # Test that the corresponding exceptions are raised according to the returned http status code
  def test_bad_request_on_get(self):
    self.cs.stub_request('countries.json', 'custom_api_error.json', status=400)
    self.assertRaises(self.error_responses[400], self.cs.countries)

  def test_unauthorized_on_get(self):
    self.cs.stub_request('countries.json', 'custom_api_error.json', status=401)
    self.assertRaises(self.error_responses[401], self.cs.countries)

  def test_not_found_on_get(self):
    self.cs.stub_request('countries.json', None, status=404)
    self.assertRaises(self.error_responses[404], self.cs.countries)

  def test_other_client_error_on_get(self):
    self.cs.stub_request('countries.json', None, status=418)
    self.assertRaises(self.error_responses[418], self.cs.countries)

  def test_server_error_on_get(self):
    self.cs.stub_request('countries.json', None, status=500)
    self.assertRaises(self.error_responses[500], self.cs.countries)

  def test_bad_request_on_post(self):
    client = Client(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
    client.stub_request('clients.json', 'custom_api_error.json', status=400)
    self.assertRaises(self.error_responses[400], client.create, "Client Company Name",
      "(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")

  def test_unauthorized_on_post(self):
    client = Client(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
    client.stub_request('clients.json', 'custom_api_error.json', status=401)
    self.assertRaises(self.error_responses[401], client.create, "Client Company Name",
      "(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")

  def test_not_found_on_post(self):
    client = Client(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
    client.stub_request('clients.json', None, status=404)
    self.assertRaises(self.error_responses[404], client.create, "Client Company Name",
      "(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")

  def test_other_client_error_on_post(self):
    client = Client(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
    client.stub_request('clients.json', None, status=418)
    self.assertRaises(self.error_responses[418], client.create, "Client Company Name",
      "(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")

  def test_server_error_on_post(self):
    client = Client(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
    client.stub_request('clients.json', None, status=500)
    self.assertRaises(self.error_responses[500], client.create, "Client Company Name", 
      "(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")

  def test_bad_request_on_put(self):
    template = Template(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
    template.stub_request('templates/uhiuhiuhiuhiuhiuhiuh.json', 'custom_api_error.json', status=400)
    self.assertRaises(self.error_responses[400], template.update, "Template One Updated", "http://templates.org/index.html", 
      "http://templates.org/files.zip")

  def test_unauthorized_on_put(self):
    template = Template(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
    template.stub_request('templates/uhiuhiuhiuhiuhiuhiuh.json', 'custom_api_error.json', status=401)
    self.assertRaises(self.error_responses[401], template.update, "Template One Updated", "http://templates.org/index.html", 
      "http://templates.org/files.zip")

  def test_not_found_on_put(self):
    template = Template(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
    template.stub_request('templates/uhiuhiuhiuhiuhiuhiuh.json', None, status=404)
    self.assertRaises(self.error_responses[404], template.update, "Template One Updated", "http://templates.org/index.html", 
      "http://templates.org/files.zip")

  def test_other_client_error_on_put(self):
    template = Template(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
    template.stub_request('templates/uhiuhiuhiuhiuhiuhiuh.json', None, status=418)
    self.assertRaises(self.error_responses[418], template.update, "Template One Updated", "http://templates.org/index.html", 
      "http://templates.org/files.zip")

  def test_server_error_on_put(self):
    template = Template(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
    template.stub_request('templates/uhiuhiuhiuhiuhiuhiuh.json', None, status=500)
    self.assertRaises(self.error_responses[500], template.update, "Template One Updated", "http://templates.org/index.html", 
      "http://templates.org/files.zip")
  
  def test_bad_request_on_delete(self):
    template = Template(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
    template.stub_request('templates/uhiuhiuhiuhiuhiuhiuh.json', 'custom_api_error.json', status=400)
    self.assertRaises(self.error_responses[400], template.delete)

  def test_unauthorized_on_delete(self):
    template = Template(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
    template.stub_request('templates/uhiuhiuhiuhiuhiuhiuh.json', 'custom_api_error.json', status=401)
    self.assertRaises(self.error_responses[401], template.delete)

  def test_not_found_on_delete(self):
    template = Template(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
    template.stub_request('templates/uhiuhiuhiuhiuhiuhiuh.json', None, status=404)
    self.assertRaises(self.error_responses[404], template.delete)

  def test_other_client_error_on_delete(self):
    template = Template(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
    template.stub_request('templates/uhiuhiuhiuhiuhiuhiuh.json', None, status=418)
    self.assertRaises(self.error_responses[418], template.delete)

  def test_server_error_on_delete(self):
    template = Template(self.cs.auth_details, "uhiuhiuhiuhiuhiuhiuh")
    template.stub_request('templates/uhiuhiuhiuhiuhiuhiuh.json', None, status=500)
    self.assertRaises(self.error_responses[500], template.delete)

class OAuthCreateSendTestCase(unittest.TestCase, CreateSendTestCase):
  """Test when using OAuth to authenticate"""
  def setUp(self):
    self.cs = CreateSend({"access_token": "ASP95S4aR+9KsgfHB0dapTYxNA==", "refresh_token": "5S4aASP9R+9KsgfHB0dapTYxNA=="})
    # Mapping of http status codes to the exceptions expected to be raised
    self.error_responses = {
      400: BadRequest, 401: Unauthorized, 404: NotFound, 418: ClientError,
      500: ServerError }

class ApiKeyCreateSendTestCase(unittest.TestCase, CreateSendTestCase):
  """Test when using an API key to authenticate"""
  def setUp(self):
    self.cs = CreateSend({'api_key': '123123123123123123123'})
    # Mapping of http status codes to the exceptions expected to be raised
    self.error_responses = {
      400: BadRequest, 401: Unauthorized, 404: NotFound, 418: ClientError,
      500: ServerError }
