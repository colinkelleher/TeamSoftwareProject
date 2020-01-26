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

    sql = "SELECT * FROM %s WHERE %s = %s" % (table, column_name, value)

    cursor.execute(sql)
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

    sql = "SELECT * FROM %s WHERE %s = %s AND %s = %s" % (table, column_name1, value1, column_name2, value2)

    cursor.execute(sql)
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

        location_info = select_all_with_conditions("locations", "id", info["location_id"])
        if location_info:
            location_info = location_info[-1]
            #todo Finish location_info. Will implement get_location_info() first
        info["location_info"] = {}
        info["comment_id"] = str(prod_info[4])
        info["photo"] = prod_info[5]

    return info

if __name__ == "__main__":
    print(get_product_info(1))