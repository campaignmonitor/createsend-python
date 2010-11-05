import unittest

from createsend import Campaign

class CampaignTestCase(unittest.TestCase):

***REMOVED***def setUp(self):
***REMOVED******REMOVED***self.campaign_id = ""
***REMOVED******REMOVED***self.campaign = Campaign(self.campaign_id)

***REMOVED***def test_create(self):
***REMOVED******REMOVED***client_id = '87y8d7qyw8d7yq8w7ydwqwd'
***REMOVED******REMOVED***self.campaign.stub_request("create_campaign.json")
***REMOVED******REMOVED***campaign_id = self.campaign.create(client_id, "subject", "name", "g'day", "good.day@example.com", "good.day@example.com", 
***REMOVED******REMOVED******REMOVED***"http://example.com/campaign.html", "http://example.com/campaign.txt", [ '7y12989e82ue98u2e', 'dh9w89q8w98wudwd989' ],
***REMOVED******REMOVED******REMOVED***[ 'y78q9w8d9w8ud9q8uw', 'djw98quw9duqw98uwd98' ])
***REMOVED******REMOVED***self.assertEquals(campaign_id, "787y87y87y87y87y87y87")

***REMOVED***def test_sendpreview(self):
***REMOVED******REMOVED***self.campaign.stub_request(None)
***REMOVED******REMOVED***self.campaign.send_preview([ "test+89898u9@example.com", "test+787y8y7y8@example.com" ], "random")

***REMOVED***def test_send(self):
***REMOVED******REMOVED***self.campaign.stub_request(None)
***REMOVED******REMOVED***self.campaign.send("confirmation@example.com")

***REMOVED***def test_delete(self):
***REMOVED******REMOVED***self.campaign.stub_request(None)
***REMOVED******REMOVED***self.campaign.delete()
***REMOVED***
***REMOVED***def test_summary(self):
***REMOVED******REMOVED***self.campaign.stub_request("campaign_summary.json")
***REMOVED******REMOVED***summary = self.campaign.summary()
***REMOVED******REMOVED***self.assertEquals(summary.Recipients, 5)
***REMOVED******REMOVED***self.assertEquals(summary.TotalOpened, 10)
***REMOVED******REMOVED***self.assertEquals(summary.Clicks, 0)
***REMOVED******REMOVED***self.assertEquals(summary.Unsubscribed, 0)
***REMOVED******REMOVED***self.assertEquals(summary.Bounced, 0)
***REMOVED******REMOVED***self.assertEquals(summary.UniqueOpened, 5)
***REMOVED******REMOVED***self.assertEquals(summary.WebVersionURL, "http://clientone.createsend.com/t/ViewEmail/r/3A433FC72FFE3B8B/C67FD2F38AC4859C/")

***REMOVED***def test_lists(self):
***REMOVED******REMOVED***self.campaign.stub_request("campaign_lists.json")
***REMOVED******REMOVED***lists = self.campaign.lists()
***REMOVED******REMOVED***self.assertEquals(len(lists), 2)
***REMOVED******REMOVED***self.assertEquals(lists[0].Name, "List One")
***REMOVED******REMOVED***self.assertEquals(lists[0].ListID, "a58ee1d3039b8bec838e6d1482a8a965")

***REMOVED***# TODO: Add this test once segments has been implemented
***REMOVED***# def test_segments(self):
***REMOVED***#***REMOVED*** pass

