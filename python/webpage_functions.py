from cgitb import Hook
from cgi import FieldStorage
from html import escape
from http.cookies import SimpleCookie
from os import environ
from string import Template
from pprint import pprint
import sys

from python.users.user import user
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


def print_html(filename, inputs={}, cookie2=None):
    """
    Prints a html page from files in py_html
    Also prints the cookie that has been set
    Adds in absolute urls where specified
        Substitutes for example ${bootstrap} for /~kpp1/public_html/cgi-bin/.../Bootstrap
    Does same thing for inputs so like
        ${content} in html and inputs={'content': 'Hello World'}

    @param filename: Html file from py_html to print
    @param inputs: Dictionary of other html inputs to insert
    """
    print('Content-Type: text/html')
    if cookie2:
        print(cookie2)
    print()
    template = get_html_template(filename)
    # Need to merge default dictionary with inputs dict
    default = {
        'qrScanner':    """
                            <script src="${js}/qrscanner.js"></script>
                            <script src="${js}/libs/jsQR.js"></script>
                        """,
        'nav': get_nav(user.get_nav_items())
    }
    # First run inputs and default through templating
    # Then substitute absolute paths into that template
    merged = {**inputs, **default}
    template = Template(template.safe_substitute(merged))
    print(template.safe_substitute(path_stuff.get_urls()))


if not user.is_authorized():
    print_html('404.html')
    exit(0)


# if __name__ == '__main__':
#     raise KeyError('Hello maybe')


