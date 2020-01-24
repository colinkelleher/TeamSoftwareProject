from python.databases.connectToDatabase import connect
from python.databases.databaseQueries import select_all_with_conditions

def update_location(product_id, location_id):
    """
    Function to update a products location
    :param product_id: String/Int representing the product id
    :param location_id: String/Int representing the location id
    :return: None
    """
    location = select_all_with_conditions("locations", "id", location_id)
    product = select_all_with_conditions("products", "id", product_id)
    if len(location) == 0:
        print("location not found")
        return
    if len(product) == 0:
        print("product not found")
        return

    try:
        connection, cursor = connect()
        cursor.execute("""UPDATE products
                          SET location = ?
                          WHERE id = ?;
        """, (location_id, product_id))
        connection.commit()
        print("updated")

    except:
        print("db error")
if __name__ == "__main__":
    update_location("1", "1")
