from distutils.core import setup

from createsend.createsend import __version__

setup(
    name="createsend",
    version=__version__,
    description="A library which implements the complete functionality of the Campaign Monitor API.",
    author="Dylan Stein",
    author_email='djstein@ncsu.edu',
    url="http://campaignmonitor.github.io/createsend-python/",
    license="MIT",
    keywords="createsend campaign monitor email",
    packages=['createsend'],
    package_data={'createsend': ['cacert.pem']},
    install_requires=['six'],
)
