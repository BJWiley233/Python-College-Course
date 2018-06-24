#!/usr/bin/python
print("content-type: text/html\n\n")

# Import the library with the CGI components and functionality
import cgi
import random
import math
# Use the CGI library to gain access to the information entered in the HTML format
form = cgi.FieldStorage()
html = ""

def randomNumber():
        number = random.randint(0,100)
        return number

number = randomNumber()
        
try:
        # All data from a form is a string, convert to an integer to loop through
        id = int(form.getvalue('number'))
	
		
except ValueError:
        html = html + "<p>You did not enter a number.</p>"
        
else: 
        if int(form.getvalue('number')) not in range(1, 101):
            html = html + "<p>Out of range.  Please select and integer between 1 and 100.</p>"

if id in range(1,101):
    if id == number:
            html = html + "<p>" + "Congrats! You guessed " + str(id) + " and the computer number was " + str(number) + "." + "</p>"
    
    elif math.fabs(id-number) <= 10: 
            html = html + "<p>" + "Too bad, but you were close! You entered " + str(id) + " and the computer number was " + str(number) + "." + "</p>"
        
    else:
            html = html + "<p>" + "You were WAY off! You entered " + str(id) + " and the computer number was " + str(number) + "." + "</p>"

        
# Finally output the HTML code and the final html variable
print("<html>")
print("<body>")
print("<h1>Results Page</h1>")
print(html)
print("<a")
print('href="http://www.site03.zourn.com/Week%203/form_NumberGuess.html"><font color="blue">Guess/Try Again?</font>')
print("</a>")
print("<p></p>")
print("<a")
print('href="http://www.site03.zourn.com/"><font color="blue">home</font>')
print("</a>")
print("</body>")
print("</html>")
