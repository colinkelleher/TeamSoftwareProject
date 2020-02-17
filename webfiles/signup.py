#!/usr/bin/python3

from python.webpage_functions import user, print_html, get_form_data, has_form_data
from python.password import Password
from python.login import register

if has_form_data():
    # collect data
    fname, lname, email, pword = get_form_data("fname"), get_form_data("lname"), get_form_data("email"), Password(get_form_data("pword"))
    registered = register(email, pword, fname, lname)
    if registered:
        ## Print "successfully registered" page
        print_html()
    else:
        print_html("signup.html")
else:
    print_html("signup.html")