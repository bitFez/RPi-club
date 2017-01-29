# All credit to Jithin Sanal who posted this on Hackster.io
# H_bridge
# Run by using terminal like so:
# python H_bridge

import RPi.GPIO as GPIO ## import GPIO library
import curses #

GPIO.setwarnings(False)

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)

GPIO.output(29, True)
GPIO.output(31, True)
try:
    while True:
        char = screen.getch()
        if char ==ord('q'):
            break
        elif char == curses.KEY_UP:
            print("up")
            GPIO.output(33, True)
            GPIO.output(11, False)
            GPIO.output(13, True)
            GPIO.output(15, False)

        elif char == curses.KEY_DOWN:
            print("Down")
            GPIO.output(33, False)
            GPIO.output(11, True)
            GPIO.output(13, False)
            GPIO.output(15, True)

        elif char == curses.KEY_RIGHT:
            print("Right")
            GPIO.output(33, True)
            GPIO.output(11, False)
            GPIO.output(13, False)
            GPIO.output(15, True)

        elif char == curses.KEY_LEFT:
            print("Left")
            GPIO.output(33, False)
            GPIO.output(11, True)
            GPIO.output(13, True)
            GPIO.output(15, False)

        elif char == 10:
            print("Stop")
            GPIO.output(33, False)
            GPIO.output(11, False)
            GPIO.output(13, False)
            GPIO.output(15, False)

finally:
    #Close down curses properly, inc turn echo back on!
    curses.nobreak(); screen.keypad(0); curses.echo()
    curses.endwin()
