#!/usr/bin/python3

from python.webpage_functions import print_main
from python.user import get_user
from python.databases.databaseQueries import select_all_with_conditions


user_email = get_user().email

user_info = select_all_with_conditions("users", "email", user_email)[0]

print_main('profile.html', {"image": user_info["image"], "firstName": user_info["fname"],
                            "secondName": user_info["lname"], "email": user_info["email"],
                            "role": user_info["role"]})
