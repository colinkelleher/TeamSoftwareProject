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
        return {
                'Charts': [('chartsjs.html', 'Charts.js')],
                'Components': [
                    ('cards.html', 'Cards'),
                    ('forms.html', 'Forms'),
                    {'Icons': [
                        ('icons.html', 'Solid Icons'),
                        ('icons.html#regular-icons', 'Regular Icons'),
                        ('icons.html#brand-icons', 'Brand Icons')
                    ]},
                    ('stats.html', 'Stats'),
                    ('tables.html', 'Tables'),
                    ('typography.html', 'Typography'),
                    ('userinterface.html', 'User Interface')
                ],
                'Layouts': [
                    ('blank.html', 'Blank'),
                    ('content.html', 'Content'),
                    ('login.html', 'Log in'),
                    ('signup.html', 'Sign up')
                ],
                'About': [
                    ('https://github.com/HackerThemes/spur-template', 'Github'),
                    ('http://hackerthemes.com', 'HacketThemes')
                ]
            }


class User(NotLoggedInUser):

    def __init__(self, session):
        NotLoggedInUser.__init__(self, session)
        self.logged_in = True
        self.user_id = session['user_id']
        self.fname = session['fname']
        self.lname = session['lname']
        self.image = session['image']


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


def print_404_and_exit():
    print('Content-Type: text/html')
    print()
    message = "<img src ='/TeamSoftwareProject/images/404.gif' id='map'/> "
    print(message)
    exit(0)


user = get_user()

if not user.is_authorized():
    print_404_and_exit()

