from six.moves.urllib.parse import quote
import unittest

from createsend.campaign import Campaign


class CampaignTestCase(object):

***REMOVED******REMOVED***def test_create(self):
***REMOVED******REMOVED******REMOVED******REMOVED***client_id = '87y8d7qyw8d7yq8w7ydwqwd'
***REMOVED******REMOVED******REMOVED******REMOVED***c = Campaign()
***REMOVED******REMOVED******REMOVED******REMOVED***c.stub_request("campaigns/%s.json" % client_id, "create_campaign.json")
***REMOVED******REMOVED******REMOVED******REMOVED***campaign_id = c.create(client_id, "subject", "name", "g'day", "good.day@example.com", "good.day@example.com",
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** "http://example.com/campaign.html", "http://example.com/campaign.txt", [
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** '7y12989e82ue98u2e', 'dh9w89q8w98wudwd989'],
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** ['y78q9w8d9w8ud9q8uw', 'djw98quw9duqw98uwd98'])

***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"\"TextUrl\": \"http://example.com/campaign.txt\"" in c.faker.actual_body, True)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(c.campaign_id, "787y87y87y87y87y87y8712341234")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(campaign_id, "787y87y87y87y87y87y8712341234")

***REMOVED******REMOVED***def test_create_with_none_text_url(self):
***REMOVED******REMOVED******REMOVED******REMOVED***client_id = '87y8d7qyw8d7yq8w7ydwqwd'
***REMOVED******REMOVED******REMOVED******REMOVED***c = Campaign()
***REMOVED******REMOVED******REMOVED******REMOVED***c.stub_request("campaigns/%s.json" % client_id, "create_campaign.json")
***REMOVED******REMOVED******REMOVED******REMOVED***campaign_id = c.create(client_id, "subject", "name", "g'day", "good.day@example.com", "good.day@example.com",
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** "http://example.com/campaign.html", None, [
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** '7y12989e82ue98u2e', 'dh9w89q8w98wudwd989'],
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** ['y78q9w8d9w8ud9q8uw', 'djw98quw9duqw98uwd98'])

***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual("\"TextUrl\": null" in c.faker.actual_body, True)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(c.campaign_id, "787y87y87y87y87y87y8712341234")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(campaign_id, "787y87y87y87y87y87y8712341234")

***REMOVED******REMOVED***def test_create_from_template(self):
***REMOVED******REMOVED******REMOVED******REMOVED***template_content = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Singlelines": [
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Content": "This is a heading",
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Href": "http://example.com/"
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***}
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***],
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Multilines": [
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Content": "<p>This is example</p><p>multiline <a href=\"http://example.com\">content</a>...</p>"
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***}
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***],
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Images": [
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Content": "http://example.com/image.png",
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Alt": "This is alt text for an image",
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Href": "http://example.com/"
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***}
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***],
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Repeaters": [
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Items": [
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Layout": "My layout",
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Singlelines": [
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Content": "This is a repeater heading",
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Href": "http://example.com/"
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***}
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***],
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Multilines": [
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Content": "<p>This is example</p><p>multiline <a href=\"http://example.com\">content</a>...</p>"
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***}
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***],
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Images": [
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Content": "http://example.com/repeater-image.png",
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Alt": "This is alt text for a repeater image",
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Href": "http://example.com/"
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***}
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***]
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***}
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***]
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***}
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***]
***REMOVED******REMOVED******REMOVED******REMOVED***}

***REMOVED******REMOVED******REMOVED******REMOVED***# template_content as defined above would be used to fill the content of
***REMOVED******REMOVED******REMOVED******REMOVED***# a template with markup similar to the following:
***REMOVED******REMOVED******REMOVED******REMOVED***#
***REMOVED******REMOVED******REMOVED******REMOVED***# <html>
***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED*** <head><title>My Template</title></head>
***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED*** <body>
***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED******REMOVED*** <p><singleline>Enter heading...</singleline></p>
***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED******REMOVED*** <div><multiline>Enter description...</multiline></div>
***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED******REMOVED*** <img id="header-image" editable="true" width="500" />
***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED******REMOVED*** <repeater>
***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED******REMOVED******REMOVED*** <layout label="My layout">
***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED******REMOVED******REMOVED******REMOVED*** <div class="repeater-item">
***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** <p><singleline></singleline></p>
***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** <div><multiline></multiline></div>
***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** <img editable="true" width="500" />
***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED******REMOVED******REMOVED******REMOVED*** </div>
***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED******REMOVED******REMOVED*** </layout>
***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED******REMOVED*** </repeater>
***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED******REMOVED*** <p><unsubscribe>Unsubscribe</unsubscribe></p>
***REMOVED******REMOVED******REMOVED******REMOVED***#***REMOVED*** </body>
***REMOVED******REMOVED******REMOVED******REMOVED***# </html>

