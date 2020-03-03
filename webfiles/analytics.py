#!/usr/bin/python3

from python.webpage_functions import print_main
from python.stockInfo.graphing_functions.graphing_functions import *

create_graph_of_product_history()
create_graph_of_times_all_locations_have_been_used()
create_graph_of_how_full_locations_are()

print_main("analytics.html")
