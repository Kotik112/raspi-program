"""
Bridge class is used to represent a Hue Bridge. It is used to control the bridge and get information about it.
This class is a subclass of the Bridge class from the phue library.

The Bridge class also contains a list of Light objects representing the lights connected to the bridge.
"""

from phue import Bridge
from models.Light import Light

class Bridge(Bridge):
    BRIDGE_IP = '192.168.1.128'
    USERNAME = "Gmj4oGzNYxJUMP85FJoOoA38iok0H3PlXCAImxoo"


    def __init__(self):
        """Initialize the Bridge object and connect to the bridge."""
        super().__init__(ip=Bridge.BRIDGE_IP, username=Bridge.USERNAME)
        

    def get_lights(self):  #Funktionen är buggad.
        #self.lights = []
        """Get the lights connected to the bridge."""
        

    def print_lights(self):
        """Print the lights connected to the bridge."""
        for light in self.lights:
            print(str(light))

    def turn_on(self, light_id):
        """Turn on the light."""
        self.set_light(light_id, 'on', True)

    def turn_off(self, light_id):
        """Turn off the light."""
        self.set_light(light_id, 'on', False)

    def set_brightness(self, light_id, brightness):
        """Set the brightness of the light."""
        self.set_light(light_id, 'bri', brightness)

    def set_color(self, light_id, color):
        """Set the color of the light."""
        self.set_light(light_id, 'xy', color)

    def set_color_temperature(self, light_id, color_temperature):
        """Set the color temperature of the light."""
        self.set_light(light_id, 'ct', color_temperature)

    def set_alert(self, light_id, alert):
        """Set the alert of the light."""
        self.set_light(light_id, 'alert', alert)

    def set_effect(self, light_id, effect):
        """Set the effect of the light."""
        self.set_light(light_id, 'effect', effect)

    def set_transition_time(self, light_id, transition_time):
        """Set the transition time of the light."""
        self.set_light(light_id, 'transitiontime', transition_time)

    def set_color_loop(self, light_id, color_loop):
        """Set the color loop of the light."""
        self.set_light(light_id, 'colorloop', color_loop)

    if __name__ == '__main__':
        bridge = Bridge()
        bridge.print_lights()