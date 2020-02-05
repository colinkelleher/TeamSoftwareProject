import matplotlib.pyplot as plt
import csv

product_history_csv_path = "../output/product_history.csv"
path_to_created_graphs = "../output/created_graphs"


def create_graph_of_product_history():
    """
    This function creates a graph of total products stored, and saves it as a png
    """
    with open(product_history_csv_path) as csv_file:
        csv_reader = csv.reader(csv_file)

        items = {}

        for index, row in enumerate(csv_reader):
            if index == 0:
                pass
            else:
                if row[1] in items.keys():
                    items[row[1]] += 1
                else:
                    items[row[1]] = 1

    item_names = []
    item_count = []

    for item in items.keys():

        item_names.append(item)
        item_count.append(items[item])

    index = [i for i in range(0, len(item_names), 1)]

    plt.bar(index, item_count)
    plt.xlabel("Item")
    plt.ylabel("No. of Items")
    plt.xticks(index, item_names)
    plt.title("Total number of each items ever stored")

    plt.savefig(path_to_created_graphs + "/product_history.png", bbox_inches="tight")


if __name__ == "__main__":
    create_graph_of_product_history()
