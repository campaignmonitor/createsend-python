import unittest

from createsend.createsend import Template


class TemplateTestCase(object):

***REMOVED******REMOVED***def test_create(self):
***REMOVED******REMOVED******REMOVED******REMOVED***client_id = '87y8d7qyw8d7yq8w7ydwqwd'
***REMOVED******REMOVED******REMOVED******REMOVED***t = Template()
***REMOVED******REMOVED******REMOVED******REMOVED***t.stub_request("templates/%s.json" % client_id, "create_template.json")
***REMOVED******REMOVED******REMOVED******REMOVED***template_id = t.create(client_id, "Template One", "http://templates.org/index.html",
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** "http://templates.org/files.zip")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(template_id, "98y2e98y289dh89h9383891234")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(t.template_id, "98y2e98y289dh89h9383891234")

***REMOVED******REMOVED***def test_details(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.template.stub_request(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"templates/%s.json" % self.template.template_id, "template_details.json")
***REMOVED******REMOVED******REMOVED******REMOVED***t = self.template.details()
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(t.TemplateID, "98y2e98y289dh89h938389")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(t.Name, "Template One")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***t.PreviewURL, "http://preview.createsend.com/createsend/templates/previewTemplate.aspx?ID=01AF532CD8889B33&d=r&c=E816F55BFAD1A753")
***REMOVED******REMOVED******REMOVED******REMOVED***self.assertEquals(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***t.ScreenshotURL, "http://preview.createsend.com/ts/r/14/833/263/14833263.jpg?0318092600")

***REMOVED******REMOVED***def test_update(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.template.stub_request("templates/%s.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.template.template_id, None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.template.update(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Template One Updated", "http://templates.org/index.html", "http://templates.org/files.zip")

***REMOVED******REMOVED***def test_delete(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.template.stub_request("templates/%s.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.template.template_id, None)
***REMOVED******REMOVED******REMOVED******REMOVED***self.template.delete()


class OAuthTemplateTestCase(unittest.TestCase, TemplateTestCase):
***REMOVED******REMOVED***"""Test when using OAuth to authenticate"""

***REMOVED******REMOVED***def setUp(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.template = Template(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{"access_token": "ASP95S4aR+9KsgfHB0dapTYxNA==",
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"refresh_token": "5S4aASP9R+9KsgfHB0dapTYxNA=="},
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"98y2e98y289dh89h938389")


class ApiKeyTemplateTestCase(unittest.TestCase, TemplateTestCase):
***REMOVED******REMOVED***"""Test when using an API key to authenticate"""

***REMOVED******REMOVED***def setUp(self):
***REMOVED******REMOVED******REMOVED******REMOVED***self.template = Template(
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***{'api_key': '123123123123123123123'},
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"98y2e98y289dh89h938389")
