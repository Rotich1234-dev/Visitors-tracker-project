import sqlite3
import os
# Define the User class

from datetime import datetime



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
    company_id = input("company_id: ")
    reason_for_visit = input("reason: ")
    car_plate = input("car plate: ")
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
    company_id INTEGERR,
    visitor_experience VARCHAR(300),
    reason_for_visit VARCHAR(300),
    car_plate VARCHAR(20)
); ''')
    time_in = datetime.now()

    c.execute("INSERT INTO visitors (first_name, last_name, email ,id_no, time_in, company_id, reason_for_visit, car_plate ) "
              "VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (first_name,last_name, email, id_no, time_in, company_id, reason_for_visit, car_plate))
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
        print(" visitor experience : ", post[8])
        print(" Reason for Visit : ", post[9])
        print(" Car Plate : ", post[10])
        x = c.execute("SELECT name FROM companies where id="+str(post[7])+"")
        y = x.fetchone()
        print(" Company : ", y)
        print("\n")
       
    print(' — — — SUCCESS — — — \n')
    conn.close()
    home()

def home():
    print(" — — — — MENU — — — -")
    print(" 1. Login")
    print(" 2. Register")
    print(" 3. Update Timeout")
    print(" 4. view")
    print(" 5. Exit")
    print(" 6. Delete entry")
    print(" — — — — — — — — — — ")
    action = input("What would you like to do: ").lower()
    
    if action == "2":
        register()
    elif action == "1": 
        login()
    elif action == "3":
        update_time_out()
    elif action == "4":
        getAllPosts()
    elif action == '5':
        os.system('clear') # For Windows
        print('----- Thank You -----')
    elif action == "6" :
        delete_company()
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

def delete_company():
    id = input("company id: ")
    conn = sqlite3.connect('visitors.db')
    c = conn.cursor()
    c.execute("SELECT * FROM companies WHERE id = ?", (id))
    c.execute("DELETE FROM companies WHERE id = ?", (id))
    
    if c.rowcount == 0:
        print("Company not found.")
    else:
        conn.commit()  
        conn.close()
        print("company deleted successfully.")

# Call the function to execute the update.
home()





  
