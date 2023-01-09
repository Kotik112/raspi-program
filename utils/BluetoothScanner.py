"""Link to the original source:
https://stackoverflow.com/questions/43418193/how-to-use-python-to-scan-and-communicate-with-ble-device-under-windows-environm

Documentation for bleak:
https://bleak.readthedocs.io/en/latest/
"""
import asyncio
from bleak import BleakScanner

class BluetoothScanner:
    def __init__(self, target_addresses):
        self.target_addresses = target_addresses

    async def run(self):
        # Scan for devices for 20 seconds. The default is 5 seconds.
        devices = await BleakScanner.discover(timeout=15) 
        for d in devices:
            if d.address in self.target_addresses:
                print(f"Target device found with MAC address {d.address} found!")
                if d.address == "FF:FF:10:5B:DE:6C":
                    print("ARMAN tag found.")
                return True
        return False

if __name__ == "__main__":
    BLE_TAG_MAC = "FF:FF:10:5B:DE:6C"  # iTag
    #ALDO_TAG_MAC = "FF:FF:10:5B:54:94"   # Aldo tag

    scanner = BluetoothScanner(BLE_TAG_MAC)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(scanner.run())
    loop.close()
