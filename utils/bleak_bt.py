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
        devices = await BleakScanner.discover(timeout=20) 
        for d in devices:
            if d.address in self.target_addresses:
                print(f"Target device  >>\033[1m{d.name}\033[0m<< with MAC address {d.address} found!")
            else:
                print(d)

if __name__ == "__main__":
    PHONE_MAC_ADDRESS = "88:29:9C:36:73:54"  # My phone
    BUDS_MAC_ADDRESS = "C8:7B:9A:EF:87:65"   # My ear buds

    scanner = BluetoothScanner([PHONE_MAC_ADDRESS, BUDS_MAC_ADDRESS])
    loop = asyncio.get_event_loop()
    loop.run_until_complete(scanner.run())
