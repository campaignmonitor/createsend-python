import unittest
import urllib

***REMOVED***

class ListTestCase(object):

***REMOVED***def test_create_without_unsubscribe_setting(self):
***REMOVED******REMOVED***l = List()
***REMOVED******REMOVED***l.stub_request("lists/%s.json" % self.client_id, "create_list.json")
***REMOVED******REMOVED***list_id = l.create(self.client_id, "List One", "", False, "")
***REMOVED******REMOVED***self.assertEquals(list_id, "e3c5f034d68744f7881fdccf13c2daee1234")
***REMOVED******REMOVED***self.assertEquals(l.list_id, "e3c5f034d68744f7881fdccf13c2daee1234")

***REMOVED***def test_create_with_unsubscribe_setting(self):
***REMOVED******REMOVED***l = List()
***REMOVED******REMOVED***l.stub_request("lists/%s.json" % self.client_id, "create_list.json")
***REMOVED******REMOVED***list_id = l.create(self.client_id, "List One", "", False, "", "OnlyThisList")
***REMOVED******REMOVED***self.assertEquals(list_id, "e3c5f034d68744f7881fdccf13c2daee1234")
***REMOVED******REMOVED***self.assertEquals(l.list_id, "e3c5f034d68744f7881fdccf13c2daee1234")

***REMOVED***def test_update_without_unsubscribe_setting(self):
***REMOVED******REMOVED***self.list.stub_request("lists/%s.json" % self.list.list_id, None)
***REMOVED******REMOVED***self.list.update("List One Renamed", "", False, "")

***REMOVED***def test_update_with_unsubscribe_setting(self):
***REMOVED******REMOVED***self.list.stub_request("lists/%s.json" % self.list.list_id, None)
***REMOVED******REMOVED***self.list.update("List One Renamed", "", False, "", "OnlyThisList")

***REMOVED***def test_update_with_unsubscribe_setting_and_supp_list_options(self):
***REMOVED******REMOVED***self.list.stub_request("lists/%s.json" % self.list.list_id, None)
***REMOVED******REMOVED***self.list.update("List One Renamed", "", False, "", "OnlyThisList", True, True)

***REMOVED***def test_delete(self):
***REMOVED******REMOVED***self.list.stub_request("lists/%s.json" % self.list.list_id, None)
***REMOVED******REMOVED***self.list.delete()

***REMOVED***def test_create_custom_field(self):
***REMOVED******REMOVED***self.list.stub_request("lists/%s/customfields.json" % self.list.list_id,
***REMOVED******REMOVED***"create_custom_field.json", None,
***REMOVED******REMOVED***"{\"DataType\": \"Date\", \"FieldName\": \"new date field\", \"Options\": [], \"VisibleInPreferenceCenter\": true}")
***REMOVED******REMOVED***personalisation_tag = self.list.create_custom_field("new date field", "Date")
***REMOVED******REMOVED***self.assertEquals(personalisation_tag, "[newdatefield]")

***REMOVED***def test_create_custom_field_with_options_and_visible_in_preference_center(self):
***REMOVED******REMOVED***options = ["one", "two"]
***REMOVED******REMOVED***self.list.stub_request("lists/%s/customfields.json" % self.list.list_id,
***REMOVED******REMOVED***"create_custom_field.json", None,
***REMOVED******REMOVED***"{\"DataType\": \"MultiSelectOne\", \"FieldName\": \"newsletter format\", \"Options\": [\"one\", \"two\"], \"VisibleInPreferenceCenter\": false}")
***REMOVED******REMOVED***personalisation_tag = self.list.create_custom_field("newsletter format",
***REMOVED******REMOVED***"MultiSelectOne", options, False)
***REMOVED******REMOVED***self.assertEquals(personalisation_tag, "[newdatefield]")

