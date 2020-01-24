from password import Password
from python.databases.databaseQueries import select_all_with_conditions

from os import environ
from hashlib import sha256
from time import time
from shelve import open
from http.cookies import SimpleCookie

def loggedIn():
    """ Checks if a user is logged in

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

def isAdmin(username):
    """Function to check if a user has admin rights

    Queries the users database to see if the current user has a role with
        admin rights. Should only be used if user is already confirmed to be
        logged in.
    ### can be changed to not need username arg, but should be already stored from loggedIn() above

    @param username -> unique id in DB (currently an id number)
    @return True or False - is the user an admin
    """

    # assumption that role will be the string "admin" for admin rights
    result = select_all_with_2_conditions("users","id",username,"role","admin")
    if len(result) > 0:
        # This user is an admin
        return True
    # not admin
    return False
#end isAdmin

def tryLogIn(username, password):
    """Function to attempt to log in a user

    Function takes in a username and password and queries them against the
        database. If successful, a cookie is created and given to the user
        as proof of login. Escaped username and password can be taken from a
        form and used here. It is assumed that the user isn't already logged in.
    @param  username -> unique id in DB (currently an id number)
            password -> Password object
    @return if unsuccessful ->   returns None
            if successful ->    returns the cookie
                                the cookie must be printed to the webpage header
    """
    result = select_all_with_2_conditions("users","id",username,"password",str(password))
    if len(result) == 0:
        return None

    cookie = SimpleCookie()
    sid = sha256(repr(time()).encode()).hexdigest()
    cookie['sid'] = sid
    session_store = open('sessions/sess_' + sid, writeback=True)
    session_store['authenticated'] = True
    session_store['username'] = username
    session_store.close()
    #print(cookie) ### EDIT THIS - cookie needs to be appropriately printed to http header.
    return cookie
#end tryLogIn

def logOut():
    """Function to log out the current users

    Takes users cookie and sets the 'authenticated' value to False, logging them out
    @return True or False ->    True if unsuccessful,
                                False if unsuccessful
    """
    try:
        cookie = SimpleCookie()
        http_cookie_header = environ.get('HTTP_COOKIE')
        if http_cookie_header:
            cookie.load(http_cookie_header)
            if 'sid' in cookie:
                sid = cookie['sid'].value
                session_store = open('sessions/sess_' + sid, writeback=True)
                session_store['authenticated'] = False
                session_store.close()
        # successfully logged out
        return True
    except IOError:
        #failed to access the session files
        return False
