import sqlite3

CONN = sqlite3.connect('visitors.db')
CURSOR = CONN.cursor()
# CREATE TABLE companies (
#     id INTEGER PRIMARY KEY,
#     name VARCHAR(30),
#     description VARCHAR(300)
# );

# CREATE TABLE visitors (
#     id INTEGER PRIMARY KEY,
#     name VARCHAR(30),
#     id_no VARCHAR(30),
#     time_in DATETIME,
#     time_out DATETIME,
#     reason_for_visit VARCHAR(300),
#     car_plate VARCHAR(20)
# );

# CREATE TABLE company_visitors (
#     visitor_id INTEGER REFERENCES visitors(id),
#     company_id INTEGER REFERENCES companies(id),
#     PRIMARY KEY (visitor_id, company_id)
# );
