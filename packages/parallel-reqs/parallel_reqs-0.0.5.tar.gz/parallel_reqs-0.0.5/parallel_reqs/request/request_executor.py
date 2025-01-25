import aiohttp
import asyncio
import time
from .requests import Request
from parallel_reqs.response import Response

class RequestExecutor:
    def __init__(self, page_size = 500):
        self.requests = []
        self.execution_time = 0
        self.responses = []
        self.page_size = page_size
        self.timeout = 4

    def add_request(self, request ):
        if not isinstance(request, Request):
            raise TypeError("Request not valid")
        
        self.requests.append(request)

    def run(self):
        asyncio.run( self.execute_requests() )
        return self.responses

    def paginate(self):
        for i in range(0, len(self.requests), self.page_size):
            yield self.requests[i:i + self.page_size]

    async def execute_requests(self):
        start_time = time.time()
        async with aiohttp.ClientSession() as session:
            page_number = 1
            for page in self.paginate():
                print(f"Processing page {page_number} with {len(page)} requests")
                tasks = [self.send_request(session, req) for req in page]
                responses = await asyncio.gather(*tasks, return_exceptions=True)
                self.responses.extend(responses)
                page_number += 1
        end_time = time.time() 
        self.execution_time = end_time - start_time
        return self.responses

    async def send_request(self, session, request):
        try:
            start_time = time.time()
            if request.method == 'GET':
                async with session.get(request.url, params=request.params, headers=request.headers, timeout=self.timeout) as response:
                    end_time = time.time() 
                    execution_time = end_time - start_time
                    return Response(response.status, dict(response.headers), await response.text(), execution_time)
            if request.method == 'POST':
                async with session.post(request.url, params=request.params, data=request.data, headers=request.headers, timeout=self.timeout) as response:
                    end_time = time.time() 
                    execution_time = end_time - start_time
                    return Response(response.status, dict(response.headers), await response.text(), execution_time)
            if request.method == 'PUT':
                async with session.put(request.url, params=request.params, data=request.data, headers=request.headers, timeout=self.timeout) as response:
                    end_time = time.time() 
                    execution_time = end_time - start_time
                    return Response(response.status, dict(response.headers), await response.text(), execution_time)        
            if request.method == 'DELETE':
                async with session.delete(request.url, params=request.params, headers=request.headers, timeout=self.timeout) as response:
                    end_time = time.time() 
                    execution_time = end_time - start_time
                    return Response(response.status, dict(response.headers, timeout=self.timeout), await response.text(), execution_time)
            raise ValueError(f"Metodo non supportato: {request.method}")
        except Exception as e:
            return Response( 501, {}, "Errors: %s" % e, 0)
        
