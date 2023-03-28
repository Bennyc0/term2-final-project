import sqlite3

database_link = "./static/data/database.db"

# User Log In
def validate_user(email, password):
    connect = sqlite3.connect(database_link)
    cursor = connect.cursor()

    result = cursor.execute('SELECT * FROM userbase WHERE email = ? AND password = ?', (email, password))
    information = {
        "username": ""
    }
    
    for item in result:
        information = {
            "username": item[0],
            "email": item[1],
            "password": item[2]
        }

    connect.close()
    return information['username']


# User Sign Up
def sign_up_user(username, email, password):
    connect = sqlite3.connect(database_link)
    cursor = connect.cursor()

    cursor.execute('INSERT INTO userbase(username, email, password) VALUES (?, ?, ?)', (username, email, password))

    connect.commit()
    connect.close()


# Store/Add Information
def store_information(username, time, food_item, amount, calories):
    connect = sqlite3.connect(database_link)
    cursor = connect.cursor()

    cursor.execute('INSERT INTO user_intake(username, time, food_item, amount, calories) VALUES (?, ?, ?, ?, ?)', (username, time, food_item, amount, calories))

    connect.commit()
    connect.close()


# Edit Information
def edit_information(food_item, amount, calories, rowid):
    connect = sqlite3.connect(database_link)
    cursor = connect.cursor()

    cursor.execute('UPDATE user_intake SET food_item = ?, amount = ?, calories = ? WHERE rowid = ?', (food_item, amount, calories, rowid))
    
    connect.commit()
    connect.close()


# Delete Information
def delete_information(rowid):
    connect = sqlite3.connect(database_link)
    cursor = connect.cursor()

    cursor.execute('DELETE FROM user_intake WHERE rowid = ?', (rowid,))
    
    connect.commit()
    connect.close()


# Get Information From Specific Date
def get_date_information(username, date):
    user_information = []

    connect = sqlite3.connect(database_link)
    cursor = connect.cursor()

    result = cursor.execute('SELECT rowid, * FROM user_intake WHERE username = ? AND time LIKE ?', (username, date + "%"))

    for row in result:
        instance = {
            'rowid': row[0],
            'username': row[1],
            'time': row[2],
            'food_item': row[3],
            'amount': row[4],
            'calories': row[5]
        }

        user_information.append(instance)

    connect.close()
    return user_information


# Get Information (From a specific row)
def get_row_information(rowid):
    connect = sqlite3.connect(database_link)
    cursor = connect.cursor()

    result = cursor.execute('SELECT rowid, * FROM user_intake WHERE rowid = ?', (rowid,))

    for row in result:
        instance = {
            'rowid': row[0],
            'username': row[1],
            'time': row[2],
            'food_item': row[3],
            'amount': row[4],
            'calories': row[5]
        }

    connect.close()
    return instance


# Get User Information
def get_user_information(username):
    user_information = []

    connect = sqlite3.connect(database_link)
    cursor = connect.cursor()

    result = cursor.execute('SELECT rowid, * FROM user_intake WHERE username = ?', (username,))

    for row in result:
        instance = {
            'rowid': row[0],
            'username': row[1],
            'time': row[2],
            'food_item': row[3],
            'amount': row[4],
            'calories': row[5]
        }

        user_information.append(instance)

    connect.close()
    return user_information