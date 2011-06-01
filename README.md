# createsend

A python library which implements the complete functionality of v3 of the CreateSend API.

## Installation

    pip install createsend

## Examples

### Basic usage
Retrieve a list of all your clients.

    from createsend import *
    
    CreateSend.api_key = 'your_api_key'

    cs = CreateSend()
    clients = cs.clients()
    
    for c in clients:
      print "%s: %s" % (c.ClientID, c.Name)

Results in:

    4a397ccaaa55eb4e6aa1221e1e2d7122: Client One
    a206def0582eec7dae47d937a4109cb2: Client Two

### Handling errors
If the createsend API returns an error, an exception will be thrown. For example, if you attempt to create a campaign and enter empty values for subject etc:

    from createsend import *

    CreateSend.api_key = 'your_api_key'

    try:
      cl = Client("4a397ccaaa55eb4e6aa1221e1e2d7122")
      id = Campaign().create(cl.client_id, "", "", "", "", "", "", "", [], [])
      print "New campaign ID: %s" % id
    except BadRequest as br:
      print "Bad request error: %s" % br
      print "Error Code:    %s" % br.data.Code
      print "Error Message: %s" % br.data.Message
    except Exception as e:
      print "Error: %s" % e

Results in:

    Bad request error: The CreateSend API responded with the following error - 304: Campaign Subject Required
    Error Code:    304
    Error Message: Campaign Subject Required

### Expected input and output
The best way of finding out the expected input and output of a particular method in a particular class is to use the unit tests as a reference.

For example, if you wanted to find out how to call the Subscriber.add() method, you would look at the file test/test_subscriber.py

    def test_add_with_custom_fields(self):
      self.subscriber.stub_request("subscribers/%s.json" % self.list_id, "add_subscriber.json")
      custom_fields = [ { "Key": 'website', "Value": 'http://example.com/' } ]
      email_address = self.subscriber.add(self.list_id, "subscriber@example.com", "Subscriber", custom_fields, True)
      self.assertEquals(email_address, "subscriber@example.com")
