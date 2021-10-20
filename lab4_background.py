#!/usr/bin/python3

# This code runs continually in the background to apply
# the stored PWM slider value to the GPIO output

# Importing libraries:
import RPi.GPIO as GPIO
import time
import json

whitePin = 19
bluePin = 16
greenPin = 20

# setting pins as outputs
GPIO.setmode(GPIO.BCM)
GPIO.setup(whitePin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)

white = GPIO.PWM(whitePin, 100) # PWM object on our pin at 100 Hz
white.start(0) # start with white LED off

blue = GPIO.PWM(bluePin, 100) # PWM object on our pin at 100 Hz
blue.start(0) # start with blue LED off

green = GPIO.PWM(greenPin, 100) # PWM object on our pin at 100 Hz
green.start(0) # start with green LED off

while True:
  with open("lab4.txt", 'r') as f:
    data = json.load(f)
  dutyCycle = str(data['slider'])
  selectedLED = str(data['option'])

  if selectedLED == 'white':
    white.ChangeDutyCycle(dutyCycle)
  elif selectedLED == 'green':
    green.ChangeDutyCycle(dutyCycle)
  elif selectedLED == 'blue':
    blue.ChangeDutyCycle(dutyCycle)
  time.sleep(0.1)
