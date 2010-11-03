import sys
import os
from distutils.core import setup

from createsend import __version__

setup(name = "createsend",
      version = __version__,
      description = "A wrapper for the CreateSend API v3",
      author = "James Dennes",
      author_email = 'jdennes@gmail.com',
      packages = ['createsend'])
