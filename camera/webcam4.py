#-------------------------------------------------------------------------------
# Name:        Webcame capture
# Purpose:     Take stills using imgproc & save to file
#
# Author:      Ali Mulla
#
# Created:     07/09/2013
# Copyright:   (c) Ali 2013
# Thanks:      based on the script of http://www.cl.cam.ac.uk/ students
#              and Matt Venn
#-------------------------------------------------------------------------------
import os
from imgproc import *

def capture_image(filename="frame.jpg"):
    # open the webcam
    my_camera = Camera(320, 240)
    # grab an image from the camera
    my_image = my_camera.grabImage()
    command = "my_image" % filename
    status = os.system(command)
    return status

#take a picture
capture_image()