import sqlite3
from os import path


def connect(url="../databases/database.db"):
    """
    :param url: String --> path to the database to be connected to
    :return: connection --> sqlite3.connect() obj
             cursor --> sqlite3.cursor obj
    :raises: FileNotFoundError if the path given does not point to a file
    """
    if path.exists(url):
        connection = sqlite3.connect(url)
        cursor = connection.cursor()

        return connection, cursor

    else:
        FileNotFoundError("This is not a valid path")


if __name__ == "__main__":
    connect()
