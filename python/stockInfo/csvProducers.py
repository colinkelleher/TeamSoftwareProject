import csv
import os

from python.path_stuff import get_abs_paths

# Location of product csv file
product_history_output_path = get_abs_paths()['data_store'] + "/product_history.csv"


def add_product_to_history(product_id, product_title, location_id, location_name):
    """
    Logs a product being added to the system in a csv file called product_history.csv

    TODO Maybe pass arguments as some sort of object to make code cleaner?

    Arguments:
        product_id -- The id of the product
        product_title -- The name of the product
        location_id -- The id of the location of the object
        location_name -- The name of the location it is stored in
    """

    fields = ["id", "title", "location_id", "location_name"]

    if not os.path.exists(product_history_output_path):
        with open(product_history_output_path, "w+", newline="") as file:
            writer = csv.DictWriter(file, fields)
            writer.writeheader()

    with open(product_history_output_path, "a", newline="") as file:
        writer = csv.DictWriter(file, fields)
        writer.writerow({"id": product_id, "title": product_title, "location_id": location_id,
                         "location_name": location_name})


if __name__ == "__main__":

    for i in range(1, 11, 1):
        add_product_to_history(i, "ham", 1, "Meat Fridge")

    for i in range(11, 26, 1):
        add_product_to_history(i, "fish", 2, "Fish Fridge")

    for i in range(26, 37, 1):
        add_product_to_history(i, "ham", 3, "Meat Fridge 2")
