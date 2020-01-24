from password import Password
from os import environ
from hashlib import sha256
from time import time
from shelve import open
from http.cookies import SimpleCookie

def loggedIn():
    """
    Function to check if user is logged in or not. Should be run on every page
    which requires a user to be logged in to use.
    """
#end loggedIn

def isAdmin():
    """
    Function to check if a (loggged in) user has admin rights
    @returns true or false
    """
#end isAdmin

def tryLogIn():
    """
    Function to attempt to log in a user using username and password supplied
    """
#end tryLogIn