***REMOVED***def test_recipients(self):
***REMOVED******REMOVED***self.campaign.stub_request("campaign_recipients.json")
***REMOVED******REMOVED***res = self.campaign.recipients(page=1, page_size=20)
***REMOVED******REMOVED***self.assertEquals(res.ResultsOrderedBy, "email")
***REMOVED******REMOVED***self.assertEquals(res.OrderDirection, "asc")
***REMOVED******REMOVED***self.assertEquals(res.PageNumber, 1)
***REMOVED******REMOVED***self.assertEquals(res.PageSize, 20)
***REMOVED******REMOVED***self.assertEquals(res.RecordsOnThisPage, 20)
***REMOVED******REMOVED***self.assertEquals(res.TotalNumberOfRecords, 2200)
***REMOVED******REMOVED***self.assertEquals(res.NumberOfPages, 110)
***REMOVED******REMOVED***self.assertEquals(len(res.Results), 20)
***REMOVED******REMOVED***self.assertEquals(res.Results[0].EmailAddress, "subs+6g76t7t0@example.com")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].ListID, "a994a3caf1328a16af9a69a730eaa706")
***REMOVED***
***REMOVED***def test_opens(self):
***REMOVED******REMOVED***min_date = "2010-01-01"
***REMOVED******REMOVED***self.campaign.stub_request("campaign_opens.json")
***REMOVED******REMOVED***opens = self.campaign.opens(min_date)
***REMOVED******REMOVED***self.assertEquals(len(opens), 5)
***REMOVED******REMOVED***self.assertEquals(opens[0].EmailAddress, "subs+6576576576@example.com")
***REMOVED******REMOVED***self.assertEquals(opens[0].ListID, "512a3bc577a58fdf689c654329b50fa0")
***REMOVED******REMOVED***self.assertEquals(opens[0].Date, "2010-10-11 08:29:00")
***REMOVED******REMOVED***self.assertEquals(opens[0].IPAddress, "192.168.126.87")

***REMOVED***def test_clicks(self):
***REMOVED******REMOVED***min_date = "2010-01-01"
***REMOVED******REMOVED***self.campaign.stub_request("campaign_clicks.json")
***REMOVED******REMOVED***clicks = self.campaign.clicks(min_date)
***REMOVED******REMOVED***self.assertEquals(len(clicks), 3)
***REMOVED******REMOVED***self.assertEquals(clicks[0].EmailAddress, "subs+6576576576@example.com")
***REMOVED******REMOVED***self.assertEquals(clicks[0].URL, "http://video.google.com.au/?hl=en&tab=wv")
***REMOVED******REMOVED***self.assertEquals(clicks[0].ListID, "512a3bc577a58fdf689c654329b50fa0")
***REMOVED******REMOVED***self.assertEquals(clicks[0].Date, "2010-10-11 08:29:00")
***REMOVED******REMOVED***self.assertEquals(clicks[0].IPAddress, "192.168.126.87")

***REMOVED***def test_unsubscribes(self):
***REMOVED******REMOVED***min_date = "2010-01-01"
***REMOVED******REMOVED***self.campaign.stub_request("campaign_unsubscribes.json")
***REMOVED******REMOVED***unsubscribes = self.campaign.unsubscribes(min_date)
***REMOVED******REMOVED***self.assertEquals(len(unsubscribes), 1)
***REMOVED******REMOVED***self.assertEquals(unsubscribes[0].EmailAddress, "subs+6576576576@example.com")
***REMOVED******REMOVED***self.assertEquals(unsubscribes[0].ListID, "512a3bc577a58fdf689c654329b50fa0")
***REMOVED******REMOVED***self.assertEquals(unsubscribes[0].Date, "2010-10-11 08:29:00")
***REMOVED******REMOVED***self.assertEquals(unsubscribes[0].IPAddress, "192.168.126.87")

***REMOVED***def test_bounces(self):
***REMOVED******REMOVED***self.campaign.stub_request("campaign_bounces.json")
***REMOVED******REMOVED***bounces = self.campaign.bounces()
***REMOVED******REMOVED***self.assertEquals(len(bounces), 2)
***REMOVED******REMOVED***self.assertEquals(bounces[0].EmailAddress, "asdf@softbouncemyemail.com")
***REMOVED******REMOVED***self.assertEquals(bounces[0].ListID, "654523a5855b4a440bae3fb295641546")
***REMOVED******REMOVED***self.assertEquals(bounces[0].BounceType, "Soft")
***REMOVED******REMOVED***self.assertEquals(bounces[0].Date, "2010-07-02 16:46:00")
***REMOVED******REMOVED***self.assertEquals(bounces[0].Reason, "Bounce - But No Email Address Returned ")
