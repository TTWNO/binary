#Counter.py
# this is a change in this file
import RPi.GPIO as GPIO
import time

list_of_pins = [23, 24, 25, 5, 6, 13, 19, 26, 21]

#set BCM mode
GPIO.setmode(GPIO.BCM)

#set the LED's
for pin in list_of_pins:
  GPIO.setup(pin, GPIO.OUT)

#we set everything on low at start
for pin in list_of_pins:
  GPIO.output(pin, GPIO.LOW)

def ledOn(pin):
  for pin_index in range(list_of_pins):
    if pin == pin_index:
      GPIO.output(list_of_pins[pin_index], GPIO.HIGH)

def ledOff(pin):
  for pin_index in range(list_of_pins):
    if pin == pin_index:
      GPIO.output(list_of_pins[pin_index], GPIO.LOW)

x = 0
while( x < 9):
	ledOn(x)
	time.sleep(0.1)
	ledOff(x)
	x = x + 1



