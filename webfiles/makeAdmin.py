#!/usr/bin/python3

from python.webpage_functions import print_html, get_form_data, has_form_data, print_main, get_user
from python.databases.databaseQueries import select_all_with_conditions, update_user
if get_user().logged_in:
    if has_form_data():
        user_id = get_form_data("users")
        updated = update_user(int(user_id), "role", "1")
userForm = ""
users = select_all_with_conditions("users", "role", "0")
if len(users) > 0:
    for row in users:
        userForm += '<option value="%s">%s %s</option>' %(row["id"],row["fname"],row["lname"])
else:
    userForm += '<option value="">None</option>'

if get_user().logged_in:
    if has_form_data():
        user_id = get_form_data("users")
        updated = update_user(int(user_id), "role", "1")
        if updated:
            #successful
            print_main("makeAdmin.html", dict(msg="Successful!", users=userForm))
        else:
            #failed
            print_main("makeAdmin.html", dict(msg="Unsuccessful, try again", users=userForm))
    else:
        print_main("makeAdmin.html", dict(msg="", users=userForm))
else:
    print_html('redirect.html', dict(url='/index.py'))
