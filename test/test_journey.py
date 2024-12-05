import unittest

from createsend.journey import Journey


class JourneyTestCase:

    def test_summary(self):
        self.journey.stub_request(
            "journeys/%s.json" % self.journey_id, "journey_summary.json")
        summary = self.journey.summary()
        self.assertEqual(summary.JourneyID, "a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1")
        self.assertEqual(summary.Name, "New journey")
        self.assertEqual(summary.TriggerType, "On Subscription")
        self.assertEqual(summary.Status, "Active")
        email_one = summary.Emails[0]
        self.assertEqual(email_one.EmailID, "b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1")
        self.assertEqual(email_one.Name, "1")
        self.assertEqual(email_one.Bounced, 7)
        self.assertEqual(email_one.Clicked, 1)
        self.assertEqual(email_one.Opened, 12)
        self.assertEqual(email_one.Sent, 11)
        self.assertEqual(email_one.UniqueOpened, 4)
        self.assertEqual(email_one.Unsubscribed, 1)


class OAuthJourneyTestCase(unittest.TestCase, JourneyTestCase):
    """Test when using OAuth to authenticate"""

    def setUp(self):
        self.journey_id = "787y87y87y87y87y87y87"
        self.journey = Journey(
            {"access_token": "ASP95S4aR+9KsgfHB0dapTYxNA==", "refresh_token": "5S4aASP9R+9KsgfHB0dapTYxNA=="}, self.journey_id)


class ApiKeyJourneyTestCase(unittest.TestCase, JourneyTestCase):
    """Test when using an API key to authenticate"""

    def setUp(self):
        self.journey_id = "787y87y87y87y87y87y87"
        self.journey = Journey(
            {'api_key': '123123123123123123123'}, self.journey_id)
