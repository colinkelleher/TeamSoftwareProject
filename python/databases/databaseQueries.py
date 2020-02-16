from python.databases.connectToDatabase import connect
from string import Template

connection, cursor = connect()


def execute(statement, *args):
    if 'sqlite3' in str(cursor.__class__):
        statement = statement.replace('%s', '?')
    cursor.execute(statement, args)


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


def select_all_with_conditions(table, column_name, value):
    """
    This function will return the results from a select statement with a where clause

    Arguments:
        table -- Name of the table to query
        column_name -- The name of the column that is being compared
        value -- The value that is to be matched

    Returns:
        result -- List of tuples representing each row returned
    """

    sql = Template("SELECT * FROM ${table} WHERE ${column_name} = %s")
    sql = sql.substitute(dict(table=table, column_name=column_name))

    execute(sql, value)
    result = cursor.fetchall()

    return result


def select_all_with_2_conditions(table, column_name1, value1, column_name2, value2):
    """
    This function will return the results from a select statement with a where clause

    Arguments:
        table -- Name of the table to query
        column_name (1 & 2) -- The name of the respective column that is being compared
        value (1 & 2) -- The respective value that is to be matched

    Returns:
        result -- List of tuples representing each row returned
    """
    sql = Template("SELECT * FROM ${table} WHERE ${column1} = %s AND ${column2} = %s")
    sql = sql.substitute(dict(table=table, column1=column_name1, column2=column_name2))

    execute(sql, value1, value2)

    result = cursor.fetchall()

    return result


def get_location_info(location_id):
    """
        Function will return the locations information
        :param location: Integer representing the location id
        :return: dictionary containing all information about a location
                {"id" : int,
                "title" : string,
                "description" : string,
                "comment_id" : string,
                "map" : string,
                "location_type" : int}
        """
    info = {}
    location_info = select_all_with_conditions("locations", "id", location_id)
    if location_info:
        location_info= location_info[-1]
        info["id"] = int(location_info[0])
        info["title"] = location_info[1]
        info["description"] = location_info[2]
        info["comment_id"] = location_info[3]
        info["map"] = location_info[4]
        info["location_type"] = location_info[5]

    return info


def select_all_with_join(table1, table2, on_condition1, on_condition2, where_condition, where_value):
    """
    Select all rows of one table joined with another

    Arguments:
        table1 -- The first table of the join
        table2 -- The second table of the join
        on_condition1 -- The condition of the first table to match with the second
        on_condition2 -- The condition of the second table to match with the first
        where_condition -- The field of the table to compare
        where_value -- The value of the where_condition to match
    Returns:
        result -- A list of tuples which contain the fields of each row

    """

    sql = Template("SELECT * FROM ${table1} JOIN ${table2} ON ${condition1} = ${condition2} "
                   "WHERE ${where_condition} = %s")
    sql = sql.substitute(dict(table1=table1, table2=table2, condition1=on_condition1, condition2=on_condition2,
                              where_condition=where_condition))

    execute(sql, where_value)

    result = cursor.fetchall()

    return result


def get_product_info(prod_id):
    """
    Function will return the products information
    :param prod_id: Integer representing the product id
    :return: dictionary containing all information about a product
            {"id" : int,
            "title" : string,
            "description" : string,
            "location_id" : int,
            "location_info" : dictionary,
            "comment_id" : string,
            "photo" : string}
    """
    info = {}
    prod_info = select_all_with_conditions("products", "id", prod_id)
    if prod_info:
        prod_info = prod_info[-1]
        info["id"] = int(prod_info[0])
        info["title"] = prod_info[1]
        info["description"] = prod_info[2]
        info["location_id"] = int(prod_info[3])
        info["location_info"] = get_location_info(info["location_id"])
        info["comment_id"] = str(prod_info[4])
        info["photo"] = prod_info[5]

    return info


def get_product_that_expires_on(date):
    """
    This function returns all products, and the location of it, that are expiring on a given date

    Arguments:
        date -- A string representing the date of expiry you wish to query against '(YYYY-MM-DD)'

    Returns:
        products - A list where each item is a tuple of of each row returned by the query

    """

    products = select_all_with_join("products", "locations", "products.location", "locations.id",
                                    "expiry_date", date)

    return products


def select_fullness_of_locations():
    """
    This function joins the product and location tables, groups them by location id,
    and gets the info about the table id, its title, its total capacity and how full it
    currently is

    Returns:
        result -- A list of tuples, where each tuple
                  is a row in the returned table, (id, name, capacity, how full it is)
    """

    sql = "SELECT l.id, l.title, l.capacity, SUM(p.volume) " \
          "FROM locations AS l JOIN products AS p " \
          "ON l.id = p.location GROUP BY l.id"

    execute(sql)

    result = cursor.fetchall()

    return result


def get_count_of_product_expiring_soon(limit=100):
    """
    This function groups product that is expiring by date, and returns a count of how much is expiring in the
    coming days. How far into the future you see is determined by the limit variable.

    Arguments:
        limit -- int - Represents the number of rows you wish to see in the result

    Returns:
        result -- List of tuples representing each row in the selection
    """

    sql = """SELECT count(*), expiry_date
             FROM products
             GROUP BY expiry_date
             ORDER BY expiry_date
             LIMIT %d;
            """ % limit

    execute(sql)

    result = cursor.fetchall()

    return result

def add_user(fname, lname, email, password):
    """
    Adds user info to the database
    returns True if successful
    """
    try:
        cursor.execute("""INSERT INTO users (email, fname, lname, password, role)
                          VALUES (?, ?, ?, ? , ?)""", (email, fname, lname, password, "0"))
        connection.commit()
    except Exception as e:
        return False

    return True

if __name__ == "__main__":
    print(get_product_info(1))
    print(get_location_info(1))

    print(select_all_with_join("products", "locations", "products.location", "locations.id", "expiry_date", "2020-01-30"))

    print(get_product_that_expires_on("2020-01-30"))

    print(select_fullness_of_locations())

    print()

    print(get_count_of_product_expiring_soon())
