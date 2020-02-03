from python.login import *

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

    def __init__(self, session=None):
        self.logged_in = False
        self.user_id = None
        self.fname = None
        self.lname = None
        self.image = None

    def is_authorized(self):
        # uri = os.environ['REQUEST_URI']
        return True

    def get_nav_items(self):
        return [
            {
                'Home': [
                    'fas fa-home',
                    '${root}/index.py'
                ]
            }
        ]


class User(NotLoggedInUser):

    def __init__(self, session):
        NotLoggedInUser.__init__(self, session)
        self.logged_in = True
        self.user_id = session['user_id']
        self.fname = session['fname']
        self.lname = session['lname']
        self.image = session['image']

    def get_nav_items(self):
        return [
            {
                'Home': [
                    'fas fa-home',
                    '${root}/index.py'
                ]
            }
        ]


class Manager(User):

    def __init__(self, session):
        User.__init__(self, session)


def get_user():
    logged_in, session = loggedIn()
    if not logged_in:
        return NotLoggedInUser()
    if session['role'] == '1':
        return Manager(session)
    else:
        return User(session)


user = get_user()


