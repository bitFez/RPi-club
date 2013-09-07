#-------------------------------------------------------------------------------
# Name:        Webcame capture
# Purpose:     Take stills using imgproc & save to file
#
# Author:      Ali Mulla
#
# Created:     07/09/2013
# Copyright:   (c) Ali 2013
# Version      0.4
#-------------------------------------------------------------------------------
import PIL.Image
from imgproc import *

# open the webcam
my_camera = Camera(320, 240)
# grab an image from the camera
my_image = my_camera.grabImage()

im = PIL.Image.new("RGB", (my_image.width, my_image.height))
im.PIL.save("image.png")
