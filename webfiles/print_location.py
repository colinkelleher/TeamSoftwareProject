#!/usr/bin/python3

from python.webpage_functions import print_html, get_form_data, has_form_data
from python.databases.databaseQueries import select_all_with_conditions
from python.htmlGenerators.qrElement import create_qr_info

if has_form_data():
    if get_form_data('id'):
        lid = get_form_data('id')
        location_info = select_all_with_conditions('locations', 'id', lid)[0]
        print_html('print_qr.html', dict(title=location_info['title'], qrcode=create_qr_info(int(lid))))

    else:
        print_html('404.html')
else:
    print_html('404.html')
