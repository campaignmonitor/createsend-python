from urllib.parse import quote
import unittest

from createsend.journey_email import JourneyEmail


class JourneyEmailTestCase:

***REMOVED******REMOVED***def test_bounces_no_params(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.journey_email.stub_request(self.no_param_uri_for("bounces"), "journey_email_bounces_no_params.json")
***REMOVED******REMOVED******REMOVED******REMOVED***bounces = self.journey_email.bounces()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(bounces.Results), 2)
***REMOVED******REMOVED******REMOVED******REMOVED***bounce_one = bounces.Results[0]
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounce_one.EmailAddress, "asdf@softbouncemyemail.comX")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounce_one.BounceType, "Soft")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounce_one.Date, "2019-08-20 14:24:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounce_one.Reason, "Soft Bounce - Dns Failure")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounces.ResultsOrderedBy, "Date")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounces.OrderDirection, "ASC")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounces.PageNumber, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounces.PageSize, 1000)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounces.RecordsOnThisPage, 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounces.TotalNumberOfRecords, 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounces.NumberOfPages, 1)

***REMOVED******REMOVED***def test_bounces_with_params(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.journey_email.stub_request(self.param_uri_for("bounces", "2019-01-01", 1, 10, "desc"), "journey_email_bounces_with_params.json")
***REMOVED******REMOVED******REMOVED******REMOVED***bounces = self.journey_email.bounces(date="2019-01-01", page=1, page_size=10, order_direction="desc")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(bounces.Results), 2)
***REMOVED******REMOVED******REMOVED******REMOVED***bounce_one = bounces.Results[0]
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounce_one.EmailAddress, "asdf@hardbouncemyemail.com")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounce_one.BounceType, "Hard")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounce_one.Date, "2019-08-21 04:26:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounce_one.Reason, "Hard Bounce")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounces.ResultsOrderedBy, "Date")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounces.OrderDirection, "DESC")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounces.PageNumber, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounces.PageSize, 10)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounces.RecordsOnThisPage, 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounces.TotalNumberOfRecords, 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(bounces.NumberOfPages, 1)

