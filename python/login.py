try:
    from python.password import Password
    from python.databases.databaseQueries import select_all_with_conditions, select_all_with_2_conditions, add_user
    from python.path_stuff import get_abs_paths

except:
    from password import Password
    from databases.databaseQueries import select_all_with_conditions, select_all_with_2_conditions, add_user, update_user

from os import environ
from hashlib import sha256
from time import time
from shelve import open
from http.cookies import SimpleCookie

"""
loggedIn() -> Can be run to check if a user is logged in on loading each page
isAdmin() -> Can be run to check if a user has admin rights before allowing access to restricted content
tryLogIn() -> To be run to change state from logged out to logged in
logOut() -> To be run to change state from logged in to logged out
register() -> Adds user details to database (should sanatize in future)
"""

# Add these so can know that someone just logged in
# Before a cookie has been printed
_loggedIn = False
_user_id = ''


def loggedIn():
    """ Checks if a user is logged in

    Function to check if user is logged in or not. Should be run on every page
    which requires a user to be logged in to use.
    @return authenticated -> boolean showing if already logged in or not
            user_id -> string of this user's user_id, empty string if unsuccessful
    """
    if _loggedIn:
        return _loggedIn, _user_id

    authenticated = False
    user_id = ""

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
            #print(get_abs_paths()['python'] + 'sessions/sess_' + sid)
            session_store = open(get_abs_paths()['python'] + '/sessions/sess_' + sid, writeback = True)
            authenticated = session_store.get("authenticated")
            user_id = session_store.get("user_id")

    #authenticated, user_id = False, ""

    return authenticated, user_id


# end loggedIn

def isAdmin(user_id):
    """Function to check if a user has admin rights

    Queries the users database to see if the current user has a role with
        admin rights. Should only be used if user is already confirmed to be
        logged in.
    ### can be changed to not need user_id arg, but should be already stored from loggedIn() above

    @param user_id -> unique id in DB (currently an id number)
    @return True or False - is the user an admin
    """

    # assumption that role will be the string "admin" for admin rights
    result = select_all_with_2_conditions("users", "email", user_id, "role", "1")
    if len(result) > 0:
        # This user is an admin
        return True
    # not admin
    return False


# end isAdmin

def tryLogIn(user_id, password):
    """Function to attempt to log in a user

    Function takes in a user_id and password and queries them against the
        database. If successful, a cookie is created and given to the user
        as proof of login. Escaped user_id and password can be taken from a
        form and used here. It is assumed that the user isn't already logged in.
    @param  user_id -> unique id in DB (email)
            password -> Password object
    @return if unsuccessful ->   returns None
            if successful ->    returns the cookie
                                the cookie must be printed to the webpage header
    """
    try:
        result = select_all_with_2_conditions("users", "email", user_id, "password", str(password))
        if len(result) == 0:
            return None

        cookie = SimpleCookie()
        sid = sha256(repr(time()).encode()).hexdigest()
        cookie['sid'] = sid
        session_store = open(get_abs_paths()['python'] + '/sessions/sess_' + sid, writeback = True)
        session_store['authenticated'] = True
        session_store['user_id'] = user_id
        session_store.close()
        global _loggedIn, _user_id
        _loggedIn, _user_id = True, user_id
    except Exception as e:
        print('Content-Type: text/html\n')
        print(e)
        exit(0)
    # print(cookie) ### EDIT THIS - cookie needs to be appropriately printed to http header.
    return cookie


# end tryLogIn

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
                path = get_abs_paths()['python'] + '/sessions/sess_' + sid
                session_store = open(path, writeback = True)
                session_store['authenticated'] = False
                session_store.close()
                global _loggedIn
                _loggedIn = False
        # successfully logged out
        return True
    except IOError as e:
        # failed to access the session files
        print(e)
        return False

def register(email, pword, fname, lname):
    """ Function to add a user to the database

    Takes in the email, first name, last name and password and adds to the
    Database if they satisfy all conditions
    @param  email, first name, last name - all Strings
            password - Password object
    @ return boolean -  True if successfully added
                        False if error occurs
    """
    # Sanitize the input as necessary####################

    return add_user(fname, lname, email, pword)
#end register

def makeAdmin(email):
    """ function to make a user an admin

    @param email of the user to be made admin
    @returns True or False if successful or not
    """
    updated = update_user(email, "role", "1")
    return updated
#end makeAdmin
