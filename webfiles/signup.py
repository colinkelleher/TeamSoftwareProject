#!/usr/bin/python3

from python.webpage_functions import print_html, get_form_data, has_form_data, print_main, get_user
from python.password import Password
from python.login import register


if not get_user().logged_in:
    if has_form_data():
        # collect data
        fname, lname, email, pword = get_form_data("fname"), get_form_data("lname"), get_form_data("email"), Password(get_form_data("pword"))
        #send to db
        registered = register(email, str(pword), fname, lname)
        print(registered)
        # check if successfully registered
        if registered:
            ## Print "successfully registered" page
            print_html('redirect.html', dict(url='/index.py'))
        else:
            # print signup page
            #### preferably with error message
            print_html("signup.html")
    else:
        print_html("signup.html")
else:
    print_html('redirect.html', dict(url='/index.py'))
