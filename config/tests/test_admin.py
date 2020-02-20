from http import HTTPStatus

from django.test import Client, TestCase


class AdminTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_call_to_admin_without_slash(self):
        """A GET to /admin redirects to /admin/"""
        response = self.client.get("/admin")
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
