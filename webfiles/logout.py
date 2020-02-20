#!/usr/bin/python3

from python.webpage_functions import print_html
from python.password import Password
from python.login import logOut

logOut()
print_html('redirect.html', dict(url='index.py'))
