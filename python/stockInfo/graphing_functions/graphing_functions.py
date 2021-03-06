import csv
from python.databases.databaseQueries import select_fullness_of_locations, get_count_of_product_expiring_soon
from python.path_stuff import get_abs_paths

product_history_csv_path = get_abs_paths()["data_store"] + "/product_history.csv"
path_to_created_graphs = get_abs_paths()["data_store"] + "/created_graphs"


def _draw_bar_chart(title, x_label, y_label, x_items, item_counts, png_name):
    import matplotlib.pyplot as plt

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

    locations = _get_number_of_occurrences_in_csv_file_by_index(product_history_csv_path, 2)

    location_names = []
    location_count = []

    for location in locations.keys():
        location_names.append(location)
        location_count.append(locations[location])

    _draw_bar_chart("Times Locations Have Been Used", "Location", "Times Used", location_names, location_count,
                    "location_history")


def get_how_full_locations_are():
    rows = select_fullness_of_locations()

    full_size = []
    empty_size = []
    location_names = []

    for row in rows:
        used = row['full']
        capacity = row['capacity']

        full_size.append(float((used / capacity) * 100))
        empty_size.append(float(100 - ((used / capacity) * 100)))

        location_names.append(row["title"])

    return location_names, full_size, empty_size

def create_graph_of_how_full_locations_are():
    """
    This function creates a graph showing how much space has been used in each location
    """
    import matplotlib.pyplot as plt

    location_names, full_size, empty_size = get_how_full_locations_are()
    index = [i for i in range(0, len(location_names), 1)]

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
    import matplotlib.pyplot as plt

    rows = select_fullness_of_locations()

    labels = []
    sizes = []

    for row in rows:
        labels.append(row['title'])
        sizes.append(row['full'])

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
    ax1.axis("equal")

    plt.title("Percentage of Total Product Stored")

    plt.savefig(path_to_created_graphs + "/pie_chart_of_space_used.png", bbox_inches="tight")


def get_count_of_expiring_food():
    rows = get_count_of_product_expiring_soon()

    dates = []
    date_count = []

    for row in rows:
        dates.append(row['expiry_date'])
        date_count.append(row['count'])

    return dates, date_count


def create_bar_chart_showing_count_of_expiring_food():
    """
    This function creates a bar chart where each day that has product expiring on it is represented by a bar,
    and the height of the bar represents how much product is expiring on that day

    """

    rows = get_count_of_product_expiring_soon(10)

    dates = []
    date_count = []

    for row in rows:
        print(row)
        date = row['expiry_date']
        new_date = date[8:10] +"-" +date[5:7]
        print(new_date)
        dates.append(new_date)
        date_count.append(row['count'])

    _draw_bar_chart("Products expiring in the next 10 days", "Date", "Number of Products", dates, date_count, "product_expiring_soon")


if __name__ == "__main__":
    create_bar_chart_showing_count_of_expiring_food()
