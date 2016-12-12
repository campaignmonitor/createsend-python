***REMOVED***
import re
from six.moves.http_client import HTTPSConnection
import socket
import ssl
try:
***REMOVED***import json
except ImportError:
***REMOVED***import simplejson as json

class CertificateError(ValueError):
***REMOVED***"""
***REMOVED***Raised when an error occurs when attempting to verify an SSL certificate.
***REMOVED***"""
***REMOVED***pass

def _dnsname_to_pat(dn):
***REMOVED***pats = []
***REMOVED***for frag in dn.split(r'.'):
***REMOVED******REMOVED***if frag == '*':
***REMOVED******REMOVED******REMOVED***# When '*' is a fragment by itself, it matches a non-empty dotless
***REMOVED******REMOVED******REMOVED***# fragment.
***REMOVED******REMOVED******REMOVED***pats.append('[^.]+')
***REMOVED******REMOVED***else:
***REMOVED******REMOVED******REMOVED***# Otherwise, '*' matches any dotless fragment.
***REMOVED******REMOVED******REMOVED***frag = re.escape(frag)
***REMOVED******REMOVED******REMOVED***pats.append(frag.replace(r'\*', '[^.]*'))
***REMOVED***return re.compile(r'\A' + r'\.'.join(pats) + r'\Z', re.IGNORECASE)

def match_hostname(cert, hostname):
***REMOVED***"""
***REMOVED***This is a backport of the match_hostname() function from Python 3.2,
***REMOVED***essential when using SSL.
***REMOVED***Verifies that *cert* (in decoded format as returned by
***REMOVED***SSLSocket.getpeercert()) matches the *hostname*.***REMOVED***RFC 2818 rules
***REMOVED***are mostly followed, but IP addresses are not accepted for *hostname*.

***REMOVED***CertificateError is raised on failure. On success, the function
***REMOVED***returns nothing.
***REMOVED***"""
***REMOVED***if not cert:
***REMOVED******REMOVED***raise ValueError("empty or no certificate")
***REMOVED***dnsnames = []
***REMOVED***san = cert.get('subjectAltName', ())
***REMOVED***for key, value in san:
***REMOVED******REMOVED***if key == 'DNS':
***REMOVED******REMOVED******REMOVED***if _dnsname_to_pat(value).match(hostname):
***REMOVED******REMOVED******REMOVED******REMOVED***return
***REMOVED******REMOVED******REMOVED***dnsnames.append(value)
***REMOVED***if not san:
***REMOVED******REMOVED***# The subject is only checked when subjectAltName is empty
***REMOVED******REMOVED***for sub in cert.get('subject', ()):
***REMOVED******REMOVED******REMOVED***for key, value in sub:
***REMOVED******REMOVED******REMOVED******REMOVED***# XXX according to RFC 2818, the most specific Common Name
***REMOVED******REMOVED******REMOVED******REMOVED***# must be used.
***REMOVED******REMOVED******REMOVED******REMOVED***if key == 'commonName':
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***if _dnsname_to_pat(value).match(hostname):
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***return
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***dnsnames.append(value)
***REMOVED***if len(dnsnames) > 1:
***REMOVED******REMOVED***raise CertificateError("hostname %r "
***REMOVED******REMOVED******REMOVED***"doesn't match either of %s"
***REMOVED******REMOVED******REMOVED***% (hostname, ', '.join(map(repr, dnsnames))))
***REMOVED***elif len(dnsnames) == 1:
***REMOVED******REMOVED***raise CertificateError("hostname %r "
***REMOVED******REMOVED******REMOVED***"doesn't match %r"
***REMOVED******REMOVED******REMOVED***% (hostname, dnsnames[0]))
***REMOVED***else:
***REMOVED******REMOVED***raise CertificateError("no appropriate commonName or "
***REMOVED******REMOVED******REMOVED***"subjectAltName fields were found")

class VerifiedHTTPSConnection(HTTPSConnection):
***REMOVED***"""
***REMOVED***A connection that includes SSL certificate verification.
***REMOVED***"""
***REMOVED***def connect(self):
***REMOVED******REMOVED***self.connection_kwargs = {}
***REMOVED******REMOVED***# for > py2.5
***REMOVED******REMOVED***if hasattr(self, 'timeout'):
***REMOVED******REMOVED******REMOVED***self.connection_kwargs.update(timeout = self.timeout)

