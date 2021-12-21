from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    #http headers
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    #http do stuff
    self.wfile.write("Hello, I am alive! :)".encode())
    return