***REMOVED***
import re
from six.moves.http_client import HTTPSConnection
import socket
import ssl
try:
***REMOVED******REMOVED***import json
except ImportError:
***REMOVED******REMOVED***import simplejson as json


class CertificateError(ValueError):
***REMOVED******REMOVED***"""
***REMOVED******REMOVED***Raised when an error occurs when attempting to verify an SSL certificate.
***REMOVED******REMOVED***"""
***REMOVED******REMOVED***pass


def _dnsname_to_pat(dn):
***REMOVED******REMOVED***pats = []
***REMOVED******REMOVED***for frag in dn.split(r'.'):
***REMOVED******REMOVED******REMOVED******REMOVED***if frag == '*':
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***# When '*' is a fragment by itself, it matches a non-empty dotless
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***# fragment.
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***pats.append('[^.]+')
***REMOVED******REMOVED******REMOVED******REMOVED***else:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***# Otherwise, '*' matches any dotless fragment.
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***frag = re.escape(frag)
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***pats.append(frag.replace(r'\*', '[^.]*'))
***REMOVED******REMOVED***return re.compile(r'\A' + r'\.'.join(pats) + r'\Z', re.IGNORECASE)


def match_hostname(cert, hostname):
***REMOVED******REMOVED***"""
***REMOVED******REMOVED***This is a backport of the match_hostname() function from Python 3.2,
***REMOVED******REMOVED***essential when using SSL.
***REMOVED******REMOVED***Verifies that *cert* (in decoded format as returned by
***REMOVED******REMOVED***SSLSocket.getpeercert()) matches the *hostname*.***REMOVED***RFC 2818 rules
***REMOVED******REMOVED***are mostly followed, but IP addresses are not accepted for *hostname*.

***REMOVED******REMOVED***CertificateError is raised on failure. On success, the function
***REMOVED******REMOVED***returns nothing.
***REMOVED******REMOVED***"""
***REMOVED******REMOVED***if not cert:
***REMOVED******REMOVED******REMOVED******REMOVED***raise ValueError("empty or no certificate")
***REMOVED******REMOVED***dnsnames = []
***REMOVED******REMOVED***san = cert.get('subjectAltName', ())
***REMOVED******REMOVED***for key, value in san:
***REMOVED******REMOVED******REMOVED******REMOVED***if key == 'DNS':
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***if _dnsname_to_pat(value).match(hostname):
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***return
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***dnsnames.append(value)
***REMOVED******REMOVED***if not san:
***REMOVED******REMOVED******REMOVED******REMOVED***# The subject is only checked when subjectAltName is empty
***REMOVED******REMOVED******REMOVED******REMOVED***for sub in cert.get('subject', ()):
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***for key, value in sub:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***# XXX according to RFC 2818, the most specific Common Name
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***# must be used.
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***if key == 'commonName':
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***if _dnsname_to_pat(value).match(hostname):
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***return
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***dnsnames.append(value)
***REMOVED******REMOVED***if len(dnsnames) > 1:
***REMOVED******REMOVED******REMOVED******REMOVED***raise CertificateError("hostname %r "
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** "doesn't match either of %s"
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** % (hostname, ', '.join(map(repr, dnsnames))))
***REMOVED******REMOVED***elif len(dnsnames) == 1:
***REMOVED******REMOVED******REMOVED******REMOVED***raise CertificateError("hostname %r "
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** "doesn't match %r"
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** % (hostname, dnsnames[0]))
***REMOVED******REMOVED***else:
***REMOVED******REMOVED******REMOVED******REMOVED***raise CertificateError("no appropriate commonName or "
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** "subjectAltName fields were found")


class VerifiedHTTPSConnection(HTTPSConnection):
***REMOVED******REMOVED***"""
***REMOVED******REMOVED***A connection that includes SSL certificate verification.
***REMOVED******REMOVED***"""

