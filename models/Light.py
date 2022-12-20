"""
This module contains the Light class. This class is a subclass of the Light class from the phue library.
A Light object represents a light connected to the bridge. It contains the light's id, name, state and brightness.
"""

from phue import Light

class Light(Light):
    def __init__(self, bridge, light_id):
        """Initialize the Light object."""
        super().__init__(bridge, light_id)
        self.id = light_id
        self.name = self.get_name()

    def get_name(self):
        """Get the name of the light."""
        return self.name

def __str__(self):
    """Return a string representation of the light."""
    return f'Light: {self.name}, id: {self.id}'

def __repr__(self):
    """Return a string representation of the light."""
    return f'Light: {self.name}, id: {self.id}'
