#!/usr/bin/python3
try: import fix_import
except: pass
from cgi import FieldStorage
from python.login import *
from python.html_components import *

print('Content-Type: text/html')
print()
print_head()
print_nav()
print_main()