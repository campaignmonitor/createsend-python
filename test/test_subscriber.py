import unittest
import urllib

***REMOVED***

class SubscriberTestCase(unittest.TestCase):

***REMOVED***def setUp(self):
***REMOVED******REMOVED***self.api_key = '123123123123123123123'
***REMOVED******REMOVED***CreateSend.api_key = self.api_key
***REMOVED******REMOVED***self.list_id = "d98h2938d9283d982u3d98u88"
***REMOVED******REMOVED***self.subscriber = Subscriber(self.list_id, "subscriber@example.com")

***REMOVED***def test_get(self):
***REMOVED******REMOVED***email = "subscriber@example.com"
***REMOVED******REMOVED***self.subscriber.stub_request("subscribers/%s.json?email=%s" % (self.list_id, urllib.quote(email)), "subscriber_details.json")
***REMOVED******REMOVED***subscriber = self.subscriber.get(self.list_id, email)
***REMOVED******REMOVED***self.assertEquals(subscriber.EmailAddress, email)
***REMOVED******REMOVED***self.assertEquals(subscriber.Name, "Subscriber One")
***REMOVED******REMOVED***self.assertEquals(subscriber.Date, "2010-10-25 10:28:00")
***REMOVED******REMOVED***self.assertEquals(subscriber.State, "Active")
***REMOVED******REMOVED***self.assertEquals(len(subscriber.CustomFields), 3)
***REMOVED******REMOVED***self.assertEquals(subscriber.CustomFields[0].Key, 'website')
***REMOVED******REMOVED***self.assertEquals(subscriber.CustomFields[0].Value, 'http://example.com')

***REMOVED***def test_add_without_custom_fields(self):
***REMOVED******REMOVED***self.subscriber.stub_request("subscribers/%s.json" % self.list_id, "add_subscriber.json")
***REMOVED******REMOVED***email_address = self.subscriber.add(self.list_id, "subscriber@example.com", "Subscriber", [], True)
***REMOVED******REMOVED***self.assertEquals(email_address, "subscriber@example.com")

***REMOVED***def test_add_with_custom_fields(self):
***REMOVED******REMOVED***self.subscriber.stub_request("subscribers/%s.json" % self.list_id, "add_subscriber.json")
***REMOVED******REMOVED***custom_fields = [ { "Key": 'website', "Value": 'http://example.com/' } ]
***REMOVED******REMOVED***email_address = self.subscriber.add(self.list_id, "subscriber@example.com", "Subscriber", custom_fields, True)
***REMOVED******REMOVED***self.assertEquals(email_address, "subscriber@example.com")

***REMOVED***def test_add_with_custom_fields_including_multioption(self):
***REMOVED******REMOVED***self.subscriber.stub_request("subscribers/%s.json" % self.list_id, "add_subscriber.json")
***REMOVED******REMOVED***custom_fields = [ { "Key": 'multioptionselectone', "Value": 'myoption' },
***REMOVED******REMOVED******REMOVED***{ "Key": 'multioptionselectmany', "Value": 'firstoption' },
***REMOVED******REMOVED******REMOVED***{ "Key": 'multioptionselectmany', "Value": 'secondoption' } ]
***REMOVED******REMOVED***email_address = self.subscriber.add(self.list_id, "subscriber@example.com", "Subscriber", custom_fields, True)
***REMOVED******REMOVED***self.assertEquals(email_address, "subscriber@example.com")

***REMOVED***def test_update_with_custom_fields(self):
***REMOVED******REMOVED***new_email = "new_email_address@example.com"
***REMOVED******REMOVED***self.subscriber.stub_request("subscribers/%s.json?email=%s" % (self.list_id, urllib.quote(self.subscriber.email_address)), None)
***REMOVED******REMOVED***custom_fields = [ { "Key": 'website', "Value": 'http://example.com/' } ]
***REMOVED******REMOVED***self.subscriber.update(new_email, "Subscriber", custom_fields, True)
***REMOVED******REMOVED***self.assertEquals(self.subscriber.email_address, new_email)

