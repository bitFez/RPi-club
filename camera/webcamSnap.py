#!/usr/bin/python
#-------------------------------------------------------------------------------
# Name:        webcamSnap
# Purpose:
#
# Author:      Ali Mulla of www.learnICT.it
#
# Created:     13/09/2013
# Version:     1.0
# Licence:     Free to use, please give credit
#-------------------------------------------------------------------------------

# This line imports the ability to use commands are used in the terminal window
import os


# This part defines a function for taking the snap with date stamp on filename
def takeSnap(filename="snap_%d%m%y_%h%s.jpg"):
    # This part is the command that would have been written into terminal
    os.system ("fswebcam --no-banner -r 600x480 -d /dev/video0 %s" % filename)

#takes the photo
takeSnap()
