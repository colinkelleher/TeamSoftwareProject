#!/usr/bin/python3

from python.webpage_functions import print_main, get_html_template
from python.stockInfo.graphing_functions.graphing_functions import get_how_full_locations_are, \
    get_count_of_expiring_food
from json import dumps


def get_chart_data(name, data, backgroundColor):
    """
    Creates bar data dictionary
    :param name what the data is called
    :data list of data
    :backgroundColor javascript string color or hex
    """
    return dict(label=name, data=data, backgroundColor=backgroundColor)


def _get_chart(type, title, column_names, *bar_data):
    """
    Returns javascript bar chart html
    *bar_data will be stacked if more than one is given

    :param title the title of the bar chart
    :param column_names the names of each column under the bar chart
    :*bar_data as much bar data dictionaries as you want
    """
    global bar_html
    return bar_html.safe_substitute(type=type, title=title, column_names=column_names, bar_data=dumps([*bar_data]))


def get_pie_chart(title, column_names, *bar_data):
    return _get_chart('pie', title, column_names, *bar_data)


def get_bar_chart(title, column_names, *bar_data):
    return _get_chart('bar', title, column_names, *bar_data)


bar_html = get_html_template('chart_template.html')
output = ''

# Get bar chart for location space usage
names, full_space, empty_space = get_how_full_locations_are()
used_data = get_chart_data('Space Used', full_space, 'blue')
empty_data = get_chart_data('Total Space', empty_space, 'red')
output += get_bar_chart('Location Space Usage', names, used_data, empty_data)

# Get bar chart for dates food expires at
dates, dates_count = get_count_of_expiring_food()
expiring_data = get_chart_data('Amount of Product', dates_count, 'blue')
output += get_bar_chart('Product Expiring On', dates, expiring_data)

print_main(output)
