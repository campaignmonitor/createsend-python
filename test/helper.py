import os

def get_fake_opener(filename):
  def fake_opener(filename):
    return open("%s/fixtures/%s" % (os.path.dirname(__file__), filename))
  return fake_opener
