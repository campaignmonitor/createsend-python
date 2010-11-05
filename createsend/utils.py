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

def get_faker(filename, status=None):
  class Faker(object):
    def __init__(self, filename, status):
      self.filename = filename
      self.status = status
    def open(self):
      if self.filename:
        return open("%s/../test/fixtures/%s" % (os.path.dirname(__file__), self.filename)).read()
      else:
        return ''
  return Faker(filename, status)
