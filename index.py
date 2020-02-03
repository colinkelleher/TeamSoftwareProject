#!/usr/bin/python3

from python.webpage_functions import user, print_html, get_form_data
from python.htmlGenerators import viewProducts, nav


# Either show login page or landing page
if user.logged_in:
    # Need to add check form data in case user is trying to log in
    print_html('login.html')
else:
    print_html('main.html', dict(nav=nav.get_nav(), main=viewProducts.create_table_of_locations()))

