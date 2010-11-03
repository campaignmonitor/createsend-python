***REMOVED***
import json

def json_to_py(j):
***REMOVED***
***REMOVED***print j
***REMOVED***
***REMOVED***o = json.loads(j)
***REMOVED***if isinstance(o, dict):
***REMOVED***	return dict_to_object(o)
***REMOVED***elif isinstance(o, list):
***REMOVED******REMOVED***return dict_to_object({ "response": o }).response
***REMOVED***else:
***REMOVED******REMOVED***raise Exception("Sorry, can't process that type.")

def dict_to_object(d):
	"""Recursively converts a dict to an object"""
	top = type('new', (object,), d)
	seqs = tuple, list, set, frozenset
	for i, j in d.items():
	***REMOVED***if isinstance(j, dict):
	***REMOVED******REMOVED***setattr(top, i, dict_to_object(j))
	***REMOVED***elif isinstance(j, seqs):
	***REMOVED******REMOVED***setattr(top, i, type(j)(dict_to_object(sj) if isinstance(sj, dict) else sj for sj in j))
	***REMOVED***else:
	***REMOVED******REMOVED***setattr(top, i, j)
	return top

def get_fake_opener(filename):
***REMOVED***def fake_opener():
***REMOVED******REMOVED***return open("%s/../test/fixtures/%s" % (os.path.dirname(__file__), filename))
***REMOVED***return fake_opener
