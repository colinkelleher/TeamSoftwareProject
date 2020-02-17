#!/usr/bin/python3
import json
from cgi import FieldStorage
from python.login import *
from python.databases.databaseQueries import get_product_info

"""
API endpoint for getting product information.

An ajax request is made to execute this endpoint. Url is /api/get_product_info?pid=PRODUCT_ID .
API returns json containing the product info
"""
print('Content-Type: text/html')
print()
message = "ERROR"
if not loggedIn():
    pass
else:
    form_data = FieldStorage()
    pid = form_data.getfirst("pid")
    if pid:
        result = get_product_info(pid)
        if result:
            print(json.dumps(result))
