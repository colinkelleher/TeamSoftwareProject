#!/usr/bin/python3

from python.webpage_functions import print_main, get_html_template
from python.stockInfo.graphing_functions.graphing_functions_js import *
from python.stockInfo.graphing_functions.graphing_functions import get_how_full_locations_are
from json import dumps

# Randomized list from https://gist.github.com/mucar/3898821
colorArray = ['#E6B333', '#66664D', '#FF1A66', '#4DB380', '#809900', '#4DB3FF', '#80B300', '#3366E6', '#4D8066',
              '#E666B3', '#E6FF80', '#66991A', '#FFB399', '#E666FF', '#00E680', '#809980', '#1AB399', '#E6331A',
              '#6680B3', '#66E64D', '#FF4D4D', '#99E6E6', '#4D80CC', '#9900B3', '#B366CC', '#FFFF99', '#B33300',
              '#CCCC00', '#999933', '#33991A', '#E6B3B3', '#B3B31A', '#66994D', '#4D8000', '#00B3E6', '#33FFCC',
              '#CCFF1A', '#6666FF', '#991AFF', '#FF99E6', '#CC9999', '#CC80CC', '#FF33FF', '#B34D4D', '#999966',
              '#FF6633', '#FF3380', '#1AFF33', '#99FF99', '#E64D66']


def get_chart_data(name, data, backgroundColor):
    """
    Creates bar data dictionary
    :param name what the data is called
    :data list of data
    :backgroundColor javascript string color or hex
    """
    return dict(label=name, data=data, backgroundColor=backgroundColor)


def _get_chart(type, title, column_names, scales, *bar_data):
    """
    Returns javascript bar chart html
    *bar_data will be stacked if more than one is given

    :param title the title of the bar chart
    :param column_names the names of each column under the bar chart
    :*bar_data as much bar data dictionaries as you want
    """
    global bar_html
    return bar_html.safe_substitute(type=type, title=title, column_names=column_names, scales=scales,
                                    bar_data=dumps([*bar_data]))


def get_pie_chart(title, column_names, *bar_data):
    return _get_chart('pie', title, column_names, '', *bar_data)


def get_bar_chart(title, column_names, *bar_data):
    scales = '''
        scales: {
                xAxes: [{
                    stacked: true,
                }],
                yAxes: [{
                    stacked: true,
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
    '''
    return _get_chart('bar', title, column_names, scales, *bar_data)


bar_html = get_html_template('chart_template.html')
output = ''

# Get bar chart for location space usage
names, full_space, empty_space = get_how_full_locations_are()
used_data = get_chart_data('Space Used', full_space, 'blue')
empty_data = get_chart_data('Total Space', empty_space, 'red')
output += get_bar_chart('Location Space Usage', names, used_data, empty_data)

# Get bar chart for dates food expires at
dates, dates_count = count_of_expiring_food()
expiring_data = get_chart_data('Amount of Product', dates_count, 'blue')
output += get_bar_chart('Product Expiring On', dates, expiring_data)

# count_of_expiring_food_to_total_of_that_product
names, total, expiring = count_of_expiring_food_to_total_of_that_product()
total_data = get_chart_data('Total Product', total, 'blue')
expiring_data = get_chart_data('Expiring Product', expiring, 'red')
output += get_bar_chart('Number of Products Expiring in 10 days', names, expiring_data, total_data)

# pie_chart_showing_distribution_of_products
names, values = pie_chart_showing_distribution_of_products()
data = get_chart_data('Products', values, colorArray)
output += get_pie_chart('Distribution of Product', names, data)

print_main(output)
