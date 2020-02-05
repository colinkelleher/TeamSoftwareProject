from python.databases.connectToDatabase import connect
from python.databases.databaseQueries import select_all_with_conditions

def update_location(product_id, location_id):
    """
    Function to update a products location
    :param product_id: String/Int representing the product id
    :param location_id: String/Int representing the location id
    :return: 0 --> Location not found
             -1 --> product not found
             -2 --> Error with database
             1 --> Updated okay
    """
    location = select_all_with_conditions("locations", "id", location_id)
    product = select_all_with_conditions("products", "id", product_id)
    if len(location) == 0:
        return 0
    if len(product) == 0:
        return -1

    try:
        connection, cursor = connect()
        cursor.execute("""UPDATE products
                          SET location = ?
                          WHERE id = ?;
        """, (location_id, product_id))
        connection.commit()
        return 1

    except Exception as e:
        print('Content-Type: text/html')
        print()
        print(str(e))
        return -2
if __name__ == "__main__":
    update_location("1", "1")
