import unittest
import urllib

***REMOVED***

class TransactionalTestCase(object):

***REMOVED******REMOVED***def test_smart_email_list(self):
***REMOVED******REMOVED******REMOVED******REMOVED***status = "all"
***REMOVED******REMOVED******REMOVED******REMOVED***self.tx.stub_request("transactional/smartEmail?status=%s" % status, "tx_smartemails.json")
***REMOVED******REMOVED******REMOVED******REMOVED***list = self.tx.smart_email_list(status)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(list[0].Name, "Welcome email")

***REMOVED******REMOVED***def test_active_smart_email_list(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.tx.stub_request("transactional/smartEmail?status=active", "tx_smartemails.json")
***REMOVED******REMOVED******REMOVED******REMOVED***list = self.tx.smart_email_list(status="active")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(list[0].Status, "Active")

***REMOVED******REMOVED***def test_smart_email_list_with_client(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.tx.stub_request("transactional/smartEmail?status=all&clientID=%s" % self.client_id, "tx_smartemails.json")
***REMOVED******REMOVED******REMOVED******REMOVED***list = self.tx.smart_email_list(client_id=self.client_id)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(list[0].Name, "Welcome email")

***REMOVED******REMOVED***def test_smart_email_details(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.tx.stub_request("transactional/smartEmail/%s" % self.smart_email_id, "tx_smartemail_details.json")
***REMOVED******REMOVED******REMOVED******REMOVED***email = self.tx.smart_email_details(self.smart_email_id)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(email.Name, "Reset Password")

***REMOVED******REMOVED***def test_smart_email_send_single(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.tx.stub_request("transactional/smartEmail/%s/send" % self.smart_email_id, "tx_send_single.json")
***REMOVED******REMOVED******REMOVED******REMOVED***send = self.tx.smart_email_send(self.smart_email_id,***REMOVED***"\"Bob Sacamano\" <bob@example.com>")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(send[0].Status, "Received")

***REMOVED******REMOVED***def test_smart_email_send_multiple(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.tx.stub_request("transactional/smartEmail/%s/send" % self.smart_email_id, "tx_send_multiple.json")
***REMOVED******REMOVED******REMOVED******REMOVED***send = self.tx.smart_email_send(self.smart_email_id,***REMOVED***["\"Bob Sacamano\" <bob@example.com>", "\"Newman\" <newman@example.com>"])
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(send[1].Recipient, "\"Newman\" <newman@example.com>")

***REMOVED******REMOVED***def test_classic_email_send(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.tx.stub_request("transactional/classicEmail/send", "tx_send_single.json")
***REMOVED******REMOVED******REMOVED******REMOVED***send = self.tx.classic_email_send("This is the subject", "from@example.com", "\"Bob Sacamano\" <bob@example.com>")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(send[0].Recipient, "\"Bob Sacamano\" <bob@example.com>")

***REMOVED******REMOVED***def test_classic_email_groups(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.tx.stub_request("transactional/classicEmail/groups", "tx_classicemail_groups.json")
***REMOVED******REMOVED******REMOVED******REMOVED***groups = self.tx.classic_email_groups()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(groups[0].Group, "Password Reset")

***REMOVED******REMOVED***def test_classic_email_groups_with_client(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.tx.stub_request("transactional/classicEmail/groups?clientID=%s" % self.client_id, "tx_classicemail_groups.json")
***REMOVED******REMOVED******REMOVED******REMOVED***groups = self.tx.classic_email_groups(client_id=self.client_id)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(groups[0].Group, "Password Reset")

***REMOVED******REMOVED***def test_statistics(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.tx.stub_request("transactional/statistics", "tx_statistics_classic.json")
***REMOVED******REMOVED******REMOVED******REMOVED***stats = self.tx.statistics()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(stats.Query.Group, "Password Reset")

***REMOVED******REMOVED***def test_statistics_with_options(self):
***REMOVED******REMOVED******REMOVED******REMOVED***start = "2014-02-03"
***REMOVED******REMOVED******REMOVED******REMOVED***end = "2015-02-02"
***REMOVED******REMOVED******REMOVED******REMOVED***self.tx.stub_request('transactional/statistics?to=%s&from=%s&clientID=%s' % (end, start, self.client_id), "tx_statistics_classic.json")
***REMOVED******REMOVED******REMOVED******REMOVED***stats = self.tx.statistics({'clientID': self.client_id, 'from': start, 'to': end})
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(stats.Query.Group, "Password Reset")

***REMOVED******REMOVED***def test_timeline(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.tx.stub_request("transactional/messages", "tx_messages.json")
***REMOVED******REMOVED******REMOVED******REMOVED***timeline = self.tx.message_timeline()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(timeline), 3)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(timeline[0].Status, "Delivered")

***REMOVED******REMOVED***def test_timeline_classic_with_options(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.tx.stub_request('transactional/messages?status=%s&group=%s' % ("all", "Password+Reset"), "tx_messages_classic.json")
***REMOVED******REMOVED******REMOVED******REMOVED***timeline = self.tx.message_timeline({'status':'all','group':'Password Reset'})
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(timeline[0].Group, "Password Reset")

***REMOVED******REMOVED***def test_timeline_smart_with_options(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.tx.stub_request('transactional/messages?status=%s&smartEmailID=%s' % ("all", self.smart_email_id), "tx_messages_smart.json")
***REMOVED******REMOVED******REMOVED******REMOVED***timeline = self.tx.message_timeline({'status':'all','smartEmailID':self.smart_email_id})
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(timeline[0].SmartEmailID, self.smart_email_id)

***REMOVED******REMOVED***def test_message_details(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.tx.stub_request('transactional/messages/%s?statistics=False' % (self.message_id), "tx_message_details.json")
***REMOVED******REMOVED******REMOVED******REMOVED***msg = self.tx.message_details(self.message_id, statistics=False)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(msg.MessageID, self.message_id)

***REMOVED******REMOVED***def test_message_details_with_stats(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.tx.stub_request('transactional/messages/%s?statistics=True' % (self.message_id), "tx_message_details_with_statistics.json")
***REMOVED******REMOVED******REMOVED******REMOVED***msg = self.tx.message_details(self.message_id, statistics=True)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(msg.Opens), 1)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(len(msg.Clicks), 1)

***REMOVED******REMOVED***def test_message_resend(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.tx.stub_request('transactional/messages/%s/resend' % (self.message_id), "tx_send_single.json")
***REMOVED******REMOVED******REMOVED******REMOVED***send = self.tx.message_resend(self.message_id)
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEqual(send[0].Status, "Received")


class OAuthTransactionalTestCase(unittest.TestCase, TransactionalTestCase):
***REMOVED***"""Test when using OAuth to authenticate"""
***REMOVED***def setUp(self):
***REMOVED******REMOVED***self.client_id***REMOVED******REMOVED******REMOVED***= '87y8d7qyw8d7yq8w7ydwqwd'
***REMOVED******REMOVED***self.smart_email_id = '21dab350-f484-11e4-ad38-6c4008bc7468'
***REMOVED******REMOVED***self.message_id***REMOVED******REMOVED*** = 'ddc697c7-0788-4df3-a71a-a7cb935f00bd'
***REMOVED******REMOVED***self.before_id***REMOVED******REMOVED******REMOVED***= 'e2e270e6-fbce-11e4-97fc-a7cf717ca157'
***REMOVED******REMOVED***self.after_id***REMOVED******REMOVED******REMOVED*** = 'e96fc6ca-fbce-11e4-949f-c3ccd6a68863'
***REMOVED******REMOVED***self.tx = Transactional(
***REMOVED******REMOVED******REMOVED***{"access_token": "ASP95S4aR+9KsgfHB0dapTYxNA==", "refresh_token": "5S4aASP9R+9KsgfHB0dapTYxNA=="}, "admin@example.com")

class ApiKeyTransactionalTestCase(unittest.TestCase, TransactionalTestCase):
***REMOVED***"""Test when using an API key to authenticate"""
***REMOVED***def setUp(self):
***REMOVED******REMOVED***self.client_id***REMOVED******REMOVED******REMOVED***= '87y8d7qyw8d7yq8w7ydwqwd'
***REMOVED******REMOVED***self.smart_email_id = '21dab350-f484-11e4-ad38-6c4008bc7468'
***REMOVED******REMOVED***self.message_id***REMOVED******REMOVED*** = 'ddc697c7-0788-4df3-a71a-a7cb935f00bd'
***REMOVED******REMOVED***self.before_id***REMOVED******REMOVED******REMOVED***= 'e2e270e6-fbce-11e4-97fc-a7cf717ca157'
***REMOVED******REMOVED***self.after_id***REMOVED******REMOVED******REMOVED*** = 'e96fc6ca-fbce-11e4-949f-c3ccd6a68863'
***REMOVED******REMOVED***self.tx = Transactional(
***REMOVED******REMOVED******REMOVED***{'api_key': '123123123123123123123'}, "admin@example.com")

