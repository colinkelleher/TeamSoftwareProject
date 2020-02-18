#!/usr/bin/python3

from python.webpage_functions import get_html_template, print_main
print_main(get_html_template('updateLocation.html').safe_substitute())
