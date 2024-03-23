# Visitors-tracker-project

## Introduction:

The Visitor Management System is a simple application designed to manage visitors' records for a given facility. It provides functionalities for CRUD operations (Create, Read, Update, Delete) on visitor records, as well as other administrative tasks such as user registration, login, and updating visit records.

## Functionalities:

1. Create: Allows users to register new visitor records by providing necessary details such as first name, last name, email, ID number, company ID, reason for visit, and car plate.

2. Read: Provides options to view visitor records and company details.

3. View Visitors: Displays all existing visitor records along with their details such as first name, last name, email, ID number, time in, time out, visitor experience, reason for visit, car plate, and associated company.
View Companies: Displays details of all registered companies, including their name, description, location, and address.
4. Update: Enables users to update visit records by marking the time out and providing a visitor experience.

5. Delete: Provides functionality to delete visitor records from the system.

6. User Registration: Allows new users to register themselves by providing necessary information such as first name, last name, email, ID number, company ID, reason for visit, and car plate.

7. Login: Allows registered users to log in to the system by providing their credentials (first name and ID number).

8. Update Timeout: Allows users to update the time out and provide a visitor experience for a specific visit record.

## Implementation:

The Visitor Management System is implemented using Python and SQLite database. Here's an overview of the main components:

Database: The SQLite database stores visitor records and company details. It consists of two main tables: visitors and companies, where visitor records and company details are stored, respectively.

Python Script: The main functionality of the system is implemented using a Python script. The script handles user input, database operations, and other functionalities such as registration, login, CRUD operations, and administrative tasks.

User Interface: The user interface is primarily a command-line interface (CLI) where users interact with the system by entering commands and providing necessary information.

Usage:

To use the Visitor Management System, follow these steps:

Ensure you have Python installed on your system.
Download the provided Python script (visitors.py) and SQLite database file (visitors.db) to your local machine.
Run the Python script using a Python interpreter (e.g., python visitors.py).
Follow the on-screen instructions to perform various operations such as registration, login, viewing visitors/companies, updating visit records, and deleting visitor records.
Note:

Make sure to handle exceptions and input validation to ensure the robustness and reliability of the system.
Ensure proper security measures are implemented, such as password hashing for user authentication and protection against SQL injection attacks.
This is a basic implementation of a visitor management system and can be extended further to include additional features and functionalities as per specific requirements.

### Author
@Rotich Jane Jepkemboi
jeanetterotich@gmail.com