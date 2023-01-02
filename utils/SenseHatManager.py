"""
SenseHatManager class which is used to manage the SenseHat.
This class is a subclass of the SenseHat class from the sense_hat library.

The class contains methods for listening to joystick events and for displaying text on the SenseHat display.
The class will also be used to change the colours of the Bridge lights depending on the joystick events.

"""

from sense_hat import SenseHat
from time import sleep
from threading import Thread
from models import Bridge

class SenseHatManager(SenseHat):
    def __init__(self):
        """Initialize the SenseHat object and connect to the SenseHat."""
        super().__init__()
        self.set_rotation(180) # Rotate the display 180 degrees
        self.clear() # Clear the display
        print("******  Connected to SenseHat  ******")

    def listen_to_joystick(self):
        """Listen to joystick events and call the corresponding function."""
        while True:
            for event in self.stick.get_events():
                if event.action == 'pressed':
                    if event.direction == 'up':
                        print("Up pressed")
                        self.on_up_pressed()
                    elif event.direction == 'down':
                        print("Down pressed")
                        self.on_down_pressed()
                    elif event.direction == 'left':
                        print("Left pressed")
                        self.on_left_pressed()
                    elif event.direction == 'right':
                        print("Right pressed")
                        self.on_right_pressed()
                    elif event.direction == 'middle':
                        print("Middle pressed")
                        self.on_middle_pressed()

    def on_up_pressed(self):
        """Function that is called when the up button is pressed."""
        self.show_message("Up pressed")
        # TODO: Change the color of the lights

    def on_down_pressed(self):
        """Function that is called when the down button is pressed."""
        self.show_message("Down pressed")
        # TODO: Change the color of the lights

    def on_left_pressed(self):
        """Function that is called when the left button is pressed."""
        self.show_message("Left pressed")
        # TODO: Change the color of the lights

    def on_right_pressed(self):
        """Function that is called when the right button is pressed."""
        self.show_message("Right pressed")

    def on_middle_pressed(self):
        """Function that is called when the middle button is pressed."""
        self.show_message("Middle pressed")

    def show_message(self, message):
        """Display a message on the SenseHat display."""
        self.clear()
        self.show_message(message, scroll_speed=0.05, text_colour=[255, 255, 255])
        sleep(1)
        self.clear()

    def start_listening(self):
        """Start listening to joystick events."""
        Thread(target=self.listen_to_joystick).start()

if __name__ == "__main__":
    sense_hat = SenseHatManager() # Skapa en SenseHatManager
    sense_hat.start_listening()   # Starta lyssnandet på knapptryck
    while True:
        sleep(1)
