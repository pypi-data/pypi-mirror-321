class Response:
    def __init__(self, status_code, headers, text, execution_time):
        self._status_code = int(status_code)
        
        if not isinstance(headers, dict):
            raise TypeError("headers deve essere un dizionario")
        
        self._headers = headers
        
        self._text = text
        self._execution_time = execution_time

    @staticmethod    
    def create(status_code, headers, text, execution_time):
        return Response(status_code, headers, text, execution_time)

    @property
    def status_code(self):
        return self._status_code

    @property
    def headers(self):
        return self._headers

    @property
    def text(self):
        return self._text

    @property 
    def execution_time(self): 
        return self._execution_time
    