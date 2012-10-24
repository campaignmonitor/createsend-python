# createsend-python history

## v2.3.0 - 10 Oct, 2012   (2293fc80)

* Added support for creating campaigns from templates.
* Added support for unsuppressing an email address.
* Improved documentation and tests for getting active subscribers. Clearly
documented the data structure for multi option multi select fields.

## v2.2.0 - 17 Sep, 2012   (879f83f4)

* Added WorldviewURL field to campaign summary response.
* Added Latitude, Longitude, City, Region, CountryCode, and CountryName fields
in campaign opens and clicks responses.

## v2.1.0 - 30 Aug, 2012   (205ebd1f)

* Added support basic / unlimited pricing.

## v2.0.0 - 22 Aug, 2012   (6cd3f8a9)

* Added support for UnsubscribeSetting field when creating, updating, and
getting list details.
* Added support for including AddUnsubscribesToSuppList and
ScrubActiveWithSuppList fields when updating a list.
* Added support for getting all client lists to which a subscriber with a
specific email address belongs.
* Removed deprecated warnings and disallowed calls to be made in a deprecated
manner.

## v1.1.1 - 2 Aug, 2012   (2380c0d0)

* Improved documentation to indicate support for Python 2.5, 2.6, and 2.7
* Added support for specifying whether subscription-based autoresponders should
be restarted when adding or updating subscribers.

## v1.1.0 - 15 Jun, 2012   (f5ea7476)

* Added Travis CI support.
* Added support for newly released team management functionality.

## v1.0.2 - 2 Dec, 2011   (a231886b)

* Added support for compatibility with Python 2.5 by using old "except" syntax.

## v1.0.1 - 31 Oct, 2011   (a1bf076d)

* Added support for deleting a subscriber.
* Added support for specifying a 'clear' field when updating or importing
subscribers.
* Added support for queuing subscription-based autoresponders when importing
subscribers.
* Added support for retrieving deleted subscribers.
* Added support for including more social sharing stats in campaign summary.
* Added support for unscheduling a campaign.

## v1.0.0 - 26 Oct, 2011   (644ff8aa)

* Initial release which support current Campaign Monitor API.