***REMOVED******REMOVED******REMOVED******REMOVED***client_id = '87y8d7qyw8d7yq8w7ydwqwd'
***REMOVED******REMOVED******REMOVED******REMOVED***c = Campaign()
***REMOVED******REMOVED******REMOVED******REMOVED***c.stub_request("campaigns/%s/fromtemplate.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** client_id, "create_campaign.json")
***REMOVED******REMOVED******REMOVED******REMOVED***campaign_id = c.create_from_template(client_id, "subject", "name", "g'day", "good.day@example.com", "good.day@example.com",
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** ['7y12989e82ue98u2e', 'dh9w89q8w98wudwd989'], [
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** 'y78q9w8d9w8ud9q8uw', 'djw98quw9duqw98uwd98'],
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** "7j8uw98udowy12989e8298u2e", template_content)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(c.campaign_id, "787y87y87y87y87y87y8712341234")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(campaign_id, "787y87y87y87y87y87y8712341234")

***REMOVED******REMOVED***def test_send_preview_with_single_recipient(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.campaign.stub_request(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"campaigns/%s/sendpreview.json" % self.campaign_id, None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.campaign.send_preview("test+89898u9@example.com", "random")

***REMOVED******REMOVED***def test_send_preview_with_multiple_recipients(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.campaign.stub_request(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"campaigns/%s/sendpreview.json" % self.campaign_id, None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.campaign.send_preview(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***["test+89898u9@example.com", "test+787y8y7y8@example.com"], "random")

***REMOVED******REMOVED***def test_send(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.campaign.stub_request(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"campaigns/%s/send.json" % self.campaign_id, None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.campaign.send("confirmation@example.com")

***REMOVED******REMOVED***def test_unschedule(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.campaign.stub_request(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"campaigns/%s/unschedule.json" % self.campaign_id, None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.campaign.unschedule()

***REMOVED******REMOVED***def test_delete(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.campaign.stub_request("campaigns/%s.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.campaign_id, None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.campaign.delete()

***REMOVED******REMOVED***def test_summary(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.campaign.stub_request(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"campaigns/%s/summary.json" % self.campaign_id, "campaign_summary.json")
***REMOVED******REMOVED******REMOVED******REMOVED***summary = self.campaign.summary()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(summary.Name, "Last Campaign")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(summary.Recipients, 5)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(summary.TotalOpened, 10)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(summary.Clicks, 0)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(summary.Unsubscribed, 0)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(summary.Bounced, 0)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(summary.UniqueOpened, 5)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(summary.Mentions, 23)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(summary.Forwards, 11)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(summary.Likes, 32)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(summary.WebVersionURL,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"http://createsend.com/t/r-3A433FC72FFE3B8B")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(summary.WebVersionTextURL,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"http://createsend.com/t/r-3A433FC72FFE3B8B/t")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***summary.WorldviewURL, "http://client.createsend.com/reports/wv/r/3A433FC72FFE3B8B")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(summary.SpamComplaints, 23)

***REMOVED******REMOVED***def test_email_client_usage(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.campaign.stub_request(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"campaigns/%s/emailclientusage.json" % self.campaign_id, "email_client_usage.json")
***REMOVED******REMOVED******REMOVED******REMOVED***ecu = self.campaign.email_client_usage()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(ecu), 6)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(ecu[0].Client, "iOS Devices")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(ecu[0].Version, "iPhone")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(ecu[0].Percentage, 19.83)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(ecu[0].Subscribers, 7056)

***REMOVED******REMOVED***def test_lists_and_segments(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.campaign.stub_request("campaigns/%s/listsandsegments.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.campaign_id, "campaign_listsandsegments.json")
***REMOVED******REMOVED******REMOVED******REMOVED***ls = self.campaign.lists_and_segments()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(ls.Lists), 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(ls.Segments), 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(ls.Lists[0].Name, "List One")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(ls.Lists[0].ListID,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"a58ee1d3039b8bec838e6d1482a8a965")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(ls.Segments[0].Title, "Segment for campaign")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(ls.Segments[0].ListID,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"2bea949d0bf96148c3e6a209d2e82060")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(ls.Segments[0].SegmentID,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"dba84a225d5ce3d19105d7257baac46f")

***REMOVED******REMOVED***def test_recipients(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.campaign.stub_request("campaigns/%s/recipients.json?orderfield=email&page=1&pagesize=20&orderdirection=asc" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.campaign_id, "campaign_recipients.json")
***REMOVED******REMOVED******REMOVED******REMOVED***res = self.campaign.recipients(page=1, page_size=20)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(res.ResultsOrderedBy, "email")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(res.OrderDirection, "asc")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(res.PageNumber, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(res.PageSize, 20)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(res.RecordsOnThisPage, 20)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(res.TotalNumberOfRecords, 2200)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(res.NumberOfPages, 110)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(res.Results), 20)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(res.Results[0].EmailAddress,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"subs+6g76t7t0@example.com")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(res.Results[0].ListID,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"a994a3caf1328a16af9a69a730eaa706")

***REMOVED******REMOVED***def test_opens(self):
***REMOVED******REMOVED******REMOVED******REMOVED***min_date = "2010-01-01"
***REMOVED******REMOVED******REMOVED******REMOVED***self.campaign.stub_request("campaigns/%s/opens.json?date=%s&orderfield=date&page=1&pagesize=1000&orderdirection=asc" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.campaign_id, quote(min_date, '')), "campaign_opens.json")
***REMOVED******REMOVED******REMOVED******REMOVED***opens = self.campaign.opens(min_date)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(opens.Results), 5)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***opens.Results[0].EmailAddress, "subs+6576576576@example.com")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.Results[0].ListID,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"512a3bc577a58fdf689c654329b50fa0")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.Results[0].Date, "2010-10-11 08:29:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.Results[0].IPAddress, "192.168.126.87")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.Results[0].Latitude, -33.8683)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.Results[0].Longitude, 151.2086)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.Results[0].City, "Sydney")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.Results[0].Region, "New South Wales")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.Results[0].CountryCode, "AU")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.Results[0].CountryName, "Australia")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.ResultsOrderedBy, "date")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.OrderDirection, "asc")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.PageNumber, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.PageSize, 1000)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.RecordsOnThisPage, 5)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.TotalNumberOfRecords, 5)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.NumberOfPages, 1)

***REMOVED******REMOVED***def test_clicks(self):
***REMOVED******REMOVED******REMOVED******REMOVED***min_date = "2010-01-01"
***REMOVED******REMOVED******REMOVED******REMOVED***self.campaign.stub_request("campaigns/%s/clicks.json?date=%s&orderfield=date&page=1&pagesize=1000&orderdirection=asc" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.campaign_id, quote(min_date, '')), "campaign_clicks.json")
***REMOVED******REMOVED******REMOVED******REMOVED***clicks = self.campaign.clicks(min_date)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(clicks.Results), 3)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***clicks.Results[0].EmailAddress, "subs+6576576576@example.com")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***clicks.Results[0].URL, "http://video.google.com.au/?hl=en&tab=wv")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***clicks.Results[0].ListID, "512a3bc577a58fdf689c654329b50fa0")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.Results[0].Date, "2010-10-11 08:29:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.Results[0].IPAddress, "192.168.126.87")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.Results[0].Latitude, -33.8683)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.Results[0].Longitude, 151.2086)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.Results[0].City, "Sydney")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.Results[0].Region, "New South Wales")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.Results[0].CountryCode, "AU")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.Results[0].CountryName, "Australia")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.ResultsOrderedBy, "date")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.OrderDirection, "asc")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.PageNumber, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.PageSize, 1000)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.RecordsOnThisPage, 3)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.TotalNumberOfRecords, 3)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.NumberOfPages, 1)

***REMOVED******REMOVED***def test_unsubscribes(self):
***REMOVED******REMOVED******REMOVED******REMOVED***min_date = "2010-01-01"
***REMOVED******REMOVED******REMOVED******REMOVED***self.campaign.stub_request("campaigns/%s/unsubscribes.json?date=%s&orderfield=date&page=1&pagesize=1000&orderdirection=asc" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.campaign_id, quote(min_date, '')), "campaign_unsubscribes.json")
***REMOVED******REMOVED******REMOVED******REMOVED***unsubscribes = self.campaign.unsubscribes(min_date)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(unsubscribes.Results), 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribes.Results[
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***0].EmailAddress, "subs+6576576576@example.com")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribes.Results[
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***0].ListID, "512a3bc577a58fdf689c654329b50fa0")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribes.Results[0].Date, "2010-10-11 08:29:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribes.Results[0].IPAddress, "192.168.126.87")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribes.ResultsOrderedBy, "date")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribes.OrderDirection, "asc")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribes.PageNumber, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribes.PageSize, 1000)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribes.RecordsOnThisPage, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribes.TotalNumberOfRecords, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribes.NumberOfPages, 1)

***REMOVED******REMOVED***def test_spam(self):
***REMOVED******REMOVED******REMOVED******REMOVED***min_date = "2010-01-01"
***REMOVED******REMOVED******REMOVED******REMOVED***self.campaign.stub_request("campaigns/%s/spam.json?date=%s&orderfield=date&page=1&pagesize=1000&orderdirection=asc" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.campaign_id, quote(min_date, '')), "campaign_spam.json")
***REMOVED******REMOVED******REMOVED******REMOVED***spam = self.campaign.spam(min_date)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(spam.Results), 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***spam.Results[0].EmailAddress, "subs+6576576576@example.com")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(spam.Results[0].ListID,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"512a3bc577a58fdf689c654329b50fa0")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(spam.Results[0].Date, "2010-10-11 08:29:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(spam.ResultsOrderedBy, "date")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(spam.OrderDirection, "asc")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(spam.PageNumber, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(spam.PageSize, 1000)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(spam.RecordsOnThisPage, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(spam.TotalNumberOfRecords, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(spam.NumberOfPages, 1)

***REMOVED******REMOVED***def test_bounces(self):
***REMOVED******REMOVED******REMOVED******REMOVED***min_date = "2010-01-01"
***REMOVED******REMOVED******REMOVED******REMOVED***self.campaign.stub_request("campaigns/%s/bounces.json?date=%s&orderfield=date&page=1&pagesize=1000&orderdirection=asc" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.campaign_id, quote(min_date, '')), "campaign_bounces.json")
***REMOVED******REMOVED******REMOVED******REMOVED***bounces = self.campaign.bounces(min_date)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(bounces.Results), 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***bounces.Results[0].EmailAddress, "asdf@softbouncemyemail.com")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***bounces.Results[0].ListID, "654523a5855b4a440bae3fb295641546")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounces.Results[0].BounceType, "Soft")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounces.Results[0].Date, "2010-07-02 16:46:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***bounces.Results[0].Reason, "Bounce - But No Email Address Returned ")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounces.ResultsOrderedBy, "date")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounces.OrderDirection, "asc")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounces.PageNumber, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounces.PageSize, 1000)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounces.RecordsOnThisPage, 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounces.TotalNumberOfRecords, 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounces.NumberOfPages, 1)


class OAuthCampaignTestCase(unittest.TestCase, CampaignTestCase):
***REMOVED******REMOVED***"""Test when using OAuth to authenticate"""

***REMOVED******REMOVED***def setUp(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.campaign_id = "787y87y87y87y87y87y87"
***REMOVED******REMOVED******REMOVED******REMOVED***self.campaign = Campaign(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{"access_token": "ASP95S4aR+9KsgfHB0dapTYxNA==", "refresh_token": "5S4aASP9R+9KsgfHB0dapTYxNA=="}, self.campaign_id)


class ApiKeyCampaignTestCase(unittest.TestCase, CampaignTestCase):
***REMOVED******REMOVED***"""Test when using an API key to authenticate"""

***REMOVED******REMOVED***def setUp(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.campaign_id = "787y87y87y87y87y87y87"
***REMOVED******REMOVED******REMOVED******REMOVED***self.campaign = Campaign(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{'api_key': '123123123123123123123'}, self.campaign_id)
