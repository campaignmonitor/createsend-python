# createsend

A python library which implements the complete functionality of v3 of the createsend API.

## Installation

***REMOVED******REMOVED***pip install -e git+http://github.com/jdennes/createsend-python.git#egg=createsend

## Example

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

If the createsend API returns an error, an exception will be thrown. For example, if you attempt to create a campaign and enter empty values for subject etc:

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
