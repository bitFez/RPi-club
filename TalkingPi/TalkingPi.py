#-------------------------------------------------------------------------------
# Name:        TalkingPi
# Purpose:
#
# Author:      Dan Aldred
#
# Created:     09/01/2014
# Copyright:
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Talking Raspberry Pi, based on code by Rollcode.com

import sys, subprocess, urllib, time

def getSpeech(phrase):
    googleAPIurl = "http://translate.google.com/translate_tts?tl=en&"
    param = {'q': phrase}
    data = urllib.urlencode(param)
    googleAPIurl += data # Combine the data from the Google API
    return googleAPIurl

def raspberryTalk(text): # This will call mplayer and will play the sound
    subprocess.call(["mplayer",getSpeech(text)], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

raspberryTalk("Hello from the Raspberry Pi")
time.sleep(1)
raspberryTalk("Please enter your phrase")

say = raw_input("What do you want to say? ")

if __name__ == "__main__":
    raspberryTalk(say)
