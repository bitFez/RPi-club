#!/usr/bin/python
#-------------------------------------------------------------------------------
# Name:        webcamSnap
# Purpose:     Takes a picture using a webcam on the raspberry pi from within Python
#              - VERY IMPORTANT - You need to have installed fswebcam using terminal
#              on the RPi
# Author:      Ali Mulla of www.learnICT.it
#
# Created:     13/09/2013
# Version:     1.3
# Licence:     Free to use, please give credit
#-------------------------------------------------------------------------------

# This line imports the ability to use commands that are used in the command line
from subprocess import call
# This line imports the time 
from datetime import datetime

# This part is the function which runs the webcam and captures and image
def capture():
    dt = datetime.now().isoformat() # This grabs current time
    dtime = dt[0:4]+dt[5:7]+dt[8:10]+dt[11:13]+dt[14:16]+dt[17:19] # This formarts the time to add to filename
    # this line runs the code that captures the image (adding the current time to filename)
    call(["fswebcam", "-d","/dev/video0", "-r", "640x480", "--no-banner", "./%d.jpg" % int(dtime)])
    
# This line runs / calls the above function
capture()
