#!/usr/bin/python3

from python.webpage_functions import print_html, get_form_data, has_form_data
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
    'comments': ''
}


def show_add_product():
    # get_form_data might return None so switch that to '' for printing
    for k, v in values.items():
        if not v:
            values[k] = ''

    print_html('add_product.html', values)


reason = "No reason"
valid = False

if has_form_data():
    for key in values.keys():
        values[key] = get_form_data(key)
    for r in required:
        if not values[r] or values[r] == '':
            valid = False
            break
        else:
            valid = True

    if valid:
        vals = [values[x] for x in order]
        vals[3] = 1
        result = addProduct(vals)
        if result == -1:
            valid = False
        else:
            print_html('redirect.html', dict(url='${webfiles}/viewProduct.py'))

if not valid:
    show_add_product()
