#!/usr/local/bin/python3
from python.databases.connectToDatabase import connect
from python.databases.databaseQueries import select_all_with_conditions
from cgitb import enable
from cgi import FieldStorage
from html import escape
enable()

def processRequest():
    # function to deal with form data and pass it to the appropriate function
    form_data = FieldStorage()
    if len(form_data) != 0:
        request_type = escape(form_data.getfirst("request_type", "").strip())
        title = escape(form_data.getfirst("title", "").strip())
        description = escape(form_data.getfirst("description", "").strip())
        location = escape(form_data.getfirst("location", "").strip())
        comments = escape(form_data.getfirst("comments", "").strip())
        if request_type == "add":
            if not title or not description or not location or not comments:
                print("Make sure to fill in all the details when adding a product.")
            else:
                vals = [title, description, location, comments]
                addProduct(vals)
        elif request_type == "remove":
            if not title or not description or not location or not comments:
                print("Make sure to fill in all the details when removing a product.")
            else:
                vals = [title, description, location, comments]
                removeProduct(vals)
        else:
            print("Please choose a valid request type(add or remove).")

def addProduct(vals):
    # function to add a product to the database
    # returns 1 if successful, -1 otherwise
    try:
        connection, cursor = connect()
        sql = "INSERT INTO products (title, location, description, comments) VALUES (?, ?, ?, ?);"
        cursor.execute(sql, vals[0], vals[1], vals[2], vals[3],)
        connection.commit()
        return 1
    except:
        return -1

def removeProduct(vals):
    # function to remove a product from the database
    # Will add a check after initial testing to see if the product is in the database before attempting to remove
    # returns 1 if successful, -1 otherwise
    try:
        connection, cursor = connect()
        sql = "DELETE FROM products WHERE title=? and description=? and location=? and comments=?;"
        cursor.execute(sql, vals[0], vals[1], vals[2], vals[3],)
        connection.commit()
        return 1
    except:
        return -1

if __name__ == "__main__":
    processRequest()
