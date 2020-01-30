from cgitb import enable
from cgi import FieldStorage
from html import escape
from http.cookies import SimpleCookie
from os import environ
from string import Template
from pprint import pprint

from python.users.user import user
from python import path_stuff


"""
Handles web page specific things like
    Getting the current user in user variable
    Enable debugging
    Create or load a cookie into a variable
    Escape out form data and strip it
    Prints html files from py_html folder, 
        adding in absolute urls and using string.Template for adding in python generated html
"""
enable()

cookie_header = environ.get('HTTP_COOKIE')
cookie = SimpleCookie()
if cookie_header:
    cookie.load(cookie_header)


def has_form_data():
    return len(FieldStorage()) != 0


def get_form_data(key):
    """
    Escapes and strips form data
    Returns None if no form data and "" if key not found
    @param key: Form value to get
    @type key: String
    @return: Form data
    """
    form_data = FieldStorage()
    if len(form_data) == 0:
        return None
    return escape(form_data.getfirst(key, "").strip())


def print_html(filename, inputs={}):
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
    print(cookie)
    print()
    login_html = path_stuff.get_abs_paths()['py_html'] + '/' + filename
    template = Template(open(login_html, 'r').read())
    # Need to merge default dictionary with inputs dict
    default = {
        'qrScanner':    """
                            <script src="${js}/qrscanner.js"></script>
                            <script src="${js}/libs/jsQR.js"></script>
                        """
    }
    # First run inputs and default through templating
    # Then substitute absolute paths into that template
    merged = {**inputs, **default}
    template = Template(template.safe_substitute(merged))
    print(template.safe_substitute(path_stuff.get_urls()))


