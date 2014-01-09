#-------------------------------------------------------------------------------
# Name:        Temp1
# Purpose:     Sensing Temperature in Celcius
#
# Author:      Ali Mulla
# Version:     0.1 (untested)
# Created:     12/10/2013
# Copyright:   No Copyright
# Thanks:      This has been edited to display just the temp in celcius from
#              from the brilliant example written by Simon Monk, Adafruit.
#-------------------------------------------------------------------------------

import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

#To read the temp run:
print("The temperature is " + read_temp())
