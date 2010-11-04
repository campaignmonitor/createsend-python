import unittest

from createsend import Segment

class SegmentTestCase(unittest.TestCase):

  def setUp(self):
    self.list_id = "98y2e98y289dh89h938389"
    self.segment = Segment(self.list_id)

  def test_subscribers(self):
    min_date = "2010-01-01"
    self.segment.stub_request("segment_subscribers.json")
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
    self.segment.stub_request(None)
    self.segment.delete()
