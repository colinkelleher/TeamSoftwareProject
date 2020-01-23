from python.databases.connectToDatabase import connect

connection, cursor = connect()


def populate_users_table():
    """
    This method populates the users table
    """

    print("Populating users table")
    try:
        cursor.execute("""INSERT INTO users (fname, lname, password, role) 
                          VALUES ('Liam', 'de la Cour', '123', 1)""")
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
        sql = "INSERT INTO products (title, description, location, comments) VALUES (%s, %s, %s, %s)"

        val = [
            ("Cod", "Some smelly Cod", 1, 1),
            ("Salmon", "Tasty Salmon", 1, 2),
            ("Strawberries", "Eww", 2, 3),
            ("Pineapples", "Pen Pineapple Apple Pen", 2, 4)
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
        sql = "INSERT INTO locations (title, description, comments, location_type) VALUES (%s, %s, %s, %s)"

        val = [
            ("Fish Fridge", "Where the fish be stored", 5, 1),
            ("Fruit Fridge", "Where the fruits go", 6, 2)
        ]

        cursor.executemany(sql, val)
        connection.commit()

        print("Populated locations table")


    except Exception as e:
        print(e)


if __name__ == "__main__":
    populate_users_table()
    populate_products_table()
    populate_locations_table()

