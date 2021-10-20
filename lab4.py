#!/usr/bin/python37all
import cgi
import json

# retrieve data
data = cgi.FieldStorage()
brightness = data.getvalue('slider')
selected_led = data.getvalue('option')
data = {"slider":brightness, "option":selected_led}

# put into json
with open('led-pwm.txt', 'w') as f:  
  json.dump(data,f)

# new html page
print('Content-type:text/html\n\n')
print('<html>')

print('<form action="/cgi-bin/lab4.py" method="POST">')
# selecting LED
print('<input type="radio" name="option" value="white" checked> white LED <br>')
print('<input type="radio" name="option" value="blue"> blue LED <br>')
print('<input type="radio" name="option" value="green"> green LED <br>')
# selecting brightness
print('<input type="range" name="slider" min ="0" max="100" value ="%s"><br>' % brightness)
print('<input type="submit" value="Change LED brightness">')
print('</form>')

print('</html>')

