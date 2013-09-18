# This code assumes that you will use the LED with another code in which case you can
# just call the function to have the led on/off when required
# first we need to import the libraries that are needed to turn the led on and off

import RPi.GPIO as GPIO

#do not do this if you have already done it with another code recipe you're combining
#clear up the current board setup.
GPIO.cleanup()
#set the RPi to use the RPi board pin numbers
GPIO.setmode(GPIO.board)

#Now we will set the pin number we will use to send the signal to the LED
GPIO.setup(7, GPIO.out)

# this is a variable that will be used to determine whether the LED should be on or off
led7state = 0

#function to turn on LED
def turnonled7():
    led7state = 1
    
#function to turn LED off
def turnoffled7():
    led7state = 0
    
if led7state == 1:
    GPIO.output(7, GPIO.HIGH)
else:
    GPIO.output(7, GPIO.LOW)
