from urllib.parse import quote
import unittest

from createsend.journey_email import JourneyEmail


class JourneyEmailTestCase:

    def test_bounces_no_params(self):
        self.journey_email.stub_request(self.no_param_uri_for("bounces"), "journey_email_bounces_no_params.json")
        bounces = self.journey_email.bounces()
        self.assertEqual(len(bounces.Results), 2)
        bounce_one = bounces.Results[0]
        self.assertEqual(bounce_one.EmailAddress, "asdf@softbouncemyemail.comX")
        self.assertEqual(bounce_one.BounceType, "Soft")
        self.assertEqual(bounce_one.Date, "2019-08-20 14:24:00")
        self.assertEqual(bounce_one.Reason, "Soft Bounce - Dns Failure")
        self.assertEqual(bounces.ResultsOrderedBy, "Date")
        self.assertEqual(bounces.OrderDirection, "ASC")
        self.assertEqual(bounces.PageNumber, 1)
        self.assertEqual(bounces.PageSize, 1000)
        self.assertEqual(bounces.RecordsOnThisPage, 2)
        self.assertEqual(bounces.TotalNumberOfRecords, 2)
        self.assertEqual(bounces.NumberOfPages, 1)

    def test_bounces_with_params(self):
        self.journey_email.stub_request(self.param_uri_for("bounces", "2019-01-01", 1, 10, "desc"), "journey_email_bounces_with_params.json")
        bounces = self.journey_email.bounces(date="2019-01-01", page=1, page_size=10, order_direction="desc")
        self.assertEqual(len(bounces.Results), 2)
        bounce_one = bounces.Results[0]
        self.assertEqual(bounce_one.EmailAddress, "asdf@hardbouncemyemail.com")
        self.assertEqual(bounce_one.BounceType, "Hard")
        self.assertEqual(bounce_one.Date, "2019-08-21 04:26:00")
        self.assertEqual(bounce_one.Reason, "Hard Bounce")
        self.assertEqual(bounces.ResultsOrderedBy, "Date")
        self.assertEqual(bounces.OrderDirection, "DESC")
        self.assertEqual(bounces.PageNumber, 1)
        self.assertEqual(bounces.PageSize, 10)
        self.assertEqual(bounces.RecordsOnThisPage, 2)
        self.assertEqual(bounces.TotalNumberOfRecords, 2)
        self.assertEqual(bounces.NumberOfPages, 1)

    def test_clicks_no_params(self):
        self.journey_email.stub_request(self.no_param_uri_for("clicks"), "journey_email_clicks_no_params.json")
        clicks = self.journey_email.clicks()
        self.assertEqual(len(clicks.Results), 2)
        click_one = clicks.Results[0]
        self.assertEqual(click_one.EmailAddress, "asdf@example.com")
        self.assertEqual(click_one.Date, "2019-08-19 10:23:00")
        self.assertEqual(click_one.URL, "http://mail.google.com/mail/?hl=en&tab=wm")
        self.assertEqual(click_one.IPAddress, "198.148.196.144")
        self.assertEqual(click_one.Latitude, -33.8591)
        self.assertEqual(click_one.Longitude, 151.200195)
        self.assertEqual(click_one.City, "Sydney")
        self.assertEqual(click_one.Region, "New South Wales")
        self.assertEqual(click_one.CountryCode, "AU")
        self.assertEqual(click_one.CountryName, "Australia")
        self.assertEqual(clicks.ResultsOrderedBy, "Date")
        self.assertEqual(clicks.OrderDirection, "ASC")
        self.assertEqual(clicks.PageNumber, 1)
        self.assertEqual(clicks.PageSize, 1000)
        self.assertEqual(clicks.RecordsOnThisPage, 2)
        self.assertEqual(clicks.TotalNumberOfRecords, 2)
        self.assertEqual(clicks.NumberOfPages, 1)

    def test_clicks_with_params(self):
        self.journey_email.stub_request(self.param_uri_for("clicks", "2019-01-01", 1, 10, "desc"), "journey_email_clicks_with_params.json")
        clicks = self.journey_email.clicks(date="2019-01-01", page=1, page_size=10, order_direction="desc")
        self.assertEqual(len(clicks.Results), 2)
        click_one = clicks.Results[0]
        self.assertEqual(click_one.EmailAddress, "asdf+2@example.com")
        self.assertEqual(click_one.Date, "2019-08-19 10:24:00")
        self.assertEqual(click_one.URL, "https://example.com")
        self.assertEqual(click_one.IPAddress, "198.148.196.144")
        self.assertEqual(click_one.Latitude, -33.8591)
        self.assertEqual(click_one.Longitude, 151.200195)
        self.assertEqual(click_one.City, "Sydney")
        self.assertEqual(click_one.Region, "New South Wales")
        self.assertEqual(click_one.CountryCode, "AU")
        self.assertEqual(click_one.CountryName, "Australia")
        self.assertEqual(clicks.ResultsOrderedBy, "Date")
        self.assertEqual(clicks.OrderDirection, "DESC")
        self.assertEqual(clicks.PageNumber, 1)
        self.assertEqual(clicks.PageSize, 10)
        self.assertEqual(clicks.RecordsOnThisPage, 2)
        self.assertEqual(clicks.TotalNumberOfRecords, 2)
        self.assertEqual(clicks.NumberOfPages, 1)

    def test_opens_no_params(self):
        self.journey_email.stub_request(self.no_param_uri_for("opens"), "journey_email_opens_no_params.json")
        opens = self.journey_email.opens()
        self.assertEqual(len(opens.Results), 2)
        open_one = opens.Results[0]
        self.assertEqual(open_one.EmailAddress, "asdf@example.com")
        self.assertEqual(open_one.Date, "2019-08-19 10:23:00")
        self.assertEqual(open_one.IPAddress, "198.148.196.144")
        self.assertEqual(open_one.Latitude, -33.8591)
        self.assertEqual(open_one.Longitude, 151.200195)
        self.assertEqual(open_one.City, "Sydney")
        self.assertEqual(open_one.Region, "New South Wales")
        self.assertEqual(open_one.CountryCode, "AU")
        self.assertEqual(open_one.CountryName, "Australia")
        self.assertEqual(opens.ResultsOrderedBy, "Date")
        self.assertEqual(opens.OrderDirection, "ASC")
        self.assertEqual(opens.PageNumber, 1)
        self.assertEqual(opens.PageSize, 1000)
        self.assertEqual(opens.RecordsOnThisPage, 2)
        self.assertEqual(opens.TotalNumberOfRecords, 2)
        self.assertEqual(opens.NumberOfPages, 1)

    def test_opens_with_params(self):
        self.journey_email.stub_request(self.param_uri_for("opens", "2019-01-01", 1, 10, "desc"), "journey_email_opens_with_params.json")
        opens = self.journey_email.opens(date="2019-01-01", page=1, page_size=10, order_direction="desc")
        self.assertEqual(len(opens.Results), 2)
        open_one = opens.Results[0]
        self.assertEqual(open_one.EmailAddress, "asdf+2@example.com")
        self.assertEqual(open_one.Date, "2019-08-19 10:24:00")
        self.assertEqual(open_one.IPAddress, "198.148.196.144")
        self.assertEqual(open_one.Latitude, -33.8591)
        self.assertEqual(open_one.Longitude, 151.200195)
        self.assertEqual(open_one.City, "Sydney")
        self.assertEqual(open_one.Region, "New South Wales")
        self.assertEqual(open_one.CountryCode, "AU")
        self.assertEqual(open_one.CountryName, "Australia")
        self.assertEqual(opens.ResultsOrderedBy, "Date")
        self.assertEqual(opens.OrderDirection, "DESC")
        self.assertEqual(opens.PageNumber, 1)
        self.assertEqual(opens.PageSize, 10)
        self.assertEqual(opens.RecordsOnThisPage, 2)
        self.assertEqual(opens.TotalNumberOfRecords, 2)
        self.assertEqual(opens.NumberOfPages, 1)

    def test_recipients_no_params(self):
        self.journey_email.stub_request(self.no_param_uri_for("recipients"), "journey_email_recipients_no_params.json")
        recipients = self.journey_email.recipients()
        self.assertEqual(len(recipients.Results), 4)
        recipient_one = recipients.Results[0]
        self.assertEqual(recipient_one.EmailAddress, "asdf@example.com")
        self.assertEqual(recipient_one.SentDate, "2019-08-19 10:23:00")
        self.assertEqual(recipients.ResultsOrderedBy, "SentDate")
        self.assertEqual(recipients.OrderDirection, "ASC")
        self.assertEqual(recipients.PageNumber, 1)
        self.assertEqual(recipients.PageSize, 1000)
        self.assertEqual(recipients.RecordsOnThisPage, 4)
        self.assertEqual(recipients.TotalNumberOfRecords, 4)
        self.assertEqual(recipients.NumberOfPages, 1)

    def test_recipients_with_params(self):
        self.journey_email.stub_request(self.param_uri_for("recipients", "2019-01-01", 1, 10, "desc"), "journey_email_recipients_with_params.json")
        recipients = self.journey_email.recipients(date="2019-01-01", page=1, page_size=10, order_direction="desc")
        self.assertEqual(len(recipients.Results), 4)
        recipient_one = recipients.Results[0]
        self.assertEqual(recipient_one.EmailAddress, "asdf@hardbouncemyemail.com")
        self.assertEqual(recipient_one.SentDate, "2019-08-21 04:26:00")
        self.assertEqual(recipients.ResultsOrderedBy, "SentDate")
        self.assertEqual(recipients.OrderDirection, "DESC")
        self.assertEqual(recipients.PageNumber, 1)
        self.assertEqual(recipients.PageSize, 10)
        self.assertEqual(recipients.RecordsOnThisPage, 4)
        self.assertEqual(recipients.TotalNumberOfRecords, 4)
        self.assertEqual(recipients.NumberOfPages, 1)

    def test_unsubscribes_no_params(self):
        self.journey_email.stub_request(self.no_param_uri_for("unsubscribes"), "journey_email_unsubscribes_no_params.json")
        unsubscribes = self.journey_email.unsubscribes()
        self.assertEqual(len(unsubscribes.Results), 1)
        unsubscribe_one = unsubscribes.Results[0]
        self.assertEqual(unsubscribe_one.EmailAddress, "asdf@example.com")
        self.assertEqual(unsubscribe_one.Date, "2019-08-19 10:24:00")
        self.assertEqual(unsubscribe_one.IPAddress, "198.148.196.144")
        self.assertEqual(unsubscribes.ResultsOrderedBy, "Date")
        self.assertEqual(unsubscribes.OrderDirection, "ASC")
        self.assertEqual(unsubscribes.PageNumber, 1)
        self.assertEqual(unsubscribes.PageSize, 1000)
        self.assertEqual(unsubscribes.RecordsOnThisPage, 1)
        self.assertEqual(unsubscribes.TotalNumberOfRecords, 1)
        self.assertEqual(unsubscribes.NumberOfPages, 1)

    def test_unsubscribes_with_params(self):
        self.journey_email.stub_request(self.param_uri_for("unsubscribes", "2019-01-01", 1, 10, "desc"), "journey_email_unsubscribes_with_params.json")
        unsubscribes = self.journey_email.unsubscribes(date="2019-01-01", page=1, page_size=10, order_direction="desc")
        self.assertEqual(len(unsubscribes.Results), 1)
        unsubscribe_one = unsubscribes.Results[0]
        self.assertEqual(unsubscribe_one.EmailAddress, "asdf@example.com")
        self.assertEqual(unsubscribe_one.Date, "2019-08-19 10:24:00")
        self.assertEqual(unsubscribe_one.IPAddress, "198.148.196.144")
        self.assertEqual(unsubscribes.ResultsOrderedBy, "Date")
        self.assertEqual(unsubscribes.OrderDirection, "DESC")
        self.assertEqual(unsubscribes.PageNumber, 1)
        self.assertEqual(unsubscribes.PageSize, 10)
        self.assertEqual(unsubscribes.RecordsOnThisPage, 1)
        self.assertEqual(unsubscribes.TotalNumberOfRecords, 1)
        self.assertEqual(unsubscribes.NumberOfPages, 1)

    def no_param_uri_for(self, action):
        return "journeys/email/%s/%s.json" %\
               (self.journey_email_id, action)

    def param_uri_for(self, action, date, page, pagesize, orderdirection):
        return "journeys/email/%s/%s.json?date=%s&page=%s&pagesize=%s&orderdirection=%s" %\
               (self.journey_email_id, action, quote(date, ''), page, pagesize, orderdirection)


class OAuthCampaignTestCase(unittest.TestCase, JourneyEmailTestCase):
    """Test when using OAuth to authenticate"""

    def setUp(self):
        self.journey_email_id = "787y87y87y87y87y87y87"
        self.journey_email = JourneyEmail(
            {"access_token": "ASP95S4aR+9KsgfHB0dapTYxNA==", "refresh_token": "5S4aASP9R+9KsgfHB0dapTYxNA=="}, self.journey_email_id)


class ApiKeyCampaignTestCase(unittest.TestCase, JourneyEmailTestCase):
    """Test when using an API key to authenticate"""

    def setUp(self):
        self.journey_email_id = "787y87y87y87y87y87y87"
        self.journey_email = JourneyEmail(
            {'api_key': '123123123123123123123'}, self.journey_email_id)
