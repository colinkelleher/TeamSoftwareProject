import matplotlib.pyplot as plt
import csv
from python.databases.databaseQueries import select_fullness_of_locations

product_history_csv_path = "../output/product_history.csv"
path_to_created_graphs = "../output/created_graphs"


def _draw_bar_chart(title, x_label, y_label, x_items, item_counts, png_name):
    """
    A function to draw and save bar charts as files

    Arguments:
        title -- String - The title you wish to have displayed above the graph
        x_label -- String - The label that will be displayed under the x-axis
        y_label -- String - The label that will be displayed beside the y-axis
        x_items -- List of strings - Each string is the name of the type of data, i.e. label under each bar
        item_counts -- List of floats - Each number represents the amount of items that are
                                        there, i.e. how high each bar will go
        png_name -- String - The name you wish to save the bar chart as
    """

    index = [i for i in range(0, len(x_items), 1)]

    plt.bar(index, item_counts)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(index, x_items)
    plt.title(title)

    plt.savefig(path_to_created_graphs + "/" + png_name + ".png", bbox_inches="tight")


def _get_number_of_occurrences_in_csv_file_by_index(path_to_csv_file, col_index):
    """
    This function counts the number of times a field appears in a csv file, and returns a dictionary of
    these counts

    Arguments:
        path_to_csv_file -- String - The path to the csv file you wish to parse
        col_index -- Int - The column index of the data you wish to compare (Starts at 0)

    Returns:
        items -- Dictionary - A dictionary where the key is the occurring item, and its value is the number of times
                              that it occurs
    """

    with open(path_to_csv_file) as csv_file:
        csv_reader = csv.reader(csv_file)

        items = {}

        for index, row in enumerate(csv_reader):
            if index == 0:
                pass
            else:
                if row[col_index] in items.keys():
                    items[row[col_index]] += 1
                else:
                    items[row[col_index]] = 1

        return items


def create_graph_of_product_history():
    """
    This function creates a graph of total products stored, and saves it as a png
    """

    items = _get_number_of_occurrences_in_csv_file_by_index(product_history_csv_path, 1)

    item_names = []
    item_count = []

    for item in items.keys():

        item_names.append(item)
        item_count.append(items[item])

    _draw_bar_chart("History of Products Stored", "Item", "Item Count", item_names, item_count,
                    "product_history")


def create_graph_of_times_all_locations_have_been_used():
    """
    This function creates a bar chart that shows the number of times a location has been used
    """

    locations = _get_number_of_occurrences_in_csv_file_by_index(product_history_csv_path, 3)

    location_names = []
    location_count = []

    for location in locations.keys():
        location_names.append(location)
        location_count.append(locations[location])

    _draw_bar_chart("Times Locations Have Been Used", "Location", "Times Used", location_names, location_count,
                    "location_history")


def create_graph_of_how_full_locations_are():
    """
    This function creates a graph showing how much space has been used in each location
    """

    rows = select_fullness_of_locations()

    full_size = []
    empty_size = []
    location_names = []

    index = [i for i in range(0, len(rows), 1)]

    for row in rows:
        used = row[3]
        capacity = row[2]

        full_size.append(float((used/capacity) * 100))
        empty_size.append(float(100 - ((used/capacity) * 100)))

        location_names.append(row[1])

    used = plt.bar(index, full_size, color="b")
    available = plt.bar(index, empty_size, color="r", bottom=full_size)
    plt.xticks(index, location_names)
    plt.legend((used[0], available[0]), ("Space used", "Space available"))
    plt.xlabel("Locations")
    plt.ylabel("Percent of Capacity")

    plt.savefig(path_to_created_graphs + "/location_space_used.png", bbox_inches="tight")


def create_pie_chart_showing_where_majority_of_stock_is():
    """
    This function creates a pie chart that shows what percentage of the total product stored, is
    stored at each location
    """
    rows = select_fullness_of_locations()

    labels = []
    sizes = []

    for row in rows:
        labels.append(row[1])
        sizes.append(row[3])

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
    ax1.axis("equal")

    plt.title("Percentage of Total Product Stored")

    plt.savefig(path_to_created_graphs + "/pie_chart_of_space_used.png", bbox_inches="tight")


if __name__ == "__main__":
    create_pie_chart_showing_where_majority_of_stock_is()