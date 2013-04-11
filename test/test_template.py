import unittest
import urllib

from createsend import *

class TemplateTestCase(object):

  def test_create(self):
    client_id = '87y8d7qyw8d7yq8w7ydwqwd'
    t = Template()
    t.stub_request("templates/%s.json" % client_id, "create_template.json")
    template_id = t.create(client_id, "Template One", "http://templates.org/index.html", 
      "http://templates.org/files.zip")
    self.assertEquals(template_id, "98y2e98y289dh89h9383891234")
    self.assertEquals(t.template_id, "98y2e98y289dh89h9383891234")

  def test_details(self):
    self.template.stub_request("templates/%s.json" % self.template.template_id, "template_details.json")
    t = self.template.details()
    self.assertEquals(t.TemplateID, "98y2e98y289dh89h938389")
    self.assertEquals(t.Name, "Template One")
    self.assertEquals(t.PreviewURL, "http://preview.createsend.com/createsend/templates/previewTemplate.aspx?ID=01AF532CD8889B33&d=r&c=E816F55BFAD1A753")
    self.assertEquals(t.ScreenshotURL, "http://preview.createsend.com/ts/r/14/833/263/14833263.jpg?0318092600")

  def test_update(self):
    self.template.stub_request("templates/%s.json" % self.template.template_id, None)
    self.template.update("Template One Updated", "http://templates.org/index.html", "http://templates.org/files.zip")
  
  def test_delete(self):
    self.template.stub_request("templates/%s.json" % self.template.template_id, None)
    self.template.delete()

class OAuthTemplateTestCase(unittest.TestCase, TemplateTestCase):
  """Test when using OAuth to authenticate"""
  def setUp(self):
    self.template = Template(
      {"access_token": "ASP95S4aR+9KsgfHB0dapTYxNA==", "refresh_token": "5S4aASP9R+9KsgfHB0dapTYxNA=="},
      "98y2e98y289dh89h938389")

class ApiKeyTemplateTestCase(unittest.TestCase, TemplateTestCase):
  """Test when using an API key to authenticate"""
  def setUp(self):
    self.template = Template(
      {'api_key': '123123123123123123123'},
      "98y2e98y289dh89h938389")
