# test_app_testcase.py
import unittest
from helpers.flask_app import create_app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "Hello, World!")

    def test_link_component(self):
        response = self.client.get("/link-component?path=tardis.blue&value=enter")
        self.assertEqual(
            response.data.decode("utf-8"), '<a href="tardis.blue">enter</a>'
        )

    def test_link_helper(self):
        response = self.client.get("/link-helper?path=tardis.blue&value=enter")
        self.assertEqual(
            response.data.decode("utf-8"), '<a href="tardis.blue">enter</a>'
        )
