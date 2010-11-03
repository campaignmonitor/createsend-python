***REMOVED***

def get_fake_opener(filename):
***REMOVED***def fake_opener(filename):
***REMOVED******REMOVED***return open("%s/fixtures/%s" % (os.path.dirname(__file__), filename))
***REMOVED***return fake_opener
