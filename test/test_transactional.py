import unittest
import urllib

from createsend import *

class TransactionalTestCase(object):

    def test_smart_email_list(self):
        status = "all"
        self.tx.stub_request("transactional/smartEmail?status=%s" % status, "tx_smartemails.json")
        list = self.tx.smart_email_list(status)
        self.assertEqual(list[0].Name, "Welcome email")

    def test_active_smart_email_list(self):
        self.tx.stub_request("transactional/smartEmail?status=active", "tx_smartemails.json")
        list = self.tx.smart_email_list(status="active")
        self.assertEqual(list[0].Status, "Active")

    def test_smart_email_list_with_client(self):
        self.tx.stub_request("transactional/smartEmail?status=all&clientID=%s" % self.client_id, "tx_smartemails.json")
        list = self.tx.smart_email_list(client_id=self.client_id)
        self.assertEqual(list[0].Name, "Welcome email")

    def test_smart_email_details(self):
        self.tx.stub_request("transactional/smartEmail/%s" % self.smart_email_id, "tx_smartemail_details.json")
        email = self.tx.smart_email_details(self.smart_email_id)
        self.assertEqual(email.Name, "Reset Password")

    def test_smart_email_send_single(self):
        self.tx.stub_request("transactional/smartEmail/%s/send" % self.smart_email_id, "tx_send_single.json")
        send = self.tx.smart_email_send(self.smart_email_id,  "\"Bob Sacamano\" <bob@example.com>")
        self.assertEqual(send[0].Status, "Received")

    def test_smart_email_send_multiple(self):
        self.tx.stub_request("transactional/smartEmail/%s/send" % self.smart_email_id, "tx_send_multiple.json")
        send = self.tx.smart_email_send(self.smart_email_id,  ["\"Bob Sacamano\" <bob@example.com>", "\"Newman\" <newman@example.com>"])
        self.assertEqual(send[1].Recipient, "\"Newman\" <newman@example.com>")

    def test_classic_email_send(self):
        self.tx.stub_request("transactional/classicEmail/send", "tx_send_single.json")
        send = self.tx.classic_email_send("This is the subject", "from@example.com", "\"Bob Sacamano\" <bob@example.com>")
        self.assertEqual(send[0].Recipient, "\"Bob Sacamano\" <bob@example.com>")

    def test_classic_email_groups(self):
        self.tx.stub_request("transactional/classicEmail/groups", "tx_classicemail_groups.json")
        groups = self.tx.classic_email_groups()
        self.assertEqual(groups[0].Group, "Password Reset")

    def test_classic_email_groups_with_client(self):
        self.tx.stub_request("transactional/classicEmail/groups?clientID=%s" % self.client_id, "tx_classicemail_groups.json")
        groups = self.tx.classic_email_groups(client_id=self.client_id)
        self.assertEqual(groups[0].Group, "Password Reset")

    def test_statistics(self):
        self.tx.stub_request("transactional/statistics", "tx_statistics_classic.json")
        stats = self.tx.statistics()
        self.assertEqual(stats.Query.Group, "Password Reset")

    def test_statistics_with_options(self):
        start = "2014-02-03"
        end = "2015-02-02"
        self.tx.stub_request('transactional/statistics?to=%s&from=%s&clientID=%s' % (end, start, self.client_id), "tx_statistics_classic.json")
        stats = self.tx.statistics({'clientID': self.client_id, 'from': start, 'to': end})
        self.assertEqual(stats.Query.Group, "Password Reset")

    def test_timeline(self):
        self.tx.stub_request("transactional/messages", "tx_messages.json")
        timeline = self.tx.message_timeline()
        self.assertEqual(len(timeline), 3)
        self.assertEqual(timeline[0].Status, "Delivered")

    def test_timeline_classic_with_options(self):
        self.tx.stub_request('transactional/messages?status=%s&group=%s' % ("all", "Password+Reset"), "tx_messages_classic.json")
        timeline = self.tx.message_timeline({'status':'all','group':'Password Reset'})
        self.assertEqual(timeline[0].Group, "Password Reset")

    def test_timeline_smart_with_options(self):
        self.tx.stub_request('transactional/messages?status=%s&smartEmailID=%s' % ("all", self.smart_email_id), "tx_messages_smart.json")
        timeline = self.tx.message_timeline({'status':'all','smartEmailID':self.smart_email_id})
        self.assertEqual(timeline[0].SmartEmailID, self.smart_email_id)

    def test_message_details(self):
        self.tx.stub_request('transactional/messages/%s?statistics=False' % (self.message_id), "tx_message_details.json")
        msg = self.tx.message_details(self.message_id, statistics=False)
        self.assertEqual(msg.MessageID, self.message_id)

    def test_message_details_with_stats(self):
        self.tx.stub_request('transactional/messages/%s?statistics=True' % (self.message_id), "tx_message_details_with_statistics.json")
        msg = self.tx.message_details(self.message_id, statistics=True)
        self.assertEqual(len(msg.Opens), 1)
        self.assertEqual(len(msg.Clicks), 1)

    def test_message_resend(self):
        self.tx.stub_request('transactional/messages/%s/resend' % (self.message_id), "tx_send_single.json")
        send = self.tx.message_resend(self.message_id)
        self.assertEqual(send[0].Status, "Received")


class OAuthTransactionalTestCase(unittest.TestCase, TransactionalTestCase):
  """Test when using OAuth to authenticate"""
  def setUp(self):
    self.client_id      = '87y8d7qyw8d7yq8w7ydwqwd'
    self.smart_email_id = '21dab350-f484-11e4-ad38-6c4008bc7468'
    self.message_id     = 'ddc697c7-0788-4df3-a71a-a7cb935f00bd'
    self.before_id      = 'e2e270e6-fbce-11e4-97fc-a7cf717ca157'
    self.after_id       = 'e96fc6ca-fbce-11e4-949f-c3ccd6a68863'
    self.tx = Transactional(
      {"access_token": "ASP95S4aR+9KsgfHB0dapTYxNA==", "refresh_token": "5S4aASP9R+9KsgfHB0dapTYxNA=="}, "admin@example.com")

class ApiKeyTransactionalTestCase(unittest.TestCase, TransactionalTestCase):
  """Test when using an API key to authenticate"""
  def setUp(self):
    self.client_id      = '87y8d7qyw8d7yq8w7ydwqwd'
    self.smart_email_id = '21dab350-f484-11e4-ad38-6c4008bc7468'
    self.message_id     = 'ddc697c7-0788-4df3-a71a-a7cb935f00bd'
    self.before_id      = 'e2e270e6-fbce-11e4-97fc-a7cf717ca157'
    self.after_id       = 'e96fc6ca-fbce-11e4-949f-c3ccd6a68863'
    self.tx = Transactional(
      {'api_key': '123123123123123123123'}, "admin@example.com")

