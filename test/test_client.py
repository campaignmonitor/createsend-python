import unittest

from createsend import *

class ClientTestCase(unittest.TestCase):

  def setUp(self):
    self.api_key = '123123123123123123123'
    CreateSend.api_key = self.api_key
    self.cl = Client("4a397ccaaa55eb4e6aa1221e1e2d7122")

  def test_create(self):
    self.cl.stub_request("clients.json", "create_client.json")
    client_id = self.cl.create("Client Company Name", "Client Contact Name", "client@example.com", "(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")
    self.assertEquals("32a381c49a2df99f1d0c6f3c112352b9", client_id)

  def test_details(self):
    self.cl.stub_request("clients/%s.json" % self.cl.client_id, "client_details.json")
    cl = self.cl.details()
    self.assertEquals(cl.ApiKey, "639d8cc27198202f5fe6037a8b17a29a59984b86d3289bc9")
    self.assertEquals(cl.BasicDetails.ClientID, "4a397ccaaa55eb4e6aa1221e1e2d7122")
    self.assertEquals(cl.BasicDetails.ContactName, "Client One (contact)")
    self.assertEquals(cl.AccessDetails.Username, "clientone")
    self.assertEquals(cl.AccessDetails.AccessLevel, 23)

  def test_campaigns(self):
    self.cl.stub_request("clients/%s/campaigns.json" % self.cl.client_id, "campaigns.json")
    campaigns = self.cl.campaigns()
    self.assertEquals(len(campaigns), 2)
    self.assertEquals(campaigns[0].CampaignID, 'fc0ce7105baeaf97f47c99be31d02a91')
    self.assertEquals(campaigns[0].WebVersionURL, 'http://hello.createsend.com/t/ViewEmail/r/765E86829575EE2C/C67FD2F38AC4859C/')
    self.assertEquals(campaigns[0].Subject, 'Campaign One')
    self.assertEquals(campaigns[0].Name, 'Campaign One')
    self.assertEquals(campaigns[0].SentDate, '2010-10-12 12:58:00')
    self.assertEquals(campaigns[0].TotalRecipients, 2245)

  def test_drafts(self):
    self.cl.stub_request("clients/%s/drafts.json" % self.cl.client_id, "drafts.json")
    drafts = self.cl.drafts()
    self.assertEquals(len(drafts), 2)
    self.assertEquals(drafts[0].CampaignID, '7c7424792065d92627139208c8c01db1')
    self.assertEquals(drafts[0].Name, 'Draft One')
    self.assertEquals(drafts[0].Subject, 'Draft One')
    self.assertEquals(drafts[0].DateCreated, '2010-08-19 16:08:00')
    self.assertEquals(drafts[0].PreviewURL, 'http://hello.createsend.com/t/ViewEmail/r/E97A7BB2E6983DA1/C67FD2F38AC4859C/')

  def test_lists(self):
    self.cl.stub_request("clients/%s/lists.json" % self.cl.client_id, "lists.json")
    lists = self.cl.lists()
    self.assertEquals(len(lists), 2)
    self.assertEquals(lists[0].ListID, 'a58ee1d3039b8bec838e6d1482a8a965')
    self.assertEquals(lists[0].Name, 'List One')
    
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

  def test_templates(self):
    self.cl.stub_request("clients/%s/templates.json" % self.cl.client_id, "templates.json")
    templates = self.cl.templates()
    self.assertEquals(len(templates), 2)
    self.assertEquals(templates[0].TemplateID, '5cac213cf061dd4e008de5a82b7a3621')
    self.assertEquals(templates[0].Name, 'Template One')

  def test_set_basics(self):
    self.cl.stub_request("clients/%s/setbasics.json" % self.cl.client_id, None)
    self.cl.set_basics("Client Company Name", "Client Contact Name", "client@example.com", "(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")

  def test_set_access(self):
    self.cl.stub_request("clients/%s/setaccess.json" % self.cl.client_id, None)
    self.cl.set_access("username", "password", 321)

  def test_set_payg_billing(self):
    self.cl.stub_request("clients/%s/setpaygbilling.json" % self.cl.client_id, None)
    self.cl.set_payg_billing("CAD", True, True, 150)

  def test_set_monthly_billing(self):
    self.cl.stub_request("clients/%s/setmonthlybilling.json" % self.cl.client_id, None)
    self.cl.set_monthly_billing("CAD", True, 150)

  def test_delete(self):
    self.cl.stub_request("clients/%s.json" % self.cl.client_id, None)
    self.cl.delete()
