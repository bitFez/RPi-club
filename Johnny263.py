# This uses a hbridge module
# guide found @ https://projects.raspberrypi.org/en/projects/build-a-buggy/2
# and merged with another guide found @ https://gpiozero.readthedocs.io/en/v1.1.0/recipes.html#keyboard-controlled-robot

from evdev import InputDevice, list_devices, ecodes
from gpiozero import Robot
johnny = Robot(left=(7,8), right=(9,10))

devices = [InputDevice(device) for device in list_devices()]
keyboard = devices[0]  # this may vary

keypress_actions = {
    ecodes.KEY_UP: johnny.forward,
    ecodes.KEY_DOWN: johnny.backward,
    ecodes.KEY_LEFT: johnny.left,
    ecodes.KEY_RIGHT: johnny.right,
}

for event in keyboard.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:  # key down
            keypress_actions[event.code]()
        if event.value == 0:  # key up
            johnny.stop()
