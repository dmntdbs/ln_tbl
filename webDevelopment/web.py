#!/usr/bin/python

#----------------------------------
#		python
#----------------------------------


from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler

server = HTTPServer(("", 8000), SimpleHTTPRequestHandler)
server.serve_forever()

