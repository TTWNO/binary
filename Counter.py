#Counter.py
# this is a change in this file
import RPi.GPIO as GPIO
import time

#set BCM mode
GPIO.setmode(GPIO.BCM)

#set the LED's
GPIO.setup(21,GPIO.OUT)  #256
GPIO.setup(26,GPIO.OUT)  #128
GPIO.setup(19,GPIO.OUT)  #64
GPIO.setup(13,GPIO.OUT)  #32
GPIO.setup(6,GPIO.OUT)   #16
GPIO.setup(5,GPIO.OUT)   #8
GPIO.setup(25,GPIO.OUT)  #4
GPIO.setup(24,GPIO.OUT)  #2
GPIO.setup(23,GPIO.OUT)  #1

#we set everything on low at start
GPIO.output(23,GPIO.LOW)
GPIO.output(24,GPIO.LOW)
GPIO.output(25, GPIO.LOW)
GPIO.output(5,GPIO.LOW)
GPIO.output(6,GPIO.LOW)
GPIO.output(13,GPIO.LOW)
GPIO.output(19,GPIO.LOW)
GPIO.output(26,GPIO.LOW)
GPIO.output(21,GPIO.LOW)

def ledOn(pin):
	if (pin == 0):
		GPIO.output(23,GPIO.HIGH)
	if (pin == 1):
		GPIO.output(24,GPIO.HIGH)
	if (pin == 2):
		GPIO.output(25,GPIO.HIGH)
	if (pin == 3):
		GPIO.output(5,GPIO.HIGH)
	if (pin == 4):
		GPIO.output(6,GPIO.HIGH)
	if (pin == 5):
		GPIO.output(13,GPIO.HIGH)
	if (pin == 6):
		GPIO.output(19,GPIO.HIGH)
	if (pin == 7):
		GPIO.output(26,GPIO.HIGH)
	if (pin == 8):
		GPIO.output(21,GPIO.HIGH)

def ledOff(pin):
	if (pin == 0):
		GPIO.output(23,GPIO.LOW)
	if (pin == 1):
		GPIO.output(24,GPIO.LOW)
	if (pin == 2):
		GPIO.output(25,GPIO.LOW)
	if (pin == 3):
		GPIO.output(5,GPIO.LOW)
	if (pin == 4):
		GPIO.output(6,GPIO.LOW)
	if (pin == 5):
		GPIO.output(13,GPIO.LOW)
	if (pin == 6):
		GPIO.output(19,GPIO.LOW)
	if (pin == 7):
		GPIO.output(26,GPIO.LOW)
	if (pin == 8):
		GPIO.output(21,GPIO.LOW)



x = 0
while( x < 9):
	ledOn(x)
	time.sleep(0.1)
	ledOff(x)
	x = x + 1



