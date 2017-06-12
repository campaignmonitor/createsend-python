from distutils.core import setup

from createsend.createsend import __version__

setup(
***REMOVED******REMOVED***name="createsend",
***REMOVED******REMOVED***version=__version__,
***REMOVED******REMOVED***description="A library which implements the complete functionality of the Campaign Monitor API.",
***REMOVED******REMOVED***author="Dylan Stein",
***REMOVED******REMOVED***author_email='djstein@ncsu.edu',
***REMOVED******REMOVED***url="http://campaignmonitor.github.io/createsend-python/",
***REMOVED******REMOVED***license="MIT",
***REMOVED******REMOVED***keywords="createsend campaign monitor email",
***REMOVED******REMOVED***packages=['createsend'],
***REMOVED******REMOVED***package_data={'createsend': ['cacert.pem']},
***REMOVED******REMOVED***install_requires=['six'],
)
