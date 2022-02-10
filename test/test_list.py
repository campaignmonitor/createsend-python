# -*- coding: utf-8 -*-

from six.moves.urllib.parse import quote
import unittest

from createsend.list import List


class ListTestCase(object):

***REMOVED******REMOVED***def test_create_without_unsubscribe_setting(self):
***REMOVED******REMOVED******REMOVED******REMOVED***l = List()
***REMOVED******REMOVED******REMOVED******REMOVED***l.stub_request("lists/%s.json" % self.client_id, "create_list.json")
***REMOVED******REMOVED******REMOVED******REMOVED***list_id = l.create(self.client_id, "List One", "", False, "")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(list_id, "e3c5f034d68744f7881fdccf13c2daee1234")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(l.list_id, "e3c5f034d68744f7881fdccf13c2daee1234")

***REMOVED******REMOVED***def test_create_with_unsubscribe_setting(self):
***REMOVED******REMOVED******REMOVED******REMOVED***l = List()
***REMOVED******REMOVED******REMOVED******REMOVED***l.stub_request("lists/%s.json" % self.client_id, "create_list.json")
***REMOVED******REMOVED******REMOVED******REMOVED***list_id = l.create(self.client_id, "List One",
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** "", False, "", "OnlyThisList")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(list_id, "e3c5f034d68744f7881fdccf13c2daee1234")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(l.list_id, "e3c5f034d68744f7881fdccf13c2daee1234")

