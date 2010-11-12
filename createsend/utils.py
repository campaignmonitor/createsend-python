import os
import json

def json_to_py(j):
  o = json.loads(j)
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

def get_faker(expected_url, filename, status=None):

  class Faker(object):
    """Represents a fake web request, including the expected URL, an open 
    function which reads the expected response from a fixture file, and the
    expected response status code."""
    def __init__(self, expected_url, filename, status):
      self.url = self.createsend_url(expected_url)
      self.filename = filename
      self.status = status

    def open(self):
      if self.filename:
        return open("%s/../test/fixtures/%s" % (os.path.dirname(__file__), self.filename)).read()
      else:
        return ''

    def createsend_url(self, url):
      if url.startswith("http"):
        return url
      else:
        return "http://api.createsend.com/api/v3/%s" % url

  return Faker(expected_url, filename, status)
