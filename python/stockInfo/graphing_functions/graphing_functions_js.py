from python.databases.databaseQueries import *

"""
This file contains functions to return values to be passed into analytics_charts.js.
"""


def count_of_expiring_food():
    """
    This function returns data to create a bar chart where each day that has product expiring on it is represented by a bar,
    and the height of the bar represents how many products are expiring on that day
    """

    rows = get_count_of_product_expiring_soon(10)

    column_names = []
    values = []

    for row in rows:
        date = row['expiry_date']
        new_date = date[8:10] + "-" + date[5:7]
        column_names.append(new_date)
        values.append(row['count'])
    return column_names, values


def count_of_expiring_food_to_total_of_that_product():
    """
    This function creates returns values for a double bar chart comparing the count of each product in
    the database with the number of that product expiring in the next 10 days.

    """
    temp1 = get_list_of_product_expiring_soon(20)
    temp2 = getCountOfEachProduct()
    products = [list(elem) for elem in temp2]
    expiring_products = [list(elem) for elem in temp1]
    for product in products:
        product.append(0)

    for expiring_product in expiring_products:
        for product in products:
            if expiring_product[3] == product[1]:
                product[2] += 1

    column_names = []
    total_products = []
    expiring_products = []

    for product in products:
        column_names.append(product[1])
        total_products.append(product[0])
        expiring_products.append(product[2])
    return column_names, total_products, expiring_products


def pie_chart_showing_distribution_of_products():
    """
    This function creates returns values for a pie chart which will show the disturbution of
    quantity within the product database.

    """
    temp = getCountOfEachProduct()
    products = [list(elem) for elem in temp]

    column_names = []
    values = []
    for product in products:
        column_names.append(product[1])
        values.append(product[0])

    return column_names, values


if __name__ == "__main__":
    print(pie_chart_showing_distribution_of_products())
    print()
    print(count_of_expiring_food_to_total_of_that_product())
    print()
    print(count_of_expiring_food())
