from python.login import *
from python.users.user import User


class Admin(User):

    def getType(self):
        return "admin"



