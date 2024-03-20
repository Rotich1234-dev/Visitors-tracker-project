import sqlite3

# Define the User class

from datetime import datetime


class Visitor:
    def __init__(self, first_name, last_name, id_no,email,reason,car_plate):
        self.first_name = first_name
        self.last_name = last_name
        self.id_no = id_no
        self.email = email
        self.reason = reason
        self.car_plate = car_plate
        self.loggedIn = True

# Function to create the database table if it doesn't exist


def create_table():
    conn = sqlite3.connect('visitors.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    username TEXT,
                    password TEXT
                )''')
    conn.commit()
    conn.close()
# Function to register a new user


def register():
    print("<!><!><!><!><!><!><!>REGISTRATION<!><!><!><!><!><!><!>")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    id_no = input("Id Number: ")
    email = input("email: ")
    reason_for_visit = input("reason: ")
    car_plate = input("car plate: ")
    visitor = Visitor(first_name, last_name, id_no,email,reason_for_visit,car_plate)
    # print("Welcome, " + user.name)
    
    # Save user data to the database
    conn = sqlite3.connect('visitors.db')
    c = conn.cursor()
    c.execute(''' CREATE TABLE IF NOT EXISTS visitors (
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    email VARCHAR(30),
    id_no VARCHAR(30),
    time_in DATETIME,
    reason_for_visit VARCHAR(300),
    car_plate VARCHAR(20)
); ''')
    time_in = datetime.now()

    c.execute("INSERT INTO visitors (first_name, last_name, email ,id_no, time_in, reason_for_visit, car_plate ) "
              "VALUES (?, ?, ?, ?, ?, ?, ?)", (first_name,last_name, email, id_no, time_in, reason_for_visit, car_plate))
    conn.commit()
    conn.close()
    print("========REGISTRATION SUCCESSFUL WELCOME!=========")
    home()

# Function to handle the main menu


def home():
    print("Login, Register")
    a = input("What would you like to do: ")
    if a.lower() == "register":
        register()
    elif a.lower() == "login":
        login()
    else:
        print("Choose a valid option")
        home()

# Function to log in a user


def login():
    l = input("Username: ")
    l2 = input("Password: ")
    conn = sqlite3.connect('visitors.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (l,))
    user = c.fetchone()
    conn.close()

    if user and user[3] == l2:
        print("Welcome, " + user[1])
    else:
        print("Incorrect username or password")
        login()
    home()

# Create the users table


create_table()

# Start the program
home()