#!/usr/bin/python3

from python.webpage_functions import print_html, get_form_data, has_form_data, print_main
from python.addRemoveProduct import addProduct
"""
Checks if (title, location, description, comments) form values are there
If not, resends form with as much data as possible filled in
Else adds product and redirects to view product page
"""
required = ['title', 'loc']
order = ['title', 'description', 'loc', 'comments']

values = {
    'title': '',
    'description': '',
    'loc': '',
    'comments': '',
    'result': ''
}

og = values.copy()

def show_add_product():
    # get_form_data might return None so switch that to '' for printing
    for k, v in values.items():
        if not v:
            values[k] = ''
    print_main('add_product.html', values)


reason = "No reason"
valid = False

if has_form_data():
    title = get_form_data("title")
    location = get_form_data("loc")
    description = get_form_data("description")
    date = get_form_data("date")
    comments = get_form_data("comments")
    result = addProduct(title, description, location, comments=comments, expiry_date=date)
    og['result'] = date

    print_main('add_product.html', {'result':result})
    valid = True
if not valid:
    show_add_product()
