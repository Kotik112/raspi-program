"""
Script för att styra Philips Hue-lampor

För att köra scriptet behöver du en Hue Bridge och en eller flera Hue-lampor.

Dokumentation för phue-biblioteket:
https://github.com/studioimaginaire/phue/blob/master/README.md

Dokumentation för Converter-biblioteket: (använt för att konvertera färg från RGB till XY)
https://github.com/benknight/hue-python-rgb-converter

TODO: Kolla på create_schedule(), create_group_schedule() och create_scene()

"""


from models.Bridge import Bridge
import asyncio
# from utils.MessagingClient import MessagingClient
from utils.bluetooth import BluetoothScanner


light_list = []  # Lista av alla lampor

DEBUG = False
# Only used during development phase
def debug_print():
    """Printa information om lamporna ifall DEBUG är True"""
    if DEBUG:
        print(f"Number of lights: {len(light_list)}")
        for l in light_list:
            light_info = bridge.get_light(l.light_id)
            # print(light_info['capabilities']['control'])
            # Check if the light has color capabilities
            if 'xy' in light_info['state']:
                print(f'Light: {l.name}, id: {l.light_id}: has color capabilities.')
            else:
                print(f'Light: {l.name}, id: {l.light_id}: does not have color capabilities.')

            if 'colorloop' in light_info['state']:
                print(f'Light: {l.name}, id: {l.light_id}: has colorloop capabilities.')
        

def sort_lights(list):
    """Sortera lamporna i olika grupper baserat på vilket rum de är i"""
    group1 = list[:5]
    group2 = list[5:7]
    group3 = list[7:11]
    group4 = list[11:]

    return group1, group2, group3, group4
"""
def main():
    global light_list # global variabel för att kunna använda den i andra funktioner
    light_list = bridge.lights
    bedroom1, hallway, bedroom2, kitchen = sort_lights(light_list)

    message_client = MessagingClient()
    #message_client.send_message("Hello from Raspberry Pi")
    
    # DEBUG output för utveckling ifall DEBUG variabeln är True
    debug_print()
        

    # Tända alla lampor i bedroom1 och sätt ljusstyrka till 100
    for l in bedroom1:
        pass
"""

# For testing purposes only in UK
def main():
    # bridge = Bridge()
    bt_scanner = BluetoothScanner(["88:29:9C:36:73:54", "C8:7B:9A:EF:87:65"])
    print("Scanning for devices... (10 seconds)")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bt_scanner.run())


if __name__ == '__main__':
    main()
