from urllib.parse import quote
import unittest

from createsend.client import Client


class ClientTestCase:

***REMOVED******REMOVED***def test_create(self):
***REMOVED******REMOVED******REMOVED******REMOVED***c = Client()
***REMOVED******REMOVED******REMOVED******REMOVED***c.stub_request("clients.json", "create_client.json")
***REMOVED******REMOVED******REMOVED******REMOVED***client_id = c.create(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Client Company Name", "(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual("32a381c49a2df99f1d0c6f3c112352b9", client_id)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual("32a381c49a2df99f1d0c6f3c112352b9", c.client_id)

***REMOVED******REMOVED***def test_details(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.stub_request("clients/%s.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.cl.client_id, "client_details.json")
***REMOVED******REMOVED******REMOVED******REMOVED***cl = self.cl.details()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***cl.ApiKey, "639d8cc27198202f5fe6037a8b17a29a59984b86d3289bc9")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(cl.BasicDetails.ClientID,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"4a397ccaaa55eb4e6aa1221e1e2d7122")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(cl.BasicDetails.ContactName, "Client One (contact)")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(cl.AccessDetails.Username, "clientone")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(cl.AccessDetails.AccessLevel, 23)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(cl.BillingDetails.Credits, 500)

***REMOVED******REMOVED***def test_campaigns(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.stub_request("clients/%s/campaigns.json?sentfromdate=&senttodate=&page=1&tags=&pagesize=1000&orderdirection=desc" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.cl.client_id, "campaigns.json")
***REMOVED******REMOVED******REMOVED******REMOVED***sentCampaigns = self.cl.campaigns()
***REMOVED******REMOVED******REMOVED******REMOVED***campaigns = sentCampaigns.Results
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(campaigns), 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(campaigns[0].CampaignID,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***'fc0ce7105baeaf97f47c99be31d02a91')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(campaigns[0].WebVersionURL,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***'http://createsend.com/t/r-765E86829575EE2C')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(campaigns[0].WebVersionTextURL,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***'http://createsend.com/t/r-765E86829575EE2C/t')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(campaigns[0].Subject, 'Campaign One')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(campaigns[0].Name, 'Campaign One')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(campaigns[0].SentDate, '2010-10-12 12:58:00')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(campaigns[0].TotalRecipients, 2245)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(campaigns[0].FromName, 'My Name')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(campaigns[0].FromEmail, 'myemail@example.com')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(campaigns[0].ReplyTo, 'myemail@example.com')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(campaigns[0].Tags, ["Tag1", "Tag2"])
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(sentCampaigns.ResultsOrderedBy, "SentDate")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(sentCampaigns.OrderDirection, "desc")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(sentCampaigns.PageNumber, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(sentCampaigns.PageSize, 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(sentCampaigns.RecordsOnThisPage, 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(sentCampaigns.TotalNumberOfRecords, 49)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(sentCampaigns.NumberOfPages, 25)

***REMOVED******REMOVED***def test_scheduled(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.stub_request("clients/%s/scheduled.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.cl.client_id, "scheduled_campaigns.json")
***REMOVED******REMOVED******REMOVED******REMOVED***campaigns = self.cl.scheduled()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(campaigns), 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(campaigns[0].DateScheduled, "2011-05-25 10:40:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(campaigns[0].ScheduledTimeZone,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"(GMT+10:00) Canberra, Melbourne, Sydney")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(campaigns[0].CampaignID,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"827dbbd2161ea9989fa11ad562c66937")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(campaigns[0].Name, "Magic Issue One")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(campaigns[0].Subject, "Magic Issue One")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(campaigns[0].DateCreated, "2011-05-24 10:37:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(campaigns[0].PreviewURL,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"http://createsend.com/t/r-DD543521A87C9B8B")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(campaigns[0].PreviewTextURL,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"http://createsend.com/t/r-DD543521A87C9B8B/t")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(campaigns[0].FromName, 'My Name')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(campaigns[0].FromEmail, 'myemail@example.com')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(campaigns[0].ReplyTo, 'myemail@example.com')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(campaigns[0].Tags, [])

***REMOVED******REMOVED***def test_drafts(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.stub_request("clients/%s/drafts.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.cl.client_id, "drafts.json")
***REMOVED******REMOVED******REMOVED******REMOVED***drafts = self.cl.drafts()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(drafts), 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(drafts[0].CampaignID,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***'7c7424792065d92627139208c8c01db1')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(drafts[0].Name, 'Draft One')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(drafts[0].Subject, 'Draft One')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(drafts[0].DateCreated, '2010-08-19 16:08:00')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(drafts[0].PreviewURL,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***'http://createsend.com/t/r-E97A7BB2E6983DA1')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(drafts[0].PreviewTextURL,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***'http://createsend.com/t/r-E97A7BB2E6983DA1/t')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(drafts[0].FromName, 'My Name')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(drafts[0].FromEmail, 'myemail@example.com')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(drafts[0].ReplyTo, 'myemail@example.com')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(drafts[0].Tags, ["Tags5"])
***REMOVED******REMOVED***
***REMOVED******REMOVED***def test_tags(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.stub_request("clients/%s/tags.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.cl.client_id, "tags.json")
***REMOVED******REMOVED******REMOVED******REMOVED***tags = self.cl.tags()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(tags), 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(tags[0].Name, 'Happy')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(tags[0].NumberOfCampaigns, 3)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(tags[1].Name, 'Sad')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(tags[1].NumberOfCampaigns, 1)

***REMOVED******REMOVED***def test_lists(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.stub_request("clients/%s/lists.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.cl.client_id, "lists.json")
***REMOVED******REMOVED******REMOVED******REMOVED***lists = self.cl.lists()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(lists), 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(lists[0].ListID, 'a58ee1d3039b8bec838e6d1482a8a965')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(lists[0].Name, 'List One')

***REMOVED******REMOVED***def test_lists_for_email(self):
***REMOVED******REMOVED******REMOVED******REMOVED***email = "valid@example.com"
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.stub_request("clients/%s/listsforemail.json?email=%s" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.cl.client_id, quote(email)), "listsforemail.json")
***REMOVED******REMOVED******REMOVED******REMOVED***lists = self.cl.lists_for_email(email)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(lists), 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(lists[0].ListID, 'ab4a2b57c7c8f1ba62f898a1af1a575b')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(lists[0].ListName, 'List Number One')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(lists[0].SubscriberState, 'Active')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(lists[0].DateSubscriberAdded, '2012-08-20 22:32:00')

***REMOVED******REMOVED***def test_segments(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.stub_request("clients/%s/segments.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.cl.client_id, "segments.json")
***REMOVED******REMOVED******REMOVED******REMOVED***segments = self.cl.segments()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(segments), 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(segments[0].ListID,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***'a58ee1d3039b8bec838e6d1482a8a965')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(segments[0].SegmentID,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***'46aa5e01fd43381863d4e42cf277d3a9')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(segments[0].Title, 'Segment One')

***REMOVED******REMOVED***def test_suppressionlist(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.stub_request("clients/%s/suppressionlist.json?orderfield=email&page=1&pagesize=1000&orderdirection=asc" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.cl.client_id, "suppressionlist.json")
***REMOVED******REMOVED******REMOVED******REMOVED***res = self.cl.suppressionlist()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(res.ResultsOrderedBy, "email")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(res.OrderDirection, "asc")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(res.PageNumber, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(res.PageSize, 1000)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(res.RecordsOnThisPage, 5)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(res.TotalNumberOfRecords, 5)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(res.NumberOfPages, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(res.Results), 5)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(res.Results[0].SuppressionReason, "Unsubscribed")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(res.Results[0].EmailAddress, "example+1@example.com")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(res.Results[0].Date, "2010-10-26 10:55:31")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(res.Results[0].State, "Suppressed")

***REMOVED******REMOVED***def test_suppress_with_single_email(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.stub_request("clients/%s/suppress.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.cl.client_id, None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.suppress("example@example.com")

***REMOVED******REMOVED***def test_suppress_with_multiple_emails(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.stub_request("clients/%s/suppress.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.cl.client_id, None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.suppress(["one@example.com", "two@example.com"])

***REMOVED******REMOVED***def test_unsuppress(self):
***REMOVED******REMOVED******REMOVED******REMOVED***email = "example@example.com"
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.stub_request("clients/%s/unsuppress.json?email=%s" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.cl.client_id, quote(email)), None)
***REMOVED******REMOVED******REMOVED******REMOVED***res = self.cl.unsuppress(email)

***REMOVED******REMOVED***def test_templates(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.stub_request("clients/%s/templates.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.cl.client_id, "templates.json")
***REMOVED******REMOVED******REMOVED******REMOVED***templates = self.cl.templates()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(templates), 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(templates[0].TemplateID,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***'5cac213cf061dd4e008de5a82b7a3621')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(templates[0].Name, 'Template One')

***REMOVED******REMOVED***def test_set_basics(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.stub_request("clients/%s/setbasics.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.cl.client_id, None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.set_basics(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Client Company Name", "(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")

***REMOVED******REMOVED***def test_set_payg_billing(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.stub_request("clients/%s/setpaygbilling.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.cl.client_id, None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.set_payg_billing("CAD", True, True, 150)

***REMOVED******REMOVED***def test_set_monthly_billing_implicit(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.stub_request("clients/%s/setmonthlybilling.json" % self.cl.client_id, None,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** None, "{\"Currency\": \"CAD\", \"MarkupPercentage\": 150, \"ClientPays\": true}")
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.set_monthly_billing("CAD", True, 150)

***REMOVED******REMOVED***def test_set_monthly_billing_basic(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.stub_request("clients/%s/setmonthlybilling.json" % self.cl.client_id, None, None,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** "{\"Currency\": \"CAD\", \"MonthlyScheme\": \"Basic\", \"MarkupPercentage\": 120, \"ClientPays\": false}")
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.set_monthly_billing("CAD", False, 120, "Basic")

***REMOVED******REMOVED***def test_set_monthly_billing_unlimited(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.stub_request("clients/%s/setmonthlybilling.json" % self.cl.client_id, None, None,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** "{\"Currency\": \"CAD\", \"MonthlyScheme\": \"Unlimited\", \"MarkupPercentage\": 100, \"ClientPays\": true}")
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.set_monthly_billing("CAD", True, 100, "Unlimited")

***REMOVED******REMOVED***def test_transfer_credits(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.stub_request("clients/%s/credits.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.cl.client_id, "transfer_credits.json")
***REMOVED******REMOVED******REMOVED******REMOVED***result = self.cl.transfer_credits(200, False)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(result.AccountCredits, 800)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(result.ClientCredits, 200)

***REMOVED******REMOVED***def test_people(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.stub_request("clients/%s/people.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.cl.client_id, "people.json")
***REMOVED******REMOVED******REMOVED******REMOVED***people = self.cl.people()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(2, len(people))
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual('person1@blackhole.com', people[0].EmailAddress)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual('Person One', people[0].Name)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual('Active', people[0].Status)

***REMOVED******REMOVED***def test_get_primary_contact(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.stub_request("clients/%s/primarycontact.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.cl.client_id, "client_get_primary_contact.json")
***REMOVED******REMOVED******REMOVED******REMOVED***primary_contact = self.cl.get_primary_contact()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual('person@blackhole.com', primary_contact.EmailAddress)

***REMOVED******REMOVED***def test_set_primary_contact(self):
***REMOVED******REMOVED******REMOVED******REMOVED***email = 'person@blackhole.com'
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.stub_request("clients/%s/primarycontact.json?email=%s" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.cl.client_id, quote(email, '')), 'client_set_primary_contact.json')
***REMOVED******REMOVED******REMOVED******REMOVED***result = self.cl.set_primary_contact(email)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(email, result.EmailAddress)

***REMOVED******REMOVED***def test_delete(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.stub_request("clients/%s.json" % self.cl.client_id, None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.delete()

***REMOVED******REMOVED***def test_journeys(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl.stub_request("clients/%s/journeys.json" % self.cl.client_id, "client_journeys.json")
***REMOVED******REMOVED******REMOVED******REMOVED***journeys = self.cl.journeys()
***REMOVED******REMOVED******REMOVED******REMOVED***journey_one = journeys[0]
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(journey_one.JourneyID, "b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(journey_one.ListID, "a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(journey_one.Name, "Journey 1")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(journey_one.Status, "Active")


class OAuthClientTestCase(unittest.TestCase, ClientTestCase):
***REMOVED******REMOVED***"""Test when using OAuth to authenticate"""

***REMOVED******REMOVED***def setUp(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl = Client(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{"access_token": "ASP95S4aR+9KsgfHB0dapTYxNA==", "refresh_token": "5S4aASP9R+9KsgfHB0dapTYxNA=="}, "4a397ccaaa55eb4e6aa1221e1e2d7122")


class ApiKeyClientTestCase(unittest.TestCase, ClientTestCase):
***REMOVED******REMOVED***"""Test when using an API key to authenticate"""

***REMOVED******REMOVED***def setUp(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.cl = Client(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{'api_key': '123123123123123123123'}, "4a397ccaaa55eb4e6aa1221e1e2d7122")
