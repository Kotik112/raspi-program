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
import time

bridge = Bridge()
light_list = []  # Lista av alla lampor

DEBUG = False
def debug_print():
    """Printa information om lamporna ifall DEBUG är True"""
    if DEBUG:
        print(f"Number of lights: {len(light_list)}")
        for l in light_list:
            light_info = bridge.get_light(l.light_id)
            #print(light_info['capabilities']['control'])
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

def main():
    global light_list # global variabel för att kunna använda den i andra funktioner
    light_list = bridge.lights
    bedroom1, hallway, bedroom2, kitchen = sort_lights(light_list)

    # DEBUG output för utveckling ifall DEBUG variabeln är True
    debug_print()
        

    # Tända alla lampor i bedroom1 och sätt ljusstyrka till 100
    

    bridge.set_color_loop(bedroom1) # Låser fast programmet :( kanske behöver en egen tråd eller tid som parameter/argument

    
    

if __name__ == '__main__':
    main()


"""
set_color_loop() verkar vara buggad eller så stöder inga av mina lampor det.
"""
