#!/usr/bin/python3

from python.webpage_functions import print_html, get_form_data, has_form_data, print_main
from python.addUserFunc import addUser
"""
Checks if (title, location, description, comments) form values are there
If not, resends form with as much data as possible filled in
Else adds product and redirects to view product page
"""
required = ['email', 'username']
order = ['email', 'username', 'fname', 'lname', 'password', 'role', 'image']

values = {
    'email': '',
    'username': '',
    'fname': '',
    'lname': '',
    'password': '',
    'role': '',
    'image': '',
    'result': ''
}

og = values.copy()

def showUsers():
    # get_form_data might return None so switch that to '' for printing
    for k, v in values.items():
        if not v:
            values[k] = ''
    print_main('addUser.html', values)


reason = "No reason"
valid = False

if has_form_data():
    email = get_form_data("email")
    username = get_form_data("username")
    fname = get_form_data("fname")
    lname = get_form_data("lname")
    password = get_form_data("password")
    role = get_form_data("role")
    image = get_form_data("image")
    result = addUser(email,username,fname,lname,password,role,image)
    og['result'] = email

    print_main('addUser.html', {'result':result})
    valid = True
if not valid:
    showUsers()
