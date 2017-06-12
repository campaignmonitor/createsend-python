try:
***REMOVED******REMOVED***import json
except ImportError:
***REMOVED******REMOVED***import simplejson as json
from createsend.createsend import CreateSendBase
from createsend.utils import json_to_py


class Template(CreateSendBase):
***REMOVED******REMOVED***"""Represents an email template and associated functionality."""

***REMOVED******REMOVED***def __init__(self, auth=None, template_id=None):
***REMOVED******REMOVED******REMOVED******REMOVED***self.template_id = template_id
***REMOVED******REMOVED******REMOVED******REMOVED***super(Template, self).__init__(auth)

***REMOVED******REMOVED***def create(self, client_id, name, html_url, zip_url):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Creates a new email template."""
***REMOVED******REMOVED******REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Name": name,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"HtmlPageURL": html_url,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"ZipFileURL": zip_url}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._post("/templates/%s.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***client_id, json.dumps(body))
***REMOVED******REMOVED******REMOVED******REMOVED***self.template_id = json_to_py(response)
***REMOVED******REMOVED******REMOVED******REMOVED***return self.template_id

***REMOVED******REMOVED***def details(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Gets the details of this email template."""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._get("/templates/%s.json" % self.template_id)
***REMOVED******REMOVED******REMOVED******REMOVED***return json_to_py(response)

***REMOVED******REMOVED***def update(self, name, html_url, zip_url):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Updates this email template."""
***REMOVED******REMOVED******REMOVED******REMOVED***body = {
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"Name": name,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"HtmlPageURL": html_url,
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***"ZipFileURL": zip_url}
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._put("/templates/%s.json" %
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED*** self.template_id, json.dumps(body))

***REMOVED******REMOVED***def delete(self):
***REMOVED******REMOVED******REMOVED******REMOVED***"""Deletes this email template."""
***REMOVED******REMOVED******REMOVED******REMOVED***response = self._delete("/templates/%s.json" % self.template_id)
