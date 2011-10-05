import unittest
import urllib

from createsend import *

class CampaignTestCase(unittest.TestCase):

  def setUp(self):
    self.api_key = '123123123123123123123'
    CreateSend.api_key = self.api_key
    self.campaign_id = "787y87y87y87y87y87y87"
    self.campaign = Campaign(self.campaign_id)

  def test_create(self):
    client_id = '87y8d7qyw8d7yq8w7ydwqwd'
    self.campaign.stub_request("campaigns/%s.json" % client_id, "create_campaign.json")
    campaign_id = self.campaign.create(client_id, "subject", "name", "g'day", "good.day@example.com", "good.day@example.com", 
      "http://example.com/campaign.html", "http://example.com/campaign.txt", [ '7y12989e82ue98u2e', 'dh9w89q8w98wudwd989' ],
      [ 'y78q9w8d9w8ud9q8uw', 'djw98quw9duqw98uwd98' ])
    self.assertEquals(campaign_id, "787y87y87y87y87y87y87")

  def test_sendpreview(self):
    self.campaign.stub_request("campaigns/%s/sendpreview.json" % self.campaign_id, None)
    self.campaign.send_preview([ "test+89898u9@example.com", "test+787y8y7y8@example.com" ], "random")

  def test_send(self):
    self.campaign.stub_request("campaigns/%s/send.json" % self.campaign_id, None)
    self.campaign.send("confirmation@example.com")

  def test_unschedule(self):
    self.campaign.stub_request("campaigns/%s/unschedule.json" % self.campaign_id, None)
    self.campaign.unschedule()

  def test_delete(self):
    self.campaign.stub_request("campaigns/%s.json" % self.campaign_id, None)
    self.campaign.delete()
  
  def test_summary(self):
    self.campaign.stub_request("campaigns/%s/summary.json" % self.campaign_id, "campaign_summary.json")
    summary = self.campaign.summary()
    self.assertEquals(summary.Recipients, 5)
    self.assertEquals(summary.TotalOpened, 10)
    self.assertEquals(summary.Clicks, 0)
    self.assertEquals(summary.Unsubscribed, 0)
    self.assertEquals(summary.Bounced, 0)
    self.assertEquals(summary.UniqueOpened, 5)
    self.assertEquals(summary.TwitterTweets, 23)
    self.assertEquals(summary.ForwardToAFriends, 11)
    self.assertEquals(summary.FacebookLikes, 32)
    self.assertEquals(summary.WebVersionURL, "http://createsend.com/t/r-3A433FC72FFE3B8B")

  def test_lists_and_segments(self):
    self.campaign.stub_request("campaigns/%s/listsandsegments.json" % self.campaign_id, "campaign_listsandsegments.json")
    ls = self.campaign.lists_and_segments()
    self.assertEquals(len(ls.Lists), 1)
    self.assertEquals(len(ls.Segments), 1)
    self.assertEquals(ls.Lists[0].Name, "List One")
    self.assertEquals(ls.Lists[0].ListID, "a58ee1d3039b8bec838e6d1482a8a965")
    self.assertEquals(ls.Segments[0].Title, "Segment for campaign")
    self.assertEquals(ls.Segments[0].ListID, "2bea949d0bf96148c3e6a209d2e82060")
    self.assertEquals(ls.Segments[0].SegmentID, "dba84a225d5ce3d19105d7257baac46f")

  def test_recipients(self):
    self.campaign.stub_request("campaigns/%s/recipients.json?orderfield=email&page=1&pagesize=20&orderdirection=asc" % self.campaign_id, "campaign_recipients.json")
    res = self.campaign.recipients(page=1, page_size=20)
    self.assertEquals(res.ResultsOrderedBy, "email")
    self.assertEquals(res.OrderDirection, "asc")
    self.assertEquals(res.PageNumber, 1)
    self.assertEquals(res.PageSize, 20)
    self.assertEquals(res.RecordsOnThisPage, 20)
    self.assertEquals(res.TotalNumberOfRecords, 2200)
    self.assertEquals(res.NumberOfPages, 110)
    self.assertEquals(len(res.Results), 20)
    self.assertEquals(res.Results[0].EmailAddress, "subs+6g76t7t0@example.com")
    self.assertEquals(res.Results[0].ListID, "a994a3caf1328a16af9a69a730eaa706")

  def test_opens(self):
    min_date = "2010-01-01"
    self.campaign.stub_request("campaigns/%s/opens.json?date=%s&orderfield=date&page=1&pagesize=1000&orderdirection=asc" % (self.campaign_id, urllib.quote(min_date, '')), "campaign_opens.json")
    opens = self.campaign.opens(min_date)
    self.assertEquals(len(opens.Results), 5)
    self.assertEquals(opens.Results[0].EmailAddress, "subs+6576576576@example.com")
    self.assertEquals(opens.Results[0].ListID, "512a3bc577a58fdf689c654329b50fa0")
    self.assertEquals(opens.Results[0].Date, "2010-10-11 08:29:00")
    self.assertEquals(opens.Results[0].IPAddress, "192.168.126.87")
    self.assertEquals(opens.ResultsOrderedBy, "date")
    self.assertEquals(opens.OrderDirection, "asc")
    self.assertEquals(opens.PageNumber, 1)
    self.assertEquals(opens.PageSize, 1000)
    self.assertEquals(opens.RecordsOnThisPage, 5)
    self.assertEquals(opens.TotalNumberOfRecords, 5)
    self.assertEquals(opens.NumberOfPages, 1)

  def test_clicks(self):
    min_date = "2010-01-01"
    self.campaign.stub_request("campaigns/%s/clicks.json?date=%s&orderfield=date&page=1&pagesize=1000&orderdirection=asc" % (self.campaign_id, urllib.quote(min_date, '')), "campaign_clicks.json")
    clicks = self.campaign.clicks(min_date)
    self.assertEquals(len(clicks.Results), 3)
    self.assertEquals(clicks.Results[0].EmailAddress, "subs+6576576576@example.com")
    self.assertEquals(clicks.Results[0].URL, "http://video.google.com.au/?hl=en&tab=wv")
    self.assertEquals(clicks.Results[0].ListID, "512a3bc577a58fdf689c654329b50fa0")
    self.assertEquals(clicks.Results[0].Date, "2010-10-11 08:29:00")
    self.assertEquals(clicks.Results[0].IPAddress, "192.168.126.87")
    self.assertEquals(clicks.ResultsOrderedBy, "date")
    self.assertEquals(clicks.OrderDirection, "asc")
    self.assertEquals(clicks.PageNumber, 1)
    self.assertEquals(clicks.PageSize, 1000)
    self.assertEquals(clicks.RecordsOnThisPage, 3)
    self.assertEquals(clicks.TotalNumberOfRecords, 3)
    self.assertEquals(clicks.NumberOfPages, 1)

  def test_unsubscribes(self):
    min_date = "2010-01-01"
    self.campaign.stub_request("campaigns/%s/unsubscribes.json?date=%s&orderfield=date&page=1&pagesize=1000&orderdirection=asc" % (self.campaign_id, urllib.quote(min_date, '')), "campaign_unsubscribes.json")
    unsubscribes = self.campaign.unsubscribes(min_date)
    self.assertEquals(len(unsubscribes.Results), 1)
    self.assertEquals(unsubscribes.Results[0].EmailAddress, "subs+6576576576@example.com")
    self.assertEquals(unsubscribes.Results[0].ListID, "512a3bc577a58fdf689c654329b50fa0")
    self.assertEquals(unsubscribes.Results[0].Date, "2010-10-11 08:29:00")
    self.assertEquals(unsubscribes.Results[0].IPAddress, "192.168.126.87")
    self.assertEquals(unsubscribes.ResultsOrderedBy, "date")
    self.assertEquals(unsubscribes.OrderDirection, "asc")
    self.assertEquals(unsubscribes.PageNumber, 1)
    self.assertEquals(unsubscribes.PageSize, 1000)
    self.assertEquals(unsubscribes.RecordsOnThisPage, 1)
    self.assertEquals(unsubscribes.TotalNumberOfRecords, 1)
    self.assertEquals(unsubscribes.NumberOfPages, 1)

  def test_bounces(self):
    min_date = "2010-01-01"
    self.campaign.stub_request("campaigns/%s/bounces.json?date=%s&orderfield=date&page=1&pagesize=1000&orderdirection=asc" % (self.campaign_id, urllib.quote(min_date, '')), "campaign_bounces.json")
    bounces = self.campaign.bounces(min_date)
    self.assertEquals(len(bounces.Results), 2)
    self.assertEquals(bounces.Results[0].EmailAddress, "asdf@softbouncemyemail.com")
    self.assertEquals(bounces.Results[0].ListID, "654523a5855b4a440bae3fb295641546")
    self.assertEquals(bounces.Results[0].BounceType, "Soft")
    self.assertEquals(bounces.Results[0].Date, "2010-07-02 16:46:00")
    self.assertEquals(bounces.Results[0].Reason, "Bounce - But No Email Address Returned ")
    self.assertEquals(bounces.ResultsOrderedBy, "date")
    self.assertEquals(bounces.OrderDirection, "asc")
    self.assertEquals(bounces.PageNumber, 1)
    self.assertEquals(bounces.PageSize, 1000)
    self.assertEquals(bounces.RecordsOnThisPage, 2)
    self.assertEquals(bounces.TotalNumberOfRecords, 2)
    self.assertEquals(bounces.NumberOfPages, 1)
