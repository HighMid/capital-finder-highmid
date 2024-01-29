from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        path = self.path
        url_components = parse.urlparse(path)
        query = parse.parse_qs(url_components.query)
        
        country = query.get('country')
        capital = query.get('capital')
        
        message = ''
        
        if country:
            country_name = country[0]
            response = requests.get(f'https://restcountries.com/v3.1/name/{country_name}')
            data = response.json()
            capital_name = data[0]['capital'][0]
            message = f'The capital of {country_name} is {capital_name}'
            
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
        return