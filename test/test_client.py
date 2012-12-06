import unittest

***REMOVED***

class ClientTestCase(unittest.TestCase):

***REMOVED***def setUp(self):
***REMOVED******REMOVED***self.api_key = '123123123123123123123'
***REMOVED******REMOVED***CreateSend.api_key = self.api_key
***REMOVED******REMOVED***self.cl = Client("4a397ccaaa55eb4e6aa1221e1e2d7122")

***REMOVED***def test_create(self):
***REMOVED******REMOVED***self.cl.stub_request("clients.json", "create_client.json")
***REMOVED******REMOVED***client_id = self.cl.create("Client Company Name", "(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")
***REMOVED******REMOVED***self.assertEquals("32a381c49a2df99f1d0c6f3c112352b9", client_id)

***REMOVED***def test_details(self):
***REMOVED******REMOVED***self.cl.stub_request("clients/%s.json" % self.cl.client_id, "client_details.json")
***REMOVED******REMOVED***cl = self.cl.details()
***REMOVED******REMOVED***self.assertEquals(cl.ApiKey, "639d8cc27198202f5fe6037a8b17a29a59984b86d3289bc9")
***REMOVED******REMOVED***self.assertEquals(cl.BasicDetails.ClientID, "4a397ccaaa55eb4e6aa1221e1e2d7122")
***REMOVED******REMOVED***self.assertEquals(cl.BasicDetails.ContactName, "Client One (contact)")
***REMOVED******REMOVED***self.assertEquals(cl.AccessDetails.Username, "clientone")
***REMOVED******REMOVED***self.assertEquals(cl.AccessDetails.AccessLevel, 23)
***REMOVED******REMOVED***self.assertEquals(cl.BillingDetails.Credits, 500)

***REMOVED***def test_campaigns(self):
***REMOVED******REMOVED***self.cl.stub_request("clients/%s/campaigns.json" % self.cl.client_id, "campaigns.json")
***REMOVED******REMOVED***campaigns = self.cl.campaigns()
***REMOVED******REMOVED***self.assertEquals(len(campaigns), 2)
***REMOVED******REMOVED***self.assertEquals(campaigns[0].CampaignID, 'fc0ce7105baeaf97f47c99be31d02a91')
***REMOVED******REMOVED***self.assertEquals(campaigns[0].WebVersionURL, 'http://createsend.com/t/r-765E86829575EE2C')
***REMOVED******REMOVED***self.assertEquals(campaigns[0].WebVersionTextURL, 'http://createsend.com/t/r-765E86829575EE2C/t')
***REMOVED******REMOVED***self.assertEquals(campaigns[0].Subject, 'Campaign One')
***REMOVED******REMOVED***self.assertEquals(campaigns[0].Name, 'Campaign One')
***REMOVED******REMOVED***self.assertEquals(campaigns[0].SentDate, '2010-10-12 12:58:00')
***REMOVED******REMOVED***self.assertEquals(campaigns[0].TotalRecipients, 2245)
***REMOVED******REMOVED***self.assertEquals(campaigns[0].FromName, 'My Name')
***REMOVED******REMOVED***self.assertEquals(campaigns[0].FromEmail, 'myemail@example.com')
***REMOVED******REMOVED***self.assertEquals(campaigns[0].ReplyTo, 'myemail@example.com')

***REMOVED***def test_scheduled(self):
***REMOVED******REMOVED***self.cl.stub_request("clients/%s/scheduled.json" % self.cl.client_id, "scheduled_campaigns.json")
***REMOVED******REMOVED***campaigns = self.cl.scheduled()
***REMOVED******REMOVED***self.assertEquals(len(campaigns), 2)
***REMOVED******REMOVED***self.assertEquals(campaigns[0].DateScheduled, "2011-05-25 10:40:00")
***REMOVED******REMOVED***self.assertEquals(campaigns[0].ScheduledTimeZone, "(GMT+10:00) Canberra, Melbourne, Sydney")
***REMOVED******REMOVED***self.assertEquals(campaigns[0].CampaignID, "827dbbd2161ea9989fa11ad562c66937")
***REMOVED******REMOVED***self.assertEquals(campaigns[0].Name, "Magic Issue One")
***REMOVED******REMOVED***self.assertEquals(campaigns[0].Subject, "Magic Issue One")
***REMOVED******REMOVED***self.assertEquals(campaigns[0].DateCreated, "2011-05-24 10:37:00")
***REMOVED******REMOVED***self.assertEquals(campaigns[0].PreviewURL, "http://createsend.com/t/r-DD543521A87C9B8B")
***REMOVED******REMOVED***self.assertEquals(campaigns[0].PreviewTextURL, "http://createsend.com/t/r-DD543521A87C9B8B/t")
***REMOVED******REMOVED***self.assertEquals(campaigns[0].FromName, 'My Name')
***REMOVED******REMOVED***self.assertEquals(campaigns[0].FromEmail, 'myemail@example.com')
***REMOVED******REMOVED***self.assertEquals(campaigns[0].ReplyTo, 'myemail@example.com')

