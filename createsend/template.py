import json
from createsend import CreateSendBase
from utils import json_to_py

class Template(CreateSendBase):

***REMOVED***def __init__(self, template_id=None):
***REMOVED******REMOVED***self.template_id = template_id
***REMOVED******REMOVED***super(Template, self).__init__()

***REMOVED***def create(self, client_id, name, html_url, zip_url, screenshot_url):
***REMOVED******REMOVED***body = { 
***REMOVED******REMOVED******REMOVED***"Name": name,
***REMOVED******REMOVED******REMOVED***"HtmlPageURL": html_url,
***REMOVED******REMOVED******REMOVED***"ZipFileURL": zip_url,
***REMOVED******REMOVED******REMOVED***"ScreenshotURL": screenshot_url }
***REMOVED******REMOVED***response = self._post("/templates/%s.json" % client_id, json.dumps(body))
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def details(self):
***REMOVED******REMOVED***response = self._get("/templates/%s.json" % self.template_id)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def update(self, name, html_url, zip_url, screenshot_url):
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"Name": name,
***REMOVED******REMOVED******REMOVED***"HtmlPageURL": html_url,
***REMOVED******REMOVED******REMOVED***"ZipFileURL": zip_url,
***REMOVED******REMOVED******REMOVED***"ScreenshotURL": screenshot_url }
***REMOVED******REMOVED***response = self._put("/templates/%s.json" % self.template_id, json.dumps(body))

***REMOVED***def delete(self):
***REMOVED******REMOVED***response = self._delete("/templates/%s.json" % self.template_id)
