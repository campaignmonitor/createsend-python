from os import path
from codecs import open
***REMOVED***

try:
***REMOVED******REMOVED***from setuptools import setup, find_packages
except ImportError:
***REMOVED******REMOVED***print("Please install setuptools: pip install setuptools")
***REMOVED******REMOVED***sys.exit(1)

from lib.release import __version__, __author__

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as requirements_file:
***REMOVED******REMOVED***install_requirements = requirements_file.read().splitlines()
***REMOVED******REMOVED***if not install_requirements:
***REMOVED******REMOVED******REMOVED******REMOVED***print("Unable to read requirements from the requirements.txt file.")
***REMOVED******REMOVED******REMOVED******REMOVED***sys.exit(2)

setup(
***REMOVED******REMOVED***name="createsend",
***REMOVED******REMOVED***version=__version__,
***REMOVED******REMOVED***description="A library which implements the complete functionality of the Campaign Monitor API.",
***REMOVED******REMOVED***author=__author__,
***REMOVED******REMOVED***author_email='support@campaignmonitor.com',
***REMOVED******REMOVED***url="http://campaignmonitor.github.io/createsend-python/",
***REMOVED******REMOVED***license="MIT",
***REMOVED******REMOVED***keywords="createsend campaign monitor email",
***REMOVED******REMOVED***install_requires=install_requirements,
***REMOVED******REMOVED***packages=find_packages('lib'),
***REMOVED******REMOVED***package_dir={'': 'lib'},
***REMOVED******REMOVED***package_data={'': ['cacert.pem']},
)
