#!/bin/sh filename=$(date +"%m-%d-%y-%H%M%S")
import time

def takepic():
    fswebcam -d /dev/video0 /home/pi/matt/$filename.jpg
    
for i in range(5):
    takepic()
    time.sleep(5)
