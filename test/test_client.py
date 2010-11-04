import unittest

from createsend import Client

class ClientTestCase(unittest.TestCase):

***REMOVED***def setUp(self):
***REMOVED******REMOVED***self.cl = Client()

***REMOVED***def test_create(self):
***REMOVED******REMOVED***self.cl.stub_request("create_client.json")
***REMOVED******REMOVED***client_id = self.cl.create("Client Company Name", "Client Contact Name", "client@example.com", "(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")
***REMOVED******REMOVED***self.assertEquals("32a381c49a2df99f1d0c6f3c112352b9", client_id)

***REMOVED***def test_details(self):
***REMOVED******REMOVED***self.cl.stub_request("client_details.json")
***REMOVED******REMOVED***cl = self.cl.details()
***REMOVED******REMOVED***self.assertEquals(cl.BasicDetails.ClientID, "4a397ccaaa55eb4e6aa1221e1e2d7122")
***REMOVED******REMOVED***self.assertEquals(cl.BasicDetails.ContactName, "Client One (contact)")
***REMOVED******REMOVED***self.assertEquals(cl.AccessDetails.Username, "clientone")
***REMOVED******REMOVED***self.assertEquals(cl.AccessDetails.AccessLevel, 23)
***REMOVED***
***REMOVED***def test_campaigns(self):
***REMOVED******REMOVED***self.cl.stub_request("campaigns.json")
***REMOVED******REMOVED***campaigns = self.cl.campaigns()
***REMOVED******REMOVED***self.assertEquals(len(campaigns), 2)
***REMOVED******REMOVED***self.assertEquals(campaigns[0].CampaignID, 'fc0ce7105baeaf97f47c99be31d02a91')
***REMOVED******REMOVED***self.assertEquals(campaigns[0].WebVersionURL, 'http://hello.createsend.com/t/ViewEmail/r/765E86829575EE2C/C67FD2F38AC4859C/')
***REMOVED******REMOVED***self.assertEquals(campaigns[0].Subject, 'Campaign One')
***REMOVED******REMOVED***self.assertEquals(campaigns[0].Name, 'Campaign One')
***REMOVED******REMOVED***self.assertEquals(campaigns[0].SentDate, '2010-10-12 12:58:00')
***REMOVED******REMOVED***self.assertEquals(campaigns[0].TotalRecipients, 2245)

***REMOVED***def test_drafts(self):
***REMOVED******REMOVED***self.cl.stub_request("drafts.json")
***REMOVED******REMOVED***drafts = self.cl.drafts()
***REMOVED******REMOVED***self.assertEquals(len(drafts), 2)
***REMOVED******REMOVED***self.assertEquals(drafts[0].CampaignID, '7c7424792065d92627139208c8c01db1')
***REMOVED******REMOVED***self.assertEquals(drafts[0].Name, 'Draft One')
***REMOVED******REMOVED***self.assertEquals(drafts[0].Subject, 'Draft One')
***REMOVED******REMOVED***self.assertEquals(drafts[0].DateCreated, '2010-08-19 16:08:00')
***REMOVED******REMOVED***self.assertEquals(drafts[0].PreviewURL, 'http://hello.createsend.com/t/ViewEmail/r/E97A7BB2E6983DA1/C67FD2F38AC4859C/')

***REMOVED***def test_lists(self):
***REMOVED******REMOVED***self.cl.stub_request("lists.json")
***REMOVED******REMOVED***lists = self.cl.lists()
***REMOVED******REMOVED***self.assertEquals(len(lists), 2)
***REMOVED******REMOVED***self.assertEquals(lists[0].ListID, 'a58ee1d3039b8bec838e6d1482a8a965')
***REMOVED******REMOVED***self.assertEquals(lists[0].Name, 'List One')
***REMOVED******REMOVED***
***REMOVED***def test_segments(self):
***REMOVED******REMOVED***self.cl.stub_request("segments.json")
***REMOVED******REMOVED***segments = self.cl.lists()
***REMOVED******REMOVED***self.assertEquals(len(segments), 2)
***REMOVED******REMOVED***self.assertEquals(segments[0].ListID, 'a58ee1d3039b8bec838e6d1482a8a965')
***REMOVED******REMOVED***self.assertEquals(segments[0].SegmentID, '46aa5e01fd43381863d4e42cf277d3a9')
***REMOVED******REMOVED***self.assertEquals(segments[0].Title, 'Segment One')

***REMOVED***def test_suppressionlist(self):
***REMOVED******REMOVED***self.cl.stub_request("suppressionlist.json")
***REMOVED******REMOVED***res = self.cl.suppressionlist()
***REMOVED******REMOVED***self.assertEquals(res.ResultsOrderedBy, "email")
***REMOVED******REMOVED***self.assertEquals(res.OrderDirection, "asc")
***REMOVED******REMOVED***self.assertEquals(res.PageNumber, 1)
***REMOVED******REMOVED***self.assertEquals(res.PageSize, 1000)
***REMOVED******REMOVED***self.assertEquals(res.RecordsOnThisPage, 5)
***REMOVED******REMOVED***self.assertEquals(res.TotalNumberOfRecords, 5)
***REMOVED******REMOVED***self.assertEquals(res.NumberOfPages, 1)
***REMOVED******REMOVED***self.assertEquals(len(res.Results), 5)
***REMOVED******REMOVED***self.assertEquals(res.Results[0].EmailAddress, "example+1@example.com")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].Date, "2010-10-26 10:55:31")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].State, "Suppressed")

***REMOVED***def test_templates(self):
***REMOVED******REMOVED***self.cl.stub_request("templates.json")
***REMOVED******REMOVED***templates = self.cl.templates()
***REMOVED******REMOVED***self.assertEquals(len(templates), 2)
***REMOVED******REMOVED***self.assertEquals(templates[0].TemplateID, '5cac213cf061dd4e008de5a82b7a3621')
***REMOVED******REMOVED***self.assertEquals(templates[0].Name, 'Template One')

***REMOVED***def test_set_basics(self):
***REMOVED******REMOVED***self.cl.stub_request(None)
***REMOVED******REMOVED***self.cl.set_basics("Client Company Name", "Client Contact Name", "client@example.com", "(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")

***REMOVED***def test_set_access(self):
***REMOVED******REMOVED***self.cl.stub_request(None)
***REMOVED******REMOVED***self.cl.set_access("username", "password", 321)

***REMOVED***def test_set_payg_billing(self):
***REMOVED******REMOVED***self.cl.stub_request(None)
***REMOVED******REMOVED***self.cl.set_payg_billing("CAD", True, True, 150)

***REMOVED***def test_set_monthly_billing(self):
***REMOVED******REMOVED***self.cl.stub_request(None)
***REMOVED******REMOVED***self.cl.set_monthly_billing("CAD", True, True, 150)

***REMOVED***def test_delete(self):
***REMOVED******REMOVED***self.cl.stub_request(None)
***REMOVED******REMOVED***self.cl.delete()
