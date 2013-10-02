# Import required Python libraries
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # note - using BCM naming method
GPIO.setup(7, GPIO.IN) # Pin 26 on board is GPIO 7 for the PIR data
sensing_var=1
trigger_state=0 # 0 for off & 1 for on
while sensing_var==1 : #If PIR sensor is activated
    if GPIO.input(7): # then the LEDs will be on
        Trigger_state=1
        time.sleep(0.75)
    print("on") #This is to show activity on screen as well as LED on/off
    else: # Else LEDs will be left off
        time.sleep(0.75)
    Trigger_state=0
    print("off") #This is to show activity on screen as well as LED on/off
