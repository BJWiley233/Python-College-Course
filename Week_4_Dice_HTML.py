#!/usr/bin/python
print("content-type: text/html\n\n")

# Import the library with the CGI components and functionality
import cgi
import random
# Use the CGI library to gain access to the information entered in the HTML format
form = cgi.FieldStorage()
html = ""

def roll(num_of_dice):
        number = [1, 2, 3, 4, 5, 6]
        rolledNumbers = []
        for i in range(0,num_of_dice):
                rolledNumbers.append(random.choice(number))
        # return list of numbers
        return rolledNumbers

dice_Roll = roll(1)[0]

try:
        # All data from a form is a string, convert to an integer to loop through
        id = int(form.getvalue('number'))
	
		
except ValueError:
        html = html + "<p>Please enter only a number.</p>"
        
else: 
        if int(form.getvalue('number')) not in range(1, 7):
            html = html + "<p>Out of range.  Please select and number between 1 and 6.</p>"

if id in range(1,7):
    if id == dice_Roll:
        html = html + "<p>" + "Congrats! You entered " + str(id) + " and the die rolled a " + str(dice_Roll) + "." + "</p>"
    else:
        html = html + "<p>" + "Too bad. You entered " + str(id) + " and the die rolled a " + str(dice_Roll) + "." + "</p>"

        
# Finally output the HTML code and the final html variable
print("<html>")
print("<body>")
print("<h1>Results Page</h1>")
print(html)
print("<a")
print('href="http://www.site03.zourn.com/Week%204/form_GuessDie.html"><font color="blue">Guess/Try Again?</font>')
print("</a>")
print("<p></p>")
print("<a")
print('href="http://www.site03.zourn.com/"><font color="blue">home</font>')
print("</a>")
print("</body>")
print("</html>")
