#!/usr/bin/env python
###########################
# Created by Ajit Jaoker
###########################

import sys
import os
import pygame
import pygame.camera
from pygame.locals import *

from twython import Twython
CONSUMER_KEY = 'XXXXX'
CONSUMER_SECRET = 'XXXXX'
ACCESS_KEY = 'XXXXX'
ACCESS_SECRET = 'XXXXX'
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()
image = cam.get_image()
pygame.image.save(image,'webcam.jpg')
photo = open('webcam.jpg','rb')
api.update_status_with_media(media=photo, status='My RPi be tweeting images now => ')
