from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from datetime import datetime

HOST = '0.0.0.0'

PORT = 8000

# In-memory storage
messages = {}

class SimpleHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200, content_type='application/json'):
        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        response = json.dumps(messages)
        self.wfile.write(response.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)

        try:
            data = json.loads(post_data)
            message = data.get('message')
            if message:
                timestamp = datetime.now().isoformat()
                messages[timestamp] = message
                self._set_headers(200)
                response = json.dumps({"status": "ok"})
            else:
                self._set_headers(400)
                response = json.dumps({"error": "Missing 'message' field"})
        except json.JSONDecodeError:
            self._set_headers(400)
            response = json.dumps({"error": "Invalid JSON"})

        try:
            self.wfile.write(response.encode('utf-8'))
        except BrokenPipeError:
            print("Client disconnected before response could be sent.")

    def _send_json_response(self, payload, status=200):
        response_bytes = json.dumps(payload).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(response_bytes)))
        self.end_headers()
        self.wfile.write(response_bytes)

def run():
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"Serving on http://{HOST}:{PORT}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
#curl -X POST http://localhost:8000 -H "Content-Type: application/json" -d '{"message": "Solomiya!"}'