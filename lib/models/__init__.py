import sqlite3

CONN = sqlite3.connect('visitors.db')
CURSOR = CONN.cursor()
