import unittest
from parallel_reqs import Request 

class TestRequest(unittest.TestCase):

    def test_valid_initialization(self):
        request = Request(url="http://example.com", method="GET")
        self.assertEqual(request.url, "http://example.com")
        self.assertEqual(request.method, "GET")
        self.assertIsNone(request.params)
        self.assertIsNone(request.data)
        self.assertIsNone(request.headers)

    def test_invalid_method(self):
        with self.assertRaises(ValueError):
            Request(url="http://example.com", method="INVALID")

    def test_headers_type(self):
        with self.assertRaises(TypeError):
            Request(url="http://example.com", headers="not a dict")

    def test_create_method(self):
        request = Request.create(url="http://example.com", method="POST")
        self.assertEqual(request.url, "http://example.com")
        self.assertEqual(request.method, "POST")