***REMOVED***def test_import_subscribers(self):
***REMOVED******REMOVED***self.subscriber.stub_request("subscribers/%s/import.json" % self.list_id, "import_subscribers.json")
***REMOVED******REMOVED***subscribers = [
***REMOVED******REMOVED******REMOVED***{ "EmailAddress": "example+1@example.com", "Name": "Example One" },
***REMOVED******REMOVED******REMOVED***{ "EmailAddress": "example+2@example.com", "Name": "Example Two" },
***REMOVED******REMOVED******REMOVED***{ "EmailAddress": "example+3@example.com", "Name": "Example Three" },
***REMOVED******REMOVED***]
***REMOVED******REMOVED***import_result = self.subscriber.import_subscribers(self.list_id, subscribers, True)
***REMOVED******REMOVED***self.assertEquals(len(import_result.FailureDetails), 0)
***REMOVED******REMOVED***self.assertEquals(import_result.TotalUniqueEmailsSubmitted, 3)
***REMOVED******REMOVED***self.assertEquals(import_result.TotalExistingSubscribers, 0)
***REMOVED******REMOVED***self.assertEquals(import_result.TotalNewSubscribers, 3)
***REMOVED******REMOVED***self.assertEquals(len(import_result.DuplicateEmailsInSubmission), 0)

***REMOVED***def test_import_subscribers_partial_success(self):
***REMOVED******REMOVED***# Stub request with 400 Bad Request as the expected response status
***REMOVED******REMOVED***self.subscriber.stub_request("subscribers/%s/import.json" % self.list_id, "import_subscribers_partial_success.json", 400)
***REMOVED******REMOVED***subscribers = [
***REMOVED******REMOVED******REMOVED***{ "EmailAddress": "example+1@example", "Name": "Example One" },
***REMOVED******REMOVED******REMOVED***{ "EmailAddress": "example+2@example.com", "Name": "Example Two" },
***REMOVED******REMOVED******REMOVED***{ "EmailAddress": "example+3@example.com", "Name": "Example Three" },
***REMOVED******REMOVED***]
***REMOVED******REMOVED***import_result = self.subscriber.import_subscribers(self.list_id, subscribers, True)
***REMOVED******REMOVED***self.assertEquals(len(import_result.FailureDetails), 1)
***REMOVED******REMOVED***self.assertEquals(import_result.FailureDetails[0].EmailAddress, "example+1@example")
***REMOVED******REMOVED***self.assertEquals(import_result.FailureDetails[0].Code, 1)
***REMOVED******REMOVED***self.assertEquals(import_result.FailureDetails[0].Message, "Invalid Email Address")
***REMOVED******REMOVED***self.assertEquals(import_result.TotalUniqueEmailsSubmitted, 3)
***REMOVED******REMOVED***self.assertEquals(import_result.TotalExistingSubscribers, 2)
***REMOVED******REMOVED***self.assertEquals(import_result.TotalNewSubscribers, 0)
***REMOVED******REMOVED***self.assertEquals(len(import_result.DuplicateEmailsInSubmission), 0)

***REMOVED***def test_ubsubscribe(self):
***REMOVED******REMOVED***self.subscriber.stub_request("subscribers/%s/unsubscribe.json" % self.list_id, None)
***REMOVED******REMOVED***self.subscriber.unsubscribe()

***REMOVED***def test_history(self):
***REMOVED******REMOVED***self.subscriber.stub_request("subscribers/%s/history.json?email=%s" % (self.list_id, urllib.quote(self.subscriber.email_address)), "subscriber_history.json")
***REMOVED******REMOVED***history = self.subscriber.history()
***REMOVED******REMOVED***self.assertEquals(len(history), 1)
***REMOVED******REMOVED***self.assertEquals(history[0].Name, "Campaign One")
***REMOVED******REMOVED***self.assertEquals(history[0].Type, "Campaign")
***REMOVED******REMOVED***self.assertEquals(history[0].ID, "fc0ce7105baeaf97f47c99be31d02a91")
***REMOVED******REMOVED***self.assertEquals(len(history[0].Actions), 6)
***REMOVED******REMOVED***self.assertEquals(history[0].Actions[0].Event, "Open")
***REMOVED******REMOVED***self.assertEquals(history[0].Actions[0].Date, "2010-10-12 13:18:00")
***REMOVED******REMOVED***self.assertEquals(history[0].Actions[0].IPAddress, "192.168.126.87")
***REMOVED******REMOVED***self.assertEquals(history[0].Actions[0].Detail, "")
