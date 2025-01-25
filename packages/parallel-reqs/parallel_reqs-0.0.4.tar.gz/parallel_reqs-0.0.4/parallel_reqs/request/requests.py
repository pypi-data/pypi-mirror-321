import re

class Request:
    VALID_METHODS = {'GET', 'POST', 'PUT', 'DELETE'}

    def __init__(self, url, method='GET', params=None, data=None, headers=None):
        # Verifica che url sia un URL valido
        #if not re.match(r'^https?://', url):
        #    raise ValueError("URL not valid: http:// o https://")
        self._url = url

        # Verifica che method sia uno dei valori consentiti
        if method.upper() not in self.VALID_METHODS:
            raise ValueError(f"Method not supported: {method} ")
        self._method = method.upper()

        self._params = params
        self._data = data

        # Verifica che headers sia un dizionario
        if headers is not None and not isinstance(headers, dict):
            raise TypeError("headers deve essere un dizionario")
        self._headers = headers

    @staticmethod    
    def create(url, method='GET', params=None, data=None, headers=None):
        return Request(url, method, params, data, headers)
    
    @property
    def url(self):
        return self._url

    @property
    def method(self):
        return self._method

    @property
    def params(self):
        return self._params

    @property
    def data(self):
        return self._data

    @property
    def headers(self):
        return self._headers
