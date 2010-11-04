import unittest

from createsend import Segment

class SegmentTestCase(unittest.TestCase):

***REMOVED***def setUp(self):
***REMOVED******REMOVED***self.segment_id = "98y2e98y289dh89h938389"
***REMOVED******REMOVED***self.segment = Segment(self.segment_id)

***REMOVED***def test_subscribers(self):
***REMOVED******REMOVED***min_date = "2010-01-01"
***REMOVED******REMOVED***self.segment.stub_request("segment_subscribers.json")
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
***REMOVED******REMOVED***self.segment.stub_request(None)
***REMOVED******REMOVED***self.segment.delete()
