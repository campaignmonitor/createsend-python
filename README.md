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
***REMOVED***

cs = CreateSend()
cs.auth({
	'access_token': 'your access token',
	'refresh_token': 'your refresh token' })
***REMOVED***
```

All OAuth tokens have an expiry time, and can be renewed with a corresponding refresh token. If your access token expires when attempting to make an API call, the `ExpiredOAuthToken` exception will be raised, so your code should handle this. Here's an example of how you could do this:

```python
***REMOVED***

try:
	cs = CreateSend()
	cs.auth({
		'access_token': 'your access token',
		'refresh_token': 'your refresh token' })
***REMOVED******REMOVED***
except ExpiredOAuthToken as eot:
	access_token, refresh_token = cs.refresh_token()
	# retry...
except Exception as e:
***REMOVED***print "Error: %s" % e

***REMOVED***rescue CreateSend::ExpiredOAuthToken => eot
***REMOVED******REMOVED***access_token, refresh_token = CreateSend.refresh_token
***REMOVED******REMOVED***retry unless (tries -= 1).zero?
***REMOVED******REMOVED***p "Error: #{eot}"
***REMOVED***rescue Exception => e
***REMOVED******REMOVED***p "Error: #{e}"
end
```

### Using an API key

```python
***REMOVED***

cs = CreateSend()
cs.auth({'api_key': 'your api key'})
***REMOVED***
```

## Basic usage
Retrieve a list of all your clients.

```python
***REMOVED***

cs = CreateSend()
cs.auth({
	'access_token': 'your access token',
	'refresh_token': 'your refresh token' })
***REMOVED***

for c in clients:
***REMOVED***print "%s: %s" % (c.ClientID, c.Name)
```

Results in:

```
4a397ccaaa55eb4e6aa1221e1e2d7122: Client One
a206def0582eec7dae47d937a4109cb2: Client Two
```

## Handling errors
If the Campaign Monitor API returns an error, an exception will be raised. For example, if you attempt to create a campaign and enter empty values for subject etc:

```python
***REMOVED***

campaign = Campaign()
campaign.auth({
	'access_token': 'your access token',
	'refresh_token': 'your refresh token' })

try:
***REMOVED***id = campaign.create("4a397ccaaa55eb4e6aa1221e1e2d7122", "", "", "", "", "", "", "", [], [])
***REMOVED***print "New campaign ID: %s" % id
except BadRequest as br:
***REMOVED***print "Bad request error: %s" % br
***REMOVED***print "Error Code:***REMOVED******REMOVED***%s" % br.data.Code
***REMOVED***print "Error Message: %s" % br.data.Message
except Exception as e:
***REMOVED***print "Error: %s" % e
```

Results in:

```
Bad request error: The CreateSend API responded with the following error - 304: Campaign Subject Required
Error Code:***REMOVED******REMOVED***304
Error Message: Campaign Subject Required
```

## Expected input and output
The best way of finding out the expected input and output of a particular method in a particular class is to use the unit tests as a reference.

For example, if you wanted to find out how to call the Subscriber.add() method, you would look at the file test/test_subscriber.py

```python
def test_add_with_custom_fields(self):
***REMOVED***self.subscriber.stub_request("subscribers/%s.json" % self.list_id, "add_subscriber.json")
***REMOVED***custom_fields = [ { "Key": 'website', "Value": 'http://example.com/' } ]
***REMOVED***email_address = self.subscriber.add(self.list_id, "subscriber@example.com", "Subscriber", custom_fields, True)
***REMOVED***self.assertEquals(email_address, "subscriber@example.com")
```

## Contributing
1. Fork the repository
2. Make your changes, including tests for your changes.
3. Ensure that the build passes, by running `rake` (CI runs on: `2.5`, `2.6`, and `2.7`)
4. It should go without saying, but do not increment the version number in your commits.
5. Submit a pull request.
