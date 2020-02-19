from cgitb import Hook
from cgi import FieldStorage
from html import escape
from http.cookies import SimpleCookie
from os import environ
from string import Template
from pprint import pprint
import sys

from python.users.user import get_user
from python import path_stuff
from python.htmlGenerators.nav import get_nav


"""
Handles web page specific things like
    Getting the current user in user variable
    Enable debugging
    Create or load a cookie into a variable
    Escape out form data and strip it
    Prints html files from py_html folder, 
        adding in absolute urls and using string.Template for adding in python generated html
"""


"""
Normal cgitb.enable doesn't want to work for some reason
But if I print Content-Type: text/html
And then run the handle method that cgitb uses it works
No fancy html formatting though
"""
class Logger(Hook):

    def handle(self, info=None):
        print('Content-Type: text/html\n')
        print(super().handle(info))


# Intercept all exceptions and pass them to Logger class just like cgitb does
sys.excepthook = Logger()

form_data = FieldStorage()

_cookie = None


def set_cookie(cookie):
    """
    Set global cookie to be printed
    Run print_html or print_main to print the cookie after
    """
    global _cookie
    _cookie = cookie


def has_form_data():
    return len(form_data) != 0


def get_form_data(key):
    """
    Escapes and strips form data
    Returns None if no form data and "" if key not found
    @param key: Form value to get
    @type key: String
    @return: Form data
    """
    return escape(form_data.getfirst(key, "").strip())


def get_html_template(filename):
    path = path_stuff.get_abs_paths()['py_html'] + '/' + filename
    return Template(open(path, 'r').read())


def print_html(filename, inputs={}):
    """
    Prints a html page from files in py_html
    Also prints the cookie that has been set
    Does same thing for inputs so like
        ${content} in html and inputs={'content': 'Hello World'}

    @param filename: Html file from py_html to print
    @param inputs: Dictionary of other html inputs to insert
    """
    print('Content-Type: text/html')
    if _cookie:
        print(_cookie)
    print()
    template = get_html_template(filename)
    # Need to merge default dictionary with inputs dict
    default = {
        'qrScanner':    """
                            <script src="/js/qrscanner.js"></script>
                            <script src="/js/libs/jsQR.js"></script>
                        """,
        'nav': get_nav(get_user().get_nav_items())
    }
    # First substitute all user inputs in the html like ${main} into whatever passed through in inputs dict
    # Then substitute defaults above like nav
    inputted = Template(template.safe_substitute(inputs))
    html = inputted.safe_substitute(default)
    # Print the html
    print(html)


def print_main(content, inputs={}):
    """
    Prints main.html and sets content of page
    :param content: Main part of the page that changes
    :param inputs: If your content uses string templates you can input them here
    :return: Nothing
    """
    inputs['main'] = content
    print_html('main.html', inputs)


if not get_user().is_authorized():
    print_html('redirect.html', dict(url='/index.py'))
    exit(0)