***REMOVED******REMOVED***def connect(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.connection_kwargs = {}
***REMOVED******REMOVED******REMOVED******REMOVED***# for > py2.5
***REMOVED******REMOVED******REMOVED******REMOVED***if hasattr(self, 'timeout'):
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.connection_kwargs.update(timeout=self.timeout)

***REMOVED******REMOVED******REMOVED******REMOVED***# for >= py2.7
***REMOVED******REMOVED******REMOVED******REMOVED***if hasattr(self, 'source_address'):
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.connection_kwargs.update(source_address=self.source_address)

***REMOVED******REMOVED******REMOVED******REMOVED***sock = socket.create_connection(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***(self.host, self.port), **self.connection_kwargs)

***REMOVED******REMOVED******REMOVED******REMOVED***# for >= py2.7
***REMOVED******REMOVED******REMOVED******REMOVED***if getattr(self, '_tunnel_host', None):
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.sock = sock
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self._tunnel()

***REMOVED******REMOVED******REMOVED******REMOVED***cert_path = os.path.join(os.path.dirname(__file__), 'cacert.pem')

***REMOVED******REMOVED******REMOVED******REMOVED***self.sock = ssl.wrap_socket(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***sock,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.key_file,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.cert_file,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***cert_reqs=ssl.CERT_REQUIRED,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***ca_certs=cert_path)

***REMOVED******REMOVED******REMOVED******REMOVED***try:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***match_hostname(self.sock.getpeercert(), self.host)
***REMOVED******REMOVED******REMOVED******REMOVED***except CertificateError:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.sock.shutdown(socket.SHUT_RDWR)
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.sock.close()
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***raise


def json_to_py(j):
***REMOVED******REMOVED***o = json.loads(j.decode('utf-8'))
***REMOVED******REMOVED***if isinstance(o, dict):
***REMOVED******REMOVED******REMOVED******REMOVED***return dict_to_object(o)
***REMOVED******REMOVED***else:
***REMOVED******REMOVED******REMOVED******REMOVED***return dict_to_object({"response": o}).response


def dict_to_object(d):
***REMOVED******REMOVED***"""Recursively converts a dict to an object"""
***REMOVED******REMOVED***top = type('CreateSendModel', (object,), d)
***REMOVED******REMOVED***seqs = tuple, list, set, frozenset
***REMOVED******REMOVED***for i, j in list(d.items()):
***REMOVED******REMOVED******REMOVED******REMOVED***if isinstance(j, dict):
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***setattr(top, i, dict_to_object(j))
***REMOVED******REMOVED******REMOVED******REMOVED***elif isinstance(j, seqs):
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***setattr(top, i, type(j)(dict_to_object(sj)
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***if isinstance(sj, dict) else sj for sj in j))
***REMOVED******REMOVED******REMOVED******REMOVED***else:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***setattr(top, i, j)
***REMOVED******REMOVED***return top


def get_faker(expected_url, filename, status=None, body=None):

***REMOVED******REMOVED***class Faker(object):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Represents a fake web request, including the expected URL, an open 
***REMOVED******REMOVED******REMOVED******REMOVED***function which reads the expected response from a fixture file, and the
***REMOVED******REMOVED******REMOVED******REMOVED***expected response status code."""

***REMOVED******REMOVED******REMOVED******REMOVED***def __init__(self, expected_url, filename, status, body=None):
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.url = self.createsend_url(expected_url)
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.filename = filename
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.status = status
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***self.body = body

***REMOVED******REMOVED******REMOVED******REMOVED***def open(self):
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***if self.filename:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***return open("%s/../test/fixtures/%s" % (os.path.dirname(__file__), self.filename), mode='rb').read()
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***else:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***return ''

***REMOVED******REMOVED******REMOVED******REMOVED***def createsend_url(self, url):
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***if url.startswith("http"):
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***return url
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***else:
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***return "https://api.createsend.com/api/v3.1/%s" % url

***REMOVED******REMOVED***return Faker(expected_url, filename, status, body)
