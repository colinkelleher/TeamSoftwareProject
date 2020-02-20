#!/usr/bin/python3

from python.webpage_functions import print_main
from python.user import get_user
from python.databases.databaseQueries import select_all_with_conditions


# Get the users email address, the key of the database
user_email = get_user().email

# use this key to search for the users info and get a dictionary of info
user_info = select_all_with_conditions("users", "email", user_email)[0]

# Print the html page with users info
print_main('profile.html', {"image": user_info["image"], "firstName": user_info["fname"],
                            "secondName": user_info["lname"], "email": user_info["email"],
                            "role": user_info["role"]})