***REMOVED******REMOVED***def test_clicks_no_params(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.journey_email.stub_request(self.no_param_uri_for("clicks"), "journey_email_clicks_no_params.json")
***REMOVED******REMOVED******REMOVED******REMOVED***clicks = self.journey_email.clicks()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(clicks.Results), 2)
***REMOVED******REMOVED******REMOVED******REMOVED***click_one = clicks.Results[0]
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(click_one.EmailAddress, "asdf@example.com")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(click_one.Date, "2019-08-19 10:23:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(click_one.URL, "http://mail.google.com/mail/?hl=en&tab=wm")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(click_one.IPAddress, "198.148.196.144")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(click_one.Latitude, -33.8591)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(click_one.Longitude, 151.200195)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(click_one.City, "Sydney")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(click_one.Region, "New South Wales")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(click_one.CountryCode, "AU")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(click_one.CountryName, "Australia")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.ResultsOrderedBy, "Date")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.OrderDirection, "ASC")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.PageNumber, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.PageSize, 1000)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.RecordsOnThisPage, 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.TotalNumberOfRecords, 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.NumberOfPages, 1)

***REMOVED******REMOVED***def test_clicks_with_params(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.journey_email.stub_request(self.param_uri_for("clicks", "2019-01-01", 1, 10, "desc"), "journey_email_clicks_with_params.json")
***REMOVED******REMOVED******REMOVED******REMOVED***clicks = self.journey_email.clicks(date="2019-01-01", page=1, page_size=10, order_direction="desc")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(clicks.Results), 2)
***REMOVED******REMOVED******REMOVED******REMOVED***click_one = clicks.Results[0]
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(click_one.EmailAddress, "asdf+2@example.com")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(click_one.Date, "2019-08-19 10:24:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(click_one.URL, "https://example.com")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(click_one.IPAddress, "198.148.196.144")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(click_one.Latitude, -33.8591)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(click_one.Longitude, 151.200195)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(click_one.City, "Sydney")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(click_one.Region, "New South Wales")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(click_one.CountryCode, "AU")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(click_one.CountryName, "Australia")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.ResultsOrderedBy, "Date")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.OrderDirection, "DESC")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.PageNumber, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.PageSize, 10)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.RecordsOnThisPage, 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.TotalNumberOfRecords, 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(clicks.NumberOfPages, 1)

***REMOVED******REMOVED***def test_opens_no_params(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.journey_email.stub_request(self.no_param_uri_for("opens"), "journey_email_opens_no_params.json")
***REMOVED******REMOVED******REMOVED******REMOVED***opens = self.journey_email.opens()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(opens.Results), 2)
***REMOVED******REMOVED******REMOVED******REMOVED***open_one = opens.Results[0]
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(open_one.EmailAddress, "asdf@example.com")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(open_one.Date, "2019-08-19 10:23:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(open_one.IPAddress, "198.148.196.144")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(open_one.Latitude, -33.8591)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(open_one.Longitude, 151.200195)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(open_one.City, "Sydney")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(open_one.Region, "New South Wales")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(open_one.CountryCode, "AU")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(open_one.CountryName, "Australia")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.ResultsOrderedBy, "Date")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.OrderDirection, "ASC")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.PageNumber, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.PageSize, 1000)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.RecordsOnThisPage, 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.TotalNumberOfRecords, 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.NumberOfPages, 1)

***REMOVED******REMOVED***def test_opens_with_params(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.journey_email.stub_request(self.param_uri_for("opens", "2019-01-01", 1, 10, "desc"), "journey_email_opens_with_params.json")
***REMOVED******REMOVED******REMOVED******REMOVED***opens = self.journey_email.opens(date="2019-01-01", page=1, page_size=10, order_direction="desc")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(opens.Results), 2)
***REMOVED******REMOVED******REMOVED******REMOVED***open_one = opens.Results[0]
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(open_one.EmailAddress, "asdf+2@example.com")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(open_one.Date, "2019-08-19 10:24:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(open_one.IPAddress, "198.148.196.144")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(open_one.Latitude, -33.8591)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(open_one.Longitude, 151.200195)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(open_one.City, "Sydney")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(open_one.Region, "New South Wales")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(open_one.CountryCode, "AU")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(open_one.CountryName, "Australia")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.ResultsOrderedBy, "Date")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.OrderDirection, "DESC")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.PageNumber, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.PageSize, 10)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.RecordsOnThisPage, 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.TotalNumberOfRecords, 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(opens.NumberOfPages, 1)

***REMOVED******REMOVED***def test_recipients_no_params(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.journey_email.stub_request(self.no_param_uri_for("recipients"), "journey_email_recipients_no_params.json")
***REMOVED******REMOVED******REMOVED******REMOVED***recipients = self.journey_email.recipients()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(recipients.Results), 4)
***REMOVED******REMOVED******REMOVED******REMOVED***recipient_one = recipients.Results[0]
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(recipient_one.EmailAddress, "asdf@example.com")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(recipient_one.SentDate, "2019-08-19 10:23:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(recipients.ResultsOrderedBy, "SentDate")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(recipients.OrderDirection, "ASC")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(recipients.PageNumber, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(recipients.PageSize, 1000)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(recipients.RecordsOnThisPage, 4)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(recipients.TotalNumberOfRecords, 4)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(recipients.NumberOfPages, 1)

***REMOVED******REMOVED***def test_recipients_with_params(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.journey_email.stub_request(self.param_uri_for("recipients", "2019-01-01", 1, 10, "desc"), "journey_email_recipients_with_params.json")
***REMOVED******REMOVED******REMOVED******REMOVED***recipients = self.journey_email.recipients(date="2019-01-01", page=1, page_size=10, order_direction="desc")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(recipients.Results), 4)
***REMOVED******REMOVED******REMOVED******REMOVED***recipient_one = recipients.Results[0]
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(recipient_one.EmailAddress, "asdf@hardbouncemyemail.com")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(recipient_one.SentDate, "2019-08-21 04:26:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(recipients.ResultsOrderedBy, "SentDate")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(recipients.OrderDirection, "DESC")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(recipients.PageNumber, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(recipients.PageSize, 10)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(recipients.RecordsOnThisPage, 4)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(recipients.TotalNumberOfRecords, 4)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(recipients.NumberOfPages, 1)

***REMOVED******REMOVED***def test_unsubscribes_no_params(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.journey_email.stub_request(self.no_param_uri_for("unsubscribes"), "journey_email_unsubscribes_no_params.json")
***REMOVED******REMOVED******REMOVED******REMOVED***unsubscribes = self.journey_email.unsubscribes()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(unsubscribes.Results), 1)
***REMOVED******REMOVED******REMOVED******REMOVED***unsubscribe_one = unsubscribes.Results[0]
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribe_one.EmailAddress, "asdf@example.com")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribe_one.Date, "2019-08-19 10:24:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribe_one.IPAddress, "198.148.196.144")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribes.ResultsOrderedBy, "Date")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribes.OrderDirection, "ASC")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribes.PageNumber, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribes.PageSize, 1000)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribes.RecordsOnThisPage, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribes.TotalNumberOfRecords, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribes.NumberOfPages, 1)

***REMOVED******REMOVED***def test_unsubscribes_with_params(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.journey_email.stub_request(self.param_uri_for("unsubscribes", "2019-01-01", 1, 10, "desc"), "journey_email_unsubscribes_with_params.json")
***REMOVED******REMOVED******REMOVED******REMOVED***unsubscribes = self.journey_email.unsubscribes(date="2019-01-01", page=1, page_size=10, order_direction="desc")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(unsubscribes.Results), 1)
***REMOVED******REMOVED******REMOVED******REMOVED***unsubscribe_one = unsubscribes.Results[0]
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribe_one.EmailAddress, "asdf@example.com")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribe_one.Date, "2019-08-19 10:24:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribe_one.IPAddress, "198.148.196.144")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribes.ResultsOrderedBy, "Date")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribes.OrderDirection, "DESC")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribes.PageNumber, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribes.PageSize, 10)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribes.RecordsOnThisPage, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribes.TotalNumberOfRecords, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(unsubscribes.NumberOfPages, 1)

***REMOVED******REMOVED***def no_param_uri_for(self, action):
***REMOVED******REMOVED******REMOVED******REMOVED***return "journeys/email/%s/%s.json" %\
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.journey_email_id, action)

***REMOVED******REMOVED***def param_uri_for(self, action, date, page, pagesize, orderdirection):
***REMOVED******REMOVED******REMOVED******REMOVED***return "journeys/email/%s/%s.json?date=%s&page=%s&pagesize=%s&orderdirection=%s" %\
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.journey_email_id, action, quote(date, ''), page, pagesize, orderdirection)


class OAuthCampaignTestCase(unittest.TestCase, JourneyEmailTestCase):
***REMOVED******REMOVED***"""Test when using OAuth to authenticate"""

***REMOVED******REMOVED***def setUp(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.journey_email_id = "787y87y87y87y87y87y87"
***REMOVED******REMOVED******REMOVED******REMOVED***self.journey_email = JourneyEmail(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{"access_token": "ASP95S4aR+9KsgfHB0dapTYxNA==", "refresh_token": "5S4aASP9R+9KsgfHB0dapTYxNA=="}, self.journey_email_id)


class ApiKeyCampaignTestCase(unittest.TestCase, JourneyEmailTestCase):
***REMOVED******REMOVED***"""Test when using an API key to authenticate"""

***REMOVED******REMOVED***def setUp(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.journey_email_id = "787y87y87y87y87y87y87"
***REMOVED******REMOVED******REMOVED******REMOVED***self.journey_email = JourneyEmail(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{'api_key': '123123123123123123123'}, self.journey_email_id)
