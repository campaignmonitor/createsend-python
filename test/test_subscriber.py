from six.moves.urllib.parse import quote
import unittest

from createsend import *

class SubscriberTestCase(object):

  def test_get(self):
    email = "subscriber@example.com"
    self.subscriber.stub_request("subscribers/%s.json?email=%s" % (self.list_id, quote(email)), "subscriber_details.json")
    subscriber = self.subscriber.get(self.list_id, email)
    self.assertEquals(subscriber.EmailAddress, email)
    self.assertEquals(subscriber.Name, "Subscriber One")
    self.assertEquals(subscriber.Date, "2010-10-25 10:28:00")
    self.assertEquals(subscriber.State, "Active")
    self.assertEquals(len(subscriber.CustomFields), 3)
    self.assertEquals(subscriber.CustomFields[0].Key, 'website')
    self.assertEquals(subscriber.CustomFields[0].Value, 'http://example.com')
    self.assertEquals(subscriber.ReadsEmailWith, "Gmail")

  def test_get_without_arguments(self):
    email = "subscriber@example.com"
    self.subscriber.stub_request("subscribers/%s.json?email=%s" % (self.list_id, quote(email)), "subscriber_details.json")
    subscriber = self.subscriber.get()
    self.assertEquals(subscriber.EmailAddress, email)
    self.assertEquals(subscriber.Name, "Subscriber One")
    self.assertEquals(subscriber.Date, "2010-10-25 10:28:00")
    self.assertEquals(subscriber.State, "Active")
    self.assertEquals(len(subscriber.CustomFields), 3)
    self.assertEquals(subscriber.CustomFields[0].Key, 'website')
    self.assertEquals(subscriber.CustomFields[0].Value, 'http://example.com')
    self.assertEquals(subscriber.ReadsEmailWith, "Gmail")

  def test_add_without_custom_fields(self):
    self.subscriber.stub_request("subscribers/%s.json" % self.list_id, "add_subscriber.json")
    email_address = self.subscriber.add(self.list_id, "subscriber@example.com", "Subscriber", [], True)
    self.assertEquals(email_address, "subscriber@example.com")

  def test_add_with_custom_fields(self):
    self.subscriber.stub_request("subscribers/%s.json" % self.list_id, "add_subscriber.json")
    custom_fields = [ { "Key": 'website', "Value": 'http://example.com/' } ]
    email_address = self.subscriber.add(self.list_id, "subscriber@example.com", "Subscriber", custom_fields, True)
    self.assertEquals(email_address, "subscriber@example.com")

  def test_add_with_custom_fields_including_multioption(self):
    self.subscriber.stub_request("subscribers/%s.json" % self.list_id, "add_subscriber.json")
    custom_fields = [ { "Key": 'multioptionselectone', "Value": 'myoption' },
      { "Key": 'multioptionselectmany', "Value": 'firstoption' },
      { "Key": 'multioptionselectmany', "Value": 'secondoption' } ]
    email_address = self.subscriber.add(self.list_id, "subscriber@example.com", "Subscriber", custom_fields, True)
    self.assertEquals(email_address, "subscriber@example.com")

  def test_update_with_custom_fields(self):
    new_email = "new_email_address@example.com"
    self.subscriber.stub_request("subscribers/%s.json?email=%s" % (self.list_id, quote(self.subscriber.email_address)), None)
    custom_fields = [ { "Key": 'website', "Value": 'http://example.com/' } ]
    self.subscriber.update(new_email, "Subscriber", custom_fields, True)
    self.assertEquals(self.subscriber.email_address, new_email)

  def test_update_with_custom_fields_including_clear_option(self):
    new_email = "new_email_address@example.com"
    self.subscriber.stub_request("subscribers/%s.json?email=%s" % (self.list_id, quote(self.subscriber.email_address)), None)
    custom_fields = [ { "Key": 'website', "Value": 'http://example.com/', "Clear": True } ]
    self.subscriber.update(new_email, "Subscriber", custom_fields, True)
    self.assertEquals(self.subscriber.email_address, new_email)

  def test_import_subscribers(self):
    self.subscriber.stub_request("subscribers/%s/import.json" % self.list_id, "import_subscribers.json")
    subscribers = [
      { "EmailAddress": "example+1@example.com", "Name": "Example One" },
      { "EmailAddress": "example+2@example.com", "Name": "Example Two" },
      { "EmailAddress": "example+3@example.com", "Name": "Example Three" },
    ]
    import_result = self.subscriber.import_subscribers(self.list_id, subscribers, True)
    self.assertEquals(len(import_result.FailureDetails), 0)
    self.assertEquals(import_result.TotalUniqueEmailsSubmitted, 3)
    self.assertEquals(import_result.TotalExistingSubscribers, 0)
    self.assertEquals(import_result.TotalNewSubscribers, 3)
    self.assertEquals(len(import_result.DuplicateEmailsInSubmission), 0)

  def test_import_subscribers_start_subscription_autoresponders(self):
    self.subscriber.stub_request("subscribers/%s/import.json" % self.list_id, "import_subscribers.json")
    subscribers = [
      { "EmailAddress": "example+1@example.com", "Name": "Example One" },
      { "EmailAddress": "example+2@example.com", "Name": "Example Two" },
      { "EmailAddress": "example+3@example.com", "Name": "Example Three" },
    ]
    import_result = self.subscriber.import_subscribers(self.list_id, subscribers, True, True)
    self.assertEquals(len(import_result.FailureDetails), 0)
    self.assertEquals(import_result.TotalUniqueEmailsSubmitted, 3)
    self.assertEquals(import_result.TotalExistingSubscribers, 0)
    self.assertEquals(import_result.TotalNewSubscribers, 3)
    self.assertEquals(len(import_result.DuplicateEmailsInSubmission), 0)

  def test_import_subscribers_with_custom_fields_including_clear_option(self):
    self.subscriber.stub_request("subscribers/%s/import.json" % self.list_id, "import_subscribers.json")
    subscribers = [
      { "EmailAddress": "example+1@example.com", "Name": "Example One", "CustomFields": [ { "Key": "website", "Value": "", "Clear": True } ] },
      { "EmailAddress": "example+2@example.com", "Name": "Example Two", "CustomFields": [ { "Key": "website", "Value": "", "Clear": False } ] },
      { "EmailAddress": "example+3@example.com", "Name": "Example Three", "CustomFields": [ { "Key": "website", "Value": "", "Clear": False } ] },
    ]
    import_result = self.subscriber.import_subscribers(self.list_id, subscribers, True)
    self.assertEquals(len(import_result.FailureDetails), 0)
    self.assertEquals(import_result.TotalUniqueEmailsSubmitted, 3)
    self.assertEquals(import_result.TotalExistingSubscribers, 0)
    self.assertEquals(import_result.TotalNewSubscribers, 3)
    self.assertEquals(len(import_result.DuplicateEmailsInSubmission), 0)

  def test_import_subscribers_partial_success(self):
    # Stub request with 400 Bad Request as the expected response status
    self.subscriber.stub_request("subscribers/%s/import.json" % self.list_id, "import_subscribers_partial_success.json", 400)
    subscribers = [
      { "EmailAddress": "example+1@example", "Name": "Example One" },
      { "EmailAddress": "example+2@example.com", "Name": "Example Two" },
      { "EmailAddress": "example+3@example.com", "Name": "Example Three" },
    ]
    import_result = self.subscriber.import_subscribers(self.list_id, subscribers, True)
    self.assertEquals(len(import_result.FailureDetails), 1)
    self.assertEquals(import_result.FailureDetails[0].EmailAddress, "example+1@example")
    self.assertEquals(import_result.FailureDetails[0].Code, 1)
    self.assertEquals(import_result.FailureDetails[0].Message, "Invalid Email Address")
    self.assertEquals(import_result.TotalUniqueEmailsSubmitted, 3)
    self.assertEquals(import_result.TotalExistingSubscribers, 2)
    self.assertEquals(import_result.TotalNewSubscribers, 0)
    self.assertEquals(len(import_result.DuplicateEmailsInSubmission), 0)

  def test_import_subscribers_complete_failure_because_of_bad_request(self):
    # Stub request with 400 Bad Request as the expected response status
    self.subscriber.stub_request("subscribers/%s/import.json" % self.list_id, "custom_api_error.json", 400)
    subscribers = [
      { "EmailAddress": "example+1@example", "Name": "Example One" },
      { "EmailAddress": "example+2@example.com", "Name": "Example Two" },
      { "EmailAddress": "example+3@example.com", "Name": "Example Three" },
    ]
    self.assertRaises(BadRequest, self.subscriber.import_subscribers, self.list_id, subscribers, True)

  def test_unsubscribe(self):
    self.subscriber.stub_request("subscribers/%s/unsubscribe.json" % self.list_id, None)
    self.subscriber.unsubscribe()

  def test_history(self):
    self.subscriber.stub_request("subscribers/%s/history.json?email=%s" % (self.list_id, quote(self.subscriber.email_address)), "subscriber_history.json")
    history = self.subscriber.history()
    self.assertEquals(len(history), 1)
    self.assertEquals(history[0].Name, "Campaign One")
    self.assertEquals(history[0].Type, "Campaign")
    self.assertEquals(history[0].ID, "fc0ce7105baeaf97f47c99be31d02a91")
    self.assertEquals(len(history[0].Actions), 6)
    self.assertEquals(history[0].Actions[0].Event, "Open")
    self.assertEquals(history[0].Actions[0].Date, "2010-10-12 13:18:00")
    self.assertEquals(history[0].Actions[0].IPAddress, "192.168.126.87")
    self.assertEquals(history[0].Actions[0].Detail, "")

  def test_delete(self):
    self.subscriber.stub_request("subscribers/%s.json?email=%s" % (self.list_id, quote(self.subscriber.email_address)), None)
    self.subscriber.delete()

class OAuthSubscriberTestCase(unittest.TestCase, SubscriberTestCase):
  """Test when using OAuth to authenticate"""
  def setUp(self):
    self.list_id = "d98h2938d9283d982u3d98u88"
    self.subscriber = Subscriber(
      {"access_token": "ASP95S4aR+9KsgfHB0dapTYxNA==", "refresh_token": "5S4aASP9R+9KsgfHB0dapTYxNA=="},
      self.list_id, "subscriber@example.com")

class ApiKeySubscriberTestCase(unittest.TestCase, SubscriberTestCase):
  """Test when using an API key to authenticate"""
  def setUp(self):
    self.list_id = "d98h2938d9283d982u3d98u88"
    self.subscriber = Subscriber(
      {'api_key': '123123123123123123123'},
      self.list_id, "subscriber@example.com")
