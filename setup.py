from os import path
from codecs import open
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    print("Please install setuptools: pip install setuptools")
    sys.exit(1)

from lib.release import __version__, __author__

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as requirements_file:
    install_requirements = requirements_file.read().splitlines()
    if not install_requirements:
        print("Unable to read requirements from the requirements.txt file.")
        sys.exit(2)

setup(
    name="createsend",
    version=__version__,
    description="A library which implements the complete functionality of the Campaign Monitor API.",
    author=__author__,
    author_email='support@campaignmonitor.com',
    url="http://campaignmonitor.github.io/createsend-python/",
    license="MIT",
    keywords="createsend campaign monitor email",
    install_requires=install_requirements,
    packages=find_packages('lib'),
    package_dir={'': 'lib'},
    package_data={'': ['cacert.pem']},
)
