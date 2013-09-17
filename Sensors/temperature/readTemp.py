#-------------------------------------------------------------------------------
# Name:        temperature sensor
# Purpose:     To read temperature in celcius using a DS18B20
#
# Author:      Ali Mulla of www.LearnICT.it
# Version:     0.2
# Created:     17/09/2013
# Copyright:   No copyright - Sharing is caring
# Thanks:      Matthew Kirk of Cambridge Uni &, Raspberrypispy.co.uk &
#              Adafruit.com. This is an almagamation of their works
#-------------------------------------------------------------------------------

import os  #This will allow us to give commands as we would to the terminal
#The following lines will allow us to set the device to report temperature
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

#The function to be called when needed to report temperature
def readTemp():
    tfile = open(device_file, 'r')
    text = tfile.read()
    tfile.close()
    temperature_data = text.split()[-1]
    temperature = float(temperature_data[2:])
    temperature = temperature / 1000
    print(temperature)

#calling the function
readTemp()
