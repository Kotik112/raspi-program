from models.Bridge import Bridge
# from models.Light import Light
import time

SLEEP_TIME = 5
DEBUG = True

bridge = Bridge()

light_list = []  # Lista av alla lampor

def debug_print():
    """Printa meddelande om DEBUG är True"""
    if DEBUG:
        print(f"Number of lights: {len(light_list)}")
        for l in light_list:
            print(f"Light: {l.name}, id: {l.light_id}")

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

    # DEBUG output för utveckling
    debug_print()
        

    # Tända alla lampor i bedroom1 och sätt ljusstyrka till 100
    for light in bedroom1:
        bridge.turn_on(light.light_id)
        bridge.set_brightness(light.light_id, 254)
    
    


if __name__ == '__main__':
    main()
