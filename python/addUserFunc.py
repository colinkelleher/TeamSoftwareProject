from python.databases.connectToDatabase import connect
from python.databases.databaseQueries import select_all
from cgitb import enable
from html import escape

enable()


def addUser(email, username, fname, lname, password, role, image):
    """
      Function to add a product to the database."

      @param - a list of values to be inputted

      @returns - Suitable messages if there is or there is not an error.
    """
    try:
        connection, cursor = connect()


        try:
            sql = "INSERT INTO users (email,username,fname,lname,password,role,image) VALUES (?, ?, ?, ?, ?, ?, ?);"
            cursor.execute(sql,
                           (email, username, fname, lname, password, role, image))
            connection.commit()

            return ("User successfully added!")
        except Exception as e:

            return ("User already exists. Please try again")

    except Exception as e:

        return ("ERROR %s" % e)


if __name__ == "__main__":
    # TESTING
    values = ["email","username","fname","lname","password",1,"image"]
    print(addUser(values))
    print(select_all("users"))