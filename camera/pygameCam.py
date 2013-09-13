#!/usr/bin/python
#-------------------------------------------------------------------------------
# Name:        pygameCam
# Purpose:
#
# Author:      Ali Mulla of www.learnICT.it
#
# Created:     13/09/2013
# Version:     0.1
# Licence:     Free to use, please give credit
#-------------------------------------------------------------------------------

# The following lines import the needed libraries
import pygame, sys
from pygame.locals import *
import pygame.camera

def takeSnap():
    pygame.init()
    pygame.camera.init
    width = 640
    height = 480
    cam = pygame.camera.Camera("/dev/video0",(width,height))
    cam.start()
    image = cam.get_image()
    cam.stop()
    pygame.image.save(image,str(count ) +'.jpg')

takeSnap()