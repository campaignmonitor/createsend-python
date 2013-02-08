# createsend [![Build Status](https://secure.travis-ci.org/campaignmonitor/createsend-python.png)][travis]
A python library which implements the complete functionality of the [Campaign Monitor API](http://www.campaignmonitor.com/api/).

[travis]: http://travis-ci.org/campaignmonitor/createsend-python

## Installation

```
pip install createsend
```

## Authenticating

The Campaign Monitor API supports authentication using either OAuth or an API key.

### Using OAuth

```python
from createsend import *

cs = CreateSend()
cs.auth({
	'access_token': 'your access token',
	'refresh_token': 'your refresh token' })
clients = cs.clients()
```

### Using an API key

```python
from createsend import *

cs = CreateSend()
cs.auth({'api_key': 'your api key'})
clients = cs.clients()
```

## Basic usage
Retrieve a list of all your clients.

```python
from createsend import *

cs = CreateSend()
cs.auth({
	'access_token': 'your access token',
	'refresh_token': 'your refresh token' })
clients = cs.clients()

for c in clients:
  print "%s: %s" % (c.ClientID, c.Name)
```

Results in:

```
4a397ccaaa55eb4e6aa1221e1e2d7122: Client One
a206def0582eec7dae47d937a4109cb2: Client Two
```

## Handling errors
If the createsend API returns an error, an exception will be thrown. For example, if you attempt to create a campaign and enter empty values for subject etc:

```python
from createsend import *

campaign = Campaign()
campaign.auth({
	'access_token': 'your access token',
	'refresh_token': 'your refresh token' })

try:
  id = campaign.create("4a397ccaaa55eb4e6aa1221e1e2d7122", "", "", "", "", "", "", "", [], [])
  print "New campaign ID: %s" % id
except BadRequest as br:
  print "Bad request error: %s" % br
  print "Error Code:    %s" % br.data.Code
  print "Error Message: %s" % br.data.Message
except Exception as e:
  print "Error: %s" % e
```

Results in:

```
Bad request error: The CreateSend API responded with the following error - 304: Campaign Subject Required
Error Code:    304
Error Message: Campaign Subject Required
```

## Expected input and output
The best way of finding out the expected input and output of a particular method in a particular class is to use the unit tests as a reference.

For example, if you wanted to find out how to call the Subscriber.add() method, you would look at the file test/test_subscriber.py

```python
def test_add_with_custom_fields(self):
  self.subscriber.stub_request("subscribers/%s.json" % self.list_id, "add_subscriber.json")
  custom_fields = [ { "Key": 'website', "Value": 'http://example.com/' } ]
  email_address = self.subscriber.add(self.list_id, "subscriber@example.com", "Subscriber", custom_fields, True)
  self.assertEquals(email_address, "subscriber@example.com")
```

## Contributing
1. Fork the repository
2. Make your changes, including tests for your changes.
3. Ensure that the build passes, by running `rake` (CI runs on: `2.5`, `2.6`, and `2.7`)
4. It should go without saying, but do not increment the version number in your commits.
5. Submit a pull request.
