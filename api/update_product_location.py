#!/usr/bin/python3
from cgi import FieldStorage
try:
    from python.login import *
    from python.update_product_location import update_location

except:
    from login import *
    from update_product_location import update_location

print('Content-Type: text/html')
print()
message = {"updated" : False, "message" : ""}
if loggedIn():
    message["message"] = "Sorry, you don't seem to be logged in"
else:
    form_data = FieldStorage()
    pid = form_data.getfirst("pid")
    lid = form_data.getfirst("lid")
    if pid and lid:
        result = update_location(pid, lid)
        if result:
            message["message"] = "That was updated"
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

print(str(message))
