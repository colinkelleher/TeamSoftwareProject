from python.databases.databaseQueries import select_all, select_all_with_conditions


def create_table_of_locations():
    """
    This function will create a html table containing all products and information for each location

    Returns:
        output -- The string containing the html of the tables
    """

    locations = select_all("locations")

    output = "<section>"

    for location in locations:

        output += create_table_of_products_from_location(location[0], location[1])

    output += "</section>"

    return output


def create_table_of_products_from_location(location_id, location_name):
    """
    This function creates a table from the products stores in a location

    Arguments:
        location_id - int representing the id of the location
        location_name - String representing the name of the location

    Returns:
        output - String containing the table of products
    """

    output = ""

    products_stored_in_location = select_all_with_conditions("products", "location", location_id)

    output += "<table><tr><th>%s</th></tr>" % location_name
    output += "<tr><th>Product:</th><th>Description</th></tr>"

    for product in products_stored_in_location:
        output += "<tr><td>%s</td><td>%s</td></tr>" % (product[1], product[2])

    output += "</table>"

    return output


if __name__ == "__main__":
    print(create_table_of_locations())
