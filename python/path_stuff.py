from os import listdir, chdir, getcwd, environ
from os.path import isdir, exists, abspath


def get_username_prefix():
    """
    cs1 servers need the ~kpp1 before actual path to file
    luckily environ has that in a variable
    """
    prefix = environ['CONTEXT_PREFIX']
    return prefix


def get_urls():
    """
    Return absolute url dictionary to all directories lowercase in the project
    For linking stuff in html
    """
    dirs = dict()
    paths = get_abs_paths()

    for key, path in paths.items():
        # context document root is path to public_html or whatever else the root is
        path = path[len(environ['CONTEXT_DOCUMENT_ROOT']):]
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
    dirs['root'] = getcwd()
    for file in listdir('.'):
        if isdir(file):
            dirs[file.lower()] = abspath(file)

    chdir(cwd)
    return dirs


if __name__ == '__main__':
    print(get_urls())
    print(get_abs_paths())





