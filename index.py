#!/usr/bin/python3

from python.webpage_functions import user, print_html, get_form_data, has_form_data, cookie
from python.htmlGenerators import viewProducts, nav


# Either show login page or landing page
if not user.logged_in:
        if has_form_data():
            # Page loading with incoming form data
            # Try to log in with the data
            login_id, password = get_form_data("id"), Password(get_form_data("password"))
            logInCookie = tryLogIn(login_id, password)
            if logInCookie:
                # successful
                cookie = logInCookie
                # print the main dashboard
                print_html('main.html', dict(main=viewProducts.create_table_of_locations()))
            else:
                # unsuccessful - print login page with error message
                print_html('login.html') #### Error message?
        else:
            # No data - Print log in page
            print_html('login.html')

else:
    print_html('main.html', dict(main=viewProducts.create_table_of_locations()))
