import unittest

from createsend import *

class ClientTestCase(object):

  def test_create(self):
    c = Client()
    c.stub_request("clients.json", "create_client.json")
    client_id = c.create("Client Company Name", "(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")
    self.assertEquals("32a381c49a2df99f1d0c6f3c112352b9", client_id)
    self.assertEquals("32a381c49a2df99f1d0c6f3c112352b9", c.client_id)

  def test_details(self):
    self.cl.stub_request("clients/%s.json" % self.cl.client_id, "client_details.json")
    cl = self.cl.details()
    self.assertEquals(cl.ApiKey, "639d8cc27198202f5fe6037a8b17a29a59984b86d3289bc9")
    self.assertEquals(cl.BasicDetails.ClientID, "4a397ccaaa55eb4e6aa1221e1e2d7122")
    self.assertEquals(cl.BasicDetails.ContactName, "Client One (contact)")
    self.assertEquals(cl.AccessDetails.Username, "clientone")
    self.assertEquals(cl.AccessDetails.AccessLevel, 23)
    self.assertEquals(cl.BillingDetails.Credits, 500)

  def test_campaigns(self):
    self.cl.stub_request("clients/%s/campaigns.json" % self.cl.client_id, "campaigns.json")
    campaigns = self.cl.campaigns()
    self.assertEquals(len(campaigns), 2)
    self.assertEquals(campaigns[0].CampaignID, 'fc0ce7105baeaf97f47c99be31d02a91')
    self.assertEquals(campaigns[0].WebVersionURL, 'http://createsend.com/t/r-765E86829575EE2C')
    self.assertEquals(campaigns[0].WebVersionTextURL, 'http://createsend.com/t/r-765E86829575EE2C/t')
    self.assertEquals(campaigns[0].Subject, 'Campaign One')
    self.assertEquals(campaigns[0].Name, 'Campaign One')
    self.assertEquals(campaigns[0].SentDate, '2010-10-12 12:58:00')
    self.assertEquals(campaigns[0].TotalRecipients, 2245)
    self.assertEquals(campaigns[0].FromName, 'My Name')
    self.assertEquals(campaigns[0].FromEmail, 'myemail@example.com')
    self.assertEquals(campaigns[0].ReplyTo, 'myemail@example.com')

  def test_scheduled(self):
    self.cl.stub_request("clients/%s/scheduled.json" % self.cl.client_id, "scheduled_campaigns.json")
    campaigns = self.cl.scheduled()
    self.assertEquals(len(campaigns), 2)
    self.assertEquals(campaigns[0].DateScheduled, "2011-05-25 10:40:00")
    self.assertEquals(campaigns[0].ScheduledTimeZone, "(GMT+10:00) Canberra, Melbourne, Sydney")
    self.assertEquals(campaigns[0].CampaignID, "827dbbd2161ea9989fa11ad562c66937")
    self.assertEquals(campaigns[0].Name, "Magic Issue One")
    self.assertEquals(campaigns[0].Subject, "Magic Issue One")
    self.assertEquals(campaigns[0].DateCreated, "2011-05-24 10:37:00")
    self.assertEquals(campaigns[0].PreviewURL, "http://createsend.com/t/r-DD543521A87C9B8B")
    self.assertEquals(campaigns[0].PreviewTextURL, "http://createsend.com/t/r-DD543521A87C9B8B/t")
    self.assertEquals(campaigns[0].FromName, 'My Name')
    self.assertEquals(campaigns[0].FromEmail, 'myemail@example.com')
    self.assertEquals(campaigns[0].ReplyTo, 'myemail@example.com')

  def test_drafts(self):
    self.cl.stub_request("clients/%s/drafts.json" % self.cl.client_id, "drafts.json")
    drafts = self.cl.drafts()
    self.assertEquals(len(drafts), 2)
    self.assertEquals(drafts[0].CampaignID, '7c7424792065d92627139208c8c01db1')
    self.assertEquals(drafts[0].Name, 'Draft One')
    self.assertEquals(drafts[0].Subject, 'Draft One')
    self.assertEquals(drafts[0].DateCreated, '2010-08-19 16:08:00')
    self.assertEquals(drafts[0].PreviewURL, 'http://createsend.com/t/r-E97A7BB2E6983DA1')
    self.assertEquals(drafts[0].PreviewTextURL, 'http://createsend.com/t/r-E97A7BB2E6983DA1/t')
    self.assertEquals(drafts[0].FromName, 'My Name')
    self.assertEquals(drafts[0].FromEmail, 'myemail@example.com')
    self.assertEquals(drafts[0].ReplyTo, 'myemail@example.com')

  def test_lists(self):
    self.cl.stub_request("clients/%s/lists.json" % self.cl.client_id, "lists.json")
    lists = self.cl.lists()
    self.assertEquals(len(lists), 2)
    self.assertEquals(lists[0].ListID, 'a58ee1d3039b8bec838e6d1482a8a965')
    self.assertEquals(lists[0].Name, 'List One')

  def test_lists_for_email(self):
    email = "valid@example.com"
    self.cl.stub_request("clients/%s/listsforemail.json?email=%s" % (self.cl.client_id, urllib.quote(email)), "listsforemail.json")
    lists = self.cl.lists_for_email(email)
    self.assertEquals(len(lists), 2)
    self.assertEquals(lists[0].ListID, 'ab4a2b57c7c8f1ba62f898a1af1a575b')
    self.assertEquals(lists[0].ListName, 'List Number One')
    self.assertEquals(lists[0].SubscriberState, 'Active')
    self.assertEquals(lists[0].DateSubscriberAdded, '2012-08-20 22:32:00')
    
  def test_segments(self):
    self.cl.stub_request("clients/%s/segments.json" % self.cl.client_id, "segments.json")
    segments = self.cl.segments()
    self.assertEquals(len(segments), 2)
    self.assertEquals(segments[0].ListID, 'a58ee1d3039b8bec838e6d1482a8a965')
    self.assertEquals(segments[0].SegmentID, '46aa5e01fd43381863d4e42cf277d3a9')
    self.assertEquals(segments[0].Title, 'Segment One')

  def test_suppressionlist(self):
    self.cl.stub_request("clients/%s/suppressionlist.json?orderfield=email&page=1&pagesize=1000&orderdirection=asc" % self.cl.client_id, "suppressionlist.json")
    res = self.cl.suppressionlist()
    self.assertEquals(res.ResultsOrderedBy, "email")
    self.assertEquals(res.OrderDirection, "asc")
    self.assertEquals(res.PageNumber, 1)
    self.assertEquals(res.PageSize, 1000)
    self.assertEquals(res.RecordsOnThisPage, 5)
    self.assertEquals(res.TotalNumberOfRecords, 5)
    self.assertEquals(res.NumberOfPages, 1)
    self.assertEquals(len(res.Results), 5)
    self.assertEquals(res.Results[0].SuppressionReason, "Unsubscribed")
    self.assertEquals(res.Results[0].EmailAddress, "example+1@example.com")
    self.assertEquals(res.Results[0].Date, "2010-10-26 10:55:31")
    self.assertEquals(res.Results[0].State, "Suppressed")

  def test_suppress_with_single_email(self):
    self.cl.stub_request("clients/%s/suppress.json" % self.cl.client_id, None)
    self.cl.suppress("example@example.com") 

  def test_suppress_with_multiple_emails(self):
    self.cl.stub_request("clients/%s/suppress.json" % self.cl.client_id, None)
    self.cl.suppress(["one@example.com", "two@example.com"]) 

  def test_unsuppress(self):
    email = "example@example.com"
    self.cl.stub_request("clients/%s/unsuppress.json?email=%s" % (self.cl.client_id, urllib.quote(email)), None)
    res = self.cl.unsuppress(email)

  def test_templates(self):
    self.cl.stub_request("clients/%s/templates.json" % self.cl.client_id, "templates.json")
    templates = self.cl.templates()
    self.assertEquals(len(templates), 2)
    self.assertEquals(templates[0].TemplateID, '5cac213cf061dd4e008de5a82b7a3621')
    self.assertEquals(templates[0].Name, 'Template One')

  def test_set_basics(self):
    self.cl.stub_request("clients/%s/setbasics.json" % self.cl.client_id, None)
    self.cl.set_basics("Client Company Name", "(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")

  def test_set_payg_billing(self):
    self.cl.stub_request("clients/%s/setpaygbilling.json" % self.cl.client_id, None)
    self.cl.set_payg_billing("CAD", True, True, 150)

  def test_set_monthly_billing_implicit(self):
    self.cl.stub_request("clients/%s/setmonthlybilling.json" % self.cl.client_id, None, None, "{\"Currency\": \"CAD\", \"MarkupPercentage\": 150, \"ClientPays\": true}")
    self.cl.set_monthly_billing("CAD", True, 150)   

  def test_set_monthly_billing_basic(self):
    self.cl.stub_request("clients/%s/setmonthlybilling.json" % self.cl.client_id, None, None, "{\"Currency\": \"CAD\", \"MonthlyScheme\": \"Basic\", \"MarkupPercentage\": 120, \"ClientPays\": false}")
    self.cl.set_monthly_billing("CAD", False, 120, "Basic")

  def test_set_monthly_billing_unlimited(self):
    self.cl.stub_request("clients/%s/setmonthlybilling.json" % self.cl.client_id, None, None, "{\"Currency\": \"CAD\", \"MonthlyScheme\": \"Unlimited\", \"MarkupPercentage\": 100, \"ClientPays\": true}")
    self.cl.set_monthly_billing("CAD", True, 100, "Unlimited")

  def test_transfer_credits(self):
    self.cl.stub_request("clients/%s/credits.json" % self.cl.client_id, "transfer_credits.json")
    result = self.cl.transfer_credits(200, False)
    self.assertEquals(result.AccountCredits, 800)
    self.assertEquals(result.ClientCredits, 200)

  def test_people(self):
    self.cl.stub_request("clients/%s/people.json" % self.cl.client_id, "people.json")
    people = self.cl.people()
    self.assertEquals(2, len(people))
    self.assertEquals('person1@blackhole.com', people[0].EmailAddress)
    self.assertEquals('Person One', people[0].Name)
    self.assertEquals('Active', people[0].Status)  

  def test_get_primary_contact(self):
  	self.cl.stub_request("clients/%s/primarycontact.json" % self.cl.client_id, "client_get_primary_contact.json")
  	primary_contact = self.cl.get_primary_contact()
  	self.assertEquals('person@blackhole.com', primary_contact.EmailAddress)
  	
  def test_set_primary_contact(self):
    email = 'person@blackhole.com'
    self.cl.stub_request("clients/%s/primarycontact.json?email=%s" % (self.cl.client_id, urllib.quote(email, '')), 'client_set_primary_contact.json')
    result = self.cl.set_primary_contact(email)
    self.assertEquals(email, result.EmailAddress)
      
  def test_delete(self):
    self.cl.stub_request("clients/%s.json" % self.cl.client_id, None)
    self.cl.delete()

class OAuthClientTestCase(unittest.TestCase, ClientTestCase):
  """Test when using OAuth to authenticate"""
  def setUp(self):
    self.cl = Client(
      {"access_token": "ASP95S4aR+9KsgfHB0dapTYxNA==", "refresh_token": "5S4aASP9R+9KsgfHB0dapTYxNA=="}, "4a397ccaaa55eb4e6aa1221e1e2d7122")

class ApiKeyClientTestCase(unittest.TestCase, ClientTestCase):
  """Test when using an API key to authenticate"""
  def setUp(self):
    self.cl = Client(
      {'api_key': '123123123123123123123'}, "4a397ccaaa55eb4e6aa1221e1e2d7122")
