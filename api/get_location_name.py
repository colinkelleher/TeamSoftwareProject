#!/usr/bin/python3

from json import dumps
# Import to authenticate user, as well as form data stuff
from python.webpage_functions import get_form_data, has_form_data
from python.databases.databaseQueries import select_all_with_conditions

output = dict()
if has_form_data():
    location = get_form_data('lid')
    row = select_all_with_conditions('locations', 'id', location)
    if len(row):
        output["name"] = row[0][1]

print('Content-Type: text/json')
print()
print(dumps(output))

