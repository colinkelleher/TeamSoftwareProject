from http.server import HTTPServer, CGIHTTPRequestHandler
import os

from python.databases import createDatabase, populateDatabase
from python.path_stuff import get_abs_paths

port = 8080

# Code taken and modified from
# https://github.com/Shashank9830/Python-CGI-WebApp/blob/master/webapp/simple_httpd.py
# https://stackoverflow.com/a/36989254


class CGIHandler(CGIHTTPRequestHandler):

    def is_cgi(self):
        self.cgi_info = '', self.path[1:]
        if self.path.count('/') == 1 or self.path.startswith('/api') or self.path.startswith('/webfiles'):
            return '.py' in self.path
        return False


def new_database():
    createDatabase.create_database()
    populateDatabase.populate_users_table()
    populateDatabase.populate_locations_table()
    populateDatabase.populate_products_table()


def setup():
    new_database()
    try:
        os.makedirs(get_abs_paths()['data_store'] + '/sessions')
    except FileExistsError:
        pass


try:
    setup()
    # Get PYTHONPATH variable or '' if its not there
    pythonpath = os.environ.get('PYTHONPATH') or ''
    if os.getcwd() not in pythonpath:
        # Add current working directory to PYTHONPATH and update os.environ
        pythonpath += ':' + os.getcwd()
        os.environ.update(PYTHONPATH=pythonpath)

    httpd = HTTPServer(('', port), CGIHandler)
    print("Starting simple_httpd on port: " + str(httpd.server_port))
    httpd.serve_forever()


except KeyboardInterrupt as err:
    print("User pressed Ctrl + C : " + str(err))