#!"C:\Python27\python.exe"

# the above line is for Windows. For Mac OS, use the path to your Python,
# which is usually:
#!/usr/bin/env python


# Lecture 4 - CSC210 Fall 2015
# Philip Guo

# To run:
#
# python lecture4-query-database.py


import sqlite3

# open an existing database file named 'people.db'
conn = sqlite3.connect('people.db')
c = conn.cursor()

# run these SQL queries and print out their results to the terminal:
for r in c.execute('select * from users;'):
	print r
print

for r in c.execute('select * from users order by age;'):
	print r
print

for r in c.execute('select * from users where age < 35;'):
	print r
print

for r in c.execute('select * from users where age < 35 order by name;'):
	print r
print

conn.close()