***REMOVED***def test_drafts(self):
***REMOVED******REMOVED***self.cl.stub_request("clients/%s/drafts.json" % self.cl.client_id, "drafts.json")
***REMOVED******REMOVED***drafts = self.cl.drafts()
***REMOVED******REMOVED***self.assertEquals(len(drafts), 2)
***REMOVED******REMOVED***self.assertEquals(drafts[0].CampaignID, '7c7424792065d92627139208c8c01db1')
***REMOVED******REMOVED***self.assertEquals(drafts[0].Name, 'Draft One')
***REMOVED******REMOVED***self.assertEquals(drafts[0].Subject, 'Draft One')
***REMOVED******REMOVED***self.assertEquals(drafts[0].DateCreated, '2010-08-19 16:08:00')
***REMOVED******REMOVED***self.assertEquals(drafts[0].PreviewURL, 'http://createsend.com/t/r-E97A7BB2E6983DA1')
***REMOVED******REMOVED***self.assertEquals(drafts[0].PreviewTextURL, 'http://createsend.com/t/r-E97A7BB2E6983DA1/t')
***REMOVED******REMOVED***self.assertEquals(drafts[0].FromName, 'My Name')
***REMOVED******REMOVED***self.assertEquals(drafts[0].FromEmail, 'myemail@example.com')
***REMOVED******REMOVED***self.assertEquals(drafts[0].ReplyTo, 'myemail@example.com')

***REMOVED***def test_lists(self):
***REMOVED******REMOVED***self.cl.stub_request("clients/%s/lists.json" % self.cl.client_id, "lists.json")
***REMOVED******REMOVED***lists = self.cl.lists()
***REMOVED******REMOVED***self.assertEquals(len(lists), 2)
***REMOVED******REMOVED***self.assertEquals(lists[0].ListID, 'a58ee1d3039b8bec838e6d1482a8a965')
***REMOVED******REMOVED***self.assertEquals(lists[0].Name, 'List One')

***REMOVED***def test_lists_for_email(self):
***REMOVED******REMOVED***email = "valid@example.com"
***REMOVED******REMOVED***self.cl.stub_request("clients/%s/listsforemail.json?email=%s" % (self.cl.client_id, urllib.quote(email)), "listsforemail.json")
***REMOVED******REMOVED***lists = self.cl.lists_for_email(email)
***REMOVED******REMOVED***self.assertEquals(len(lists), 2)
***REMOVED******REMOVED***self.assertEquals(lists[0].ListID, 'ab4a2b57c7c8f1ba62f898a1af1a575b')
***REMOVED******REMOVED***self.assertEquals(lists[0].ListName, 'List Number One')
***REMOVED******REMOVED***self.assertEquals(lists[0].SubscriberState, 'Active')
***REMOVED******REMOVED***self.assertEquals(lists[0].DateSubscriberAdded, '2012-08-20 22:32:00')
***REMOVED******REMOVED***
***REMOVED***def test_segments(self):
***REMOVED******REMOVED***self.cl.stub_request("clients/%s/segments.json" % self.cl.client_id, "segments.json")
***REMOVED******REMOVED***segments = self.cl.segments()
***REMOVED******REMOVED***self.assertEquals(len(segments), 2)
***REMOVED******REMOVED***self.assertEquals(segments[0].ListID, 'a58ee1d3039b8bec838e6d1482a8a965')
***REMOVED******REMOVED***self.assertEquals(segments[0].SegmentID, '46aa5e01fd43381863d4e42cf277d3a9')
***REMOVED******REMOVED***self.assertEquals(segments[0].Title, 'Segment One')

***REMOVED***def test_suppressionlist(self):
***REMOVED******REMOVED***self.cl.stub_request("clients/%s/suppressionlist.json?orderfield=email&page=1&pagesize=1000&orderdirection=asc" % self.cl.client_id, "suppressionlist.json")
***REMOVED******REMOVED***res = self.cl.suppressionlist()
***REMOVED******REMOVED***self.assertEquals(res.ResultsOrderedBy, "email")
***REMOVED******REMOVED***self.assertEquals(res.OrderDirection, "asc")
***REMOVED******REMOVED***self.assertEquals(res.PageNumber, 1)
***REMOVED******REMOVED***self.assertEquals(res.PageSize, 1000)
***REMOVED******REMOVED***self.assertEquals(res.RecordsOnThisPage, 5)
***REMOVED******REMOVED***self.assertEquals(res.TotalNumberOfRecords, 5)
***REMOVED******REMOVED***self.assertEquals(res.NumberOfPages, 1)
***REMOVED******REMOVED***self.assertEquals(len(res.Results), 5)
***REMOVED******REMOVED***self.assertEquals(res.Results[0].SuppressionReason, "Unsubscribed")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].EmailAddress, "example+1@example.com")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].Date, "2010-10-26 10:55:31")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].State, "Suppressed")

***REMOVED***def test_suppress_with_single_email(self):
***REMOVED******REMOVED***self.cl.stub_request("clients/%s/suppress.json" % self.cl.client_id, None)
***REMOVED******REMOVED***self.cl.suppress("example@example.com") 

