import unittest
from unittest.mock import patch
import socket
import ssl
import certifi

from createsend.createsend import CreateSend, Unauthorized
from createsend.utils import CertificateError, VerifiedHTTPSConnection, match_hostname


class VerifiedHTTPSConnectionTestCase(unittest.TestCase):

    def setUp(self):
        self.cs = CreateSend({'api_key': 'not an api key'})

    def test_verified_connection_no_cert(self):
        self.assertRaises(ValueError, match_hostname,
                          None, 'api.createsend.com')

    def test_verified_connection(self):
        # An actual (non-stubbed) unauthenticated request to test verification.
        self.assertRaises(Unauthorized, self.cs.clients)

    def test_verified_connection_uses_certifi_bundle(self):
        connection = VerifiedHTTPSConnection('api.createsend.com')

        with patch('createsend.utils.ssl.SSLContext') as ssl_context, \
                patch('createsend.utils.socket.create_connection') as create_connection:
            raw_socket = create_connection.return_value
            context = ssl_context.return_value
            tls_socket = context.wrap_socket.return_value
            tls_socket.getpeercert.return_value = {
                'subjectAltName': (('DNS', 'api.createsend.com'),)
            }

            connection.connect()

            ssl_context.assert_called_once_with(protocol=ssl.PROTOCOL_TLS_CLIENT)
            self.assertEqual(context.verify_mode, ssl.CERT_REQUIRED)
            context.load_verify_locations.assert_called_once_with(certifi.where())
            context.wrap_socket.assert_called_once_with(
                raw_socket, server_hostname='api.createsend.com')

    def test_verified_connection_rejects_wrong_hostname(self):
        connection = VerifiedHTTPSConnection('api.createsend.com')

        with patch('createsend.utils.ssl.SSLContext') as ssl_context, \
                patch('createsend.utils.socket.create_connection') as create_connection:
            raw_socket = create_connection.return_value
            context = ssl_context.return_value
            tls_socket = context.wrap_socket.return_value
            tls_socket.getpeercert.return_value = {
                'subjectAltName': (('DNS', 'not-api.createsend.com'),)
            }

            with self.assertRaises(CertificateError):
                connection.connect()

            tls_socket.shutdown.assert_called_once_with(socket.SHUT_RDWR)
            tls_socket.close.assert_called_once_with()