***REMOVED******REMOVED***def test_update_without_unsubscribe_setting(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.stub_request("lists/%s.json" % self.list.list_id, None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.update("List One Renamed", "", False, "")

***REMOVED******REMOVED***def test_update_with_unsubscribe_setting(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.stub_request("lists/%s.json" % self.list.list_id, None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.update("List One Renamed", "", False, "", "OnlyThisList")

***REMOVED******REMOVED***def test_update_with_unsubscribe_setting_and_supp_list_options(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.stub_request("lists/%s.json" % self.list.list_id, None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.update("List One Renamed", "", False,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** "", "OnlyThisList", True, True)

***REMOVED******REMOVED***def test_delete(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.stub_request("lists/%s.json" % self.list.list_id, None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.delete()

***REMOVED******REMOVED***def test_create_custom_field(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.stub_request("lists/%s/customfields.json" % self.list.list_id,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** "create_custom_field.json", None,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** "{\"DataType\": \"Date\", \"FieldName\": \"new date field\", \"Options\": [], \"VisibleInPreferenceCenter\": true}")
***REMOVED******REMOVED******REMOVED******REMOVED***personalisation_tag = self.list.create_custom_field(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"new date field", "Date")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(personalisation_tag, "[newdatefield]")

***REMOVED******REMOVED***def test_create_custom_field_with_options_and_visible_in_preference_center(self):
***REMOVED******REMOVED******REMOVED******REMOVED***options = ["one", "two"]
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.stub_request("lists/%s/customfields.json" % self.list.list_id,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** "create_custom_field.json", None,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** "{\"DataType\": \"MultiSelectOne\", \"FieldName\": \"newsletter format\", \"Options\": [\"one\", \"two\"], \"VisibleInPreferenceCenter\": false}")
***REMOVED******REMOVED******REMOVED******REMOVED***personalisation_tag = self.list.create_custom_field("newsletter format",
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"MultiSelectOne", options, False)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(personalisation_tag, "[newdatefield]")

***REMOVED******REMOVED***def test_update_custom_field(self):
***REMOVED******REMOVED******REMOVED******REMOVED***key = "[mycustomfield]"
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.stub_request("lists/%s/customfields/%s.json" % (self.list.list_id, quote(key)),
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** "update_custom_field.json", None,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** "{\"FieldName\": \"my renamed custom field\", \"VisibleInPreferenceCenter\": true}")
***REMOVED******REMOVED******REMOVED******REMOVED***personalisation_tag = self.list.update_custom_field(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***key, "my renamed custom field", True)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(personalisation_tag, "[myrenamedcustomfield]")

***REMOVED******REMOVED***def test_delete_custom_field(self):
***REMOVED******REMOVED******REMOVED******REMOVED***custom_field_key = "[newdatefield]"
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.stub_request("lists/%s/customfields/%s.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.list.list_id, quote(custom_field_key)), None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.delete_custom_field(custom_field_key)

***REMOVED******REMOVED***def test_update_custom_field_options(self):
***REMOVED******REMOVED******REMOVED******REMOVED***custom_field_key = "[newdatefield]"
***REMOVED******REMOVED******REMOVED******REMOVED***new_options = ["one", "two", "three"]
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.stub_request("lists/%s/customfields/%s/options.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.list.list_id, quote(custom_field_key)), None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.update_custom_field_options(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***custom_field_key, new_options, True)

***REMOVED******REMOVED***def test_details(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.stub_request("lists/%s.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.list.list_id, "list_details.json")
***REMOVED******REMOVED******REMOVED******REMOVED***details = self.list.details()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(details.ConfirmedOptIn, False)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(details.Title, "a non-basic list :)")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(details.UnsubscribePage, "")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(details.ListID, "2fe4c8f0373ce320e2200596d7ef168f")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(details.ConfirmationSuccessPage, "")

***REMOVED******REMOVED***def test_custom_fields(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.stub_request("lists/%s/customfields.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.list.list_id, "custom_fields.json")
***REMOVED******REMOVED******REMOVED******REMOVED***cfs = self.list.custom_fields()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(cfs), 3)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(cfs[0].FieldName, "website")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(cfs[0].Key, "[website]")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(cfs[0].DataType, "Text")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(cfs[0].FieldOptions, [])
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(cfs[0].VisibleInPreferenceCenter, True)

***REMOVED******REMOVED***def test_custom_fields_utf8(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.stub_request("lists/%s/customfields.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.list.list_id, "custom_fields_utf8.json")
***REMOVED******REMOVED******REMOVED******REMOVED***cfs = self.list.custom_fields()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(cfs), 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(cfs[0].FieldName, "salary_range")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(cfs[0].FieldOptions, [
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***u"£0-20k", u"£20-30k", u"£30k+"])

***REMOVED******REMOVED***def test_segments(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.stub_request("lists/%s/segments.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.list.list_id, "segments.json")
***REMOVED******REMOVED******REMOVED******REMOVED***segments = self.list.segments()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(segments), 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(segments[0].ListID,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***'a58ee1d3039b8bec838e6d1482a8a965')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(segments[0].SegmentID,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***'46aa5e01fd43381863d4e42cf277d3a9')
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(segments[0].Title, 'Segment One')

***REMOVED******REMOVED***def test_stats(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.stub_request("lists/%s/stats.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.list.list_id, "list_stats.json")
***REMOVED******REMOVED******REMOVED******REMOVED***stats = self.list.stats()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(stats.TotalActiveSubscribers, 6)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(stats.TotalUnsubscribes, 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(stats.TotalDeleted, 0)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(stats.TotalBounces, 0)

***REMOVED******REMOVED***def test_active(self):
***REMOVED******REMOVED******REMOVED******REMOVED***min_date = "2010-01-01"
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.stub_request("lists/%s/active.json?date=%s&orderfield=email&page=1&pagesize=1000&orderdirection=asc&includetrackingpreference=False" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.list.list_id, quote(min_date)), "active_subscribers.json")
***REMOVED******REMOVED******REMOVED******REMOVED***res = self.list.active(min_date)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.ResultsOrderedBy, "email")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.OrderDirection, "asc")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.PageNumber, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.PageSize, 1000)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.RecordsOnThisPage, 5)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.TotalNumberOfRecords, 5)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.NumberOfPages, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(res.Results), 5)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].EmailAddress,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"subs+7t8787Y@example.com")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].Name, "Person One")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].Date, "2010-10-25 10:28:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].ListJoinedDate, "2010-10-24 10:28:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].State, "Active")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(res.Results[0].CustomFields), 5)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].CustomFields[0].Key, "website")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].CustomFields[
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***0].Value, "http://example.com")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].CustomFields[
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***1].Key, "multi select field")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].CustomFields[1].Value, "option one")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].CustomFields[
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***2].Key, "multi select field")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].CustomFields[2].Value, "option two")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].ReadsEmailWith, "Gmail")

