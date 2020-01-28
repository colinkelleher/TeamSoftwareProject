from python.login import *
from python.users.user_types import *


class User(object):

    def factory():
        logged_in, username = loggedIn()
        if isAdmin(username):
            return Admin(logged_in)
        else:
            return User(logged_in)

    factory = staticmethod(factory)

    def __init__(self, logged_in):
        self._logged_in = logged_in

    def getType(self):
        return "normal user"


if __name__ == '__main__':
    u = User.factory()
    print(u.getType())
