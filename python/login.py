from password import Password
from python.databases.databaseQueries import select_all_with_conditions

from os import environ
from hashlib import sha256
from time import time
from shelve import open
from http.cookies import SimpleCookie

def loggedIn():
    """
    Function to check if user is logged in or not. Should be run on every page
    which requires a user to be logged in to use.
    @return authenticated -> boolean showing if already logged in or not
            username -> string of this user's username, empty string if unsuccessful
    """
    authenticated = False
    username = ""
    try:
        cookie = SimpleCookie()
        http_cookie_header = environ.get('HTTP_COOKIE')
        if not http_cookie_header:
            sid = sha256(repr(time()).encode()).hexdigest()
            cookie['sid'] = sid
        else:
            cookie.load(http_cookie_header)
            if 'sid' not in cookie:
                sid = sha256(repr(time()).encode()).hexdigest()
                cookie['sid'] = sid
            else:
                sid = cookie['sid'].value

                session_store = open('sessions/sess_' + sid, writeback=True)
                authenticated = session_store.get("authenticated")
                username = session_store.get("username")

    except IOError:
        authenticated,username = False,""

    return authenticated, username
#end loggedIn

def isAdmin():
    """
    Function to check if a (loggged in) user has admin rights
    @param username
    @return True or False
    """

    # assumption that role will be the string "admin" for admin rights
    result = select_all_with_2_conditions("users","id",username,"role","admin")
    if len(result) > 0:
        # This user is an admin
        return True
    # not admin
    return False

#end isAdmin

def tryLogIn():
    """
    Function to attempt to log in a user using username and password supplied
    """
#end tryLogIn
