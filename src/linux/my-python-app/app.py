from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class SimpleAddHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL to extract the path and query parameters
        url = urlparse(self.path)
        
        if url.path == '/add':
            # Extract query parameters
            query_components = parse_qs(url.query)
            try:
                # Retrieve 'a' and 'b' from query parameters, defaulting to 0 if missing
                a = float(query_components.get('a', [0])[0])
                b = float(query_components.get('b', [0])[0])
                
                # Perform addition
                result = a + b
                
                # Send response headers
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                
                # Send response body
                self.wfile.write(bytes(f'{{"result": {result}}}', "utf-8"))
            except ValueError:
                # Handle invalid input by sending an error response
                self.send_response(400)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(bytes('{"error": "Invalid input. Please provide numbers."}', "utf-8"))
        else:
            # Handle 404 for other paths
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    server_address = ('', 8000)  # Listen on port 8000
    httpd = HTTPServer(server_address, SimpleAddHandler)
    print("Server running on port 8000...")
    httpd.serve_forever()
  