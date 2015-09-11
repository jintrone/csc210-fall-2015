#!"C:\Python27\python.exe"

# Lecture 3 - CSC 210 Fall 2015
# Philip Guo

# first rename to lecture3.py, then
# put this file into cgi-bin/ to deploy on your server

# The above line is for Windows; for Mac and Linux, try:
#!/usr/bin/env python

# useful for debugging
import cgitb
cgitb.enable()

import datetime

import cgi
form = cgi.FieldStorage()


# prints a minimal HTTP header
print 'Content-Type: text/html'
print

# print the HTTP body, which is the HTML file representing lecture1.html

print '<html>'
print '	<head>'

print '		<title>'

print '''
			My first webpage
		</title>

		<style type="text/css">
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

print '<body>'
print '		<h1>My heading</h1>'

print '		<h2>'
print str(datetime.datetime.now())
#print '			My sub-heading'
print '		</h2>'

print '<h2>Your name is: ' + form['my_name'].value + '</h2>'

print '<h2>Your age is: ' + form['my_age'].value + '</h2>'

print '		<img src="' + form['my_image'].value + '"/>'

print '''
		<p>Hello</p>

		<h2>
			My other sub-heading
		</h2>

		<p id="myLine">a new line</p>

		<p>another one</p>

	</body>
</html>'''
