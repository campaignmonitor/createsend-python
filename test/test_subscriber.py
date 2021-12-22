from six.moves.urllib.parse import quote
import unittest

from createsend.createsend import BadRequest
from createsend.subscriber import Subscriber


class SubscriberTestCase(object):

***REMOVED******REMOVED***def test_get(self):
***REMOVED******REMOVED******REMOVED******REMOVED***email = "subscriber@example.com"
***REMOVED******REMOVED******REMOVED******REMOVED***self.subscriber.stub_request("subscribers/%s.json?email=%s&includetrackingpreference=False" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.list_id, quote(email)), "subscriber_details.json")
***REMOVED******REMOVED******REMOVED******REMOVED***subscriber = self.subscriber.get(self.list_id, email)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(subscriber.EmailAddress, email)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(subscriber.Name, "Subscriber One")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(subscriber.Date, "2010-10-25 10:28:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(subscriber.ListJoinedDate, "2010-10-25 10:28:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(subscriber.State, "Active")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(subscriber.CustomFields), 3)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(subscriber.CustomFields[0].Key, 'website')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(subscriber.CustomFields[
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***0].Value, 'http://example.com')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(subscriber.ReadsEmailWith, "Gmail")

***REMOVED******REMOVED***def test_get_without_arguments(self):
***REMOVED******REMOVED******REMOVED******REMOVED***email = "subscriber@example.com"
***REMOVED******REMOVED******REMOVED******REMOVED***self.subscriber.stub_request("subscribers/%s.json?email=%s&includetrackingpreference=False" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.list_id, quote(email)), "subscriber_details.json")
***REMOVED******REMOVED******REMOVED******REMOVED***subscriber = self.subscriber.get()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(subscriber.EmailAddress, email)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(subscriber.Name, "Subscriber One")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(subscriber.Date, "2010-10-25 10:28:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(subscriber.ListJoinedDate, "2010-10-25 10:28:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(subscriber.State, "Active")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(subscriber.CustomFields), 3)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(subscriber.CustomFields[0].Key, 'website')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(subscriber.CustomFields[
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***0].Value, 'http://example.com')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(subscriber.ReadsEmailWith, "Gmail")

***REMOVED******REMOVED***def test_get_with_tracking_preference_included(self):
***REMOVED******REMOVED******REMOVED******REMOVED***email = "subscriber@example.com"
***REMOVED******REMOVED******REMOVED******REMOVED***self.subscriber.stub_request("subscribers/%s.json?email=%s&includetrackingpreference=True" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.list_id, quote(email)), "subscriber_details_with_tracking_preference.json")
***REMOVED******REMOVED******REMOVED******REMOVED***subscriber = self.subscriber.get(self.list_id, email, include_tracking_preference=True)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(subscriber.EmailAddress, email)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(subscriber.Name, "Subscriber One")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(subscriber.Date, "2010-10-25 10:28:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(subscriber.ListJoinedDate, "2010-10-25 10:28:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(subscriber.State, "Active")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(subscriber.CustomFields), 3)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(subscriber.CustomFields[0].Key, 'website')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(subscriber.CustomFields[
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***0].Value, 'http://example.com')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(subscriber.ReadsEmailWith, "Gmail")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(subscriber.ConsentToTrack, "Yes")