***REMOVED******REMOVED***def test_active_with_tracking_preference_included(self):
***REMOVED******REMOVED******REMOVED******REMOVED***min_date = "2010-01-01"
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.stub_request("lists/%s/active.json?date=%s&orderfield=email&page=1&pagesize=1000&orderdirection=asc&includetrackingpreference=True" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.list.list_id, quote(min_date)), "active_subscribers_with_tracking_preference.json")
***REMOVED******REMOVED******REMOVED******REMOVED***res = self.list.active(min_date, include_tracking_preference=True)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.ResultsOrderedBy, "email")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.OrderDirection, "asc")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.PageNumber, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.PageSize, 1000)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.RecordsOnThisPage, 5)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.TotalNumberOfRecords, 5)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.NumberOfPages, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(res.Results), 5)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].EmailAddress,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"subs+7t8787Y@example.com")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].Name, "Person One")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].Date, "2010-10-25 10:28:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].ListJoinedDate, "2010-10-24 10:28:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].State, "Active")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(res.Results[0].CustomFields), 5)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].CustomFields[0].Key, "website")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].CustomFields[
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***0].Value, "http://example.com")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].CustomFields[
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***1].Key, "multi select field")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].CustomFields[1].Value, "option one")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].CustomFields[
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***2].Key, "multi select field")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].CustomFields[2].Value, "option two")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].ReadsEmailWith, "Gmail")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].ConsentToTrack, "Yes")

***REMOVED******REMOVED***def test_unconfirmed(self):
***REMOVED******REMOVED******REMOVED******REMOVED***min_date = "2010-01-01"
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.stub_request("lists/%s/unconfirmed.json?date=%s&orderfield=email&page=1&pagesize=1000&orderdirection=asc&includetrackingpreference=False" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.list.list_id, quote(min_date)), "unconfirmed_subscribers.json")
***REMOVED******REMOVED******REMOVED******REMOVED***res = self.list.unconfirmed(min_date)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.ResultsOrderedBy, "email")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.OrderDirection, "asc")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.PageNumber, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.PageSize, 1000)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.RecordsOnThisPage, 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.TotalNumberOfRecords, 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.NumberOfPages, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(res.Results), 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].EmailAddress,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"subs+7t8787Y@example.com")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].Name, "Unconfirmed One")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].State, "Unconfirmed")

***REMOVED******REMOVED***def test_unsubscribed(self):
***REMOVED******REMOVED******REMOVED******REMOVED***min_date = "2010-01-01"
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.stub_request("lists/%s/unsubscribed.json?date=%s&orderfield=email&page=1&pagesize=1000&orderdirection=asc&includetrackingpreference=False" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.list.list_id, quote(min_date)), "unsubscribed_subscribers.json")
***REMOVED******REMOVED******REMOVED******REMOVED***res = self.list.unsubscribed(min_date)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.ResultsOrderedBy, "email")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.OrderDirection, "asc")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.PageNumber, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.PageSize, 1000)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.RecordsOnThisPage, 5)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.TotalNumberOfRecords, 5)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.NumberOfPages, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(res.Results), 5)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***res.Results[0].EmailAddress, "subscriber@example.com")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].Name, "Unsub One")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].Date, "2010-10-25 13:11:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].ListJoinedDate, "2010-10-25 13:11:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].State, "Unsubscribed")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(res.Results[0].CustomFields), 0)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].ReadsEmailWith, "Gmail")

***REMOVED******REMOVED***def test_deleted(self):
***REMOVED******REMOVED******REMOVED******REMOVED***min_date = "2010-01-01"
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.stub_request("lists/%s/deleted.json?date=%s&orderfield=email&page=1&pagesize=1000&orderdirection=asc&includetrackingpreference=False" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.list.list_id, quote(min_date)), "deleted_subscribers.json")
***REMOVED******REMOVED******REMOVED******REMOVED***res = self.list.deleted(min_date)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.ResultsOrderedBy, "email")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.OrderDirection, "asc")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.PageNumber, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.PageSize, 1000)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.RecordsOnThisPage, 5)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.TotalNumberOfRecords, 5)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.NumberOfPages, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(res.Results), 5)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***res.Results[0].EmailAddress, "subscriber@example.com")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].Name, "Deleted One")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].Date, "2010-10-25 13:11:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].ListJoinedDate, "2010-10-25 13:11:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].State, "Deleted")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(res.Results[0].CustomFields), 0)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].ReadsEmailWith, "Gmail")

