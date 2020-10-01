#!/usr/bin/python3

from python.webpage_functions import print_html
from python.login import logOut

"""
Web page to log a user out
"""
logOut()
print_html('redirect.html', dict(url='/index.py'))
