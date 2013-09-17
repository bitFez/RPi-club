#-------------------------------------------------------------------------------
# Name:        temperature sensor
# Purpose:     To read temperature in celcius using a DS18B20
#
# Author:      Ali Mulla of www.LearnICT.it
# Version:     0.1
# Created:     17/09/2013
# Copyright:   No copyright - Sharing is caring
# Thanks:      Matthew Kirk of Cambridge Uni &, Raspberrypispy.co.uk &
#              Adafruit.com. This is an almagamation of their works
#-------------------------------------------------------------------------------

import os  #This will allow us to give commands as we would to the terminal
#The following lines will allow us to set the device to report temperature
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

#The function to be called when needed to report temperature
def readTemp():
    tfile = open("/sys/bus/w1/devices/10-000802824e58/w1_slave")
    text = tfile.read()
    tfile.close()
    temperature_data = text.split()[-1]
    temperature = float(temperature_data[2:])
    temperature = temperature / 1000
    print(temperature)

#calling the function
readTemp()
