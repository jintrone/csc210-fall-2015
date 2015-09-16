#!"C:\Python27\python.exe"

# the above line is for Windows. For Mac OS, use the path to your Python,
# which is usually:
#!/usr/bin/env python


# Lecture 4 - CSC210 Fall 2015
# Philip Guo

# Execute with URLs like:
#
# http://localhost/cgi-bin/lecture4.py?my_name=Joe&my_age=32&my_image=../cat.jpg
# http://localhost/cgi-bin/lecture4.py?my_name=Donna&my_age=37&my_image=../dog.jpg

# useful for debugging
import cgitb
cgitb.enable()

import cgi
form = cgi.FieldStorage()

my_name = form['my_name'].value
my_age = form['my_age'].value
my_image = form['my_image'].value


# insert new user data into the database
import sqlite3

conn = sqlite3.connect('people.db')
c = conn.cursor()

c.execute('insert into users values (?, ?, ?)', (my_name, my_age, my_image))
conn.commit()


import datetime

# print the http header
print "Content-Type: text/html"
print # don't forget the extra newline

print '<html>'
print ' <head>'
print '		<title>'
print '			My first webpage'
print '		</title>'
print '		<style type="text/css">'
# in Python, use ''' triple quotes ''' to create a multi-line string
print '''
			h1 {
				font-size: 100px;
				font-family: arial;
			}

			img {
				width: 300px;
			}

			p#myLine {
				color: red;
			}
		</style>

	</head>
'''

print '	<body>'
print '		<h1>My heading</h1>'
print '		<h2>'
print str(datetime.datetime.now())
print '		</h2>'

# print out the data for all users in the database
for r in c.execute('select * from users;'):
	name = r[0]
	age = r[1]
	image = r[2]

	print '<h2>' + name + '</h2>'
	print '<h2>' + str(age) + '</h2>'

	print '<img src="' + image + '"/>'
	print '<hr/>'
conn.close()

print '	</body>'
print '</html>'
