import matplotlib.pyplot as plt
import csv

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


if __name__ == "__main__":
    create_graph_of_product_history()