***REMOVED***def test_update_custom_field(self):
***REMOVED******REMOVED***key = "[mycustomfield]"
***REMOVED******REMOVED***self.list.stub_request("lists/%s/customfields/%s.json" % (self.list.list_id, urllib.quote(key)),
***REMOVED******REMOVED***"update_custom_field.json", None,
***REMOVED******REMOVED***"{\"FieldName\": \"my renamed custom field\", \"VisibleInPreferenceCenter\": true}")
***REMOVED******REMOVED***personalisation_tag = self.list.update_custom_field(key, "my renamed custom field", True)
***REMOVED******REMOVED***self.assertEquals(personalisation_tag, "[myrenamedcustomfield]")

***REMOVED***def test_delete_custom_field(self):
***REMOVED******REMOVED***custom_field_key = "[newdatefield]"
***REMOVED******REMOVED***self.list.stub_request("lists/%s/customfields/%s.json" % (self.list.list_id, urllib.quote(custom_field_key)), None)
***REMOVED******REMOVED***self.list.delete_custom_field(custom_field_key)

***REMOVED***def test_update_custom_field_options(self):
***REMOVED******REMOVED***custom_field_key = "[newdatefield]"
***REMOVED******REMOVED***new_options = [ "one", "two", "three" ]
***REMOVED******REMOVED***self.list.stub_request("lists/%s/customfields/%s/options.json" % (self.list.list_id, urllib.quote(custom_field_key)), None)
***REMOVED******REMOVED***self.list.update_custom_field_options(custom_field_key, new_options, True)

***REMOVED***def test_details(self):
***REMOVED******REMOVED***self.list.stub_request("lists/%s.json" % self.list.list_id, "list_details.json")
***REMOVED******REMOVED***details = self.list.details()
***REMOVED******REMOVED***self.assertEquals(details.ConfirmedOptIn, False)
***REMOVED******REMOVED***self.assertEquals(details.Title, "a non-basic list :)")
***REMOVED******REMOVED***self.assertEquals(details.UnsubscribePage, "")
***REMOVED******REMOVED***self.assertEquals(details.ListID, "2fe4c8f0373ce320e2200596d7ef168f")
***REMOVED******REMOVED***self.assertEquals(details.ConfirmationSuccessPage, "")

***REMOVED***def test_custom_fields(self):
***REMOVED******REMOVED***self.list.stub_request("lists/%s/customfields.json" % self.list.list_id, "custom_fields.json")
***REMOVED******REMOVED***cfs = self.list.custom_fields()
***REMOVED******REMOVED***self.assertEquals(len(cfs), 3)
***REMOVED******REMOVED***self.assertEquals(cfs[0].FieldName, "website")
***REMOVED******REMOVED***self.assertEquals(cfs[0].Key, "[website]")
***REMOVED******REMOVED***self.assertEquals(cfs[0].DataType, "Text")
***REMOVED******REMOVED***self.assertEquals(cfs[0].FieldOptions, [])
***REMOVED******REMOVED***self.assertEquals(cfs[0].VisibleInPreferenceCenter, True)

***REMOVED***def test_segments(self):
***REMOVED******REMOVED***self.list.stub_request("lists/%s/segments.json" % self.list.list_id, "segments.json")
***REMOVED******REMOVED***segments = self.list.segments()
***REMOVED******REMOVED***self.assertEquals(len(segments), 2)
***REMOVED******REMOVED***self.assertEquals(segments[0].ListID, 'a58ee1d3039b8bec838e6d1482a8a965')
***REMOVED******REMOVED***self.assertEquals(segments[0].SegmentID, '46aa5e01fd43381863d4e42cf277d3a9')
***REMOVED******REMOVED***self.assertEquals(segments[0].Title, 'Segment One')

***REMOVED***def test_stats(self):
***REMOVED******REMOVED***self.list.stub_request("lists/%s/stats.json" % self.list.list_id, "list_stats.json")
***REMOVED******REMOVED***stats = self.list.stats()
***REMOVED******REMOVED***self.assertEquals(stats.TotalActiveSubscribers, 6)
***REMOVED******REMOVED***self.assertEquals(stats.TotalUnsubscribes, 2)
***REMOVED******REMOVED***self.assertEquals(stats.TotalDeleted, 0)
***REMOVED******REMOVED***self.assertEquals(stats.TotalBounces, 0)

