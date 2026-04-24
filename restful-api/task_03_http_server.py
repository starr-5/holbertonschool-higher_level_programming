from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Root endpoint
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # /data endpoint
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            self.wfile.write(json.dumps(data).encode("utf-8"))

        # /status endpoint
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # Optional /info endpoint (mentioned in expected output)
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            self.wfile.write(json.dumps(info).encode("utf-8"))

        # Unknown endpoint → 404
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):
    server_address = ("", 8000)
    httpd = server_class(server_address, handler_class)
    print("Server running on http://localhost:8000")
    httpd.serve_forever()


if __name__ == "__main__":
    run()