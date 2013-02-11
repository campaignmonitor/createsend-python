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

If you don't use an OAuth library, you will need to manually get access tokens for your users by following the instructions included in the Campaign Monitor API [documentation](http://www.campaignmonitor.com/api/getting-started/#authenticating_with_oauth). This package provides functionality to help you do this, as described below.

You can retrieve the authorization URL for your application like so:

```python
from createsend import *

cs = CreateSend()
authorize_url = cs.authorize_url(
  client_id='Client ID for your application',
  client_secret='Client Secret for your application',
  redirect_uri='Redirect URI for your application',
  scope='The permission level your application requires',
  state='Optional state data to be included'
)

# Your app would redirect your users to authorize_url
```

Once you have an access token and refresh token for your user, you authenticate using the `auth()` method like so:

```python
from createsend import *

cs = CreateSend()
cs.auth({
  'access_token': 'your access token',
  'refresh_token': 'your refresh token' })
clients = cs.clients()
```

All OAuth tokens have an expiry time, and can be renewed with a corresponding refresh token. If your access token expires when attempting to make an API call, the `ExpiredOAuthToken` exception will be raised, so your code should handle this. Here's an example of how you could do this:

```python
from createsend import *

try:
  cs = CreateSend()
  cs.auth({
    'access_token': 'your access token',
    'refresh_token': 'your refresh token' })
  clients = cs.clients()
except ExpiredOAuthToken as eot:
  access_token, refresh_token = cs.refresh_token()
  # Save your updated access token and refresh token
  clients = cs.clients()
except Exception as e:
  print("Error: %s" % e)
```

### Using an API key

```python
from createsend import *

cs = CreateSend()
cs.auth({'api_key': 'your api key'})
clients = cs.clients()
```

## Basic usage
This example of listing all your clients and their campaigns demonstrates basic usage of the library and the data returned from the API:

```python
from createsend import *

auth = {
  'access_token': access_token,
  'refresh_token': refresh_token }
cs = CreateSend()
cs.auth(auth)
clients = cs.clients()

for cl in clients:
  print("Client: %s" % cl.Name)
  client = Client(cl.ClientID)
  client.auth(auth)
  print("- Campaigns:")
  for cm in client.campaigns():
    print("  - %s" % cm.Subject)
```

Running this example will result in something like:

```
Client: First Client
- Campaigns:
  - Newsletter Number One
  - Newsletter Number Two
Client: Second Client
- Campaigns:
  - News for January 2013
```

## Handling errors
If the Campaign Monitor API returns an error, an exception will be raised. For example, if you attempt to create a campaign and enter empty values for subject and other required fields:

```python
from createsend import *

campaign = Campaign()
campaign.auth({
  'access_token': 'your access token',
  'refresh_token': 'your refresh token' })

try:
  id = campaign.create("4a397ccaaa55eb4e6aa1221e1e2d7122", "", "", "", "", "", "", "", [], [])
  print("New campaign ID: %s" % id)
except BadRequest as br:
  print("Bad request error: %s" % br)
  print("Error Code:    %s" % br.data.Code)
  print("Error Message: %s" % br.data.Message)
except Exception as e:
  print("Error: %s" % e)
```

Running this example will result in:

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
