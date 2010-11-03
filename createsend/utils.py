
import json

def json_to_py(j):
  o = json.loads(j)
  if isinstance(o, dict):
  	return dict_to_object(o)
  elif isinstance(o, list):
    return dict_to_object({ "response": o }).response
  else:
    raise Exception("Sorry, can't process that type.")

def dict_to_object(d):
	"""Recursively converts a dict to an object"""
	top = type('new', (object,), d)
	seqs = tuple, list, set, frozenset
	for i, j in d.items():
	  if isinstance(j, dict):
	    setattr(top, i, dict_to_object(j))
	  elif isinstance(j, seqs):
	    setattr(top, i, type(j)(dict_to_object(sj) if isinstance(sj, dict) else sj for sj in j))
	  else:
	    setattr(top, i, j)
	return top
