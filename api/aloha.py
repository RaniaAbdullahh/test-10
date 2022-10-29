from http.server import BaseHTTPRequestHandler
from urllib import parse #module that deals with urls

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s=self.path
        print(s)
        url_components= parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        print(dic)

        name = dic.get('name', False)
        
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        print(dic)

        name = dic.get('name', False)

        if name:
            message = f'Hello {name}'
        else:
            message = 'Hello stranger'

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

        return