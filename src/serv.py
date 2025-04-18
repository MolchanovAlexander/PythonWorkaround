# simple_http_server.py
from http.server import SimpleHTTPRequestHandler, HTTPServer

HOST = 'localhost'
PORT = 8000

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = (HOST, PORT)
    httpd = server_class(server_address, handler_class)
    print(f"Serving HTTP on {HOST} port {PORT} (http://{HOST}:{PORT}/) ...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
