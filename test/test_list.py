import unittest

from createsend import List

class ListTestCase(unittest.TestCase):

***REMOVED***def setUp(self):
***REMOVED******REMOVED***self.client_id = "87y8d7qyw8d7yq8w7ydwqwd"
***REMOVED******REMOVED***self.list_id = "e3c5f034d68744f7881fdccf13c2daee"
***REMOVED******REMOVED***self.list = List(self.list_id)

***REMOVED***def test_create(self):
***REMOVED******REMOVED***self.list.stub_request("create_list.json")
***REMOVED******REMOVED***list_id = self.list.create(self.client_id, "List One", "", False, "")
***REMOVED******REMOVED***self.assertEquals(list_id, "e3c5f034d68744f7881fdccf13c2daee")

***REMOVED***def test_update(self):
***REMOVED******REMOVED***self.list.stub_request(None)
***REMOVED******REMOVED***self.list.update("List One Renamed", "", False, "")

***REMOVED***def test_delete(self):
***REMOVED******REMOVED***self.list.stub_request(None)
***REMOVED******REMOVED***self.list.delete()

***REMOVED***def test_create_custom_field(self):
***REMOVED******REMOVED***self.list.stub_request("create_custom_field.json")
***REMOVED******REMOVED***personalisation_tag = self.list.create_custom_field("new date field", "Date")
***REMOVED******REMOVED***self.assertEquals(personalisation_tag, "[newdatefield]")

***REMOVED***def test_delete_custom_field(self):
***REMOVED******REMOVED***custom_field_key = "[newdatefield]"
***REMOVED******REMOVED***self.list.stub_request(None)
***REMOVED******REMOVED***self.list.delete_custom_field(custom_field_key)

***REMOVED***def test_details(self):
***REMOVED******REMOVED***self.list.stub_request("list_details.json")
***REMOVED******REMOVED***details = self.list.details()
***REMOVED******REMOVED***self.assertEquals(details.ConfirmedOptIn, False)
***REMOVED******REMOVED***self.assertEquals(details.Title, "a non-basic list :)")
***REMOVED******REMOVED***self.assertEquals(details.UnsubscribePage, "")
***REMOVED******REMOVED***self.assertEquals(details.ListID, "2fe4c8f0373ce320e2200596d7ef168f")
***REMOVED******REMOVED***self.assertEquals(details.ConfirmationSuccessPage, "")

***REMOVED***def test_custom_fields(self):
***REMOVED******REMOVED***self.list.stub_request("custom_fields.json")
***REMOVED******REMOVED***cfs = self.list.custom_fields()
***REMOVED******REMOVED***self.assertEquals(len(cfs), 3)
***REMOVED******REMOVED***self.assertEquals(cfs[0].FieldName, "website")
***REMOVED******REMOVED***self.assertEquals(cfs[0].Key, "[website]")
***REMOVED******REMOVED***self.assertEquals(cfs[0].DataType, "Text")
***REMOVED******REMOVED***self.assertEquals(cfs[0].FieldOptions, [])

***REMOVED***def test_segments(self):
***REMOVED******REMOVED***self.list.stub_request("segments.json")
***REMOVED******REMOVED***segments = self.list.segments()
***REMOVED******REMOVED***self.assertEquals(len(segments), 2)
***REMOVED******REMOVED***self.assertEquals(segments[0].ListID, 'a58ee1d3039b8bec838e6d1482a8a965')
***REMOVED******REMOVED***self.assertEquals(segments[0].SegmentID, '46aa5e01fd43381863d4e42cf277d3a9')
***REMOVED******REMOVED***self.assertEquals(segments[0].Title, 'Segment One')

***REMOVED***def test_stats(self):
***REMOVED******REMOVED***self.list.stub_request("list_stats.json")
***REMOVED******REMOVED***stats = self.list.stats()
***REMOVED******REMOVED***self.assertEquals(stats.TotalActiveSubscribers, 6)
***REMOVED******REMOVED***self.assertEquals(stats.TotalUnsubscribes, 2)
***REMOVED******REMOVED***self.assertEquals(stats.TotalDeleted, 0)
***REMOVED******REMOVED***self.assertEquals(stats.TotalBounces, 0)

***REMOVED***def test_active(self):
***REMOVED******REMOVED***min_date = "2010-01-01"
***REMOVED******REMOVED***self.list.stub_request("active_subscribers.json")
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
***REMOVED******REMOVED***self.assertEquals(len(res.Results[0].CustomFields), 3)

***REMOVED***def test_unsubscribed(self):
***REMOVED******REMOVED***min_date = "2010-01-01"
***REMOVED******REMOVED***self.list.stub_request("unsubscribed_subscribers.json")
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

***REMOVED***def test_bounced(self):
***REMOVED******REMOVED***min_date = "2010-01-01"
***REMOVED******REMOVED***self.list.stub_request("bounced_subscribers.json")
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
