#!/usr/bin/python3

from python.webpage_functions import print_html, get_html_template
print_html('main.html', dict(main=get_html_template('updateLocation.html').safe_substitute()))
