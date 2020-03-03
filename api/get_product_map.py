#!/usr/bin/python3
from cgi import FieldStorage
from python.login import *
from python.databases.databaseQueries import get_product_info

"""
API endpoint for getting product location on map.

An ajax request is made to execute this endpoint. Url is /api/get_product_map?pid=PRODUCT_ID .
API returns an image tag containing the map
"""
print('Content-Type: text/html')
print()
message = "/assets/images/404.gif"
if not loggedIn():
    pass
else:
    form_data = FieldStorage()
    pid = form_data.getfirst("pid")

    result = form_data.getfirst("pid")
    if pid:
        result = get_product_info(pid)
        if result:
            map_image = result["location_info"]["map"]
            map_image = map_image.split(".")[0]
            map_image += "-min.png"
            message = map_image

print(str(message))
