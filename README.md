# createsend

[![Build Status](https://secure.travis-ci.org/campaignmonitor/createsend-python.png)](http://travis-ci.org/campaignmonitor/createsend-python)

A python library which implements the complete functionality of v3 of the CreateSend API.

## Installation

Requires Python 2.6+

***REMOVED******REMOVED***pip install createsend

## Examples

### Basic usage
Retrieve a list of all your clients.

***REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED***
***REMOVED******REMOVED***CreateSend.api_key = 'your_api_key'

***REMOVED******REMOVED***cs = CreateSend()
***REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED***
***REMOVED******REMOVED***for c in clients:
***REMOVED******REMOVED******REMOVED***print "%s: %s" % (c.ClientID, c.Name)

Results in:

***REMOVED******REMOVED***4a397ccaaa55eb4e6aa1221e1e2d7122: Client One
***REMOVED******REMOVED***a206def0582eec7dae47d937a4109cb2: Client Two

### Handling errors
If the createsend API returns an error, an exception will be thrown. For example, if you attempt to create a campaign and enter empty values for subject etc:

***REMOVED******REMOVED******REMOVED***

***REMOVED******REMOVED***CreateSend.api_key = 'your_api_key'

***REMOVED******REMOVED***try:
***REMOVED******REMOVED******REMOVED***cl = Client("4a397ccaaa55eb4e6aa1221e1e2d7122")
***REMOVED******REMOVED******REMOVED***id = Campaign().create(cl.client_id, "", "", "", "", "", "", "", [], [])
***REMOVED******REMOVED******REMOVED***print "New campaign ID: %s" % id
***REMOVED******REMOVED***except BadRequest as br:
***REMOVED******REMOVED******REMOVED***print "Bad request error: %s" % br
***REMOVED******REMOVED******REMOVED***print "Error Code:***REMOVED******REMOVED***%s" % br.data.Code
***REMOVED******REMOVED******REMOVED***print "Error Message: %s" % br.data.Message
***REMOVED******REMOVED***except Exception as e:
***REMOVED******REMOVED******REMOVED***print "Error: %s" % e

Results in:

***REMOVED******REMOVED***Bad request error: The CreateSend API responded with the following error - 304: Campaign Subject Required
***REMOVED******REMOVED***Error Code:***REMOVED******REMOVED***304
***REMOVED******REMOVED***Error Message: Campaign Subject Required

### Expected input and output
The best way of finding out the expected input and output of a particular method in a particular class is to use the unit tests as a reference.

For example, if you wanted to find out how to call the Subscriber.add() method, you would look at the file test/test_subscriber.py

***REMOVED******REMOVED***def test_add_with_custom_fields(self):
***REMOVED******REMOVED******REMOVED***self.subscriber.stub_request("subscribers/%s.json" % self.list_id, "add_subscriber.json")
***REMOVED******REMOVED******REMOVED***custom_fields = [ { "Key": 'website', "Value": 'http://example.com/' } ]
***REMOVED******REMOVED******REMOVED***email_address = self.subscriber.add(self.list_id, "subscriber@example.com", "Subscriber", custom_fields, True)
***REMOVED******REMOVED******REMOVED***self.assertEquals(email_address, "subscriber@example.com")
