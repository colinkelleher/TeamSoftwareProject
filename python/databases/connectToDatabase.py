import sqlite3
from os import path

from python.path_stuff import get_abs_paths


def connect(url="DEFAULT"):
    """
    :param url: String --> path to the database to be connected to. DEFAULT to connect to database.db
    :return: connection --> sqlite3.connect() obj
             cursor --> sqlite3.cursor obj
    :raises: FileNotFoundError if the path given does not point to a file
    """

    if url == "DEFAULT":
        url = get_abs_paths()['data_store'] + '/database.db'

    if path.exists(url):
        connection = sqlite3.connect(url)
        cursor = connection.cursor()

        return connection, cursor

    else:
        FileNotFoundError("This is not a valid path")


if __name__ == "__main__":
    connect()
