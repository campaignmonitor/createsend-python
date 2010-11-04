import unittest

from createsend import Template

class TemplateTestCase(unittest.TestCase):

***REMOVED***def setUp(self):
***REMOVED******REMOVED***self.template = Template("98y2e98y289dh89h938389")

***REMOVED***def test_create(self):
***REMOVED******REMOVED***client_id = '87y8d7qyw8d7yq8w7ydwqwd'
***REMOVED******REMOVED***self.template.stub_request("create_template.json")
***REMOVED******REMOVED***template_id = self.template.create(client_id, "Template One", "http://templates.org/index.html", 
***REMOVED******REMOVED******REMOVED***"http://templates.org/files.zip", "http://templates.org/screenshot.jpg")
***REMOVED******REMOVED***self.assertEquals(template_id, "98y2e98y289dh89h938389")
***REMOVED******REMOVED***
***REMOVED***def test_details(self):
***REMOVED******REMOVED***self.template.stub_request("template_details.json")
***REMOVED******REMOVED***t = self.template.details()
***REMOVED******REMOVED***self.assertEquals(t.TemplateID, "98y2e98y289dh89h938389")
***REMOVED******REMOVED***self.assertEquals(t.Name, "Template One")
***REMOVED******REMOVED***self.assertEquals(t.PreviewURL, "http://preview.createsend.com/createsend/templates/previewTemplate.aspx?ID=01AF532CD8889B33&d=r&c=E816F55BFAD1A753")
***REMOVED******REMOVED***self.assertEquals(t.ScreenshotURL, "http://preview.createsend.com/ts/r/14/833/263/14833263.jpg?0318092600")

***REMOVED***def test_update(self):
***REMOVED******REMOVED***self.template.stub_request(None)
***REMOVED******REMOVED***self.template.update("Template One Updated", "http://templates.org/index.html", "http://templates.org/files.zip", "http://templates.org/screenshot.jpg")
***REMOVED***
***REMOVED***def test_delete(self):
***REMOVED******REMOVED***self.template.stub_request(None)
***REMOVED******REMOVED***self.template.delete()
