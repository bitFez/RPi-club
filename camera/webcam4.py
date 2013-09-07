#-------------------------------------------------------------------------------
# Name:        Webcame capture
# Purpose:     Take stills using imgproc & save to file
#
# Author:      Ali Mulla
#
# Created:     07/09/2013
# Copyright:   (c) Ali 2013
# Version      0.3
#-------------------------------------------------------------------------------
from PIL import Image
from imgproc import *

# open the webcam
my_camera = Camera(320, 240)
# grab an image from the camera
my_image = my_camera.grabImage()

im = Image.putdata(my_image)
im.save("image.png")