***REMOVED******REMOVED***def test_add_without_custom_fields(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.subscriber.stub_request(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"subscribers/%s.json" % self.list_id, "add_subscriber.json")
***REMOVED******REMOVED******REMOVED******REMOVED***email_address = self.subscriber.add(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.list_id, "subscriber@example.com", "Subscriber", [], True, "Unchanged")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(email_address, "subscriber@example.com")

***REMOVED******REMOVED***def test_add_with_custom_fields(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.subscriber.stub_request(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"subscribers/%s.json" % self.list_id, "add_subscriber.json")
***REMOVED******REMOVED******REMOVED******REMOVED***custom_fields = [{"Key": 'website', "Value": 'http://example.com/'}]
***REMOVED******REMOVED******REMOVED******REMOVED***email_address = self.subscriber.add(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.list_id, "subscriber@example.com", "Subscriber", custom_fields, True, "No")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(email_address, "subscriber@example.com")

***REMOVED******REMOVED***def test_add_with_custom_fields_including_multioption(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.subscriber.stub_request(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"subscribers/%s.json" % self.list_id, "add_subscriber.json")
***REMOVED******REMOVED******REMOVED******REMOVED***custom_fields = [{"Key": 'multioptionselectone', "Value": 'myoption'},
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** {"Key": 'multioptionselectmany', "Value": 'firstoption'},
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** {"Key": 'multioptionselectmany', "Value": 'secondoption'}]
***REMOVED******REMOVED******REMOVED******REMOVED***email_address = self.subscriber.add(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.list_id, "subscriber@example.com", "Subscriber", custom_fields, True, "Yes")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(email_address, "subscriber@example.com")

***REMOVED******REMOVED***def test_update_with_custom_fields(self):
***REMOVED******REMOVED******REMOVED******REMOVED***new_email = "new_email_address@example.com"
***REMOVED******REMOVED******REMOVED******REMOVED***self.subscriber.stub_request("subscribers/%s.json?email=%s" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.list_id, quote(self.subscriber.email_address)), None)
***REMOVED******REMOVED******REMOVED******REMOVED***custom_fields = [{"Key": 'website', "Value": 'http://example.com/'}]
***REMOVED******REMOVED******REMOVED******REMOVED***self.subscriber.update(new_email, "Subscriber", custom_fields, True, "Yes")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(self.subscriber.email_address, new_email)

***REMOVED******REMOVED***def test_update_with_custom_fields_including_clear_option(self):
***REMOVED******REMOVED******REMOVED******REMOVED***new_email = "new_email_address@example.com"
***REMOVED******REMOVED******REMOVED******REMOVED***self.subscriber.stub_request("subscribers/%s.json?email=%s" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.list_id, quote(self.subscriber.email_address)), None)
***REMOVED******REMOVED******REMOVED******REMOVED***custom_fields = [
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{"Key": 'website', "Value": 'http://example.com/', "Clear": True}]
***REMOVED******REMOVED******REMOVED******REMOVED***self.subscriber.update(new_email, "Subscriber", custom_fields, True, "No")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(self.subscriber.email_address, new_email)

***REMOVED******REMOVED***def test_import_subscribers(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.subscriber.stub_request(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"subscribers/%s/import.json" % self.list_id, "import_subscribers.json")
***REMOVED******REMOVED******REMOVED******REMOVED***subscribers = [
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{"EmailAddress": "example+1@example.com", "Name": "Example One"},
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{"EmailAddress": "example+2@example.com", "Name": "Example Two"},
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{"EmailAddress": "example+3@example.com", "Name": "Example Three"},
***REMOVED******REMOVED******REMOVED******REMOVED***]
***REMOVED******REMOVED******REMOVED******REMOVED***import_result = self.subscriber.import_subscribers(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.list_id, subscribers, True)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(import_result.FailureDetails), 0)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(import_result.TotalUniqueEmailsSubmitted, 3)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(import_result.TotalExistingSubscribers, 0)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(import_result.TotalNewSubscribers, 3)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(import_result.DuplicateEmailsInSubmission), 0)

***REMOVED******REMOVED***def test_import_subscribers_start_subscription_autoresponders(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.subscriber.stub_request(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"subscribers/%s/import.json" % self.list_id, "import_subscribers.json")
***REMOVED******REMOVED******REMOVED******REMOVED***subscribers = [
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{"EmailAddress": "example+1@example.com", "Name": "Example One"},
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{"EmailAddress": "example+2@example.com", "Name": "Example Two"},
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{"EmailAddress": "example+3@example.com", "Name": "Example Three"},
***REMOVED******REMOVED******REMOVED******REMOVED***]
***REMOVED******REMOVED******REMOVED******REMOVED***import_result = self.subscriber.import_subscribers(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.list_id, subscribers, True, True)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(import_result.FailureDetails), 0)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(import_result.TotalUniqueEmailsSubmitted, 3)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(import_result.TotalExistingSubscribers, 0)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(import_result.TotalNewSubscribers, 3)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(import_result.DuplicateEmailsInSubmission), 0)

***REMOVED******REMOVED***def test_import_subscribers_with_custom_fields_including_clear_option(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.subscriber.stub_request(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"subscribers/%s/import.json" % self.list_id, "import_subscribers.json")
***REMOVED******REMOVED******REMOVED******REMOVED***subscribers = [
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{"EmailAddress": "example+1@example.com", "Name": "Example One",
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"CustomFields": [{"Key": "website", "Value": "", "Clear": True}]},
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{"EmailAddress": "example+2@example.com", "Name": "Example Two",
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"CustomFields": [{"Key": "website", "Value": "", "Clear": False}]},
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{"EmailAddress": "example+3@example.com", "Name": "Example Three",
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"CustomFields": [{"Key": "website", "Value": "", "Clear": False}]},
***REMOVED******REMOVED******REMOVED******REMOVED***]
***REMOVED******REMOVED******REMOVED******REMOVED***import_result = self.subscriber.import_subscribers(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.list_id, subscribers, True)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(import_result.FailureDetails), 0)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(import_result.TotalUniqueEmailsSubmitted, 3)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(import_result.TotalExistingSubscribers, 0)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(import_result.TotalNewSubscribers, 3)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(import_result.DuplicateEmailsInSubmission), 0)

