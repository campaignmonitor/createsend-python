***REMOVED***
import json

def json_to_py(j):
***REMOVED***o = json.loads(j)
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

def get_faker(filename, status=None):
***REMOVED***class Faker(object):
***REMOVED******REMOVED***def __init__(self, filename, status):
***REMOVED******REMOVED******REMOVED***self.filename = filename
***REMOVED******REMOVED******REMOVED***self.status = status
***REMOVED******REMOVED***def open(self):
***REMOVED******REMOVED******REMOVED***if self.filename:
***REMOVED******REMOVED******REMOVED******REMOVED***return open("%s/../test/fixtures/%s" % (os.path.dirname(__file__), self.filename)).read()
***REMOVED******REMOVED******REMOVED***else:
***REMOVED******REMOVED******REMOVED******REMOVED***return ''
***REMOVED***return Faker(filename, status)
