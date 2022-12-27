# Ej lyckats få denna att fungera. Får errors när jag försöker köra den.

import pygatt

# Target MAC address to look for
TARGET_MAC_ADDRESS = "88:29:9C:36:73:54"

# Create a pygatt adapter to use for scanning
adapter = pygatt.BGAPIBackend()

try:
    # Start the adapter
    adapter.start()

    # Scan for devices
    devices = adapter.scan()

    # Iterate through the list of devices
    for device in devices:
        # Check the MAC address of each device
        if device.address == TARGET_MAC_ADDRESS:
            # If the MAC address matches, perform some action
            print("Found target device with MAC address:", device.address)
        else:
            # If the MAC address does not match, perform some alternative action
            print("Found device with MAC address:", device.address)

except pygatt.exceptions.BLEError as e:   # Do I actually need to check for this exception?
    # Handle the exception
    print("An error occurred while scanning:", e)

finally:
    # Stop the adapter when finished
    adapter.stop()