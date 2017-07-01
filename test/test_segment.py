from six.moves.urllib.parse import quote
import unittest

from createsend.segment import Segment


class SegmentTestCase(object):

***REMOVED******REMOVED***def test_create(self):
***REMOVED******REMOVED******REMOVED******REMOVED***list_id = "2983492834987394879837498"
***REMOVED******REMOVED******REMOVED******REMOVED***rulegroups = [{"Rules": [{"RuleType": "EmailAddress", "Clause": "CONTAINS example.com"},***REMOVED***{
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"RuleType": "Name", "Clause": "EQUALS subscriber"}]}]
***REMOVED******REMOVED******REMOVED******REMOVED***s = Segment()
***REMOVED******REMOVED******REMOVED******REMOVED***s.stub_request("segments/%s.json" % list_id, "create_segment.json", None,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** "{\"RuleGroups\": [{\"Rules\": [{\"Clause\": \"CONTAINS example.com\", \"RuleType\": \"EmailAddress\"}, {\"Clause\": \"EQUALS subscriber\", \"RuleType\": \"Name\"}]}], \"Title\": \"new segment title\"}")
***REMOVED******REMOVED******REMOVED******REMOVED***segment_id = s.create(list_id, "new segment title", rulegroups)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(segment_id, "0246c2aea610a3545d9780bf6ab890061234")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(s.segment_id, "0246c2aea610a3545d9780bf6ab890061234")

***REMOVED******REMOVED***def test_update(self):
***REMOVED******REMOVED******REMOVED******REMOVED***rulegroups = [
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{"Rules": [{"RuleType": "Name", "Clause": "EQUALS subscriber"}]}]
***REMOVED******REMOVED******REMOVED******REMOVED***self.segment.stub_request("segments/%s.json" % self.segment.segment_id, None,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"{\"Rules\": [{\"Clause\": \"EQUALS subscriber\", \"RuleType\": \"Name\"}], \"Title\": \"new title for segment\"}")
***REMOVED******REMOVED******REMOVED******REMOVED***self.segment.update("new title for segment", rulegroups)

***REMOVED******REMOVED***def test_add_rulegroup(self):
***REMOVED******REMOVED******REMOVED******REMOVED***rulegroup = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Rules": [{"RuleType": "EmailAddress", "Clause": "CONTAINS example.com"}]}
***REMOVED******REMOVED******REMOVED******REMOVED***self.segment.stub_request("segments/%s/rules.json" % self.segment.segment_id, None, None,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"{\"Rules\": [{\"Clause\": \"CONTAINS example.com\", \"RuleType\": \"EmailAddress\"}]}")
***REMOVED******REMOVED******REMOVED******REMOVED***self.segment.add_rulegroup(rulegroup)

***REMOVED******REMOVED***def test_subscribers(self):
***REMOVED******REMOVED******REMOVED******REMOVED***min_date = "2010-01-01"
***REMOVED******REMOVED******REMOVED******REMOVED***self.segment.stub_request("segments/%s/active.json?date=%s&orderfield=email&page=1&pagesize=1000&orderdirection=asc" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***(self.segment.segment_id, quote(min_date)), "segment_subscribers.json")
***REMOVED******REMOVED******REMOVED******REMOVED***res = self.segment.subscribers(min_date)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.ResultsOrderedBy, "email")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.OrderDirection, "asc")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.PageNumber, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.PageSize, 1000)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.RecordsOnThisPage, 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.TotalNumberOfRecords, 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.NumberOfPages, 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(res.Results), 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].EmailAddress, "personone@example.com")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].Name, "Person One")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].Date, "2010-10-27 13:13:00")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].State, "Active")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Results[0].CustomFields, [])

***REMOVED******REMOVED***def test_delete(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.segment.stub_request("segments/%s.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.segment.segment_id, None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.segment.delete()

***REMOVED******REMOVED***def test_clear_rules(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.segment.stub_request("segments/%s/rules.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.segment.segment_id, None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.segment.clear_rules()

***REMOVED******REMOVED***def test_details(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.segment.stub_request("segments/%s.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.segment.segment_id, "segment_details.json")
***REMOVED******REMOVED******REMOVED******REMOVED***res = self.segment.details()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.ActiveSubscribers, 0)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(len(res.RuleGroups), 2)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.RuleGroups[0].Rules[0].RuleType, "EmailAddress")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.RuleGroups[0].Rules[
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***0].Clause, "CONTAINS @hello.com")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.RuleGroups[1].Rules[0].RuleType, "Name")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.RuleGroups[1].Rules[0].Clause, "PROVIDED")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.ListID, "2bea949d0bf96148c3e6a209d2e82060")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.SegmentID, "dba84a225d5ce3d19105d7257baac46f")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(res.Title, "My Segment")


class OAuthSegmentTestCase(unittest.TestCase, SegmentTestCase):
***REMOVED******REMOVED***"""Test when using OAuth to authenticate"""

***REMOVED******REMOVED***def setUp(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.segment_id = "98y2e98y289dh89h938389"
***REMOVED******REMOVED******REMOVED******REMOVED***self.segment = Segment(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{"access_token": "ASP95S4aR+9KsgfHB0dapTYxNA==", "refresh_token": "5S4aASP9R+9KsgfHB0dapTYxNA=="}, self.segment_id)


class ApiKeySegmentTestCase(unittest.TestCase, SegmentTestCase):
***REMOVED******REMOVED***"""Test when using an API key to authenticate"""

***REMOVED******REMOVED***def setUp(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.segment_id = "98y2e98y289dh89h938389"
***REMOVED******REMOVED******REMOVED******REMOVED***self.segment = Segment(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{'api_key': '123123123123123123123'}, self.segment_id)
