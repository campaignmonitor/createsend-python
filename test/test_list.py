from urllib.parse import quote
import unittest

from createsend.list import List


class ListTestCase:

    def test_create_without_unsubscribe_setting(self):
        l = List()
        l.stub_request("lists/%s.json" % self.client_id, "create_list.json")
        list_id = l.create(self.client_id, "List One", "", False, "")
        self.assertEqual(list_id, "e3c5f034d68744f7881fdccf13c2daee1234")
        self.assertEqual(l.list_id, "e3c5f034d68744f7881fdccf13c2daee1234")

    def test_create_with_unsubscribe_setting(self):
        l = List()
        l.stub_request("lists/%s.json" % self.client_id, "create_list.json")
        list_id = l.create(self.client_id, "List One",
                           "", False, "", "OnlyThisList")
        self.assertEqual(list_id, "e3c5f034d68744f7881fdccf13c2daee1234")
        self.assertEqual(l.list_id, "e3c5f034d68744f7881fdccf13c2daee1234")

    def test_update_without_unsubscribe_setting(self):
        self.list.stub_request("lists/%s.json" % self.list.list_id, None)
        self.list.update("List One Renamed", "", False, "")

    def test_update_with_unsubscribe_setting(self):
        self.list.stub_request("lists/%s.json" % self.list.list_id, None)
        self.list.update("List One Renamed", "", False, "", "OnlyThisList")

    def test_update_with_unsubscribe_setting_and_supp_list_options(self):
        self.list.stub_request("lists/%s.json" % self.list.list_id, None)
        self.list.update("List One Renamed", "", False,
                         "", "OnlyThisList", True, True)

    def test_delete(self):
        self.list.stub_request("lists/%s.json" % self.list.list_id, None)
        self.list.delete()

    def test_create_custom_field(self):
        self.list.stub_request("lists/%s/customfields.json" % self.list.list_id,
                               "create_custom_field.json", None,
                               "{\"DataType\": \"Date\", \"FieldName\": \"new date field\", \"Options\": [], \"VisibleInPreferenceCenter\": true}")
        personalisation_tag = self.list.create_custom_field(
            "new date field", "Date")
        self.assertEqual(personalisation_tag, "[newdatefield]")

    def test_create_custom_field_with_options_and_visible_in_preference_center(self):
        options = ["one", "two"]
        self.list.stub_request("lists/%s/customfields.json" % self.list.list_id,
                               "create_custom_field.json", None,
                               "{\"DataType\": \"MultiSelectOne\", \"FieldName\": \"newsletter format\", \"Options\": [\"one\", \"two\"], \"VisibleInPreferenceCenter\": false}")
        personalisation_tag = self.list.create_custom_field("newsletter format",
                                                            "MultiSelectOne", options, False)
        self.assertEqual(personalisation_tag, "[newdatefield]")

    def test_update_custom_field(self):
        key = "[mycustomfield]"
        self.list.stub_request(f"lists/{self.list.list_id}/customfields/{quote(key)}.json",
                               "update_custom_field.json", None,
                               "{\"FieldName\": \"my renamed custom field\", \"VisibleInPreferenceCenter\": true}")
        personalisation_tag = self.list.update_custom_field(
            key, "my renamed custom field", True)
        self.assertEqual(personalisation_tag, "[myrenamedcustomfield]")

    def test_delete_custom_field(self):
        custom_field_key = "[newdatefield]"
        self.list.stub_request("lists/%s/customfields/%s.json" %
                               (self.list.list_id, quote(custom_field_key)), None)
        self.list.delete_custom_field(custom_field_key)

    def test_update_custom_field_options(self):
        custom_field_key = "[newdatefield]"
        new_options = ["one", "two", "three"]
        self.list.stub_request("lists/%s/customfields/%s/options.json" %
                               (self.list.list_id, quote(custom_field_key)), None)
        self.list.update_custom_field_options(
            custom_field_key, new_options, True)

    def test_details(self):
        self.list.stub_request("lists/%s.json" %
                               self.list.list_id, "list_details.json")
        details = self.list.details()
        self.assertEqual(details.ConfirmedOptIn, False)
        self.assertEqual(details.Title, "a non-basic list :)")
        self.assertEqual(details.UnsubscribePage, "")
        self.assertEqual(details.ListID, "2fe4c8f0373ce320e2200596d7ef168f")
        self.assertEqual(details.ConfirmationSuccessPage, "")

    def test_custom_fields(self):
        self.list.stub_request("lists/%s/customfields.json" %
                               self.list.list_id, "custom_fields.json")
        cfs = self.list.custom_fields()
        self.assertEqual(len(cfs), 3)
        self.assertEqual(cfs[0].FieldName, "website")
        self.assertEqual(cfs[0].Key, "[website]")
        self.assertEqual(cfs[0].DataType, "Text")
        self.assertEqual(cfs[0].FieldOptions, [])
        self.assertEqual(cfs[0].VisibleInPreferenceCenter, True)

    def test_custom_fields_utf8(self):
        self.list.stub_request("lists/%s/customfields.json" %
                               self.list.list_id, "custom_fields_utf8.json")
        cfs = self.list.custom_fields()
        self.assertEqual(len(cfs), 2)
        self.assertEqual(cfs[0].FieldName, "salary_range")
        self.assertEqual(cfs[0].FieldOptions, [
                          "£0-20k", "£20-30k", "£30k+"])

    def test_segments(self):
        self.list.stub_request("lists/%s/segments.json" %
                               self.list.list_id, "segments.json")
        segments = self.list.segments()
        self.assertEqual(len(segments), 2)
        self.assertEqual(segments[0].ListID,
                          'a58ee1d3039b8bec838e6d1482a8a965')
        self.assertEqual(segments[0].SegmentID,
                          '46aa5e01fd43381863d4e42cf277d3a9')
        self.assertEqual(segments[0].Title, 'Segment One')

    def test_stats(self):
        self.list.stub_request("lists/%s/stats.json" %
                               self.list.list_id, "list_stats.json")
        stats = self.list.stats()
        self.assertEqual(stats.TotalActiveSubscribers, 6)
        self.assertEqual(stats.TotalUnsubscribes, 2)
        self.assertEqual(stats.TotalDeleted, 0)
        self.assertEqual(stats.TotalBounces, 0)

    def test_active(self):
        min_date = "2010-01-01"
        self.list.stub_request("lists/%s/active.json?date=%s&orderfield=email&page=1&pagesize=1000&orderdirection=asc&includetrackingpreference=False" %
                               (self.list.list_id, quote(min_date)), "active_subscribers.json")
        res = self.list.active(min_date)
        self.assertEqual(res.ResultsOrderedBy, "email")
        self.assertEqual(res.OrderDirection, "asc")
        self.assertEqual(res.PageNumber, 1)
        self.assertEqual(res.PageSize, 1000)
        self.assertEqual(res.RecordsOnThisPage, 5)
        self.assertEqual(res.TotalNumberOfRecords, 5)
        self.assertEqual(res.NumberOfPages, 1)
        self.assertEqual(len(res.Results), 5)
        self.assertEqual(res.Results[0].EmailAddress,
                          "subs+7t8787Y@example.com")
        self.assertEqual(res.Results[0].Name, "Person One")
        self.assertEqual(res.Results[0].Date, "2010-10-25 10:28:00")
        self.assertEqual(res.Results[0].ListJoinedDate, "2010-10-24 10:28:00")
        self.assertEqual(res.Results[0].State, "Active")
        self.assertEqual(len(res.Results[0].CustomFields), 5)
        self.assertEqual(res.Results[0].CustomFields[0].Key, "website")
        self.assertEqual(res.Results[0].CustomFields[
                          0].Value, "https://example.com")
        self.assertEqual(res.Results[0].CustomFields[
                          1].Key, "multi select field")
        self.assertEqual(res.Results[0].CustomFields[1].Value, "option one")
        self.assertEqual(res.Results[0].CustomFields[
                          2].Key, "multi select field")
        self.assertEqual(res.Results[0].CustomFields[2].Value, "option two")
        self.assertEqual(res.Results[0].ReadsEmailWith, "Gmail")

    def test_active_with_tracking_preference_included(self):
        min_date = "2010-01-01"
        self.list.stub_request("lists/%s/active.json?date=%s&orderfield=email&page=1&pagesize=1000&orderdirection=asc&includetrackingpreference=True" %
                               (self.list.list_id, quote(min_date)), "active_subscribers_with_tracking_preference.json")
        res = self.list.active(min_date, include_tracking_preference=True)
        self.assertEqual(res.ResultsOrderedBy, "email")
        self.assertEqual(res.OrderDirection, "asc")
        self.assertEqual(res.PageNumber, 1)
        self.assertEqual(res.PageSize, 1000)
        self.assertEqual(res.RecordsOnThisPage, 5)
        self.assertEqual(res.TotalNumberOfRecords, 5)
        self.assertEqual(res.NumberOfPages, 1)
        self.assertEqual(len(res.Results), 5)
        self.assertEqual(res.Results[0].EmailAddress,
                          "subs+7t8787Y@example.com")
        self.assertEqual(res.Results[0].Name, "Person One")
        self.assertEqual(res.Results[0].Date, "2010-10-25 10:28:00")
        self.assertEqual(res.Results[0].ListJoinedDate, "2010-10-24 10:28:00")
        self.assertEqual(res.Results[0].State, "Active")
        self.assertEqual(len(res.Results[0].CustomFields), 5)
        self.assertEqual(res.Results[0].CustomFields[0].Key, "website")
        self.assertEqual(res.Results[0].CustomFields[
                          0].Value, "https://example.com")
        self.assertEqual(res.Results[0].CustomFields[
                          1].Key, "multi select field")
        self.assertEqual(res.Results[0].CustomFields[1].Value, "option one")
        self.assertEqual(res.Results[0].CustomFields[
                          2].Key, "multi select field")
        self.assertEqual(res.Results[0].CustomFields[2].Value, "option two")
        self.assertEqual(res.Results[0].ReadsEmailWith, "Gmail")
        self.assertEqual(res.Results[0].ConsentToTrack, "Yes")

    def test_unconfirmed(self):
        min_date = "2010-01-01"
        self.list.stub_request("lists/%s/unconfirmed.json?date=%s&orderfield=email&page=1&pagesize=1000&orderdirection=asc&includetrackingpreference=False" %
                               (self.list.list_id, quote(min_date)), "unconfirmed_subscribers.json")
        res = self.list.unconfirmed(min_date)
        self.assertEqual(res.ResultsOrderedBy, "email")
        self.assertEqual(res.OrderDirection, "asc")
        self.assertEqual(res.PageNumber, 1)
        self.assertEqual(res.PageSize, 1000)
        self.assertEqual(res.RecordsOnThisPage, 2)
        self.assertEqual(res.TotalNumberOfRecords, 2)
        self.assertEqual(res.NumberOfPages, 1)
        self.assertEqual(len(res.Results), 2)
        self.assertEqual(res.Results[0].EmailAddress,
                          "subs+7t8787Y@example.com")
        self.assertEqual(res.Results[0].Name, "Unconfirmed One")
        self.assertEqual(res.Results[0].State, "Unconfirmed")

    def test_unsubscribed(self):
        min_date = "2010-01-01"
        self.list.stub_request("lists/%s/unsubscribed.json?date=%s&orderfield=email&page=1&pagesize=1000&orderdirection=asc&includetrackingpreference=False" %
                               (self.list.list_id, quote(min_date)), "unsubscribed_subscribers.json")
        res = self.list.unsubscribed(min_date)
        self.assertEqual(res.ResultsOrderedBy, "email")
        self.assertEqual(res.OrderDirection, "asc")
        self.assertEqual(res.PageNumber, 1)
        self.assertEqual(res.PageSize, 1000)
        self.assertEqual(res.RecordsOnThisPage, 5)
        self.assertEqual(res.TotalNumberOfRecords, 5)
        self.assertEqual(res.NumberOfPages, 1)
        self.assertEqual(len(res.Results), 5)
        self.assertEqual(
            res.Results[0].EmailAddress, "subscriber@example.com")
        self.assertEqual(res.Results[0].Name, "Unsub One")
        self.assertEqual(res.Results[0].Date, "2010-10-25 13:11:00")
        self.assertEqual(res.Results[0].ListJoinedDate, "2010-10-25 13:11:00")
        self.assertEqual(res.Results[0].State, "Unsubscribed")
        self.assertEqual(len(res.Results[0].CustomFields), 0)
        self.assertEqual(res.Results[0].ReadsEmailWith, "Gmail")

    def test_deleted(self):
        min_date = "2010-01-01"
        self.list.stub_request("lists/%s/deleted.json?date=%s&orderfield=email&page=1&pagesize=1000&orderdirection=asc&includetrackingpreference=False" %
                               (self.list.list_id, quote(min_date)), "deleted_subscribers.json")
        res = self.list.deleted(min_date)
        self.assertEqual(res.ResultsOrderedBy, "email")
        self.assertEqual(res.OrderDirection, "asc")
        self.assertEqual(res.PageNumber, 1)
        self.assertEqual(res.PageSize, 1000)
        self.assertEqual(res.RecordsOnThisPage, 5)
        self.assertEqual(res.TotalNumberOfRecords, 5)
        self.assertEqual(res.NumberOfPages, 1)
        self.assertEqual(len(res.Results), 5)
        self.assertEqual(
            res.Results[0].EmailAddress, "subscriber@example.com")
        self.assertEqual(res.Results[0].Name, "Deleted One")
        self.assertEqual(res.Results[0].Date, "2010-10-25 13:11:00")
        self.assertEqual(res.Results[0].ListJoinedDate, "2010-10-25 13:11:00")
        self.assertEqual(res.Results[0].State, "Deleted")
        self.assertEqual(len(res.Results[0].CustomFields), 0)
        self.assertEqual(res.Results[0].ReadsEmailWith, "Gmail")

    def test_bounced(self):
        min_date = "2010-01-01"
        self.list.stub_request("lists/%s/bounced.json?date=%s&orderfield=email&page=1&pagesize=1000&orderdirection=asc&includetrackingpreference=False" %
                               (self.list.list_id, quote(min_date)), "bounced_subscribers.json")
        res = self.list.bounced(min_date)
        self.assertEqual(res.ResultsOrderedBy, "email")
        self.assertEqual(res.OrderDirection, "asc")
        self.assertEqual(res.PageNumber, 1)
        self.assertEqual(res.PageSize, 1000)
        self.assertEqual(res.RecordsOnThisPage, 1)
        self.assertEqual(res.TotalNumberOfRecords, 1)
        self.assertEqual(res.NumberOfPages, 1)
        self.assertEqual(len(res.Results), 1)
        self.assertEqual(res.Results[0].EmailAddress,
                          "bouncedsubscriber@example.com")
        self.assertEqual(res.Results[0].Name, "Bounced One")
        self.assertEqual(res.Results[0].Date, "2010-10-25 13:11:00")
        self.assertEqual(res.Results[0].ListJoinedDate, "2010-10-25 13:11:00")
        self.assertEqual(res.Results[0].State, "Bounced")
        self.assertEqual(len(res.Results[0].CustomFields), 0)
        self.assertEqual(res.Results[0].ReadsEmailWith, "")

    def test_webhooks(self):
        self.list.stub_request("lists/%s/webhooks.json" %
                               self.list.list_id, "list_webhooks.json")
        hooks = self.list.webhooks()
        self.assertEqual(len(hooks), 2)
        self.assertEqual(hooks[0].WebhookID, "943678317049bc13")
        self.assertEqual(len(hooks[0].Events), 1)
        self.assertEqual(hooks[0].Events[0], "Deactivate")
        self.assertEqual(hooks[0].Url, "https://www.postbin.org/d9w8ud9wud9w")
        self.assertEqual(hooks[0].Status, "Active")
        self.assertEqual(hooks[0].PayloadFormat, "Json")

    def test_create_webhook(self):
        self.list.stub_request("lists/%s/webhooks.json" %
                               self.list.list_id, "create_list_webhook.json")
        webhook_id = self.list.create_webhook(
            ["Unsubscribe", "Spam"], "https://example.com/unsub", "json")
        self.assertEqual(webhook_id, "6a783d359bd44ef62c6ca0d3eda4412a")

    def test_test_webhook(self):
        webhook_id = "jiuweoiwueoiwueowiueo"
        self.list.stub_request("lists/%s/webhooks/%s/test.json" %
                               (self.list.list_id, webhook_id), None)
        self.list.test_webhook(webhook_id)

    def test_delete_webhook(self):
        webhook_id = "jiuweoiwueoiwueowiueo"
        self.list.stub_request("lists/%s/webhooks/%s.json" %
                               (self.list.list_id, webhook_id), None)
        self.list.delete_webhook(webhook_id)

    def test_activate_webhook(self):
        webhook_id = "jiuweoiwueoiwueowiueo"
        self.list.stub_request("lists/%s/webhooks/%s/activate.json" %
                               (self.list.list_id, webhook_id), None)
        self.list.activate_webhook(webhook_id)

    def test_deactivate_webhook(self):
        webhook_id = "jiuweoiwueoiwueowiueo"
        self.list.stub_request(
            f"lists/{self.list.list_id}/webhooks/{webhook_id}/deactivate.json", None)
        self.list.deactivate_webhook(webhook_id)


class OAuthListTestCase(unittest.TestCase, ListTestCase):
    """Test when using OAuth to authenticate"""

    def setUp(self):
        self.client_id = "87y8d7qyw8d7yq8w7ydwqwd"
        self.list_id = "e3c5f034d68744f7881fdccf13c2daee"
        self.list = List({"access_token": "ASP95S4aR+9KsgfHB0dapTYxNA==",
                          "refresh_token": "5S4aASP9R+9KsgfHB0dapTYxNA=="}, self.list_id)


class ApiKeyListTestCase(unittest.TestCase, ListTestCase):
    """Test when using an API key to authenticate"""

    def setUp(self):
        self.client_id = "87y8d7qyw8d7yq8w7ydwqwd"
        self.list_id = "e3c5f034d68744f7881fdccf13c2daee"
        self.list = List({'api_key': '123123123123123123123'}, self.list_id)