***REMOVED***def test_suppress_with_multiple_emails(self):
***REMOVED******REMOVED***self.cl.stub_request("clients/%s/suppress.json" % self.cl.client_id, None)
***REMOVED******REMOVED***self.cl.suppress(["one@example.com", "two@example.com"]) 

***REMOVED***def test_unsuppress(self):
***REMOVED******REMOVED***email = "example@example.com"
***REMOVED******REMOVED***self.cl.stub_request("clients/%s/unsuppress.json?email=%s" % (self.cl.client_id, urllib.quote(email)), None)
***REMOVED******REMOVED***res = self.cl.unsuppress(email)

***REMOVED***def test_templates(self):
***REMOVED******REMOVED***self.cl.stub_request("clients/%s/templates.json" % self.cl.client_id, "templates.json")
***REMOVED******REMOVED***templates = self.cl.templates()
***REMOVED******REMOVED***self.assertEquals(len(templates), 2)
***REMOVED******REMOVED***self.assertEquals(templates[0].TemplateID, '5cac213cf061dd4e008de5a82b7a3621')
***REMOVED******REMOVED***self.assertEquals(templates[0].Name, 'Template One')

***REMOVED***def test_set_basics(self):
***REMOVED******REMOVED***self.cl.stub_request("clients/%s/setbasics.json" % self.cl.client_id, None)
***REMOVED******REMOVED***self.cl.set_basics("Client Company Name", "(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")

***REMOVED***def test_set_payg_billing(self):
***REMOVED******REMOVED***self.cl.stub_request("clients/%s/setpaygbilling.json" % self.cl.client_id, None)
***REMOVED******REMOVED***self.cl.set_payg_billing("CAD", True, True, 150)

***REMOVED***def test_set_monthly_billing_implicit(self):
***REMOVED******REMOVED***self.cl.stub_request("clients/%s/setmonthlybilling.json" % self.cl.client_id, None, None, "{\"Currency\": \"CAD\", \"MarkupPercentage\": 150, \"ClientPays\": true}")
***REMOVED******REMOVED***self.cl.set_monthly_billing("CAD", True, 150)***REMOVED*** 

***REMOVED***def test_set_monthly_billing_basic(self):
***REMOVED******REMOVED***self.cl.stub_request("clients/%s/setmonthlybilling.json" % self.cl.client_id, None, None, "{\"Currency\": \"CAD\", \"MonthlyScheme\": \"Basic\", \"MarkupPercentage\": 120, \"ClientPays\": false}")
***REMOVED******REMOVED***self.cl.set_monthly_billing("CAD", False, 120, "Basic")

***REMOVED***def test_set_monthly_billing_unlimited(self):
***REMOVED******REMOVED***self.cl.stub_request("clients/%s/setmonthlybilling.json" % self.cl.client_id, None, None, "{\"Currency\": \"CAD\", \"MonthlyScheme\": \"Unlimited\", \"MarkupPercentage\": 100, \"ClientPays\": true}")
***REMOVED******REMOVED***self.cl.set_monthly_billing("CAD", True, 100, "Unlimited")

***REMOVED***def test_transfer_credits(self):
***REMOVED******REMOVED***self.cl.stub_request("clients/%s/credits.json" % self.cl.client_id, "transfer_credits.json")
***REMOVED******REMOVED***result = self.cl.transfer_credits(200, False)
***REMOVED******REMOVED***self.assertEquals(result.AccountCredits, 800)
***REMOVED******REMOVED***self.assertEquals(result.ClientCredits, 200)

***REMOVED***def test_people(self):
***REMOVED******REMOVED***self.cl.stub_request("clients/%s/people.json" % self.cl.client_id, "people.json")
***REMOVED******REMOVED***people = self.cl.people()
***REMOVED******REMOVED***self.assertEquals(2, len(people))
***REMOVED******REMOVED***self.assertEquals('person1@blackhole.com', people[0].EmailAddress)
***REMOVED******REMOVED***self.assertEquals('Person One', people[0].Name)
***REMOVED******REMOVED***self.assertEquals('Active', people[0].Status)***REMOVED***

***REMOVED***def test_get_primary_contact(self):
***REMOVED***	self.cl.stub_request("clients/%s/primarycontact.json" % self.cl.client_id, "client_get_primary_contact.json")
***REMOVED***	primary_contact = self.cl.get_primary_contact()
***REMOVED***	self.assertEquals('person@blackhole.com', primary_contact.EmailAddress)
***REMOVED***	
***REMOVED***def test_set_primary_contact(self):
***REMOVED******REMOVED***email = 'person@blackhole.com'
***REMOVED******REMOVED***self.cl.stub_request("clients/%s/primarycontact.json?email=%s" % (self.cl.client_id, urllib.quote(email, '')), 'client_set_primary_contact.json')
***REMOVED******REMOVED***result = self.cl.set_primary_contact(email)
***REMOVED******REMOVED***self.assertEquals(email, result.EmailAddress)
***REMOVED******REMOVED******REMOVED***
***REMOVED***def test_delete(self):
***REMOVED******REMOVED***self.cl.stub_request("clients/%s.json" % self.cl.client_id, None)
***REMOVED******REMOVED***self.cl.delete()