***REMOVED******REMOVED***def test_import_subscribers_partial_success(self):
***REMOVED******REMOVED******REMOVED******REMOVED***# Stub request with 400 Bad Request as the expected response status
***REMOVED******REMOVED******REMOVED******REMOVED***self.subscriber.stub_request("subscribers/%s/import.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.list_id, "import_subscribers_partial_success.json", 400)
***REMOVED******REMOVED******REMOVED******REMOVED***subscribers = [
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{"EmailAddress": "example+1@example", "Name": "Example One"},
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{"EmailAddress": "example+2@example.com", "Name": "Example Two"},
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{"EmailAddress": "example+3@example.com", "Name": "Example Three"},
***REMOVED******REMOVED******REMOVED******REMOVED***]
***REMOVED******REMOVED******REMOVED******REMOVED***import_result = self.subscriber.import_subscribers(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.list_id, subscribers, True)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(import_result.FailureDetails), 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(import_result.FailureDetails[
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***0].EmailAddress, "example+1@example")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(import_result.FailureDetails[0].Code, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(import_result.FailureDetails[
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***0].Message, "Invalid Email Address")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(import_result.TotalUniqueEmailsSubmitted, 3)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(import_result.TotalExistingSubscribers, 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(import_result.TotalNewSubscribers, 0)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(import_result.DuplicateEmailsInSubmission), 0)

***REMOVED******REMOVED***def test_import_subscribers_complete_failure_because_of_bad_request(self):
***REMOVED******REMOVED******REMOVED******REMOVED***# Stub request with 400 Bad Request as the expected response status
***REMOVED******REMOVED******REMOVED******REMOVED***self.subscriber.stub_request(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"subscribers/%s/import.json" % self.list_id, "custom_api_error.json", 400)
***REMOVED******REMOVED******REMOVED******REMOVED***subscribers = [
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{"EmailAddress": "example+1@example", "Name": "Example One"},
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{"EmailAddress": "example+2@example.com", "Name": "Example Two"},
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{"EmailAddress": "example+3@example.com", "Name": "Example Three"},
***REMOVED******REMOVED******REMOVED******REMOVED***]
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertRaises(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***BadRequest, self.subscriber.import_subscribers, self.list_id, subscribers, True)

***REMOVED******REMOVED***def test_unsubscribe(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.subscriber.stub_request(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"subscribers/%s/unsubscribe.json" % self.list_id, None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.subscriber.unsubscribe()

***REMOVED******REMOVED***def test_history(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.subscriber.stub_request("subscribers/%s/history.json?email=%s" % (
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.list_id, quote(self.subscriber.email_address)), "subscriber_history.json")
***REMOVED******REMOVED******REMOVED******REMOVED***history = self.subscriber.history()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(history), 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(history[0].Name, "Campaign One")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(history[0].Type, "Campaign")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(history[0].ID, "fc0ce7105baeaf97f47c99be31d02a91")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(history[0].Actions), 6)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(history[0].Actions[0].Event, "Open")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(history[0].Actions[0].Date, "2010-10-12 13:18:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(history[0].Actions[0].IPAddress, "192.168.126.87")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(history[0].Actions[0].Detail, "")

***REMOVED******REMOVED***def test_delete(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.subscriber.stub_request("subscribers/%s.json?email=%s" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.list_id, quote(self.subscriber.email_address)), None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.subscriber.delete()


class OAuthSubscriberTestCase(unittest.TestCase, SubscriberTestCase):
***REMOVED******REMOVED***"""Test when using OAuth to authenticate"""

***REMOVED******REMOVED***def setUp(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.list_id = "d98h2938d9283d982u3d98u88"
***REMOVED******REMOVED******REMOVED******REMOVED***self.subscriber = Subscriber(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{"access_token": "ASP95S4aR+9KsgfHB0dapTYxNA==",
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"refresh_token": "5S4aASP9R+9KsgfHB0dapTYxNA=="},
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.list_id, "subscriber@example.com")


class ApiKeySubscriberTestCase(unittest.TestCase, SubscriberTestCase):
***REMOVED******REMOVED***"""Test when using an API key to authenticate"""

***REMOVED******REMOVED***def setUp(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.list_id = "d98h2938d9283d982u3d98u88"
***REMOVED******REMOVED******REMOVED******REMOVED***self.subscriber = Subscriber(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{'api_key': '123123123123123123123'},
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.list_id, "subscriber@example.com")
