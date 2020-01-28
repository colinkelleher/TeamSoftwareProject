#!/usr/bin/python3
from cgi import FieldStorage
from python.login import *
from python.update_product_location import update_location

"""
            API endpoint for updating product location.
            
    An ajax request is made to execute this endpoint. Url is /api/update_product_location.py?pid=PRODUCT_ID&lid=LOCATION_ID .
    API returns json with updated and message fields
    "updated" field --> True if the location was updated. False if not
    "message" field --> Different messages depending on outcome. These are ready to be inserted into HTML and displayed to the the user.

"""
print('Content-Type: text/html')
print()
message = {"updated": False, "message": ""}
if not loggedIn():
    message["message"] = "Sorry, you don't seem to be logged in"
else:
    form_data = FieldStorage()
    pid = form_data.getfirst("pid")
    lid = form_data.getfirst("lid")
    if pid and lid:
        result = update_location(pid, lid)
        if result:
            message["message"] = "That was updated"
            message["updated"] = True
        elif result == 0:
            message["message"] = "Sorry, that location does not exist"

        elif result == -1:
            message["message"] = "Sorry, that product does not exist"

        elif result == -2:
            message["message"] = "Sorry, something went wrong"

    elif not pid and not lid:
        message["message"] = "Sorry, both the product ID and location ID are empty"

    elif not pid:
        message["message"] = "Sorry, the product ID is empty"

    elif not lid:
        message["message"] = "Sorry, the location ID is empty"

print("'%s'" % str(message), end="")
