import unittest
import urllib

from createsend import *

class SegmentTestCase(object):

  def test_create(self):
    list_id = "2983492834987394879837498"
    rules = [ { "Subject": "EmailAddress", "Clauses": [ "CONTAINS example.com" ] } ]
    s = Segment()
    s.stub_request("segments/%s.json" % list_id, "create_segment.json")
    segment_id = s.create(list_id, "new segment title", rules)
    self.assertEquals(segment_id, "0246c2aea610a3545d9780bf6ab890061234")
    self.assertEquals(s.segment_id, "0246c2aea610a3545d9780bf6ab890061234")

  def test_update(self):
    rules = [ { "Subject": "Name", "Clauses": [ "EQUALS subscriber" ] } ]
    self.segment.stub_request("segments/%s.json" % self.segment.segment_id, None)
    self.segment.update("new title for segment", rules)

  def test_add_rule(self):
    clauses = [ "CONTAINS example.com" ]
    self.segment.stub_request("segments/%s/rules.json" % self.segment.segment_id, None)
    self.segment.add_rule("EmailAddress", clauses)

  def test_subscribers(self):
    min_date = "2010-01-01"
    self.segment.stub_request("segments/%s/active.json?date=%s&orderfield=email&page=1&pagesize=1000&orderdirection=asc" % (self.segment.segment_id, urllib.quote(min_date)), "segment_subscribers.json")
    res = self.segment.subscribers(min_date)
    self.assertEquals(res.ResultsOrderedBy, "email")
    self.assertEquals(res.OrderDirection, "asc")
    self.assertEquals(res.PageNumber, 1)
    self.assertEquals(res.PageSize, 1000)
    self.assertEquals(res.RecordsOnThisPage, 2)
    self.assertEquals(res.TotalNumberOfRecords, 2)
    self.assertEquals(res.NumberOfPages, 1)
    self.assertEquals(len(res.Results), 2)
    self.assertEquals(res.Results[0].EmailAddress, "personone@example.com")
    self.assertEquals(res.Results[0].Name, "Person One")
    self.assertEquals(res.Results[0].Date, "2010-10-27 13:13:00")
    self.assertEquals(res.Results[0].State, "Active")
    self.assertEquals(res.Results[0].CustomFields, [])

  def test_delete(self):
    self.segment.stub_request("segments/%s.json" % self.segment.segment_id, None)
    self.segment.delete()

  def test_clear_rules(self):
    self.segment.stub_request("segments/%s/rules.json" % self.segment.segment_id, None)
    self.segment.clear_rules()
    
  def test_details(self):
    self.segment.stub_request("segments/%s.json" % self.segment.segment_id, "segment_details.json")
    res = self.segment.details()
    self.assertEquals(res.ActiveSubscribers, 0)
    self.assertEquals(len(res.Rules), 2)
    self.assertEquals(res.Rules[0].Subject, "EmailAddress")
    self.assertEquals(len(res.Rules[0].Clauses), 1)
    self.assertEquals(res.Rules[0].Clauses[0], "CONTAINS @hello.com")
    self.assertEquals(res.ListID, "2bea949d0bf96148c3e6a209d2e82060")
    self.assertEquals(res.SegmentID, "dba84a225d5ce3d19105d7257baac46f")
    self.assertEquals(res.Title, "My Segment")

class OAuthSegmentTestCase(unittest.TestCase, SegmentTestCase):
  """Test when using OAuth to authenticate"""
  def setUp(self):
    self.segment_id = "98y2e98y289dh89h938389"
    self.segment = Segment(self.segment_id)
    self.segment.auth({"access_token": "98u9q8uw9ddw", "refresh_token": "9u09i02e3"})

class ApiKeySegmentTestCase(unittest.TestCase, SegmentTestCase):
  """Test when using an API key to authenticate"""
  def setUp(self):
    self.segment_id = "98y2e98y289dh89h938389"
    self.segment = Segment(self.segment_id)
    self.segment.auth({'api_key': '123123123123123123123'})
