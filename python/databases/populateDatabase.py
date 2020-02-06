from python.databases.connectToDatabase import connect
from python.password import Password

connection, cursor = connect()
from random import randint


def populate_users_table():
    """
    This method populates the users table
    """

    print("Populating users table")
    _hashed_password = Password("123")
    try:
        cursor.execute("""INSERT INTO users (fname, lname, password, role) 
                          VALUES ('Liam', 'de la Cour', ? , 1)""", (str(_hashed_password),))
        connection.commit()
        print("Populated users table")
    except Exception as e:
        print(e)


def populate_products_table():
    """
    This method populates the products table
    """

    print("Populating products table")

    try:
        sql = "INSERT INTO products (title, description, location, comments) VALUES (?, ?, ?, ?)"

        for i in range(1):
            val = [
                ("Cod", "Fresh cod from off the cost of South Africa. 1tn", randint(1, 9), 1),
                ("Salmon", "Frozen salmon from the Irish sea. 2.tn", randint(1, 9), 2),
                ("Strawberries", "Fresh Wexford Strawberries. 10kg (40 x 250g)", randint(1, 9), 3),
                ("Pineapple Tin", "Tin of pineapple in syrup. 50kg (500 x 100g)", randint(1, 10), 4)
            ]

            cursor.executemany(sql, val)
            connection.commit()

        print("Populated products table")


    except Exception as e:
        print(e)


def populate_locations_table():
    """
    This method populates the locations table
    """

    print("Populating locations table")

    try:
        sql = "INSERT INTO locations (title, description, comments, location_type, map) VALUES (?, ?, ?, ?, ?)"

        val = []

        val.append(("Computer closest to main door", "Used for storing items for a short period of time", 5, 1,
                    "/TeamSoftwareProject/images/locations/%d.png" % 1))

        val.append(("Middle computer on back row", "People always forget their keys here", 5, 1,
                    "/TeamSoftwareProject/images/locations/%d.png" % 2))

        val.append(("Computer at the back right", "This is used for storing items for a long period of time", 5, 1,
                    "/TeamSoftwareProject/images/locations/%d.png" % 3))

        val.append(("Computer on the right of the middle row", "This is where phones are left during working hours", 5, 1,
                    "/TeamSoftwareProject/images/locations/%d.png" % 4))

        val.append(("Computer in the middle of the middle row", "This is where the manager stores paper work and \
                                                                items being inspected", 5, 1,
                    "/TeamSoftwareProject/images/locations/%d.png" % 5))

        val.append(("Computer on the right of the middle row", "This is where items are stored after being inspected", 5, 1,
                    "/TeamSoftwareProject/images/locations/%d.png" % 6))

        val.append(("Computer on the left of the first row", "Items are stored here if they are being sent to Lidl", 5, 1,
                    "/TeamSoftwareProject/images/locations/%d.png" % 7))

        val.append(("Computer in the middle of the fist row", "Items are stored here if they are being sent to Aldi", 5, 1,
                    "/TeamSoftwareProject/images/locations/%d.png" % 8))

        val.append(("Computer closest to the secondary door", "Items are stored here if they are being sent to SuperValu", 5, 1,
                    "/TeamSoftwareProject/images/locations/%d.png" % 9))

        cursor.executemany(sql, val)
        connection.commit()

        print("Populated locations table")


    except Exception as e:
        print(e)


if __name__ == "__main__":
    populate_users_table()
    populate_products_table()
    populate_locations_table()
