import sys
import os
from distutils.core import setup

from createsend.createsend import __version__

setup(name = "createsend",
      version = __version__,
      description = "A library which implements the complete functionality of the Campaign Monitor API.",
      author = "James Dennes",
      author_email = 'jdennes@gmail.com',
      url = "http://campaignmonitor.github.io/createsend-python/",
      license = "MIT",
      keywords = "createsend campaign monitor email",
      packages = ['createsend'],
      package_data = {'createsend': ['cacert.pem']})
