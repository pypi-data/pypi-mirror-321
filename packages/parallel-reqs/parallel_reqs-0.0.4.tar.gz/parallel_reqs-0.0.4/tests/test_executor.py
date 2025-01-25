import unittest
import asyncio
from parallel_reqs import Request
from parallel_reqs import RequestExecutor

class TestRequestExecutorRealRequests(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.executor = RequestExecutor(page_size=2)

    def test_add_valid_request(self):
        request = Request(url="https://www.example.com")
        self.executor.add_request(request)
        self.assertEqual(len(self.executor.requests), 1)
    
    def test_add_invalid_request(self):
        with self.assertRaises(TypeError):
            self.executor.add_request("not a request")

    async def test_execute_real_requests(self):
        # Aggiungi richieste reali
        request1 = Request(url="https://www.google.com")
        request2 = Request(url="https://www.example.com")
        request3 = Request(url="https://www.google.com")
        request4 = Request(url="https://www.example.com")
        
        self.executor.add_request(request1)
        self.executor.add_request(request2)
        self.executor.add_request(request3)
        self.executor.add_request(request4)
        
        responses = await self.executor.execute_requests()
        
        # Debug print
        for response in responses:
            print(f"Status: {response.status_code}")

        # Controlla che tutte le risposte abbiano stato 200
        for response in responses:
            self.assertEqual(response.status_code, 200)
