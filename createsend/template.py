import json
from createsend import CreateSendBase
from utils import json_to_py

class Template(CreateSendBase):
  """Represents an email template and associated functionality."""

  def __init__(self, template_id=None):
    self.template_id = template_id
    super(Template, self).__init__()

  def create(self, client_id, name, html_url, zip_url, screenshot_url):
    """Creates a new email template."""
    body = { 
      "Name": name,
      "HtmlPageURL": html_url,
      "ZipFileURL": zip_url,
      "ScreenshotURL": screenshot_url }
    response = self._post("/templates/%s.json" % client_id, json.dumps(body))
    return json_to_py(response)

  def details(self):
    """Gets the details of this email template."""
    response = self._get("/templates/%s.json" % self.template_id)
    return json_to_py(response)

  def update(self, name, html_url, zip_url, screenshot_url):
    """Updates this email template."""
    body = {
      "Name": name,
      "HtmlPageURL": html_url,
      "ZipFileURL": zip_url,
      "ScreenshotURL": screenshot_url }
    response = self._put("/templates/%s.json" % self.template_id, json.dumps(body))

  def delete(self):
    """Deletes this email template."""
    response = self._delete("/templates/%s.json" % self.template_id)
