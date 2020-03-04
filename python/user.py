from python.login import *
import os

"""
Creates user variable of the right kind

If the user shouldn't be allowed to view the page:
    Show the 404 page and exit
    Can handle permissions if all python webpages import this 

Three different kinds of users:
    - Someone not logged in 
    - Normal user
    - Manager
Can add role specific methods like
    Is authorized
    Nav options
    ...
"""


class NotLoggedInUser:

    def __init__(self, email=None):
        self.logged_in = False
        self.email = email

    def is_authorized(self):
        """
        Checks if a user is allowed on a page
        app.py uses SCRIPT_NAME to get name and path to script

        Anyone not logged should only be able to login or signup
        """
        uri = os.environ.get('SCRIPT_NAME') or []
        return uri in ['/webfiles/signup.py', '/index.py']

    def get_nav_items(self):
        return []


class User(NotLoggedInUser):

    def __init__(self, email):
        NotLoggedInUser.__init__(self, email)
        self.logged_in = True

    def get_nav_items(self):
        return super().get_nav_items() + [
            ('Home', 'fas fa-home', '/index.py'),
            ('Update Location', 'fas fa-qrcode', '/webfiles/updateLocation.py'),
            ('Product Location', 'fas fa-map-marker-alt', '/webfiles/viewProduct.py'),
            ('Add Product', 'fas fa-plus', '/webfiles/addProduct.py')
        ]
    
    def is_authorized(self):
        return True


class Manager(User):

    def __init__(self, email):
        User.__init__(self, email)

    def get_nav_items(self):
        return super().get_nav_items() + [
            ('Analytics', 'fas fa-chart-bar', '/webfiles/analytics_charts_js.py'),
            ('Remove Product', 'fas fa-trash-alt', '/webfiles/remove_product.py'),
            ('Manage Users', 'fas fa-male', [('Add User', '', '/webfiles/addUser.py'),
            ('Make User Admin', '', '/webfiles/makeAdmin.py'),
                                             ("Delete User", "", "/webfiles/deleteUser.py")])
        ]


def get_user():
    logged_in, email = loggedIn()
    if not logged_in:
        return NotLoggedInUser()
    if isAdmin(email):
        return Manager(email)
    else:
        return User(email)

