import unittest
import urllib

***REMOVED***

class SegmentTestCase(object):

***REMOVED***def test_create(self):
***REMOVED******REMOVED***list_id = "2983492834987394879837498"
***REMOVED******REMOVED***rules = [ { "Subject": "EmailAddress", "Clauses": [ "CONTAINS example.com" ] } ]
***REMOVED******REMOVED***s = Segment()
***REMOVED******REMOVED***s.stub_request("segments/%s.json" % list_id, "create_segment.json")
***REMOVED******REMOVED***segment_id = s.create(list_id, "new segment title", rules)
***REMOVED******REMOVED***self.assertEquals(segment_id, "0246c2aea610a3545d9780bf6ab890061234")
***REMOVED******REMOVED***self.assertEquals(s.segment_id, "0246c2aea610a3545d9780bf6ab890061234")

***REMOVED***def test_update(self):
***REMOVED******REMOVED***rules = [ { "Subject": "Name", "Clauses": [ "EQUALS subscriber" ] } ]
***REMOVED******REMOVED***self.segment.stub_request("segments/%s.json" % self.segment.segment_id, None)
***REMOVED******REMOVED***self.segment.update("new title for segment", rules)

***REMOVED***def test_add_rule(self):
***REMOVED******REMOVED***clauses = [ "CONTAINS example.com" ]
***REMOVED******REMOVED***self.segment.stub_request("segments/%s/rules.json" % self.segment.segment_id, None)
***REMOVED******REMOVED***self.segment.add_rule("EmailAddress", clauses)

***REMOVED***def test_subscribers(self):
***REMOVED******REMOVED***min_date = "2010-01-01"
***REMOVED******REMOVED***self.segment.stub_request("segments/%s/active.json?date=%s&orderfield=email&page=1&pagesize=1000&orderdirection=asc" % (self.segment.segment_id, urllib.quote(min_date)), "segment_subscribers.json")
***REMOVED******REMOVED***res = self.segment.subscribers(min_date)
***REMOVED******REMOVED***self.assertEquals(res.ResultsOrderedBy, "email")
***REMOVED******REMOVED***self.assertEquals(res.OrderDirection, "asc")
***REMOVED******REMOVED***self.assertEquals(res.PageNumber, 1)
***REMOVED******REMOVED***self.assertEquals(res.PageSize, 1000)
***REMOVED******REMOVED***self.assertEquals(res.RecordsOnThisPage, 2)
***REMOVED******REMOVED***self.assertEquals(res.TotalNumberOfRecords, 2)
***REMOVED******REMOVED***self.assertEquals(res.NumberOfPages, 1)
***REMOVED******REMOVED***self.assertEquals(len(res.Results), 2)
***REMOVED******REMOVED***self.assertEquals(res.Results[0].EmailAddress, "personone@example.com")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].Name, "Person One")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].Date, "2010-10-27 13:13:00")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].State, "Active")
***REMOVED******REMOVED***self.assertEquals(res.Results[0].CustomFields, [])

***REMOVED***def test_delete(self):
***REMOVED******REMOVED***self.segment.stub_request("segments/%s.json" % self.segment.segment_id, None)
***REMOVED******REMOVED***self.segment.delete()

***REMOVED***def test_clear_rules(self):
***REMOVED******REMOVED***self.segment.stub_request("segments/%s/rules.json" % self.segment.segment_id, None)
***REMOVED******REMOVED***self.segment.clear_rules()
***REMOVED******REMOVED***
***REMOVED***def test_details(self):
***REMOVED******REMOVED***self.segment.stub_request("segments/%s.json" % self.segment.segment_id, "segment_details.json")
***REMOVED******REMOVED***res = self.segment.details()
***REMOVED******REMOVED***self.assertEquals(res.ActiveSubscribers, 0)
***REMOVED******REMOVED***self.assertEquals(len(res.Rules), 2)
***REMOVED******REMOVED***self.assertEquals(res.Rules[0].Subject, "EmailAddress")
***REMOVED******REMOVED***self.assertEquals(len(res.Rules[0].Clauses), 1)
***REMOVED******REMOVED***self.assertEquals(res.Rules[0].Clauses[0], "CONTAINS @hello.com")
***REMOVED******REMOVED***self.assertEquals(res.ListID, "2bea949d0bf96148c3e6a209d2e82060")
***REMOVED******REMOVED***self.assertEquals(res.SegmentID, "dba84a225d5ce3d19105d7257baac46f")
***REMOVED******REMOVED***self.assertEquals(res.Title, "My Segment")

class OAuthSegmentTestCase(unittest.TestCase, SegmentTestCase):
***REMOVED***"""Test when using OAuth to authenticate"""
***REMOVED***def setUp(self):
***REMOVED******REMOVED***self.segment_id = "98y2e98y289dh89h938389"
***REMOVED******REMOVED***self.segment = Segment(self.segment_id)
***REMOVED******REMOVED***self.segment.auth({"access_token": "98u9q8uw9ddw", "refresh_token": "9u09i02e3"})

class ApiKeySegmentTestCase(unittest.TestCase, SegmentTestCase):
***REMOVED***"""Test when using an API key to authenticate"""
***REMOVED***def setUp(self):
***REMOVED******REMOVED***self.segment_id = "98y2e98y289dh89h938389"
***REMOVED******REMOVED***self.segment = Segment(self.segment_id)
***REMOVED******REMOVED***self.segment.auth({'api_key': '123123123123123123123'})
