#!/usr/bin/python3

from string import Template
from cgitb import enable

from python.users.user import user
from python import path_stuff

enable()

print('Content-Type: text/html')
print()

# Either show login page or landing page
if not user.logged_in:
    # Load py_html/login.html and replace and ${bootstrap} values in that with a path to Bootstrap folder
    login_html = path_stuff.get_abs_paths()['py_html'] + '/login.html'
    template = Template(open(login_html, 'r').read())
    print(template.safe_substitute(path_stuff.get_urls()))
else:
    print('<h1>A landing page</h1>')

