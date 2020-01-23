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
        products_stored_in_location = select_all_with_conditions("products", "location", location[0])

        output += "<table><tr><th>%s</th></tr>" % (location[1])
        output += "<tr><th>Product:</th><th>Description</th></tr>"

        for product in products_stored_in_location:
            output += "<tr><td>%s</td><td>%s</td></tr>" % (product[1], product[2])

        output += "</table>"

    output += "</section>"

    return output


if __name__ == "__main__":
    print(create_table_of_locations())
