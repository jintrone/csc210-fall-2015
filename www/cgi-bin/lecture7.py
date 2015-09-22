#!"C:\Python27\python.exe"

# the above line is for Windows. For Mac OS, use the path to your Python,
# which is usually:
#!/usr/bin/env python


# Lecture 7 - CSC210 Fall 2015
# Philip Guo

# To run, start AMPSS and visit URLs like the following:
#
# http://localhost/cgi-bin/lecture7.py?requested_name=Philip
# http://localhost/cgi-bin/lecture7.py?requested_name=Jane

# useful for debugging
import cgitb
cgitb.enable()

import cgi
form = cgi.FieldStorage()

requested_name = form['requested_name'].value

import sqlite3
conn = sqlite3.connect('people.db')
c = conn.cursor()


# print the http header
print "Content-Type: text/html"
print # don't forget the extra newline

import json
data = {}

for r in c.execute('select * from users where name=?;', [requested_name]):
	name = r[0]
	age = r[1]
	image = r[2]

	#print name + ' ' + str(age) + ' ' + image

	data['myName'] = name
	data['myAge'] = age
	data['myImage'] = image
	print json.dumps(data)

conn.close()