from python.databases.connectToDatabase import connect

connection, cursor = connect()


def select_all(table):
    """
    This function will return select everything from the provided table

    Arguments:
        table -- the name of the table you wish to select (String)

    Returns:
        result -- list of tuples representing each row returned

    """

    sql = "SELECT * FROM " + table

    cursor.execute(sql)
    result = cursor.fetchall()

    return result


if __name__ == "__main__":
    print(select_all("products"))
