import asyncio
from bleak import BleakScanner

TARGET_MAC_ADDRESS = "88:29:9C:36:73:54"  # My phone - I can't seem to find my phone!!
TARGET_BUDS_ADDRESS = "C8:7B:9A:EF:87:65" # My buds

async def run():
    devices = await BleakScanner.discover()
    for d in devices:
        if d.address == TARGET_MAC_ADDRESS or d.address == TARGET_BUDS_ADDRESS:
            print("Target device found!")  # Finds my buds, but not my phone
        else:
            print(d)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())