***REMOVED******REMOVED***def test_bounced(self):
***REMOVED******REMOVED******REMOVED******REMOVED***min_date = "2010-01-01"
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.stub_request("lists/%s/bounced.json?date=%s&orderfield=email&page=1&pagesize=1000&orderdirection=asc&includetrackingpreference=False" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.list.list_id, quote(min_date)), "bounced_subscribers.json")
***REMOVED******REMOVED******REMOVED******REMOVED***res = self.list.bounced(min_date)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.ResultsOrderedBy, "email")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.OrderDirection, "asc")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.PageNumber, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.PageSize, 1000)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.RecordsOnThisPage, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.TotalNumberOfRecords, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.NumberOfPages, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(res.Results), 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].EmailAddress,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"bouncedsubscriber@example.com")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].Name, "Bounced One")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].Date, "2010-10-25 13:11:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].ListJoinedDate, "2010-10-25 13:11:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].State, "Bounced")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(res.Results[0].CustomFields), 0)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].ReadsEmailWith, "")

***REMOVED******REMOVED***def test_webhooks(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.stub_request("lists/%s/webhooks.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.list.list_id, "list_webhooks.json")
***REMOVED******REMOVED******REMOVED******REMOVED***hooks = self.list.webhooks()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(hooks), 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(hooks[0].WebhookID, "943678317049bc13")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(hooks[0].Events), 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(hooks[0].Events[0], "Deactivate")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(hooks[0].Url, "http://www.postbin.org/d9w8ud9wud9w")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(hooks[0].Status, "Active")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(hooks[0].PayloadFormat, "Json")

***REMOVED******REMOVED***def test_create_webhook(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.stub_request("lists/%s/webhooks.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.list.list_id, "create_list_webhook.json")
***REMOVED******REMOVED******REMOVED******REMOVED***webhook_id = self.list.create_webhook(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***["Unsubscribe", "Spam"], "http://example.com/unsub", "json")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(webhook_id, "6a783d359bd44ef62c6ca0d3eda4412a")

***REMOVED******REMOVED***def test_test_webhook(self):
***REMOVED******REMOVED******REMOVED******REMOVED***webhook_id = "jiuweoiwueoiwueowiueo"
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.stub_request("lists/%s/webhooks/%s/test.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.list.list_id, webhook_id), None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.test_webhook(webhook_id)

***REMOVED******REMOVED***def test_delete_webhook(self):
***REMOVED******REMOVED******REMOVED******REMOVED***webhook_id = "jiuweoiwueoiwueowiueo"
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.stub_request("lists/%s/webhooks/%s.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.list.list_id, webhook_id), None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.delete_webhook(webhook_id)

***REMOVED******REMOVED***def test_activate_webhook(self):
***REMOVED******REMOVED******REMOVED******REMOVED***webhook_id = "jiuweoiwueoiwueowiueo"
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.stub_request("lists/%s/webhooks/%s/activate.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** (self.list.list_id, webhook_id), None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.activate_webhook(webhook_id)

***REMOVED******REMOVED***def test_deactivate_webhook(self):
***REMOVED******REMOVED******REMOVED******REMOVED***webhook_id = "jiuweoiwueoiwueowiueo"
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.stub_request(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"lists/%s/webhooks/%s/deactivate.json" % (self.list.list_id, webhook_id), None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.list.deactivate_webhook(webhook_id)


class OAuthListTestCase(unittest.TestCase, ListTestCase):
***REMOVED******REMOVED***"""Test when using OAuth to authenticate"""

***REMOVED******REMOVED***def setUp(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.client_id = "87y8d7qyw8d7yq8w7ydwqwd"
***REMOVED******REMOVED******REMOVED******REMOVED***self.list_id = "e3c5f034d68744f7881fdccf13c2daee"
***REMOVED******REMOVED******REMOVED******REMOVED***self.list = List({"access_token": "ASP95S4aR+9KsgfHB0dapTYxNA==",
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"refresh_token": "5S4aASP9R+9KsgfHB0dapTYxNA=="}, self.list_id)


class ApiKeyListTestCase(unittest.TestCase, ListTestCase):
***REMOVED******REMOVED***"""Test when using an API key to authenticate"""

***REMOVED******REMOVED***def setUp(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.client_id = "87y8d7qyw8d7yq8w7ydwqwd"
***REMOVED******REMOVED******REMOVED******REMOVED***self.list_id = "e3c5f034d68744f7881fdccf13c2daee"
***REMOVED******REMOVED******REMOVED******REMOVED***self.list = List({'api_key': '123123123123123123123'}, self.list_id)