***REMOVED***def test_active(self):
***REMOVED******REMOVED***min_date = "2010-01-01"
***REMOVED******REMOVED***self.list.stub_request("lists/%s/active.json?date=%s&orderfield=email&page=1&pagesize=1000&orderdirection=asc" % (self.list.list_id, urllib.quote(min_date)), "active_subscribers.json")
***REMOVED******REMOVED***res = self.list.active(min_date)
***REMOVED******REMOVED***self.assertEquals(res.ResultsOrderedBy, "email")
***REMOVED******REMOVED***self.assertEquals(res.OrderDirection, "asc")
***REMOVED******REMOVED***self.assertEquals(res.PageNumber, 1)
***REMOVED******REMOVED***self.assertEquals(res.PageSize, 1000)
***REMOVED******REMOVED***self.assertEquals(res.RecordsOnThisPage, 5)
***REMOVED******REMOVED***self.assertEquals(res.TotalNumberOfRecords, 5)
***REMOVED******REMOVED***self.assertEquals(res.NumberOfPages, 1)
***REMOVED******REMOVED***self.assertEquals(len(res.Results), 5)
***REMOVED******REMOVED***self.assertEquals(res.Results[0].EmailAddress, "subs+7t8787Y@example.com")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].Name, "Person One")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].Date, "2010-10-25 10:28:00")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].State, "Active")
***REMOVED******REMOVED***self.assertEquals(len(res.Results[0].CustomFields), 5)
***REMOVED******REMOVED***self.assertEquals(res.Results[0].CustomFields[0].Key, "website")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].CustomFields[0].Value, "http://example.com")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].CustomFields[1].Key, "multi select field")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].CustomFields[1].Value, "option one")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].CustomFields[2].Key, "multi select field")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].CustomFields[2].Value, "option two")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].ReadsEmailWith, "Gmail")

***REMOVED***def test_active(self):
***REMOVED******REMOVED***min_date = "2010-01-01"
***REMOVED******REMOVED***self.list.stub_request("lists/%s/unconfirmed.json?date=%s&orderfield=email&page=1&pagesize=1000&orderdirection=asc" % (self.list.list_id, urllib.quote(min_date)), "unconfirmed_subscribers.json")
***REMOVED******REMOVED***res = self.list.unconfirmed(min_date)
***REMOVED******REMOVED***self.assertEquals(res.ResultsOrderedBy, "email")
***REMOVED******REMOVED***self.assertEquals(res.OrderDirection, "asc")
***REMOVED******REMOVED***self.assertEquals(res.PageNumber, 1)
***REMOVED******REMOVED***self.assertEquals(res.PageSize, 1000)
***REMOVED******REMOVED***self.assertEquals(res.RecordsOnThisPage, 2)
***REMOVED******REMOVED***self.assertEquals(res.TotalNumberOfRecords, 2)
***REMOVED******REMOVED***self.assertEquals(res.NumberOfPages, 1)
***REMOVED******REMOVED***self.assertEquals(len(res.Results), 2)
***REMOVED******REMOVED***self.assertEquals(res.Results[0].EmailAddress, "subs+7t8787Y@example.com")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].Name, "Unconfirmed One")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].State, "Unconfirmed")

