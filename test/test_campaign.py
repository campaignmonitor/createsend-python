from six.moves.urllib.parse import quote
import unittest

from createsend.campaign import Campaign


class CampaignTestCase(object):

    def test_create(self):
        client_id = '87y8d7qyw8d7yq8w7ydwqwd'
        c = Campaign()
        c.stub_request("campaigns/%s.json" % client_id, "create_campaign.json")
        campaign_id = c.create(client_id, "subject", "name", "g'day", "good.day@example.com", "good.day@example.com",
                               "http://example.com/campaign.html", "http://example.com/campaign.txt", [
                                   '7y12989e82ue98u2e', 'dh9w89q8w98wudwd989'],
                               ['y78q9w8d9w8ud9q8uw', 'djw98quw9duqw98uwd98'])

        self.assertEqual(
            "\"TextUrl\": \"http://example.com/campaign.txt\"" in c.faker.actual_body, True)
        self.assertEqual(c.campaign_id, "787y87y87y87y87y87y8712341234")
        self.assertEqual(campaign_id, "787y87y87y87y87y87y8712341234")

    def test_create_with_none_text_url(self):
        client_id = '87y8d7qyw8d7yq8w7ydwqwd'
        c = Campaign()
        c.stub_request("campaigns/%s.json" % client_id, "create_campaign.json")
        campaign_id = c.create(client_id, "subject", "name", "g'day", "good.day@example.com", "good.day@example.com",
                               "http://example.com/campaign.html", None, [
                                   '7y12989e82ue98u2e', 'dh9w89q8w98wudwd989'],
                               ['y78q9w8d9w8ud9q8uw', 'djw98quw9duqw98uwd98'])

        self.assertEqual("\"TextUrl\": null" in c.faker.actual_body, True)
        self.assertEqual(c.campaign_id, "787y87y87y87y87y87y8712341234")
        self.assertEqual(campaign_id, "787y87y87y87y87y87y8712341234")

    def test_create_from_template(self):
        template_content = {
            "Singlelines": [
                {
                    "Content": "This is a heading",
                    "Href": "http://example.com/"
                }
            ],
            "Multilines": [
                {
                    "Content": "<p>This is example</p><p>multiline <a href=\"http://example.com\">content</a>...</p>"
                }
            ],
            "Images": [
                {
                    "Content": "http://example.com/image.png",
                    "Alt": "This is alt text for an image",
                    "Href": "http://example.com/"
                }
            ],
            "Repeaters": [
                {
                    "Items": [
                        {
                            "Layout": "My layout",
                            "Singlelines": [
                                {
                                    "Content": "This is a repeater heading",
                                    "Href": "http://example.com/"
                                }
                            ],
                            "Multilines": [
                                {
                                    "Content": "<p>This is example</p><p>multiline <a href=\"http://example.com\">content</a>...</p>"
                                }
                            ],
                            "Images": [
                                {
                                    "Content": "http://example.com/repeater-image.png",
                                    "Alt": "This is alt text for a repeater image",
                                    "Href": "http://example.com/"
                                }
                            ]
                        }
                    ]
                }
            ]
        }

        # template_content as defined above would be used to fill the content of
        # a template with markup similar to the following:
        #
        # <html>
        #   <head><title>My Template</title></head>
        #   <body>
        #     <p><singleline>Enter heading...</singleline></p>
        #     <div><multiline>Enter description...</multiline></div>
        #     <img id="header-image" editable="true" width="500" />
        #     <repeater>
        #       <layout label="My layout">
        #         <div class="repeater-item">
        #           <p><singleline></singleline></p>
        #           <div><multiline></multiline></div>
        #           <img editable="true" width="500" />
        #         </div>
        #       </layout>
        #     </repeater>
        #     <p><unsubscribe>Unsubscribe</unsubscribe></p>
        #   </body>
        # </html>

        client_id = '87y8d7qyw8d7yq8w7ydwqwd'
        c = Campaign()
        c.stub_request("campaigns/%s/fromtemplate.json" %
                       client_id, "create_campaign.json")
        campaign_id = c.create_from_template(client_id, "subject", "name", "g'day", "good.day@example.com", "good.day@example.com",
                                             ['7y12989e82ue98u2e', 'dh9w89q8w98wudwd989'], [
                                                 'y78q9w8d9w8ud9q8uw', 'djw98quw9duqw98uwd98'],
                                             "7j8uw98udowy12989e8298u2e", template_content)
        self.assertEqual(c.campaign_id, "787y87y87y87y87y87y8712341234")
        self.assertEqual(campaign_id, "787y87y87y87y87y87y8712341234")

    def test_send_preview_with_single_recipient(self):
        self.campaign.stub_request(
            "campaigns/%s/sendpreview.json" % self.campaign_id, None)
        self.campaign.send_preview("test+89898u9@example.com", "random")

    def test_send_preview_with_multiple_recipients(self):
        self.campaign.stub_request(
            "campaigns/%s/sendpreview.json" % self.campaign_id, None)
        self.campaign.send_preview(
            ["test+89898u9@example.com", "test+787y8y7y8@example.com"], "random")

    def test_send(self):
        self.campaign.stub_request(
            "campaigns/%s/send.json" % self.campaign_id, None)
        self.campaign.send("confirmation@example.com")

    def test_unschedule(self):
        self.campaign.stub_request(
            "campaigns/%s/unschedule.json" % self.campaign_id, None)
        self.campaign.unschedule()

    def test_delete(self):
        self.campaign.stub_request("campaigns/%s.json" %
                                   self.campaign_id, None)
        self.campaign.delete()

    def test_summary(self):
        self.campaign.stub_request(
            "campaigns/%s/summary.json" % self.campaign_id, "campaign_summary.json")
        summary = self.campaign.summary()
        self.assertEqual(summary.Name, "Last Campaign")
        self.assertEqual(summary.Recipients, 5)
        self.assertEqual(summary.TotalOpened, 10)
        self.assertEqual(summary.Clicks, 0)
        self.assertEqual(summary.Unsubscribed, 0)
        self.assertEqual(summary.Bounced, 0)
        self.assertEqual(summary.UniqueOpened, 5)
        self.assertEqual(summary.Mentions, 23)
        self.assertEqual(summary.Forwards, 11)
        self.assertEqual(summary.Likes, 32)
        self.assertEqual(summary.WebVersionURL,
                          "http://createsend.com/t/r-3A433FC72FFE3B8B")
        self.assertEqual(summary.WebVersionTextURL,
                          "http://createsend.com/t/r-3A433FC72FFE3B8B/t")
        self.assertEqual(
            summary.WorldviewURL, "http://client.createsend.com/reports/wv/r/3A433FC72FFE3B8B")
        self.assertEqual(summary.SpamComplaints, 23)

    def test_email_client_usage(self):
        self.campaign.stub_request(
            "campaigns/%s/emailclientusage.json" % self.campaign_id, "email_client_usage.json")
        ecu = self.campaign.email_client_usage()
        self.assertEqual(len(ecu), 6)
        self.assertEqual(ecu[0].Client, "iOS Devices")
        self.assertEqual(ecu[0].Version, "iPhone")
        self.assertEqual(ecu[0].Percentage, 19.83)
        self.assertEqual(ecu[0].Subscribers, 7056)

    def test_lists_and_segments(self):
        self.campaign.stub_request("campaigns/%s/listsandsegments.json" %
                                   self.campaign_id, "campaign_listsandsegments.json")
        ls = self.campaign.lists_and_segments()
        self.assertEqual(len(ls.Lists), 1)
        self.assertEqual(len(ls.Segments), 1)
        self.assertEqual(ls.Lists[0].Name, "List One")
        self.assertEqual(ls.Lists[0].ListID,
                          "a58ee1d3039b8bec838e6d1482a8a965")
        self.assertEqual(ls.Segments[0].Title, "Segment for campaign")
        self.assertEqual(ls.Segments[0].ListID,
                          "2bea949d0bf96148c3e6a209d2e82060")
        self.assertEqual(ls.Segments[0].SegmentID,
                          "dba84a225d5ce3d19105d7257baac46f")

    def test_recipients(self):
        self.campaign.stub_request("campaigns/%s/recipients.json?orderfield=email&page=1&pagesize=20&orderdirection=asc" %
                                   self.campaign_id, "campaign_recipients.json")
        res = self.campaign.recipients(page=1, page_size=20)
        self.assertEqual(res.ResultsOrderedBy, "email")
        self.assertEqual(res.OrderDirection, "asc")
        self.assertEqual(res.PageNumber, 1)
        self.assertEqual(res.PageSize, 20)
        self.assertEqual(res.RecordsOnThisPage, 20)
        self.assertEqual(res.TotalNumberOfRecords, 2200)
        self.assertEqual(res.NumberOfPages, 110)
        self.assertEqual(len(res.Results), 20)
        self.assertEqual(res.Results[0].EmailAddress,
                          "subs+6g76t7t0@example.com")
        self.assertEqual(res.Results[0].ListID,
                          "a994a3caf1328a16af9a69a730eaa706")

    def test_opens(self):
        min_date = "2010-01-01"
        self.campaign.stub_request("campaigns/%s/opens.json?date=%s&orderfield=date&page=1&pagesize=1000&orderdirection=asc" %
                                   (self.campaign_id, quote(min_date, '')), "campaign_opens.json")
        opens = self.campaign.opens(min_date)
        self.assertEqual(len(opens.Results), 5)
        self.assertEqual(
            opens.Results[0].EmailAddress, "subs+6576576576@example.com")
        self.assertEqual(opens.Results[0].ListID,
                          "512a3bc577a58fdf689c654329b50fa0")
        self.assertEqual(opens.Results[0].Date, "2010-10-11 08:29:00")
        self.assertEqual(opens.Results[0].IPAddress, "192.168.126.87")
        self.assertEqual(opens.Results[0].Latitude, -33.8683)
        self.assertEqual(opens.Results[0].Longitude, 151.2086)
        self.assertEqual(opens.Results[0].City, "Sydney")
        self.assertEqual(opens.Results[0].Region, "New South Wales")
        self.assertEqual(opens.Results[0].CountryCode, "AU")
        self.assertEqual(opens.Results[0].CountryName, "Australia")
        self.assertEqual(opens.ResultsOrderedBy, "date")
        self.assertEqual(opens.OrderDirection, "asc")
        self.assertEqual(opens.PageNumber, 1)
        self.assertEqual(opens.PageSize, 1000)
        self.assertEqual(opens.RecordsOnThisPage, 5)
        self.assertEqual(opens.TotalNumberOfRecords, 5)
        self.assertEqual(opens.NumberOfPages, 1)

    def test_clicks(self):
        min_date = "2010-01-01"
        self.campaign.stub_request("campaigns/%s/clicks.json?date=%s&orderfield=date&page=1&pagesize=1000&orderdirection=asc" %
                                   (self.campaign_id, quote(min_date, '')), "campaign_clicks.json")
        clicks = self.campaign.clicks(min_date)
        self.assertEqual(len(clicks.Results), 3)
        self.assertEqual(
            clicks.Results[0].EmailAddress, "subs+6576576576@example.com")
        self.assertEqual(
            clicks.Results[0].URL, "http://video.google.com.au/?hl=en&tab=wv")
        self.assertEqual(
            clicks.Results[0].ListID, "512a3bc577a58fdf689c654329b50fa0")
        self.assertEqual(clicks.Results[0].Date, "2010-10-11 08:29:00")
        self.assertEqual(clicks.Results[0].IPAddress, "192.168.126.87")
        self.assertEqual(clicks.Results[0].Latitude, -33.8683)
        self.assertEqual(clicks.Results[0].Longitude, 151.2086)
        self.assertEqual(clicks.Results[0].City, "Sydney")
        self.assertEqual(clicks.Results[0].Region, "New South Wales")
        self.assertEqual(clicks.Results[0].CountryCode, "AU")
        self.assertEqual(clicks.Results[0].CountryName, "Australia")
        self.assertEqual(clicks.ResultsOrderedBy, "date")
        self.assertEqual(clicks.OrderDirection, "asc")
        self.assertEqual(clicks.PageNumber, 1)
        self.assertEqual(clicks.PageSize, 1000)
        self.assertEqual(clicks.RecordsOnThisPage, 3)
        self.assertEqual(clicks.TotalNumberOfRecords, 3)
        self.assertEqual(clicks.NumberOfPages, 1)

    def test_unsubscribes(self):
        min_date = "2010-01-01"
        self.campaign.stub_request("campaigns/%s/unsubscribes.json?date=%s&orderfield=date&page=1&pagesize=1000&orderdirection=asc" %
                                   (self.campaign_id, quote(min_date, '')), "campaign_unsubscribes.json")
        unsubscribes = self.campaign.unsubscribes(min_date)
        self.assertEqual(len(unsubscribes.Results), 1)
        self.assertEqual(unsubscribes.Results[
                          0].EmailAddress, "subs+6576576576@example.com")
        self.assertEqual(unsubscribes.Results[
                          0].ListID, "512a3bc577a58fdf689c654329b50fa0")
        self.assertEqual(unsubscribes.Results[0].Date, "2010-10-11 08:29:00")
        self.assertEqual(unsubscribes.Results[0].IPAddress, "192.168.126.87")
        self.assertEqual(unsubscribes.ResultsOrderedBy, "date")
        self.assertEqual(unsubscribes.OrderDirection, "asc")
        self.assertEqual(unsubscribes.PageNumber, 1)
        self.assertEqual(unsubscribes.PageSize, 1000)
        self.assertEqual(unsubscribes.RecordsOnThisPage, 1)
        self.assertEqual(unsubscribes.TotalNumberOfRecords, 1)
        self.assertEqual(unsubscribes.NumberOfPages, 1)

    def test_spam(self):
        min_date = "2010-01-01"
        self.campaign.stub_request("campaigns/%s/spam.json?date=%s&orderfield=date&page=1&pagesize=1000&orderdirection=asc" %
                                   (self.campaign_id, quote(min_date, '')), "campaign_spam.json")
        spam = self.campaign.spam(min_date)
        self.assertEqual(len(spam.Results), 1)
        self.assertEqual(
            spam.Results[0].EmailAddress, "subs+6576576576@example.com")
        self.assertEqual(spam.Results[0].ListID,
                          "512a3bc577a58fdf689c654329b50fa0")
        self.assertEqual(spam.Results[0].Date, "2010-10-11 08:29:00")
        self.assertEqual(spam.ResultsOrderedBy, "date")
        self.assertEqual(spam.OrderDirection, "asc")
        self.assertEqual(spam.PageNumber, 1)
        self.assertEqual(spam.PageSize, 1000)
        self.assertEqual(spam.RecordsOnThisPage, 1)
        self.assertEqual(spam.TotalNumberOfRecords, 1)
        self.assertEqual(spam.NumberOfPages, 1)

    def test_bounces(self):
        min_date = "2010-01-01"
        self.campaign.stub_request("campaigns/%s/bounces.json?date=%s&orderfield=date&page=1&pagesize=1000&orderdirection=asc" %
                                   (self.campaign_id, quote(min_date, '')), "campaign_bounces.json")
        bounces = self.campaign.bounces(min_date)
        self.assertEqual(len(bounces.Results), 2)
        self.assertEqual(
            bounces.Results[0].EmailAddress, "asdf@softbouncemyemail.com")
        self.assertEqual(
            bounces.Results[0].ListID, "654523a5855b4a440bae3fb295641546")
        self.assertEqual(bounces.Results[0].BounceType, "Soft")
        self.assertEqual(bounces.Results[0].Date, "2010-07-02 16:46:00")
        self.assertEqual(
            bounces.Results[0].Reason, "Bounce - But No Email Address Returned ")
        self.assertEqual(bounces.ResultsOrderedBy, "date")
        self.assertEqual(bounces.OrderDirection, "asc")
        self.assertEqual(bounces.PageNumber, 1)
        self.assertEqual(bounces.PageSize, 1000)
        self.assertEqual(bounces.RecordsOnThisPage, 2)
        self.assertEqual(bounces.TotalNumberOfRecords, 2)
        self.assertEqual(bounces.NumberOfPages, 1)


class OAuthCampaignTestCase(unittest.TestCase, CampaignTestCase):
    """Test when using OAuth to authenticate"""

    def setUp(self):
        self.campaign_id = "787y87y87y87y87y87y87"
        self.campaign = Campaign(
            {"access_token": "ASP95S4aR+9KsgfHB0dapTYxNA==", "refresh_token": "5S4aASP9R+9KsgfHB0dapTYxNA=="}, self.campaign_id)


class ApiKeyCampaignTestCase(unittest.TestCase, CampaignTestCase):
    """Test when using an API key to authenticate"""

    def setUp(self):
        self.campaign_id = "787y87y87y87y87y87y87"
        self.campaign = Campaign(
            {'api_key': '123123123123123123123'}, self.campaign_id)
