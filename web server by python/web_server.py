from http.server import HTTPServer ,BaseHTTPRequestHandler
class Customer_request(BaseHTTPRequestHandler):
    def get_request(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"welcome in server")

def main():
    PORT=8000
    server=HTTPServer(('', PORT), Customer_request)
    print('Server running on port %s' %PORT)
    server.serve_forever()

    
if __name__ == "__main__":
    main()