***REMOVED***def test_unsubscribed(self):
***REMOVED******REMOVED***min_date = "2010-01-01"
***REMOVED******REMOVED***self.list.stub_request("lists/%s/unsubscribed.json?date=%s&orderfield=email&page=1&pagesize=1000&orderdirection=asc" % (self.list.list_id, urllib.quote(min_date)), "unsubscribed_subscribers.json")
***REMOVED******REMOVED***res = self.list.unsubscribed(min_date)
***REMOVED******REMOVED***self.assertEquals(res.ResultsOrderedBy, "email")
***REMOVED******REMOVED***self.assertEquals(res.OrderDirection, "asc")
***REMOVED******REMOVED***self.assertEquals(res.PageNumber, 1)
***REMOVED******REMOVED***self.assertEquals(res.PageSize, 1000)
***REMOVED******REMOVED***self.assertEquals(res.RecordsOnThisPage, 5)
***REMOVED******REMOVED***self.assertEquals(res.TotalNumberOfRecords, 5)
***REMOVED******REMOVED***self.assertEquals(res.NumberOfPages, 1)
***REMOVED******REMOVED***self.assertEquals(len(res.Results), 5)
***REMOVED******REMOVED***self.assertEquals(res.Results[0].EmailAddress, "subscriber@example.com")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].Name, "Unsub One")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].Date, "2010-10-25 13:11:00")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].State, "Unsubscribed")
***REMOVED******REMOVED***self.assertEquals(len(res.Results[0].CustomFields), 0)
***REMOVED******REMOVED***self.assertEquals(res.Results[0].ReadsEmailWith, "Gmail")

***REMOVED***def test_deleted(self):
***REMOVED******REMOVED***min_date = "2010-01-01"
***REMOVED******REMOVED***self.list.stub_request("lists/%s/deleted.json?date=%s&orderfield=email&page=1&pagesize=1000&orderdirection=asc" % (self.list.list_id, urllib.quote(min_date)), "deleted_subscribers.json")
***REMOVED******REMOVED***res = self.list.deleted(min_date)
***REMOVED******REMOVED***self.assertEquals(res.ResultsOrderedBy, "email")
***REMOVED******REMOVED***self.assertEquals(res.OrderDirection, "asc")
***REMOVED******REMOVED***self.assertEquals(res.PageNumber, 1)
***REMOVED******REMOVED***self.assertEquals(res.PageSize, 1000)
***REMOVED******REMOVED***self.assertEquals(res.RecordsOnThisPage, 5)
***REMOVED******REMOVED***self.assertEquals(res.TotalNumberOfRecords, 5)
***REMOVED******REMOVED***self.assertEquals(res.NumberOfPages, 1)
***REMOVED******REMOVED***self.assertEquals(len(res.Results), 5)
***REMOVED******REMOVED***self.assertEquals(res.Results[0].EmailAddress, "subscriber@example.com")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].Name, "Deleted One")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].Date, "2010-10-25 13:11:00")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].State, "Deleted")
***REMOVED******REMOVED***self.assertEquals(len(res.Results[0].CustomFields), 0)
***REMOVED******REMOVED***self.assertEquals(res.Results[0].ReadsEmailWith, "Gmail")

***REMOVED***def test_bounced(self):
***REMOVED******REMOVED***min_date = "2010-01-01"
***REMOVED******REMOVED***self.list.stub_request("lists/%s/bounced.json?date=%s&orderfield=email&page=1&pagesize=1000&orderdirection=asc" % (self.list.list_id, urllib.quote(min_date)), "bounced_subscribers.json")
***REMOVED******REMOVED***res = self.list.bounced(min_date)
***REMOVED******REMOVED***self.assertEquals(res.ResultsOrderedBy, "email")
***REMOVED******REMOVED***self.assertEquals(res.OrderDirection, "asc")
***REMOVED******REMOVED***self.assertEquals(res.PageNumber, 1)
***REMOVED******REMOVED***self.assertEquals(res.PageSize, 1000)
***REMOVED******REMOVED***self.assertEquals(res.RecordsOnThisPage, 1)
***REMOVED******REMOVED***self.assertEquals(res.TotalNumberOfRecords, 1)
***REMOVED******REMOVED***self.assertEquals(res.NumberOfPages, 1)
***REMOVED******REMOVED***self.assertEquals(len(res.Results), 1)
***REMOVED******REMOVED***self.assertEquals(res.Results[0].EmailAddress, "bouncedsubscriber@example.com")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].Name, "Bounced One")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].Date, "2010-10-25 13:11:00")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].State, "Bounced")
***REMOVED******REMOVED***self.assertEquals(len(res.Results[0].CustomFields), 0)
***REMOVED******REMOVED***self.assertEquals(res.Results[0].ReadsEmailWith, "")

