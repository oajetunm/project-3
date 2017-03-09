#init_db.py

import sqlite3

conn = sqlite3.connect('tweets.db')

# Put code here to create the database and tables
#
# You may want to set this up so that you can also DROP or TRUNCATE tables 
# as you are developing so that you can start from scratch when you need to

conn.close()