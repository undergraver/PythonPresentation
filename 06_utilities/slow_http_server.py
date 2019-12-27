import http.server
import socketserver
import time

PORT = 8000

delay_in_seconds = 3.5

class MySlowHandler(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		time.sleep(delay_in_seconds)
		return super().do_GET()
		
	def do_HEAD(self):
		time.sleep(delay_in_seconds)
		return super().do_HEAD()
	
Handler = MySlowHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
