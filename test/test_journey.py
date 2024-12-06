import unittest

from createsend.journey import Journey


class JourneyTestCase:

***REMOVED******REMOVED***def test_summary(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.journey.stub_request(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"journeys/%s.json" % self.journey_id, "journey_summary.json")
***REMOVED******REMOVED******REMOVED******REMOVED***summary = self.journey.summary()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(summary.JourneyID, "a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(summary.Name, "New journey")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(summary.TriggerType, "On Subscription")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(summary.Status, "Active")
***REMOVED******REMOVED******REMOVED******REMOVED***email_one = summary.Emails[0]
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(email_one.EmailID, "b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(email_one.Name, "1")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(email_one.Bounced, 7)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(email_one.Clicked, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(email_one.Opened, 12)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(email_one.Sent, 11)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(email_one.UniqueOpened, 4)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(email_one.Unsubscribed, 1)


class OAuthJourneyTestCase(unittest.TestCase, JourneyTestCase):
***REMOVED******REMOVED***"""Test when using OAuth to authenticate"""

***REMOVED******REMOVED***def setUp(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.journey_id = "787y87y87y87y87y87y87"
***REMOVED******REMOVED******REMOVED******REMOVED***self.journey = Journey(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{"access_token": "ASP95S4aR+9KsgfHB0dapTYxNA==", "refresh_token": "5S4aASP9R+9KsgfHB0dapTYxNA=="}, self.journey_id)


class ApiKeyJourneyTestCase(unittest.TestCase, JourneyTestCase):
***REMOVED******REMOVED***"""Test when using an API key to authenticate"""

***REMOVED******REMOVED***def setUp(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.journey_id = "787y87y87y87y87y87y87"
***REMOVED******REMOVED******REMOVED******REMOVED***self.journey = Journey(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{'api_key': '123123123123123123123'}, self.journey_id)
