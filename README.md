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

Depending on the environment you are developing in, you may wish to use a Python OAuth library to get access tokens for your users. If you use [Flask](http://flask.pocoo.org/), you may like to refer to this [example application](https://gist.github.com/jdennes/4754097), which uses the [Flask-OAuth](http://pythonhosted.org/Flask-OAuth/) package to authenticate.

If you don't use an OAuth library, you will need to manually get access tokens for your users by following the instructions included in the Campaign Monitor API [documentation](http://www.campaignmonitor.com/api/getting-started/#authenticating_with_oauth). This package provides functionality to help you do this, as described below. There's also another Flask [example application](https://gist.github.com/jdennes/4761254) you may wish to reference, which doesn't depend on any OAuth libraries.

The first thing your application should do is redirect your user to the Campaign Monitor authorization URL where they will have the opportunity to approve your application to access their Campaign Monitor account. You can get this authorization URL by using the `authorize_url()` function, like so:

```python
***REMOVED***

cs = CreateSend()
authorize_url = cs.authorize_url(
***REMOVED***client_id='Client ID for your application',
***REMOVED***client_secret='Client Secret for your application',
***REMOVED***redirect_uri='Redirect URI for your application',
***REMOVED***scope='The permission level your application requires',
***REMOVED***state='Optional state data to be included'
)
# Redirect your users to authorize_url.
```

If your user approves your application, they will then be redirected to the `redirect_uri` you specified, which will include a `code` parameter, and optionally a `state` parameter in the query string. Your application should implement a handler which can exchange the code passed to it for an access token, using the `exchange_token()` function like so:

```python
***REMOVED***

cs = CreateSend()
access_token, expires_in, refresh_token = cs.exchange_token(
***REMOVED***client_id='Client ID for your application',
***REMOVED***client_secret='Client Secret for your application',
***REMOVED***redirect_uri='Redirect URI for your application',
***REMOVED***code='A unique code for your user' # Get the code parameter from the query string
)
# Save access_token, expires_in, and refresh_token.
```

At this point you have an access token and refresh token for your user which you should store somewhere convenient so that your application can look up these values when your user wants to make future Campaign Monitor API calls.

Once you have an access token and refresh token for your user, you can authenticate using the `auth()` method and make further API calls like so:

```python
***REMOVED***

cs = CreateSend()
cs.auth({
***REMOVED***'access_token': 'your access token',
***REMOVED***'refresh_token': 'your refresh token' })
***REMOVED***
```

All OAuth tokens have an expiry time, and can be renewed with a corresponding refresh token. If your access token expires when attempting to make an API call, the `ExpiredOAuthToken` exception will be raised, so your code should handle this. Here's an example of how you could do this:

```python
***REMOVED***

try:
***REMOVED***cs = CreateSend()
***REMOVED***cs.auth({
***REMOVED******REMOVED***'access_token': 'your access token',
***REMOVED******REMOVED***'refresh_token': 'your refresh token' })
***REMOVED******REMOVED***
except ExpiredOAuthToken as eot:
***REMOVED***access_token, refresh_token = cs.refresh_token()
***REMOVED***# Save your updated access_token and refresh_token.
***REMOVED******REMOVED***
except Exception as e:
***REMOVED***print("Error: %s" % e)
```

### Using an API key

```python
***REMOVED***

cs = CreateSend()
cs.auth({'api_key': 'your api key'})
***REMOVED***
```

## Basic usage
This example of listing all your clients and their campaigns demonstrates basic usage of the library and the data returned from the API:

```python
***REMOVED***

auth = {
***REMOVED***'access_token': 'your access token',
***REMOVED***'refresh_token': 'your refresh token' }
cs = CreateSend()
cs.auth(auth)
***REMOVED***

***REMOVED***
***REMOVED***print("Client: %s" % cl.Name)
***REMOVED***client = Client(cl.ClientID)
***REMOVED***client.auth(auth)
***REMOVED***print("- Campaigns:")
***REMOVED***for cm in client.campaigns():
***REMOVED******REMOVED***print("***REMOVED***- %s" % cm.Subject)
```

Running this example will result in something like:

```
Client: First Client
- Campaigns:
***REMOVED***- Newsletter Number One
***REMOVED***- Newsletter Number Two
Client: Second Client
- Campaigns:
***REMOVED***- News for January 2013
```

## Handling errors
If the Campaign Monitor API returns an error, an exception will be raised. For example, if you attempt to create a campaign and enter empty values for subject and other required fields:

```python
***REMOVED***

campaign = Campaign()
campaign.auth({
***REMOVED***'access_token': 'your access token',
***REMOVED***'refresh_token': 'your refresh token' })

try:
***REMOVED***id = campaign.create("4a397ccaaa55eb4e6aa1221e1e2d7122", "", "", "", "", "", "", "", [], [])
***REMOVED***print("New campaign ID: %s" % id)
except BadRequest as br:
***REMOVED***print("Bad request error: %s" % br)
***REMOVED***print("Error Code:***REMOVED******REMOVED***%s" % br.data.Code)
***REMOVED***print("Error Message: %s" % br.data.Message)
except Exception as e:
***REMOVED***print("Error: %s" % e)
```

Running this example will result in:

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
