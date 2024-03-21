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


# def create_table():
#     conn = sqlite3.connect('visitors.db')
#     c = conn.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS users (
#                     id INTEGER PRIMARY KEY,
#                     time_out DATETIME,
#                     id_no VARCHAR(30)
#                 )''')  
#     conn.commit()
#     conn.close()
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
    time_out DATETIME,
    visitor_experience VARCHAR(300),
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
def getAllPosts():
    conn = sqlite3.connect('visitors.db')
    c = conn.cursor()
    print(' — — — All Posts — — — \n')
    c.execute("SELECT * FROM visitors")
    postList = c.fetchall()
    i = 0
    for post in postList:
        i += 1
        print(" — — — Post ", i, " — — -")
        print(" First Name : ", post[1])
        print(" Last Name : ", post[2])
        print(" Email : ", post[3])
        print(" ID Number : ", post[4])
        print(" Time In : ", post[5])
        print(" Time Out : ", post[6])
        print(" Reason for Visit : ", post[7])
        print(" Car Plate : ", post[9])
        print("\n")
    print(' — — — SUCCESS — — — \n')
    conn.close()
    home()

def home():
    print("Login, Register, Update Timeout, view")
    action = input("What would you like to do: ").lower()
    
    if action == "register":
        register()
    elif action == "login":
        login()
    elif action == "update timeout":
        update_time_out()
    elif action == "view":
        getAllPosts()
        
    else:
        print("Choose a valid option")
        home()


# Function to log in a user


def login():
    first_name = input("First Name: ")
    id_no = input("Id Number: ")
    conn = sqlite3.connect('visitors.db')
    c = conn.cursor()
    c.execute("SELECT * FROM visitors WHERE first_name=? AND id_no=?", (first_name, id_no))
    visitor = c.fetchone()
    conn.close()

    if visitor:
        print("<<<<<Welcome back, " + visitor[1])
    else:
        print("Incorrect first_name or id_no")
    home()


def update_time_out():
    id_no = input("Id Number: ")
    visitor_experience = input("How was the experience: ")
    time_out = datetime.now()
    conn = sqlite3.connect('visitors.db')
    c = conn.cursor()
    c.execute("UPDATE visitors SET time_out = ?, visitor_experience = ? WHERE id_no = ?", (time_out, visitor_experience, id_no))
    
    if c.rowcount == 0:
        print("Visitor not found.")
    else:
        conn.commit()  
        conn.close()
        print("Updated successfully.")

# Call the function to execute the update.
home()





  