***REMOVED***def test_webhooks(self):
***REMOVED******REMOVED***self.list.stub_request("lists/%s/webhooks.json" % self.list.list_id, "list_webhooks.json")
***REMOVED******REMOVED***hooks = self.list.webhooks()
***REMOVED******REMOVED***self.assertEquals(len(hooks), 2)
***REMOVED******REMOVED***self.assertEquals(hooks[0].WebhookID, "943678317049bc13")
***REMOVED******REMOVED***self.assertEquals(len(hooks[0].Events), 1)
***REMOVED******REMOVED***self.assertEquals(hooks[0].Events[0], "Deactivate")
***REMOVED******REMOVED***self.assertEquals(hooks[0].Url, "http://www.postbin.org/d9w8ud9wud9w")
***REMOVED******REMOVED***self.assertEquals(hooks[0].Status, "Active")
***REMOVED******REMOVED***self.assertEquals(hooks[0].PayloadFormat, "Json")

***REMOVED***def test_create_webhook(self):
***REMOVED******REMOVED***self.list.stub_request("lists/%s/webhooks.json" % self.list.list_id, "create_list_webhook.json")
***REMOVED******REMOVED***webhook_id = self.list.create_webhook(["Unsubscribe", "Spam"], "http://example.com/unsub", "json")
***REMOVED******REMOVED***self.assertEquals(webhook_id, "6a783d359bd44ef62c6ca0d3eda4412a")

***REMOVED***def test_test_webhook(self):
***REMOVED******REMOVED***webhook_id = "jiuweoiwueoiwueowiueo"
***REMOVED******REMOVED***self.list.stub_request("lists/%s/webhooks/%s/test.json" % (self.list.list_id, webhook_id), None)
***REMOVED******REMOVED***self.list.test_webhook(webhook_id)

***REMOVED***def test_delete_webhook(self):
***REMOVED******REMOVED***webhook_id = "jiuweoiwueoiwueowiueo"
***REMOVED******REMOVED***self.list.stub_request("lists/%s/webhooks/%s.json" % (self.list.list_id, webhook_id), None)
***REMOVED******REMOVED***self.list.delete_webhook(webhook_id)

***REMOVED***def test_activate_webhook(self):
***REMOVED******REMOVED***webhook_id = "jiuweoiwueoiwueowiueo"
***REMOVED******REMOVED***self.list.stub_request("lists/%s/webhooks/%s/activate.json" % (self.list.list_id, webhook_id), None)
***REMOVED******REMOVED***self.list.activate_webhook(webhook_id)

***REMOVED***def test_deactivate_webhook(self):
***REMOVED******REMOVED***webhook_id = "jiuweoiwueoiwueowiueo"
***REMOVED******REMOVED***self.list.stub_request("lists/%s/webhooks/%s/deactivate.json" % (self.list.list_id, webhook_id), None)
***REMOVED******REMOVED***self.list.deactivate_webhook(webhook_id)

class OAuthListTestCase(unittest.TestCase, ListTestCase):
***REMOVED***"""Test when using OAuth to authenticate"""
***REMOVED***def setUp(self):
***REMOVED******REMOVED***self.client_id = "87y8d7qyw8d7yq8w7ydwqwd"
***REMOVED******REMOVED***self.list_id = "e3c5f034d68744f7881fdccf13c2daee"
***REMOVED******REMOVED***self.list = List({"access_token": "98u9q8uw9ddw", "refresh_token": "9u09i02e3"}, self.list_id)

class ApiKeyListTestCase(unittest.TestCase, ListTestCase):
***REMOVED***"""Test when using an API key to authenticate"""
***REMOVED***def setUp(self):
***REMOVED******REMOVED***self.client_id = "87y8d7qyw8d7yq8w7ydwqwd"
***REMOVED******REMOVED***self.list_id = "e3c5f034d68744f7881fdccf13c2daee"
***REMOVED******REMOVED***self.list = List({'api_key': '123123123123123123123'}, self.list_id)
