from os import listdir, chdir, getcwd
from os.path import isdir, exists, abspath
from pathlib import Path


def get_username_prefix():
    """
    cs1 servers need the ~kpp1 before actual path to file
    check if its a cs server and return it
    """
    cwd = getcwd()
    while not exists('public_html'):
        chdir('../')
    public = Path('public_html')
    prefix = ''
    if public.group() == 'www-data':
        prefix = '/~' + public.owner()
    chdir(cwd)
    return prefix


def get_urls():
    """
    Return absolute url dictionary to all directories lowercase in the project
    For linking stuff in html
    """
    dirs = dict()
    paths = get_abs_paths()

    for key, path in paths.items():
        path = path[path.rfind('public_html') + len('public_html'):] + "/"
        path = get_username_prefix() + path
        dirs[key] = path
    return dirs


def get_abs_paths():
    """
    Returns absolute path dictionary to all directories at root of the project
    Helps when opening paths in python
    """
    cwd = getcwd()
    while not exists('README.md'):
        # Keep going up directories until you find README.md
        chdir('../')

    dirs = dict()
    for file in listdir('.'):
        if isdir(file):
            dirs[file.lower()] = abspath(file)

    chdir(cwd)
    return dirs


if __name__ == '__main__':
    print(get_urls())
    print(get_abs_paths())





