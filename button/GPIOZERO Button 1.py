# Programming GPIOZERO Buttons to carry out an action every time a button is pressed.
from gpiozero import Button
from signal import pause


# Creating a function to carry out an action
def action_for_button_press():
    code action here
    eg turn on LED

#assigning a button to GPIO (BCM layout) Pin 2
button = Button(2)

# calling the function when the button is pressed.
button.when_pressed = action_for_button_press

pause()
