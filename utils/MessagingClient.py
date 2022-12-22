import asyncio
import os
from secrets import set_env_var
import json
import time # Ifall vi vill ha en delay eller tidsstämpel

from azure.iot.device.aio import IoTHubDeviceClient

class MessagingClient:
    def __init__(self):
        set_env_var()  # Get connection string from secrets.py
        self.CONNECTION_STRING = os.getenv("IOTHUB_DEVICE_CONNECTION_STRING")
        self.client = IoTHubDeviceClient.create_from_connection_string(self.CONNECTION_STRING)
        asyncio.run(self.client.connect())       
        print("******  Connected to IoT Hub  ******")

    async def send_message(self, message):
        await self.client.send_message(message)
        print("Message sent")

    async def disconnect(self):
        await self.client.disconnect()
        print("Disconnected from IoT Hub")



if __name__ == "__main__":
    client = MessagingClient() # Skapa en client
    # Dummy data
    data = {
        "name": "John Doe",
        "age": 42,
        "isAlive": True,
        "address": {
            "streetAddress": "123 Main St",
            "city": "Anytown",
            "state": "CA",
            "postalCode": "12345-6789"
        }
    }
    data = json.dumps(data) # Konvertera till JSON
    asyncio.run(client.send_message(data)) # Skicka ett meddelande
    asyncio.run(client.disconnect()) # Disconnect