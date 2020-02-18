from os import listdir, chdir, getcwd
from os.path import isdir, exists, abspath


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
    print(get_abs_paths())





