# createsend

A python wrapper for the createsend API v3.

## Installation

    pip install -e git+http://github.com/jdennes/createsend-python.git#egg=createsend

## Example

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

If the createsend API returns an error, an exception will be thrown. For example, if you attempt to create a campaign and enter empty values for subject etc:

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
