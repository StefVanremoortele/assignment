from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO, StringIO
from utils import get_index


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        body = get_index()
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body.encode('utf-8'))
        #return StringIO(body)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())


class Server:
    
    def spawn(self):
        httpd = HTTPServer(('localhost', 80), SimpleHTTPRequestHandler)
        httpd.serve_forever()