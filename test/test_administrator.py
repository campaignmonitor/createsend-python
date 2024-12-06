from urllib.parse import quote
import unittest

from createsend.administrator import Administrator


class AdministratorTestCase:

    def test_get(self):
        email = "admin@example.com"
        self.administrator.stub_request(
            "admins.json?email=%s" % quote(email), "admin_details.json")
        administrator = self.administrator.get(email)
        self.assertEqual(administrator.EmailAddress, email)
        self.assertEqual(administrator.Name, "Admin One")
        self.assertEqual(administrator.Status, "Active")

    def test_get_without_args(self):
        email = "admin@example.com"
        self.administrator.stub_request(
            "admins.json?email=%s" % quote(email), "admin_details.json")
        administrator = self.administrator.get()
        self.assertEqual(administrator.EmailAddress, email)
        self.assertEqual(administrator.Name, "Admin One")
        self.assertEqual(administrator.Status, "Active")

    def test_add(self):
        self.administrator.stub_request("admins.json", "add_admin.json")
        result = self.administrator.add("admin@example.com", "Admin Name")
        self.assertEqual(result.EmailAddress, "admin@example.com")

    def test_update(self):
        new_email = "new_email_address@example.com"
        self.administrator.stub_request("admins.json?email=%s" % quote(
            self.administrator.email_address), None)
        self.administrator.update(new_email, "Admin New Name")
        self.assertEqual(self.administrator.email_address, new_email)

    def test_delete(self):
        self.administrator.stub_request("admins.json?email=%s" % quote(
            self.administrator.email_address), None)
        email_address = self.administrator.delete()


class OAuthAdministratorTestCase(unittest.TestCase, AdministratorTestCase):
    """Test when using OAuth to authenticate"""

    def setUp(self):
        self.administrator = Administrator(
            {"access_token": "ASP95S4aR+9KsgfHB0dapTYxNA==", "refresh_token": "5S4aASP9R+9KsgfHB0dapTYxNA=="}, "admin@example.com")


class ApiKeyAdministratorTestCase(unittest.TestCase, AdministratorTestCase):
    """Test when using an API key to authenticate"""

    def setUp(self):
        self.administrator = Administrator(
            {'api_key': '123123123123123123123'}, "admin@example.com")
