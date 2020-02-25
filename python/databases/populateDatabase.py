from python.databases.connectToDatabase import connect
from python.password import Password
import random

connection, cursor = connect()


def populate_users_table():
    """
    This method populates the users table
    """

    print("Populating users table")
    _hashed_password = Password("123")
    try:
        cursor.execute("""INSERT INTO users (email, fname, lname, password, role) 
                          VALUES ('t@t.c', 'Liam', 'de la Cour', ? , 1)""", (str(_hashed_password),))
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
        sql = "INSERT INTO products (title, description, location, comments, photo, expiry_date, volume) VALUES (?, ?, ?, ?, ?, ?, ?)"
        types_of_food = ["Cod", "Salmon", "Tuna", "Calamari", "Chicken Wings", "Chicken Breasts", "Sirloin Steak", "Strawberries",
                            "Blueberries", "Pineapples", "Cranberries", "Bananas", "Milk", "Eggs", ]
        descriptions = ["Cod fresh from the Atlantic", "Fresh fillets of salmon", "John West Tuna", "Fresh Calamari from the Irish Sea", "Shannonvale Chicken Wings", "Shannonvale Chicken Breasts",
                           "Angus Sirloin from West Cork", "Bushby's Strawberries", "Blueberries from USA", "Pineapples from South America", "Cranberries from Chile", "Bananas from Ecuador", "Milk from Clona", "Eggs from Greenfield Foods", ]
        for i in range(0,50):
            randomNum = random.randint(0, 13)

            day = random.randint(1,28)
            if day < 10:
                date="2020-03-0"+str(day)
            else:
                date = "2020-03-"+str(day)
            cursor.execute(sql, (types_of_food[randomNum], descriptions[randomNum], random.randint(1, 9), randomNum, None, date, random.randint(0, 30)))
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
        sql = "INSERT INTO locations (title, description, comments, location_type, map, capacity) VALUES (?, ?, ?, ?, ?, ?)"

        val = []

        val.append(("Computer closest to main door", "Used for storing items for a short period of time", 5, 1,
                    "/assets/images/locations/%d.png" % 1, 1000))

        val.append(("Middle computer on back row", "People always forget their keys here", 5, 1,
                    "/assets/images/locations/%d.png" % 2, 1000))

        val.append(("Computer at the back right", "This is used for storing items for a long period of time", 5, 1,
                    "/assets/images/locations/%d.png" % 3, 1000))

        val.append(("Computer on the right of the middle row", "This is where phones are left during working hours", 5, 1,
                    "/assets/images/locations/%d.png" % 4, 1000))

        val.append(("Computer in the middle of the middle row", "This is where the manager stores paper work and \
                                                                items being inspected", 5, 1,
                    "/assets/images/locations/%d.png" % 5, 1000))

        val.append(("Computer on the right of the middle row", "This is where items are stored after being inspected", 5, 1,
                    "/assets/images/locations/%d.png" % 6, 1000))

        val.append(("Computer on the left of the first row", "Items are stored here if they are being sent to Lidl", 5, 1,
                    "/assets/images/locations/%d.png" % 7, 1000))

        val.append(("Computer in the middle of the fist row", "Items are stored here if they are being sent to Aldi", 5, 1,
                    "/assets/images/locations/%d.png" % 8, 1000))

        val.append(("Computer closest to the secondary door", "Items are stored here if they are being sent to SuperValu", 5, 1,
                    "/assets/images/locations/%d.png" % 9, 1000))

        cursor.executemany(sql, val)
        connection.commit()

        print("Populated locations table")


    except Exception as e:
        print(e)


if __name__ == "__main__":
    populate_users_table()
    populate_products_table()
    populate_locations_table()
