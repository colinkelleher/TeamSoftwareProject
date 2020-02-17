from python.databases.connectToDatabase import connect


connection, cursor = connect()
"""
To generate the tables run the following in the terminal.
python3 createDatabase.py 

Note: You must be in the root of the project directory
"""


def _create_user_db():
    print("creating users table")
    cursor.execute("DROP TABLE IF EXISTS users;")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email VARCHAR(255) UNIQUE,
            username VARCHAR(255) UNIQUE,
            fname VARCHAR(255),
            lname VARCHAR(255),
            password VARCHAR(255),
            role INTEGER,
            image VARCHAR(255)
        );
    """)
    print("created users table")


def _create_product_db():
    print("creating product table")
    cursor.execute("DROP TABLE IF EXISTS products;")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(255),
            description TEXT,
            location INTEGER,
            comments INTEGER,
            photo VARCHAR(255),
            expiry_date DATE,
            volume INTEGER
        );
    """)
    print("created product table")


def _create_location_db():
    print("creating location table")
    cursor.execute("DROP TABLE IF EXISTS locations;")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS locations(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(255),
            description TEXT,
            comments TEXT,
            map VARCHAR(255),
            location_type INTEGER,
            capacity INTEGER
        );
    """)
    print("created location table")


def create_database():
    """
    Function to create the table.
    :return: None
    """
    _create_user_db()
    _create_product_db()
    _create_location_db()


if __name__ == "__main__":
    create_database()
