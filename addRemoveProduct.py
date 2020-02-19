from databases.connectToDatabase import connect
from databases.databaseQueries import select_all
from cgitb import enable
from html import escape
enable()


def addProduct(values):
    """
      Function to add a product to the database."

      @param - a list of values to be inputted

      @returns - Suitable messages if there is or there is not an error.
    """
    try:
        connection, cursor = connect()
        id = values[0]
        title = values[1]
        description = values[2]
        location = values[3]
        comments = values[4]
        photo = values[5]
        expiry_date = values[6]
        volume = values[7]
        if id == None or id == "":
            return ("Please enter and id.")
        else:
            sql = "SELECT id from products where id = ?;"
            cursor.execute(sql, (int(id),))
            if len(cursor.fetchall()) > 0:
                connection.commit()
                return ("Product is already in the database.")

            else:
                try:
                    sql = "INSERT INTO products (id, title, description, location, comments, photo, expiry_date, volume) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"
                    cursor.execute(sql, (int(values[0]), values[1], values[2], values[3], values[4], values[5], values[6], values[7]))
                    connection.commit()
                    return ("Product successfully added!")
                except Exception as e:
                    print(e)

    except Exception as e:
        print(e)

def removeProduct(id):
    """
    Function to remove a product to the database."

    @param - an id of a product to remove

    @returns - Suitable messages if there is or there is not an error.

    """

    try:
        connection, cursor = connect()


        if id == None or id == "":
            return("Please enter and id.")
        else:
            sql = "SELECT id from products where id = ?;"
            cursor.execute(sql, (int(id),))
            if len(cursor.fetchall()) == 0:
                connection.commit()
                return ("Product is not in the database.")

            else:
                try:
                    sql = "DELETE FROM products WHERE id=?;"
                    cursor.execute(sql, (int(id),))
                    connection.commit()
                    return ("Product successfully removed.")
                except Exception as e:
                    print(e)

    except Exception as e:
        print(e)



if __name__ == "__main__":
    # TESTING
    values = ["45", "x", "xx", "xxx", "xxxx", "xxxx", 34, "xxxxxx"]
    print(addProduct(values))
    print(select_all("products"))

    print("\n\n")
    print(addProduct(values))
    print(select_all("products"))
    print("\n\n")
    print(removeProduct("45"))
    print(select_all("products"))
    print(removeProduct("45"))