***REMOVED******REMOVED***# for >= py2.7
***REMOVED******REMOVED***if hasattr(self, 'source_address'):
***REMOVED******REMOVED******REMOVED***self.connection_kwargs.update(source_address = self.source_address)

***REMOVED******REMOVED***sock = socket.create_connection((self.host, self.port), **self.connection_kwargs)

***REMOVED******REMOVED***# for >= py2.7
***REMOVED******REMOVED***if getattr(self, '_tunnel_host', None):
***REMOVED******REMOVED******REMOVED***self.sock = sock
***REMOVED******REMOVED******REMOVED***self._tunnel()

***REMOVED******REMOVED***cert_path = os.path.join(os.path.dirname(__file__), 'cacert.pem')

***REMOVED******REMOVED***self.sock = ssl.wrap_socket(
***REMOVED******REMOVED******REMOVED***sock,
***REMOVED******REMOVED******REMOVED***self.key_file,
***REMOVED******REMOVED******REMOVED***self.cert_file,
***REMOVED******REMOVED******REMOVED***cert_reqs=ssl.CERT_REQUIRED,
***REMOVED******REMOVED******REMOVED***ca_certs=cert_path)

***REMOVED******REMOVED***try:
***REMOVED******REMOVED******REMOVED***match_hostname(self.sock.getpeercert(), self.host)
***REMOVED******REMOVED***except CertificateError:
***REMOVED******REMOVED******REMOVED***self.sock.shutdown(socket.SHUT_RDWR)
***REMOVED******REMOVED******REMOVED***self.sock.close()
***REMOVED******REMOVED******REMOVED***raise

def json_to_py(j):
***REMOVED***o = json.loads(j.decode('utf-8'))
***REMOVED***if isinstance(o, dict):
***REMOVED***	return dict_to_object(o)
***REMOVED***else:
***REMOVED******REMOVED***return dict_to_object({ "response": o }).response

def dict_to_object(d):
	"""Recursively converts a dict to an object"""
	top = type('CreateSendModel', (object,), d)
	seqs = tuple, list, set, frozenset
	for i, j in d.items():
	***REMOVED***if isinstance(j, dict):
	***REMOVED******REMOVED***setattr(top, i, dict_to_object(j))
	***REMOVED***elif isinstance(j, seqs):
	***REMOVED******REMOVED***setattr(top, i, type(j)(dict_to_object(sj) if isinstance(sj, dict) else sj for sj in j))
	***REMOVED***else:
	***REMOVED******REMOVED***setattr(top, i, j)
	return top

def get_faker(expected_url, filename, status=None, body = None):

***REMOVED***class Faker(object):
***REMOVED******REMOVED***"""Represents a fake web request, including the expected URL, an open 
***REMOVED******REMOVED***function which reads the expected response from a fixture file, and the
***REMOVED******REMOVED***expected response status code."""
***REMOVED******REMOVED***def __init__(self, expected_url, filename, status, body = None):
***REMOVED******REMOVED******REMOVED***self.url = self.createsend_url(expected_url)
***REMOVED******REMOVED******REMOVED***self.filename = filename
***REMOVED******REMOVED******REMOVED***self.status = status
***REMOVED******REMOVED******REMOVED***self.body = body

***REMOVED******REMOVED***def open(self):
***REMOVED******REMOVED******REMOVED***if self.filename:
***REMOVED******REMOVED******REMOVED******REMOVED***return open("%s/../test/fixtures/%s" % (os.path.dirname(__file__), self.filename), mode='rb').read()
***REMOVED******REMOVED******REMOVED***else:
***REMOVED******REMOVED******REMOVED******REMOVED***return ''

***REMOVED******REMOVED***def createsend_url(self, url):
***REMOVED******REMOVED******REMOVED***if url.startswith("http"):
***REMOVED******REMOVED******REMOVED******REMOVED***return url
***REMOVED******REMOVED******REMOVED***else:
***REMOVED******REMOVED******REMOVED******REMOVED***return "https://api.createsend.com/api/v3.1/%s" % url

***REMOVED***return Faker(expected_url, filename, status, body)
