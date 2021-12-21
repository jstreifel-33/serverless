from http.server import BaseHTTPRequestHandler
from urllib import parse


class handler(BaseHTTPRequestHandler):

    def fast_fib(self, n):
        gold_r = (1 + 5 ** 0.5) / 2
        return round((gold_r**n)/(5**0.5))


    def do_GET(self):
        #res/header
        self.send_response(200)
        self.send_header('content-type', 'text/plain')
        self.end_headers()

        #do stuff

        s = self.path
        url_components = parse.urlsplit(s)
        query_dict = parse.parse_qs(url_components.query)

        num = query_dict.get("num")[0]
        num = int(num)

        self.wfile.write(f"caluclating {num}th number of fibonacci...".encode())

        if num > 0:
            for i in range(num):
                self.wfile.write(f"\n{(self.fast_fib(i))}".encode())
        else:
            self.wfile.write(f"Error! Please enter a number greater than zero (0)!".encode())
