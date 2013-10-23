#!/usr/bin/env python

#-------------------------------------------------------------------------------
# Name:        Pygame Webcam Snap
# Purpose:     To take still images using a webcam and pygame
#
# Author:      Ali Mulla
# Version:     0.3
# Created:     22/10/2013
# Copyright:   No Copyright
# Thanks:      Thanks to Ajit Akar for the idea on CAS forums.
#-------------------------------------------------------------------------------

import sys
import os
import datetime
import pygame
import pygame.camera
from pygame.locals import *

def takeSnap(filename= "webcam" + now.strftime("%Y-%m-%d %H:%M") + ".jpg"):
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()
image = cam.get_image()
pygame.image.save(image, filename)
