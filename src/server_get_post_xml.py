from http.server import BaseHTTPRequestHandler, HTTPServer
import xml.etree.ElementTree as ET
from datetime import datetime

HOST = 'localhost'
PORT = 8000
messages = {}

class SimpleXMLHandler(BaseHTTPRequestHandler):
    def _send_xml_response(self, xml_element, status=200):
        response_bytes = ET.tostring(xml_element)
        self.send_response(status)
        self.send_header('Content-Type', 'application/xml')
        self.send_header('Content-Length', str(len(response_bytes)))
        self.end_headers()
        self.wfile.write(response_bytes)

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)

        try:
            xml_data = ET.fromstring(post_data)
            message = xml_data.findtext('message')

            if message:
                timestamp = datetime.now().isoformat()
                messages[timestamp] = message
                response = ET.Element('response')
                response.text = 'ok'
                self._send_xml_response(response)
            else:
                error = ET.Element('error')
                error.text = "Missing <message> tag"
                self._send_xml_response(error, status=400)

        except ET.ParseError:
            error = ET.Element('error')
            error.text = "Invalid XML"
            self._send_xml_response(error, status=400)

    def do_GET(self):
        root = ET.Element('messages')
        for ts, msg in messages.items():
            m = ET.SubElement(root, 'message')
            ET.SubElement(m, 'timestamp').text = ts
            ET.SubElement(m, 'text').text = msg
        self._send_xml_response(root)

def run():
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, SimpleXMLHandler)
    print(f"Serving on http://{HOST}:{PORT}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
#curl -X POST http://localhost:8000 -H "Content-Type: application/xml" -d '<root><message>Hello XML</message></root>'