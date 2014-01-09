#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ali
#
# Created:     16/09/2013
# Copyright:   (c) Ali 2013
# Version:     0.1 Need to remove LEDs and set state to 0.
#              set state to 1 when triggered
#-------------------------------------------------------------------------------

# Import required Python libraries
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)     # note - using BCM naming method
GPIO.setup(7, GPIO.IN)     # Pin 26 on board is the PIR
GPIO.setup(11, GPIO.OUT)   # Pin 23 on the board is the red LED
GPIO.setup(10, GPIO.OUT)   # Pin 21 on board is the amber LED
GPIO.setup(9, GPIO.OUT)    # Pin 19 on the board is hte green LED

sensing_var=1
while sensing_var==1 :         #If  PIR sensor is activated
    if GPIO.input(7):          # then the LEDs will be on
        GPIO.output(11, False)
        GPIO.output(10, False)
        GPIO.output(9, False)
        time.sleep(0.75)
        Print("on")           #This is to show activity on screen as well as LED on/off
    else:                     # Else LEDs will be left off
        GPIO.output(11, True)
        GPIO.output(10, True)
        GPIO.output(9, True)
        time.sleep(0.75)
        Print("off")          #This is to show activity on screen as well as LED on/off
