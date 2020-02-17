from http.server import HTTPServer, CGIHTTPRequestHandler

port = 8080


class CGIHandler(CGIHTTPRequestHandler):

    def is_cgi(self):
        self.cgi_info = '', self.path[1:]
        if self.path.count('/') == 1 or self.path.startwith('/api') or self.path.startwith('webfiles'):
            return self.path.endswith('.py')
        return False

try:
    httpd = HTTPServer(('', port), CGIHandler)
    print("Starting simple_httpd on port: " + str(httpd.server_port))
    httpd.serve_forever()

except KeyboardInterrupt as err:
    print("User pressed Ctrl + C : " + str(err))