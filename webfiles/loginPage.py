#!C:\Users\Peter\AppData\Local\Programs\Python\Python38-32\python.exe

try: import fix_import
except: pass
from cgitb import enable
enable()

from python.login import *
from python.html_components import *
from python.webpage_functions import get_form_data, has_form_data

DASHBOARD_PATH = ""
LOGIN_PATH = ""

# Some useful variables
isLoggedIn, user_id = loggedIn()

if isLoggedIn:
    # Display dashboard
    print('Content-Type: text/html')
    print()
    # Print the main dashboard page
    print_head()
    print_nav()
    print_main()
    ############################
else:
    if has_form_data():
        # Page loading with incoming form data
        # Try to log in with the data
        login_id, password = get_form_data("id"), Password(get_form_data("password"))
        logInCookie = tryLogIn(login_id, password)
        if logInCookie:
            # successful
            print('Content-Type: text/html')
            print(logInCookie)
            print()
            # print the main dashboard
            print_head()
            print_nav()
            print_main()
            ##########################
        else:
            # unsuccessful - print login page with error message
            print_login(True)
    else:
        # No data - Print log in page
        print('Content-Type: text/html')
        print()
        print_login(False)
