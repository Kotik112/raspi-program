from models.Bridge import Bridge
import time

DEBUG = True
SLEEP_TIME = 5

test_lights = [] # Kan skapa en lista av lampor här,

bridge = Bridge()
if DEBUG:
    test_lights = bridge.lights
    for l in test_lights:
        print(l)

def main():
    while True:
        bridge.set_light(13, 'on', True)
        bridge.set_light(14, 'on', False)
        time.sleep(SLEEP_TIME)
        bridge.set_light(13, 'on', False)
        bridge.set_light(14, 'on', True)
        time.sleep(SLEEP_TIME)

if __name__ == '__main__':
    main()
