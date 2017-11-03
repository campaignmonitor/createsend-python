# createsend-python history

## v4.2.6 - 3 Nov, 2017

* Removes test dependencies from install package. (#53)
* Build and upload universal wheels alongside source dists.

## v4.2.5 - 27 Oct, 2017

* Fix bug where necessary files were not included in the source distribution. (#45, #50)

## v4.2.2 - 1 Jul, 2017

* Fix bug where the six module was not set as a installation dependency.
* Remove relative imports.
* Improve Python 3 support.
* Use PEP 8 formatting.
* See [#43](https://github.com/campaignmonitor/createsend-python/pull/43) for details.

## v4.2.1 - 19 Dec, 2016

* Decode JSON API responses using UTF-8: ([#38](https://github.com/campaignmonitor/createsend-python/pull/38))

## v4.2.0 - 10 Oct, 2016

* Support Python 3: ([#27](https://github.com/campaignmonitor/createsend-python/pull/27))
* Use CGI SERVER_NAME in UA string: ([#32](https://github.com/campaignmonitor/createsend-python/pull/32))

## v4.1.1 - 7 Aug, 2015

* Fixed the MANIFEST file so that it includes new Transactional files (#25).

## v4.1.0 - 4 Aug, 2015

* Added support for Transactional Email

## v4.0.0 - 19 Feb, 2014

* Removed `CreateSend.apikey` to promote using OAuth rather than basic auth with an API key.
* Started using the `https://api.createsend.com/api/v3.1/` API endpoint.
* Added support for new segments structure.
***REMOVED**** Segments now includes a new `RuleGroups` member, instead of a `Rules` member.

***REMOVED******REMOVED***So for example, when you _previously_ would have created a segment like so:

***REMOVED******REMOVED***```python
***REMOVED******REMOVED***segment.create(list.ListID, 'Python API Segment', [ { "Subject": "EmailAddress", "Clauses": ["CONTAINS pyapi.com"] } ])
***REMOVED******REMOVED***```

***REMOVED******REMOVED***You would _now_ do this:

***REMOVED******REMOVED***```python
***REMOVED******REMOVED***segment.create(list.ListID, 'Python API Segment', [ { "Rules": [ { "RuleType": "EmailAddress", "Clause": "CONTAINS pyapi.com" } ] } ])
***REMOVED******REMOVED***```

***REMOVED**** The Add Rule call is now Add Rule Group, taking a `rulegroup` argument instead of a `subject` & `clauses` argument.

***REMOVED******REMOVED***```python
***REMOVED******REMOVED***Segment.add_rulegroup(self, rulegroup):
***REMOVED******REMOVED***```

***REMOVED******REMOVED***So for example, when you _previously_ would have added a rule like so:

***REMOVED******REMOVED***```python
***REMOVED******REMOVED***segment.add_rule( "EmailAddress", ["CONTAINS pyapi.com"] )
***REMOVED******REMOVED***```

***REMOVED******REMOVED***You would _now_ do this:

***REMOVED******REMOVED***```python
***REMOVED******REMOVED***segment.add_rulegroup( { "Rules": [ { "RuleType": "EmailAddress", "Clause": "CONTAINS pyapi.com" } ] } )
***REMOVED******REMOVED***```

## v3.4.0 - 25 Jan, 2014

* Modified several methods so that unnecessary arguments are no longer needed.

***REMOVED***The following methods were updated:
***REMOVED***- `Administrator.get()`
***REMOVED***- `Person.get()`
***REMOVED***- `Subscriber.get()`

***REMOVED***As an example using, previously you would write:

***REMOVED***```python
***REMOVED***subscriber = Subscriber(auth, 'listid', 'me@test.com').get('listid', 'me@test.com')
***REMOVED***```

***REMOVED***Now you can write:

***REMOVED***```python
***REMOVED***subscriber = Subscriber(auth, 'listid', 'me@test.com').get()
***REMOVED***```

## v3.3.0 - 13 Jul, 2013

* Added support for validating SSL certificates to avoid man-in-the-middle attacks.

## v3.2.0 - 16 May, 2013

* Added Python version and platform details to default user agent string.
* Added support for setting a custom user agent string.

***REMOVED***You can set a custom user agent string to be used for API calls by doing the following:

***REMOVED***```python
***REMOVED***CreateSend.user_agent = "custom user agent"
***REMOVED***```

## v3.1.0 - 15 Apr, 2013

* Added support for [single sign on](http://www.campaignmonitor.com/api/account/#single_sign_on) which allows initiation of external login sessions to Campaign Monitor.

## v3.0.0 - 25 Mar, 2013

* Added support for authenticating using OAuth. See the [README](README.md#authenticating) for full usage instructions.
* Refactored authentication so that it is _always_ done at the instance level. This introduces some breaking changes, which are clearly explained below.
***REMOVED**** Authentication is now _always_ done at the instance level.

***REMOVED******REMOVED******REMOVED***So when you _previously_ would have authenticated using an API key as follows:

***REMOVED******REMOVED******REMOVED***```python
***REMOVED******REMOVED******REMOVED***CreateSend.api_key = 'your_api_key'
***REMOVED******REMOVED******REMOVED***cs = CreateSend()
***REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED***```

***REMOVED******REMOVED******REMOVED***If you want to authenticate using an API key, you should _now_ do this:

***REMOVED******REMOVED******REMOVED***```python
***REMOVED******REMOVED******REMOVED***cs = CreateSend({'api_key': 'your_api_key'})
***REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED***```

***REMOVED**** Instances of any subclasses of `CreateSendBase` are now _always_ created by passing an `auth` hash as the first argument.

***REMOVED******REMOVED******REMOVED***So for example, when you _previously_ would have called `Client()` like so:

***REMOVED******REMOVED******REMOVED***```python
***REMOVED******REMOVED******REMOVED***CreateSend.api_key 'your api key'
***REMOVED******REMOVED******REMOVED***cl = Client('your client id')
***REMOVED******REMOVED******REMOVED***```

***REMOVED******REMOVED******REMOVED***You _now_ call `CreateSend::Client.new` like so:

***REMOVED******REMOVED******REMOVED***```python
***REMOVED******REMOVED******REMOVED***auth = {'api_key': 'your api key'}
***REMOVED******REMOVED******REMOVED***cl = Client(auth, 'your client id')
***REMOVED******REMOVED******REMOVED***```

## v2.6.0 - 17 Dec, 2012

* Created objects (clients, campaigns, lists, segments, and templates) now
retain identifiers they are given when created. This allows the following code
to be written:

***REMOVED***```python
***REMOVED***client = Client()
***REMOVED***client.create("Company Name", "(GMT+10:00) Canberra, Melbourne, Sydney",
***REMOVED******REMOVED***"Australia")
***REMOVED***details = client.details()
***REMOVED***```

***REMOVED***Previously, this code would have been written as follows:

***REMOVED***```python
***REMOVED***client = Client()
***REMOVED***client_id = client.create("Company Name",
***REMOVED******REMOVED***"(GMT+10:00) Canberra, Melbourne, Sydney", "Australia")
***REMOVED***client.client_id = client_id
***REMOVED***details = client.details()
***REMOVED***```

## v2.5.0 - 11 Dec, 2012

* Added support for including from name, from email, and reply to email in
drafts, scheduled, and sent campaigns.
* Added support for campaign text version urls.
* Added support for transferring credits to/from a client.
* Added support for getting account billing details as well as client credits.
* Made all date fields optional when getting paged results.

## v2.4.1 - 11 Nov, 2012

* Added the ability to set api_key for a CreateSend instance, rather than
only at the class level.

## v2.4.0 - 5 Nov, 2012

* Added Campaign.email_client_usage().
* Added support for ReadsEmailWith field on subscriber objects.
* Added support for retrieving unconfirmed subscribers for a list.
* Added support for suppressing email addresses.
* Added support for retrieving spam complaints for a campaign, as well as
adding SpamComplaints field to campaign summary output.
* Added VisibleInPreferenceCenter field to custom field output.
* Added support for setting preference center visibility when creating custom
fields.
* Added the ability to update a custom field name and preference visibility.
* Added documentation explaining that text_url may now be None or an empty
string when creating a campaign.

## v2.3.0 - 10 Oct, 2012

* Added support for creating campaigns from templates.
* Added support for unsuppressing an email address.
* Improved documentation and tests for getting active subscribers. Clearly
documented the data structure for multi option multi select fields.

## v2.2.0 - 17 Sep, 2012

* Added WorldviewURL field to campaign summary response.
* Added Latitude, Longitude, City, Region, CountryCode, and CountryName fields
in campaign opens and clicks responses.

## v2.1.0 - 30 Aug, 2012

* Added support basic / unlimited pricing.

## v2.0.0 - 22 Aug, 2012

* Added support for UnsubscribeSetting field when creating, updating, and
getting list details.
* Added support for including AddUnsubscribesToSuppList and
ScrubActiveWithSuppList fields when updating a list.
* Added support for getting all client lists to which a subscriber with a
specific email address belongs.
* Removed deprecated warnings and disallowed calls to be made in a deprecated
manner.

## v1.1.1 - 2 Aug, 2012

* Improved documentation to indicate support for Python 2.5, 2.6, and 2.7
* Added support for specifying whether subscription-based autoresponders should
be restarted when adding or updating subscribers.

## v1.1.0 - 15 Jun, 2012

* Added Travis CI support.
* Added support for newly released team management functionality.

## v1.0.2 - 2 Dec, 2011

* Added support for compatibility with Python 2.5 by using old "except" syntax.

## v1.0.1 - 31 Oct, 2011

* Added support for deleting a subscriber.
* Added support for specifying a 'clear' field when updating or importing
subscribers.
* Added support for queuing subscription-based autoresponders when importing
subscribers.
* Added support for retrieving deleted subscribers.
* Added support for including more social sharing stats in campaign summary.
* Added support for unscheduling a campaign.

## v1.0.0 - 26 Oct, 2011

* Initial release which support current Campaign Monitor API.
