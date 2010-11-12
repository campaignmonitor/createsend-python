import unittest
import urllib

from createsend import *

class ListTestCase(unittest.TestCase):

  def setUp(self):
    self.api_key = '123123123123123123123'
    CreateSend.api_key = self.api_key
    self.client_id = "87y8d7qyw8d7yq8w7ydwqwd"
    self.list_id = "e3c5f034d68744f7881fdccf13c2daee"
    self.list = List(self.list_id)

  def test_create(self):
    self.list.stub_request("lists/%s.json" % self.client_id, "create_list.json")
    list_id = self.list.create(self.client_id, "List One", "", False, "")
    self.assertEquals(list_id, "e3c5f034d68744f7881fdccf13c2daee")

  def test_update(self):
    self.list.stub_request("lists/%s.json" % self.list.list_id, None)
    self.list.update("List One Renamed", "", False, "")

  def test_delete(self):
    self.list.stub_request("lists/%s.json" % self.list.list_id, None)
    self.list.delete()

  def test_create_custom_field(self):
    self.list.stub_request("lists/%s/customfields.json" % self.list.list_id, "create_custom_field.json")
    personalisation_tag = self.list.create_custom_field("new date field", "Date")
    self.assertEquals(personalisation_tag, "[newdatefield]")

  def test_delete_custom_field(self):
    custom_field_key = "[newdatefield]"
    self.list.stub_request("lists/%s/customfields/%s.json" % (self.list.list_id, urllib.quote(custom_field_key)), None)
    self.list.delete_custom_field(custom_field_key)

  def test_details(self):
    self.list.stub_request("lists/%s.json" % self.list.list_id, "list_details.json")
    details = self.list.details()
    self.assertEquals(details.ConfirmedOptIn, False)
    self.assertEquals(details.Title, "a non-basic list :)")
    self.assertEquals(details.UnsubscribePage, "")
    self.assertEquals(details.ListID, "2fe4c8f0373ce320e2200596d7ef168f")
    self.assertEquals(details.ConfirmationSuccessPage, "")

  def test_custom_fields(self):
    self.list.stub_request("lists/%s/customfields.json" % self.list.list_id, "custom_fields.json")
    cfs = self.list.custom_fields()
    self.assertEquals(len(cfs), 3)
    self.assertEquals(cfs[0].FieldName, "website")
    self.assertEquals(cfs[0].Key, "[website]")
    self.assertEquals(cfs[0].DataType, "Text")
    self.assertEquals(cfs[0].FieldOptions, [])

  def test_segments(self):
    self.list.stub_request("lists/%s/segments.json" % self.list.list_id, "segments.json")
    segments = self.list.segments()
    self.assertEquals(len(segments), 2)
    self.assertEquals(segments[0].ListID, 'a58ee1d3039b8bec838e6d1482a8a965')
    self.assertEquals(segments[0].SegmentID, '46aa5e01fd43381863d4e42cf277d3a9')
    self.assertEquals(segments[0].Title, 'Segment One')

  def test_stats(self):
    self.list.stub_request("lists/%s/stats.json" % self.list.list_id, "list_stats.json")
    stats = self.list.stats()
    self.assertEquals(stats.TotalActiveSubscribers, 6)
    self.assertEquals(stats.TotalUnsubscribes, 2)
    self.assertEquals(stats.TotalDeleted, 0)
    self.assertEquals(stats.TotalBounces, 0)

  def test_active(self):
    min_date = "2010-01-01"
    self.list.stub_request("lists/%s/active.json?date=%s&orderfield=email&page=1&pagesize=1000&orderdirection=asc" % (self.list.list_id, urllib.quote(min_date)), "active_subscribers.json")
    res = self.list.active(min_date)
    self.assertEquals(res.ResultsOrderedBy, "email")
    self.assertEquals(res.OrderDirection, "asc")
    self.assertEquals(res.PageNumber, 1)
    self.assertEquals(res.PageSize, 1000)
    self.assertEquals(res.RecordsOnThisPage, 5)
    self.assertEquals(res.TotalNumberOfRecords, 5)
    self.assertEquals(res.NumberOfPages, 1)
    self.assertEquals(len(res.Results), 5)
    self.assertEquals(res.Results[0].EmailAddress, "subs+7t8787Y@example.com")
    self.assertEquals(res.Results[0].Name, "Person One")
    self.assertEquals(res.Results[0].Date, "2010-10-25 10:28:00")
    self.assertEquals(res.Results[0].State, "Active")
    self.assertEquals(len(res.Results[0].CustomFields), 3)

  def test_unsubscribed(self):
    min_date = "2010-01-01"
    self.list.stub_request("lists/%s/unsubscribed.json?date=%s&orderfield=email&page=1&pagesize=1000&orderdirection=asc" % (self.list.list_id, urllib.quote(min_date)), "unsubscribed_subscribers.json")
    res = self.list.unsubscribed(min_date)
    self.assertEquals(res.ResultsOrderedBy, "email")
    self.assertEquals(res.OrderDirection, "asc")
    self.assertEquals(res.PageNumber, 1)
    self.assertEquals(res.PageSize, 1000)
    self.assertEquals(res.RecordsOnThisPage, 5)
    self.assertEquals(res.TotalNumberOfRecords, 5)
    self.assertEquals(res.NumberOfPages, 1)
    self.assertEquals(len(res.Results), 5)
    self.assertEquals(res.Results[0].EmailAddress, "subscriber@example.com")
    self.assertEquals(res.Results[0].Name, "Unsub One")
    self.assertEquals(res.Results[0].Date, "2010-10-25 13:11:00")
    self.assertEquals(res.Results[0].State, "Unsubscribed")
    self.assertEquals(len(res.Results[0].CustomFields), 0)

  def test_bounced(self):
    min_date = "2010-01-01"
    self.list.stub_request("lists/%s/bounced.json?date=%s&orderfield=email&page=1&pagesize=1000&orderdirection=asc" % (self.list.list_id, urllib.quote(min_date)), "bounced_subscribers.json")
    res = self.list.bounced(min_date)
    self.assertEquals(res.ResultsOrderedBy, "email")
    self.assertEquals(res.OrderDirection, "asc")
    self.assertEquals(res.PageNumber, 1)
    self.assertEquals(res.PageSize, 1000)
    self.assertEquals(res.RecordsOnThisPage, 1)
    self.assertEquals(res.TotalNumberOfRecords, 1)
    self.assertEquals(res.NumberOfPages, 1)
    self.assertEquals(len(res.Results), 1)
    self.assertEquals(res.Results[0].EmailAddress, "bouncedsubscriber@example.com")
    self.assertEquals(res.Results[0].Name, "Bounced One")
    self.assertEquals(res.Results[0].Date, "2010-10-25 13:11:00")
    self.assertEquals(res.Results[0].State, "Bounced")
    self.assertEquals(len(res.Results[0].CustomFields), 0)
