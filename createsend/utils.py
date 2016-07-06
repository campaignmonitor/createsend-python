import os
import re
from six.moves.http_client import HTTPSConnection
import socket
import ssl
try:
  import json
except ImportError:
  import simplejson as json

class CertificateError(ValueError):
  """
  Raised when an error occurs when attempting to verify an SSL certificate.
  """
  pass

def _dnsname_to_pat(dn):
  pats = []
  for frag in dn.split(r'.'):
    if frag == '*':
      # When '*' is a fragment by itself, it matches a non-empty dotless
      # fragment.
      pats.append('[^.]+')
    else:
      # Otherwise, '*' matches any dotless fragment.
      frag = re.escape(frag)
      pats.append(frag.replace(r'\*', '[^.]*'))
  return re.compile(r'\A' + r'\.'.join(pats) + r'\Z', re.IGNORECASE)

def match_hostname(cert, hostname):
  """
  This is a backport of the match_hostname() function from Python 3.2,
  essential when using SSL.
  Verifies that *cert* (in decoded format as returned by
  SSLSocket.getpeercert()) matches the *hostname*.  RFC 2818 rules
  are mostly followed, but IP addresses are not accepted for *hostname*.

  CertificateError is raised on failure. On success, the function
  returns nothing.
  """
  if not cert:
    raise ValueError("empty or no certificate")
  dnsnames = []
  san = cert.get('subjectAltName', ())
  for key, value in san:
    if key == 'DNS':
      if _dnsname_to_pat(value).match(hostname):
        return
      dnsnames.append(value)
  if not san:
    # The subject is only checked when subjectAltName is empty
    for sub in cert.get('subject', ()):
      for key, value in sub:
        # XXX according to RFC 2818, the most specific Common Name
        # must be used.
        if key == 'commonName':
          if _dnsname_to_pat(value).match(hostname):
            return
          dnsnames.append(value)
  if len(dnsnames) > 1:
    raise CertificateError("hostname %r "
      "doesn't match either of %s"
      % (hostname, ', '.join(map(repr, dnsnames))))
  elif len(dnsnames) == 1:
    raise CertificateError("hostname %r "
      "doesn't match %r"
      % (hostname, dnsnames[0]))
  else:
    raise CertificateError("no appropriate commonName or "
      "subjectAltName fields were found")

class VerifiedHTTPSConnection(HTTPSConnection):
  """
  A connection that includes SSL certificate verification.
  """
  def connect(self):
    self.connection_kwargs = {}
    # for > py2.5
    if hasattr(self, 'timeout'):
      self.connection_kwargs.update(timeout = self.timeout)

    # for >= py2.7
    if hasattr(self, 'source_address'):
      self.connection_kwargs.update(source_address = self.source_address)

    sock = socket.create_connection((self.host, self.port), **self.connection_kwargs)

    # for >= py2.7
    if getattr(self, '_tunnel_host', None):
      self.sock = sock
      self._tunnel()

    cert_path = os.path.join(os.path.dirname(__file__), 'cacert.pem')

    self.sock = ssl.wrap_socket(
      sock,
      self.key_file,
      self.cert_file,
      cert_reqs=ssl.CERT_REQUIRED,
      ca_certs=cert_path)

    try:
      match_hostname(self.sock.getpeercert(), self.host)
    except CertificateError:
      self.sock.shutdown(socket.SHUT_RDWR)
      self.sock.close()
      raise

def json_to_py(j):
  o = json.loads(j.decode())
  if isinstance(o, dict):
  	return dict_to_object(o)
  else:
    return dict_to_object({ "response": o }).response

def dict_to_object(d):
	"""Recursively converts a dict to an object"""
	top = type('CreateSendModel', (object,), d)
	seqs = tuple, list, set, frozenset
	for i, j in d.items():
	  if isinstance(j, dict):
	    setattr(top, i, dict_to_object(j))
	  elif isinstance(j, seqs):
	    setattr(top, i, type(j)(dict_to_object(sj) if isinstance(sj, dict) else sj for sj in j))
	  else:
	    setattr(top, i, j)
	return top

def get_faker(expected_url, filename, status=None, body = None):

  class Faker(object):
    """Represents a fake web request, including the expected URL, an open 
    function which reads the expected response from a fixture file, and the
    expected response status code."""
    def __init__(self, expected_url, filename, status, body = None):
      self.url = self.createsend_url(expected_url)
      self.filename = filename
      self.status = status
      self.body = body

    def open(self):
      if self.filename:
        return open("%s/../test/fixtures/%s" % (os.path.dirname(__file__), self.filename), mode='rb').read()
      else:
        return ''

    def createsend_url(self, url):
      if url.startswith("http"):
        return url
      else:
        return "https://api.createsend.com/api/v3.1/%s" % url

  return Faker(expected_url, filename, status, body)
