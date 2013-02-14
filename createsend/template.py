try:
***REMOVED***import json
except ImportError:
***REMOVED***import simplejson as json
from createsend import CreateSendBase
from utils import json_to_py

class Template(CreateSendBase):
***REMOVED***"""Represents an email template and associated functionality."""

***REMOVED***def __init__(self, auth=None, template_id=None):
***REMOVED******REMOVED***self.template_id = template_id
***REMOVED******REMOVED***super(Template, self).__init__(auth)

***REMOVED***def create(self, client_id, name, html_url, zip_url):
***REMOVED******REMOVED***"""Creates a new email template."""
***REMOVED******REMOVED***body = { 
***REMOVED******REMOVED******REMOVED***"Name": name,
***REMOVED******REMOVED******REMOVED***"HtmlPageURL": html_url,
***REMOVED******REMOVED******REMOVED***"ZipFileURL": zip_url }
***REMOVED******REMOVED***response = self._post("/templates/%s.json" % client_id, json.dumps(body))
***REMOVED******REMOVED***self.template_id = json_to_py(response)
***REMOVED******REMOVED***return self.template_id

***REMOVED***def details(self):
***REMOVED******REMOVED***"""Gets the details of this email template."""
***REMOVED******REMOVED***response = self._get("/templates/%s.json" % self.template_id)
***REMOVED******REMOVED***return json_to_py(response)

***REMOVED***def update(self, name, html_url, zip_url):
***REMOVED******REMOVED***"""Updates this email template."""
***REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED***"Name": name,
***REMOVED******REMOVED******REMOVED***"HtmlPageURL": html_url,
***REMOVED******REMOVED******REMOVED***"ZipFileURL": zip_url }
***REMOVED******REMOVED***response = self._put("/templates/%s.json" % self.template_id, json.dumps(body))

***REMOVED***def delete(self):
***REMOVED******REMOVED***"""Deletes this email template."""
***REMOVED******REMOVED***response = self._delete("/templates/%s.json" % self.template_id)
