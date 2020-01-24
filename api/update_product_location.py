#!/usr/bin/python3
try:
    from python.login import *

except:
    from ..python.login import *

print('Content-Type: text/html')
print()
print(loggedIn())