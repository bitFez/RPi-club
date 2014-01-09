#-------------------------------------------------------------------------------
# Name:        Chatbot
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

raspberryTalk("Hello from the Raspberry Pi chat bot")
time.sleep(0.2)
raspberryTalk("I was created to get students interested in coding so I am very basic")
time.sleep(0.2)
raspberryTalk("But I have a great voice!")
time.sleep(0.3)
raspberryTalk("What is your name")
say = raw_input("What is your name? ")

raspberryTalk("Hello and welcome" + say)

raspberryTalk("Do you like cheese?")

cheese = raw_input("Do you like cheese, yes or no ").lower()

if cheese == "no":
    raspberryTalk("Me too, I hate cheese as well")
else:
    raspberryTalk("Yuk, that is so wrong")

raspberryTalk("Tell me what your favourite song is")
song = raw_input("What is your favourite song? ")

raspberryTalk(song + "sounds like a great song, shall we sing it")

raspberryTalk("la la laal da led    dd la le l ")
time.sleep(0.2)
raspberryTalk(" That's all for now" + say)
raspberryTalk("Bye Bye")

